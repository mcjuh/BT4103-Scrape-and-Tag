# -*- coding: utf-8 -*-
"""
Extraction stage. Reads data/manifests/classify.jsonl, picks the PROVIDER,
HIRER and UNCERTAIN pages, and turns each into one record that matches the
v2 schemas in schemas/ (see docs/schema_v2.md):

    ML_provider_schema_v2.json -> data/output/providers.csv / .jsonl / .json
    ML_hirer_schema_v2.json    -> data/output/hirers.csv / .jsonl / .json

The schemas drive everything. Each prompt's field list is generated from
them and every LLM reply is validated against them; a reply that fails is
retried. Only fields marked x-filled-by "llm" are asked of the model, and
the rest are filled in by code.

Providers and hirers share one code path. They differ in the prompts
(prompts/) and the per-type settings in ENTITY_CONFIG:

  HIRER     one pass: extract_hirer.md rewrites a case study as the gig its
            client could have posted. A different pool model then reviews
            it against the source. If flagged, the record is rewritten once
            and checked again; still flagged means rejected.
  PROVIDER  two passes: extract_provider_facts.md pulls neutral facts, then
            extract_provider_style.md restyles the headline, bio and
            achievements. The source is anonymised first (needs spaCy and
            en_core_web_sm).

A prompt may return {} when the page does not qualify; the file is then
recorded as "rejected" and nothing is written.

After extraction the code adds the SkillsFuture tags (taxonomy.py), checks
the text reads as Singapore (localisation.py) and copies the industry
columns from data/manifests/industry.jsonl.

Options: --entity hirer|provider, --limit, --balance, --workers, --rps,
--ping, --out-tag TAG (write a separate dataset), --export-json,
--backfill-industries.

Each file is handled by one model from llm_pool.MODEL_POOL. Pages are only
read. Progress is kept in data/manifests/extract.jsonl, so a rerun skips
written and rejected files and retries only errors.
"""

import argparse
import csv
import functools
import hashlib
import json
import os
import random
import re
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv
from jsonschema import Draft7Validator
from openai import OpenAI

import localisation
import taxonomy
from llm_pool import MODEL_POOL, model_for_file, reviewer_for_file

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT_DIR = SCRIPT_DIR.parent  # classifier_extractor/ sits one level below the project root
DATA_DIR = ROOT_DIR / "data"  # shared data lake every role reads/writes into
PAGES_DIR = DATA_DIR / "pages"
MANIFESTS_DIR = DATA_DIR / "manifests"
OUTPUT_DIR = DATA_DIR / "output"
LOGS_DIR = ROOT_DIR / "logs"
ENV_PATH = ROOT_DIR / ".env"
PROMPTS_DIR = SCRIPT_DIR / "prompts"
SCHEMAS_DIR = SCRIPT_DIR / "schemas"

CLASSIFY_MANIFEST_PATH = MANIFESTS_DIR / "classify.jsonl"
INDUSTRY_MANIFEST_PATH = MANIFESTS_DIR / "industry.jsonl"  # industry.py's output, read for --balance
EXTRACT_MANIFEST_PATH = MANIFESTS_DIR / "extract.jsonl"
PROVIDERS_CSV = OUTPUT_DIR / "providers.csv"
HIRERS_CSV = OUTPUT_DIR / "hirers.csv"
# The nested v2 records (ML_*_schema_v2.json), one per line as they're written; export_json()
# collects them into providers.json / hirers.json (a JSON array, one record per source file).
PROVIDERS_JSONL = OUTPUT_DIR / "providers.jsonl"
HIRERS_JSONL = OUTPUT_DIR / "hirers.jsonl"

BUCKET_DIRS = {
    "PROVIDER": PAGES_DIR / "provider",
    "HIRER": PAGES_DIR / "hirer",
    "UNCERTAIN": PAGES_DIR / "uncertain",
}
# UNCERTAIN is a provider candidate: classify.py defines it as a provider profile that
# also carries hirer signals.
ENTITY_TYPE_FOR_LABEL = {
    "PROVIDER": "PROVIDER",
    "UNCERTAIN": "PROVIDER",
    "HIRER": "HIRER",
}

# Everything that differs between the two entity types.
# - "prompts" run in order: the first reads the page, each later one reads the
#   previous pass's JSON.
# - "review" and "repair" are optional. A repair reruns the first pass, so only
#   single-pass types use them.
# - "localise" is the provider's own repair (see localise_provider).
# - "pass_fields" is what each pass returns (None = every LLM field). The style
#   pass returns only the fields it restyles; the rest come from the facts pass.
ENTITY_CONFIG = {
    "PROVIDER": {
        "schema": SCHEMAS_DIR / "ML_provider_schema_v2.json",
        "prompts": ["extract_provider_facts.md", "extract_provider_style.md"],
        "pass_fields": [
            ("title", "credentials", "years_experience", "about_headline", "about_bio", "services",
             "achievements", "technical_proficiency"),
            ("about_headline", "about_bio", "achievements", "how_i_work"),
        ],
        "anonymise": True,
        "csv": PROVIDERS_CSV,
        "jsonl": PROVIDERS_JSONL,
        "title_field": "title",
        "review": None,
        "repair": None,
        "localise": "repair_localise_provider.md",
    },
    "HIRER": {
        "schema": SCHEMAS_DIR / "ML_hirer_schema_v2.json",
        "prompts": ["extract_hirer.md"],
        "pass_fields": [None],
        "anonymise": False,
        "csv": HIRERS_CSV,
        "jsonl": HIRERS_JSONL,
        "title_field": "gig_title",
        "review": "review_hirer.md",
        "repair": "repair_hirer.md",
        "localise": None,
    },
}
# The CSV keeps the v1 text columns (derived by flat_columns()) so the enricher, labeller and
# ranker import read the same columns as before. The nested record goes to the .jsonl / .json files.
CSV_COLUMNS = {
    "HIRER": ["extracted_by_model", "source_company", "source_company_team", "hire_title",
              "hire_description", "hire_description_additional_notes", "hirer_ref",
              "duration_weeks_min", "duration_weeks_max"],
    "PROVIDER": ["extracted_by_model", "about_title", "about_description", "services_offered_title",
                 "services_offered_description", "relevant_experience", "years_experience"],
}
# Record fields that aren't text a reader sees, so the checks that scan a record's wording skip them.
NON_TEXT_FIELDS = {"source_file", "extracted_by_model", "hirer_ref", "name", "availability", "rate",
                   "tags", "duration_weeks_min", "duration_weeks_max", "years_experience"}
# Copied from industry.py's manifest, not asked of the LLM. Files industry.py hadn't tagged
# get blanks until --backfill-industries.
INDUSTRY_FIELDS = ("industry", "secondary_industry", "taxonomy_version")
# The SkillsFuture tags (taxonomy.py): written by code from tag_record()'s result, never
# asked of the extraction prompts, so they stay out of the schemas.
TAG_FIELDS = taxonomy.TAG_FIELDS
PID_PATH = LOGS_DIR / "extract.pid"  # read by monitor/dashboard.py for an exact RUNNING state

MAX_CHARS = 24000
MAX_RETRIES = 3
RETRY_BACKOFF_S = 2  # doubles each retry: 2s, 4s
MAX_CONSECUTIVE_ERRORS = 5
# Per-call cap that guards against runaway output. With thinking off, the largest record seen
# was 655 tokens across both provider passes. A cut-off reply fails loudly, not as bad JSON.
MAX_COMPLETION_TOKENS = 1500

GENERIC_TITLE_BLOCKLIST = {
    "our services", "contact us", "get in touch", "learn more", "services",
    "about us", "who we are", "what we do",
}

load_dotenv(ENV_PATH)

client = OpenAI(
    base_url=os.environ["SOCLAAS_BASE_URL"],
    api_key=os.environ["SOCLAAS_API_KEY"],
    timeout=180,  # generous: calls take ~2-10s with thinking off
    max_retries=0,  # _call_with_retries is the only retry loop
)


class Pacer:
    """Spaces requests evenly across worker threads (--rps)."""

    def __init__(self, rps: float):
        self.gap, self.next_at, self.lock = 1.0 / rps, time.monotonic(), threading.Lock()

    def wait(self):
        with self.lock:
            now = time.monotonic()
            slot = max(now, self.next_at)
            self.next_at = slot + self.gap
        time.sleep(max(0.0, slot - now))


_PACER = None  # set by main() when --rps is given


# ---------------------------------------------------------------------------
# Schemas, prompts, variations
# ---------------------------------------------------------------------------

for _cfg in ENTITY_CONFIG.values():
    _schema = json.loads(_cfg["schema"].read_text(encoding="utf-8"))
    Draft7Validator.check_schema(_schema)
    _cfg["validator"] = Draft7Validator(_schema)
    _cfg["props"] = _schema["properties"]
    _cfg["properties"] = list(_schema["properties"])
    # What the prompts ask for: the fields the schema marks x-filled-by "llm". Code or the
    # enricher fills the rest, so the LLM is never asked for them.
    _cfg["llm_fields"] = {
        k: v.get("description", "") for k, v in _schema["properties"].items() if v.get("x-filled-by") == "llm"
    }
    _cfg["pass_fields"] = [list(p) if p else list(_cfg["llm_fields"]) for p in _cfg["pass_fields"]]
    assert len(_cfg["pass_fields"]) == len(_cfg["prompts"]), "one pass_fields entry per prompt"
    assert all(set(p) <= set(_cfg["llm_fields"]) for p in _cfg["pass_fields"]), "pass_fields must be LLM fields"
    _cfg["templates"] = [(PROMPTS_DIR / p).read_text(encoding="utf-8").strip() for p in _cfg["prompts"]]
    for _key in ("review", "repair", "localise"):
        _cfg[f"{_key}_template"] = (PROMPTS_DIR / _cfg[_key]).read_text(encoding="utf-8").strip() if _cfg[_key] else None

VARIATIONS = json.loads((PROMPTS_DIR / "extract_variations.json").read_text(encoding="utf-8"))

# Tagging (tag_record): one call picks category/specialisation, a second picks skills from the
# chosen tracks. The wording and the fields read differ per entity type.
TAG_TEMPLATES = {k: (PROMPTS_DIR / f"tag_{k}.md").read_text(encoding="utf-8").strip()
                  for k in ("specialisation", "skills")}
TAG_ENTITY = {
    "HIRER": {
        "entity_label": "gig",
        "subject_rule": "The record is a GIG: a piece of work a hirer wants one specialist to do. "
                        "Tag the work to be done.",
        "skill_rule": "The record is a GIG. Choose the skills a specialist needs to do this work.",
        "text_fields": ("gig_title", "short_description", "additional_notes"),
    },
    "PROVIDER": {
        "entity_label": "provider profile",
        "subject_rule": "The record is a PROVIDER profile: one individual's own showcase. Tag the "
                        "service the person offers (the services first), supported by their "
                        "experience.",
        "skill_rule": "The record is a PROVIDER profile. Choose the skills the person clearly has and "
                      "would apply in the service they offer, as their experience shows.",
        "text_fields": ("title", "credentials", "about_headline", "about_bio", "services",
                        "achievements", "technical_proficiency"),
    },
}
# What a Singapore buyer reads, for the foreign-setting and anchor checks (localisation.py).
# Credentials are left out on purpose: they are personal facts and never localised.
SHOWN_FIELDS = {
    "HIRER": ("gig_title", "short_description"),
    "PROVIDER": ("title", "about_headline", "about_bio", "services", "achievements",
                 "technical_proficiency", "how_i_work"),
}


def roll_variations(entity_type: str, fname: str) -> tuple:
    """One weighted pick per roll in extract_variations.json. Each roll
    fills two prompt placeholders, {<roll>} (the option name) and
    {<roll>_instruction}. Seeded by file name so a rerun rolls the same."""
    rng = random.Random(f"variation:{fname}")
    kwargs, picked = {}, {}
    for roll, options in VARIATIONS.get(entity_type, {}).items():
        name = rng.choices(list(options), weights=[o["weight"] for o in options.values()], k=1)[0]
        picked[roll] = name
        kwargs[roll] = name
        kwargs[f"{roll}_instruction"] = options[name]["instruction"]
    return kwargs, picked


def _types(prop: dict) -> list:
    t = prop.get("type")
    return t if isinstance(t, list) else [t]


def _skeleton(prop: dict):
    """The empty JSON shape of a schema property, for the prompt: null for a scalar, [] for a
    list of scalars, [{...}] for a list of objects (so the model sees the item's keys)."""
    types = _types(prop)
    if "array" in types:
        items = prop.get("items", {})
        return [_skeleton(items)] if "object" in _types(items) else []
    if "object" in types:
        return {k: _skeleton(v) for k, v in prop.get("properties", {}).items()}
    return None


def _describe(prop: dict) -> str:
    """A property's description for the prompt's field list, with each key of a list of
    objects described too."""
    text = prop.get("description", "")
    items = prop.get("items", {})
    if "object" in _types(items):
        parts = "; ".join(f'"{k}": {v.get("description", "")}' for k, v in items.get("properties", {}).items())
        text += f" Each item has: {parts}"
    return text


def prompt_kwargs(entity_type: str, fname: str, rolls: dict, fields=None) -> dict:
    """The placeholders every prompt shares. `fields` is what this pass returns (default: every
    LLM field), so a pass that returns fewer is shown only those in its field list and skeleton."""
    cfg = ENTITY_CONFIG[entity_type]
    fields = list(fields or cfg["llm_fields"])
    return {
        **rolls,
        "field_block": "\n".join(f'- "{k}": {_describe(cfg["props"][k])}' for k in fields),
        "skeleton": json.dumps({k: _skeleton(cfg["props"][k]) for k in fields}, indent=2, ensure_ascii=False),
        "source_file": fname,
    }


def flatten_text(value) -> list:
    """Every string in a record value, however deeply nested (a list of services, a list of
    technical-proficiency groups), in order."""
    if isinstance(value, str):
        return [value]
    if isinstance(value, dict):
        return [s for v in value.values() for s in flatten_text(v)]
    if isinstance(value, (list, tuple)):
        return [s for v in value for s in flatten_text(v)]
    return []


def hirer_ref(fname: str) -> str:
    """A stable synthetic id for the hirer behind a gig, from the source file name. One hirer can
    post several gigs, but each crawled page yields one gig, so for now every record is its own
    hirer; grouping gigs under a shared hirer_ref would be a rule added here."""
    return "H-" + hashlib.sha1(fname.encode("utf-8")).hexdigest()[:8]


_DURATION_RE = re.compile(r"Engagement duration:\s*(\d+)(?:\s*(?:-|to|–)\s*(\d+))?\s*(week|month)", re.IGNORECASE)


def parse_duration_weeks(text) -> tuple:
    """(min, max) weeks from the "Engagement duration: 3-5 weeks." sentence, or (None, None).
    An LLM estimate, not a source fact. Months count as 4 weeks; anything over a year is
    treated as unparsed."""
    m = _DURATION_RE.search(text or "")
    if not m:
        return None, None
    lo = int(m.group(1))
    hi = int(m.group(2)) if m.group(2) else lo
    if m.group(3).lower() == "month":
        lo, hi = lo * 4, hi * 4
    lo, hi = min(lo, hi), max(lo, hi)
    return (lo, hi) if 1 <= lo and hi <= 52 else (None, None)


def _normalise(value, prop: dict):
    """Tidy a model's value for one schema property so a near-miss isn't a failed record: lists
    given as null, one object or a bulleted string become lists, blanks are dropped, lists are
    cut to maxItems, and "20 years" becomes 20. Whatever is still wrong is left for the schema
    check to reject."""
    types = _types(prop)
    if "array" in types:
        items = prop.get("items", {})
        if value is None:
            value = []
        elif isinstance(value, dict):
            value = [value]
        elif isinstance(value, str):
            value = [re.sub(r"^[-•*]\s*", "", ln.strip()) for ln in value.splitlines()]
        elif not isinstance(value, list):
            return value
        out = []
        for item in value:
            if isinstance(item, dict) and "object" not in _types(items):  # e.g. [{"achievement": "..."}]
                item = next((v for v in item.values() if isinstance(v, str)), None)
            item = _normalise(item, items)
            if item not in (None, "", [], {}):
                out.append(item)
        cap = prop.get("maxItems")
        return out[:cap] if cap else out
    if "object" in types:
        if not isinstance(value, dict):
            return value
        props = prop.get("properties", {})
        out = {k: (_normalise(v, props[k]) if k in props else v) for k, v in value.items()}
        return None if any(out.get(k) in (None, "", []) for k in prop.get("required", [])) else out
    if "integer" in types and not isinstance(value, bool):
        if isinstance(value, float):
            value = int(value)
        elif isinstance(value, str):
            m = re.search(r"\d+", value)
            value = int(m.group(0)) if m else None
        if isinstance(value, int) and not (prop.get("minimum", -10**9) <= value <= prop.get("maximum", 10**9)):
            return None
        return value
    if isinstance(value, str):
        return value.strip() or None
    return value


def _respell(value):
    """Singapore English spelling over every string in a value (localisation.singapore_spelling)."""
    if isinstance(value, str):
        return localisation.singapore_spelling(value)
    if isinstance(value, list):
        return [_respell(v) for v in value]
    if isinstance(value, dict):
        return {k: _respell(v) for k, v in value.items()}
    return value


# ---------------------------------------------------------------------------
# Anonymisation (provider pages)
# ---------------------------------------------------------------------------

NAME_PLACEHOLDER = "[CANDIDATE_NAME]"

try:
    import spacy
    _NLP = spacy.load("en_core_web_sm", exclude=["tagger", "parser", "lemmatizer", "attribute_ruler"])
except Exception:
    _NLP = None  # main() refuses to start without it

PRONOUN_MAP = [
    (r"\bhimself\b", "themself"), (r"\bHimself\b", "Themself"),
    (r"\bherself\b", "themself"), (r"\bHerself\b", "Themself"),
    (r"\bhe\b", "they"), (r"\bHe\b", "They"),
    (r"\bshe\b", "they"), (r"\bShe\b", "They"),
    (r"\bhim\b", "them"), (r"\bHim\b", "Them"),
    (r"\bhis\b", "their"), (r"\bHis\b", "Their"),
    (r"\bhers\b", "theirs"), (r"\bHers\b", "Theirs"),
    (r"\bher\b", "them"), (r"\bHer\b", "Them"),
]
LEFTOVER_PRONOUN_RE = re.compile(r"\b(he|him|his|she|her|hers|himself|herself)\b", re.IGNORECASE)


def mask_publisher(text: str, fname: str) -> str:
    """Swap the publishing firm's names (its domain stem plus PUBLISHER_ALIASES) for "the firm"
    before the model reads the page. Also swallows up to two capitalised words after the name
    ("PwC Canada", "Alvarez & Marsal GmbH"), so no qualifier is left dangling. That extension
    is case-sensitive so ordinary words are not grabbed."""
    stem = fname.split("__")[0].rsplit(".", 1)[0]
    for name in sorted([stem, *PUBLISHER_ALIASES.get(stem, [])], key=len, reverse=True):
        text = re.sub(
            rf"(?<!\w)(?i:{re.escape(name)})(?:\s+[A-Z][a-zA-Z]*){{0,2}}(?!\w)",
            "the firm", text)
    return text


_NLP_LOCK = threading.Lock()  # spaCy pipelines aren't documented as thread-safe; --workers shares one


def anonymise(text: str) -> str:
    if _NLP is not None:
        with _NLP_LOCK:
            ents = _NLP(text).ents
        names = {ent.text for ent in ents if ent.label_ == "PERSON"}
        for name in sorted(names, key=len, reverse=True):
            text = text.replace(name, NAME_PLACEHOLDER)
    for pattern, repl in PRONOUN_MAP:
        text = re.sub(pattern, repl, text)
    return text


# ---------------------------------------------------------------------------
# LLM calls
# ---------------------------------------------------------------------------

def _shows_reasoning(response) -> bool:
    """Whether the model reasoned ("thinking") before answering. Thinking is now off
    (NO_THINKING); the flag is still recorded so older records stay comparable."""
    message = response.choices[0].message
    content = message.content or ""
    extra = message.model_dump() if hasattr(message, "model_dump") else {}
    return "<think" in content.lower() or bool(extra.get("reasoning_content") or extra.get("reasoning"))


# Thinking is turned off. With it on, qwen3.8:27b used a median of about 11,800
# completion tokens (about 170 s) per record and made up most of the extraction time.
# `hidden_reasoning` is still recorded so rows from before the change stay comparable.
NO_THINKING = {"chat_template_kwargs": {"enable_thinking": False}}


def _call_llm(model: str, content: str, json_mode: bool = True) -> tuple:
    # JSON mode stops malformed JSON; every pool model accepts it. Only --ping asks
    # for plain text.
    extra = {"response_format": {"type": "json_object"}} if json_mode else {}
    if _PACER is not None:
        _PACER.wait()
    response = client.chat.completions.create(
        model=model, messages=[{"role": "user", "content": content}],
        max_completion_tokens=MAX_COMPLETION_TOKENS, extra_body=NO_THINKING, **extra)
    if json_mode and response.choices[0].finish_reason == "length":
        raise ValueError(f"reply hit the {MAX_COMPLETION_TOKENS}-token cap (runaway output?)")
    usage = {}
    if response.usage:
        usage = {
            "prompt_tokens": response.usage.prompt_tokens,
            "completion_tokens": response.usage.completion_tokens,
        }
    return response.choices[0].message.content or "", usage, _shows_reasoning(response)


def _parse_json(raw_output: str) -> dict:
    """Takes the outermost {...} rather than the whole reply, because some models wrap
    the JSON in a preamble or code fence. strict=False accepts raw newlines inside
    strings."""
    # reasoning inlined as <think>...</think> could itself contain braces
    raw_output = re.sub(r"<think>.*?</think>", "", raw_output, flags=re.DOTALL | re.IGNORECASE)
    start, end = raw_output.find("{"), raw_output.rfind("}")
    if start == -1 or end < start:
        raise ValueError(f"no JSON object in response: {raw_output[:120]!r}")
    data = json.loads(raw_output[start:end + 1], strict=False)
    if not isinstance(data, dict):
        raise ValueError("response was not a JSON object")
    return data


# Distinctive details from the prompts' own examples. A record containing one
# copied an example instead of the source.
PROMPT_EXAMPLE_LEAKS = (
    "9921894", "10203941", "USPTO patents", "S$5M engagement",
    "Computer Weekly", "40 services off mainframe", "from 3 days to 4 hours",
    # client-style examples (extract_hirer.md WHO IS HIRING, provider scope-limit
    # roll and relevant_experience shape); seen copied in the first v2 run
    "legal drafting or court representation", "payroll or HR administration",
    "general insurance agency with 40 staff", "six-outlet retail chain",
    "precision components maker", "chilled food distributor",
    # not "quantity surveyor specialising in construction disputes": it is the
    # honest description of hka.com's experts, so it blocked real records
)

# Records are anonymised: the text must not name the publishing firm. The domain stem
# (e.g. "kroll") is always checked; these are the other names a publisher goes by.
PUBLISHER_ALIASES = {
    "alvarezandmarsal": ["Alvarez & Marsal", "Alvarez and Marsal"],
    "bcg": ["Boston Consulting Group"],
    "erm": ["Environmental Resources Management"],
    "ey": ["Ernst & Young"],
    "fticonsulting": ["FTI Consulting", "FTI"],
    "grantthornton": ["Grant Thornton"],
    "pwc": ["PricewaterhouseCoopers"],
    "publicissapient": ["Publicis Sapient"],
    "rsmus": ["RSM"],
    "westmonroe": ["West Monroe"],
}
# Products that carry the publisher's name are tools the prompts say to keep ("IBM Power
# Systems" is a requirement, not the firm), so they are masked before the name check.
# Divisions ("IBM Consulting") are deliberately not listed.
PUBLISHER_PRODUCTS = {
    "ibm": ["Cloud", r"Power\w*", r"watsonx(?:\.\w+)?", r"Watson\w*", "FlashSystem", "Spectrum",
            "Instana", "Storage", "Granite", "Turbonomic", "Z", "i", "Quantum", "Apptio", "WebSphere",
            "Maximo", "Db2", "MQ", "Sterling", "Cognos", "SPSS", "Guardium", "QRadar",
            "API Connect", "z/OS", "Envizi", "DataPower", "mainframe"],
}
ORG_FIELDS = ("source_company", "source_company_team")  # metadata, allowed to name the publisher


def _join_items(items: list):
    """Models often itemise a multi-line field as a JSON list or dict, but the schema wants one
    string, so join it as "- " lines. For a dict, filled values become "key: value" lines; with
    no values, keys are kept only if they read as items (sentences), not labels."""
    if isinstance(items, dict):
        filled = [(k, v) for k, v in items.items() if isinstance(v, str) and v.strip()]
        if filled:
            items = [f"{k}: {v.strip()}" for k, v in filled]
        else:
            items = [k for k in items if " " in k.strip() and len(k.strip()) >= 20]
    lines = []
    for s in items:
        if isinstance(s, dict):  # e.g. [{"achievement": "..."}]
            s = next((v for v in s.values() if isinstance(v, str)), "")
        s = str(s).strip().lstrip("-•").strip()
        if s:
            lines.append(f"- {s}")
    return "\n".join(lines) or None


def _named_org(fname: str, doc: dict):
    """The first publisher name the record's shown text uses, or None. The
    publisher comes from the source file's domain (plus PUBLISHER_ALIASES)
    and the record's own source_company."""
    stem = fname.split("__")[0].rsplit(".", 1)[0]
    names = [stem, *PUBLISHER_ALIASES.get(stem, [])]
    if isinstance(doc.get("source_company"), str):
        names.append(doc["source_company"])
    text = " ".join(s for k, v in doc.items() if k not in ORG_FIELDS and k not in NON_TEXT_FIELDS
                    for s in flatten_text(v))
    products = PUBLISHER_PRODUCTS.get(stem)
    if products:
        # Product names matched case-sensitively, so "IBM powered the rollout" still counts
        text = re.sub(rf"(?<!\w)(?i:{re.escape(stem)})®?\s+(?:{'|'.join(products)})(?![\w/])", " ", text)
    for name in names:
        name = name.strip()
        if name and re.search(rf"(?<!\w){re.escape(name)}(?!\w)", text, re.IGNORECASE):
            return name
    return None


class ContentRejected(ValueError):
    """A reply the content checks refuse: it copied a prompt example, names the publisher, or
    lacks a gig title or description. Retried like any bad reply; if still refused, the page is
    REJECTED rather than errored, since the same model gives the same answer on every rerun."""


def _entity_doc(data: dict, entity_type: str, fname: str, model: str, source: str = "",
                base: dict = None, allowed=None):
    """A parsed extraction response -> schema-valid record, or None for {}. Raises on a schema
    mismatch so the caller retries.

    `allowed` is the fields this pass may return (default: every LLM field), and `base` the
    record so far, for a pass that returns only some fields: the reply is merged over it before
    the schema check. Keys the pass doesn't own are dropped, unknown keys are an error, and a
    blank reply for a field the record already has keeps the old value."""
    if data == {}:
        return None
    cfg = ENTITY_CONFIG[entity_type]
    props, base = cfg["props"], base or {}
    unknown = [k for k in data if k not in props]
    if unknown:
        raise ValueError(f"schema mismatch: unexpected key {unknown[0]!r}")
    allowed = set(allowed or cfg["llm_fields"])
    clean = {}
    for k, v in data.items():
        if k not in allowed:
            continue
        if isinstance(v, (list, dict)) and not {"array", "object"} & set(_types(props[k])):
            v = _join_items(v)  # a list given for a text field: join it as "- " lines
        v = _normalise(v, props[k])  # blank -> null, lists tidied, "20 years" -> 20
        # Singapore English spelling, by code: the prompts ask for it and the models often don't
        clean[k] = v if k in ORG_FIELDS else _respell(v)
    for k in allowed:
        if "array" in _types(props[k]) and k not in clean and k not in base:
            clean[k] = []  # a list field the model left out is an empty list
        if base.get(k) and clean.get(k) in (None, "", []):
            clean[k] = base[k]
    code_values = {"source_file": fname, "extracted_by_model": model}
    if entity_type == "HIRER":
        code_values["hirer_ref"] = hirer_ref(fname)
    doc = {**base, **clean, **{k: v for k, v in code_values.items() if k in props}}
    if entity_type == "PROVIDER" and not doc.get("services"):
        return None  # a showcase has at least one service; without one the page doesn't qualify
    if entity_type == "HIRER" and not (doc.get("gig_title") and doc.get("short_description")):
        # a skeleton of nulls where {} was meant (seen from qwen3.8:27b): not a gig
        raise ContentRejected("hirer record has no gig_title or short_description")
    errors = [e.message[:200] for e in cfg["validator"].iter_errors(doc)]
    if errors:
        raise ValueError(f"schema mismatch: {errors[0]}")
    text = " ".join(s for k, v in doc.items() if k not in NON_TEXT_FIELDS for s in flatten_text(v)).lower()
    # A phrase the source itself contains isn't a copy (seen: the real person
    # the patent example was taken from).
    leak = next((s for s in PROMPT_EXAMPLE_LEAKS if s.lower() in text and s.lower() not in source), None)
    if leak:
        raise ContentRejected(f"copied a prompt example ({leak!r}) instead of the source")
    org = _named_org(fname, doc)
    if org:
        raise ContentRejected(f"names {org!r}; organisations must be described generically")
    return doc


def _review_verdict(data: dict) -> dict:
    """A parsed review response -> {"decision": "keep"|"retry", "reason": str}."""
    decision = str(data.get("decision", "")).strip().lower()
    reason = data.get("reason")
    if decision not in ("keep", "retry"):
        raise ValueError(f"review decision must be keep or retry, got {data.get('decision')!r}")
    if not isinstance(reason, str) or not reason.strip():
        raise ValueError("review reason must be a non-empty string")
    return {"decision": decision, "reason": reason.strip()}


def _call_with_retries(model: str, content: str, validate, feedback: bool = False) -> tuple:
    """Returns (validate(parsed JSON), usage, hidden_reasoning). A parse or validation failure
    is retried like an API error. `model` stays fixed across retries, because switching would
    break llm_pool's deterministic file->model assignment.

    `feedback`: after a rejected REPLY (not an API error) the retry restates the reason, so
    the model isn't asked the same question again. Used by the tagging calls."""
    last_err, prompt = None, content
    for attempt in range(1, MAX_RETRIES + 1):
        replied = False
        try:
            raw_output, usage, reasoning = _call_llm(model, prompt)
            replied = True
            return validate(_parse_json(raw_output)), usage, reasoning
        except Exception as e:
            last_err = e
            if feedback and replied:
                prompt = (f"{content}\n\nYOUR PREVIOUS REPLY WAS REJECTED: {e}\n"
                          f"Fix exactly that, using only the names listed above, and return the corrected JSON.")
            if attempt < MAX_RETRIES:
                wait_s = RETRY_BACKOFF_S * (2 ** (attempt - 1))
                print(f"    [RETRY] attempt {attempt}/{MAX_RETRIES} failed ({e}); retrying in {wait_s}s", flush=True)
                time.sleep(wait_s)
    raise last_err


def _record_json(entity_type: str, doc: dict) -> str:
    """The LLM-written part of a record, as handed to a later pass."""
    fields = ENTITY_CONFIG[entity_type]["llm_fields"]
    return json.dumps({k: doc.get(k) for k in fields}, ensure_ascii=False, indent=2)


def _shown_text(entity_type: str, doc: dict) -> list:
    """The record's text a Singapore buyer reads (SHOWN_FIELDS: not the credentials), for the
    foreign-setting check."""
    return [s for k in SHOWN_FIELDS[entity_type] for s in flatten_text(doc.get(k))]


# A repair that blanks one of these has traded a foreign phrase for lost content.
_KEEP_FILLED = ("about_bio", "services", "achievements")
MAX_LOCALISE_PASSES = 2
# Said to the repair prompt when a profile never mentions Singapore. The client's providers
# all name a Singapore body or place; one with none reads as written for another market.
NO_ANCHOR_NOTE = ("The record never mentions Singapore, S$ or any Singapore law, regulator or scheme. In "
                  "services_offered_description make the \"who it is for\" clause name Singapore businesses "
                  "(e.g. \"for Singapore SMEs and family businesses\") and, where one plainly governs the "
                  "service, name ONE Singapore law, regulator or standard (e.g. MAS for financial services, "
                  "IRAS for tax, the IRDA for restructuring, PDPA for data protection, the WSH Act for "
                  "workplace safety). Name only one that fits the work, and never give the person a Singapore "
                  "licence, registration, employer or client.")


def localise_provider(doc: dict, extract_call, kwargs: dict) -> tuple:
    """Singapore check on a finished provider record (localisation.py), then up to
    MAX_LOCALISE_PASSES repair passes (prompts/repair_localise_provider.md), each told exactly
    what is still wrong. A record is flagged for foreign phrases or for having no Singapore
    anchor at all. The prompts already ask for a Singapore setting, but the models follow that
    unevenly, so this is the deterministic net.

    A rewrite replaces the record only if it has fewer problems and no field went blank, and
    the first pass that doesn't improve things ends the loop. A leftover is not an error (some
    are right to keep); the manifest records what was flagged and what remained. Returns
    (doc, meta)."""
    shown = lambda d: _shown_text("PROVIDER", d)
    problems = lambda d: (localisation.foreign_residue(shown(d)), not localisation.singapore_anchor(shown(d)))
    cost = lambda p: len(p[0]) + (1 if p[1] else 0)
    residue, no_anchor = problems(doc)
    meta = {"localisation_residue": residue, "localisation_no_anchor": no_anchor, "localisation_passes": 0}
    if not residue and not no_anchor:
        return doc, meta
    meta["localisation_repaired"] = False
    for _ in range(MAX_LOCALISE_PASSES):
        todo = [f"- {p}" for p in residue]
        if no_anchor:
            todo.append("- " + NO_ANCHOR_NOTE)
        repaired = extract_call(ENTITY_CONFIG["PROVIDER"]["localise_template"].format(
            **kwargs, problems="\n".join(todo), previous_record=_record_json("PROVIDER", doc)))
        meta["localisation_passes"] += 1
        if repaired is None:
            break
        after = problems(repaired)
        blanked = [k for k in _KEEP_FILLED if doc.get(k) and not repaired.get(k)]
        meta["localisation_blanked"] = blanked
        if blanked or cost(after) >= cost((residue, no_anchor)):
            break
        doc, (residue, no_anchor), meta["localisation_repaired"] = repaired, after, True
        if not residue and not no_anchor:
            break
    meta.update(localisation_residue_after=residue, localisation_no_anchor_after=no_anchor)
    return doc, meta


def tag_record(entity_type: str, doc: dict, fname: str) -> tuple:
    """SkillsFuture tags for a finished record, read from its own text (the ranker compares gig
    tags with provider tags, so they must describe the records it sees). Two calls to one
    model, chosen by file name with its own stage salt:
      1. category + specialisation (sector + track pairs, at most 3 tracks in 2 sectors),
      2. skills from the chosen tracks' own lists (taxonomy.skills_block), 1-8.
    Returns (the record's `tags` block, meta). `categories` is empty when the record fits no
    track, which is valid, so no skills are asked for. An invalid reply is retried and errors
    the file if it never validates."""
    cfg = TAG_ENTITY[entity_type]
    model = model_for_file(fname, "tag")
    record = "RECORD:\n```json\n" + json.dumps(
        {k: doc[k] for k in cfg["text_fields"] if doc.get(k)}, ensure_ascii=False, indent=2) + "\n```"
    kwargs = {k: cfg[k] for k in ("entity_label", "subject_rule", "skill_rule")}
    usage = {"prompt_tokens": 0, "completion_tokens": 0}

    def ask(name: str, check, **extra):
        content = f"{TAG_TEMPLATES[name].format(**kwargs, **extra)}\n\n{record}"
        result, call_usage, _ = _call_with_retries(model, content, check, feedback=True)
        for k in usage:
            usage[k] += call_usage.get(k) or 0
        return result

    meta = {"model": model, "usage": usage}
    try:
        pairs, why = ask("specialisation", lambda d: (taxonomy.parse_specialisations(d), d.get("reason")),
                         taxonomy_block=taxonomy.sector_track_block())
        meta.update(no_fit=not pairs, reason_specialisation=why)
        if not pairs:
            return taxonomy.nest([], []), meta
        (skills, dropped), why = ask("skills", lambda d: (taxonomy.parse_skills(d, pairs), d.get("reason")),
                                     skills_block=taxonomy.skills_block(pairs))
    except ValueError as e:
        # The model kept giving a sector/track pair the framework doesn't have. The extraction
        # itself is fine, so the record is written untagged (reason kept) instead of discarded.
        # Only a reply failing validation lands here; an API failure still errors the file.
        return taxonomy.nest([], []), {**meta, "no_fit": True, "tag_error": str(e)[:200]}
    return taxonomy.nest(pairs, skills), {**meta, "reason_skills": why, "dropped_skills": dropped}


def extract_entity(text: str, entity_type: str, model: str, fname: str) -> tuple:
    """Runs the entity type's prompt passes in order, then, if it has a review prompt, the
    grounding review, at most one repair, and a second review of that repair. Returns
    (document or None if the page doesn't qualify, the extracting model's usage, meta). The
    reviewer's own usage is in meta["review"]."""
    cfg = ENTITY_CONFIG[entity_type]
    rolls, picked = roll_variations(entity_type, fname)
    kwargs = prompt_kwargs(entity_type, fname, rolls)
    if cfg["anonymise"]:
        text = anonymise(mask_publisher(text, fname))
    validate = functools.partial(_entity_doc, entity_type=entity_type, fname=fname, model=model,
                                 source=text.lower())

    source = f"SOURCE MATERIAL:\n```\n{text[:MAX_CHARS]}\n```"
    usage_total = {"prompt_tokens": 0, "completion_tokens": 0}
    meta = {"rolls": picked, "hidden_reasoning": False}

    def call(call_model: str, content: str, check) -> tuple:
        result, usage, reasoning = _call_with_retries(call_model, content, check)
        meta["hidden_reasoning"] = meta["hidden_reasoning"] or reasoning
        return result, usage

    def extract_call(content: str, check=None):
        doc, usage = call(model, content, check or validate)
        for k in usage_total:
            usage_total[k] += usage.get(k) or 0
        return doc

    # Each pass returns its own fields (cfg["pass_fields"]); a later pass's reply is merged
    # over the record so far, so what it doesn't return is carried over untouched.
    doc, payload = None, source
    for template, fields in zip(cfg["templates"], cfg["pass_fields"]):
        pass_kwargs = prompt_kwargs(entity_type, fname, rolls, fields)
        doc = extract_call(f"{template.format(**pass_kwargs)}\n\n{payload}",
                           functools.partial(validate, base=doc, allowed=fields))
        if doc is None:
            break
        payload = f"INPUT RECORD:\n```json\n{_record_json(entity_type, doc)}\n```"

    # A provider's finished text is checked for a foreign setting and, if it has one,
    # repaired (up to MAX_LOCALISE_PASSES times). A hirer is only measured: its reviewer already judges the setting.
    if doc is not None and cfg["localise_template"] and quality_check(entity_type, doc)[0]:
        doc, local_meta = localise_provider(doc, extract_call, kwargs)
        meta.update(local_meta)
    elif doc is not None:
        meta["localisation_residue"] = localisation.foreign_residue(_shown_text(entity_type, doc))

    # Only review what would otherwise be written. The reviewer is always a
    # different model than the extractor, so nothing grades its own output.
    if doc is not None and cfg["review_template"] and quality_check(entity_type, doc)[0]:
        reviewer = reviewer_for_file(fname, model)

        def review(rec: dict) -> dict:
            prompt = (f"{cfg['review_template'].format(**kwargs)}\n\n{source}\n\n"
                      f"GENERATED RECORD:\n```json\n{_record_json(entity_type, rec)}\n```")
            verdict, usage = call(reviewer, prompt, _review_verdict)
            return {"model": reviewer, **verdict, "usage": usage}

        meta["review"] = review(doc)
        if meta["review"]["decision"] == "retry":
            repair = cfg["repair_template"].format(
                **kwargs, review_reason=meta["review"]["reason"], previous_record=_record_json(entity_type, doc))
            doc = extract_call(f"{cfg['templates'][0].format(**kwargs)}\n\n{repair}\n\n{source}")
            meta["repaired"] = True
            # The rewrite is reviewed once more; one that's still flagged isn't
            # written (seen: a repair that put the client's name back in).
            if doc is not None and quality_check(entity_type, doc)[0]:
                meta["review_after_repair"] = review(doc)
                if meta["review_after_repair"]["decision"] == "retry":
                    doc = None

    # Tags come last, from the finished text, and only for a record that will be written.
    if doc is not None and quality_check(entity_type, doc)[0]:
        meta["tags"], meta["tag"] = tag_record(entity_type, doc, fname)
    return doc, usage_total, meta


# ---------------------------------------------------------------------------
# Quality checks (independent of what the LLM claims)
# ---------------------------------------------------------------------------

def _norm(s) -> str:
    return re.sub(r"\s+", " ", s.strip()) if isinstance(s, str) else ""


def quality_check(entity_type: str, doc: dict) -> tuple:
    if entity_type == "HIRER":
        title = _norm(doc.get("gig_title"))
        desc = _norm(doc.get("short_description"))
        if not title or title.lower() in GENERIC_TITLE_BLOCKLIST:
            return False, f"no credible gig title (got {title!r})"
        if len(desc) < 30:
            return False, f"short_description too short ({len(desc)} chars, need >=30)"
        return True, ""

    fields = ENTITY_CONFIG["PROVIDER"]["llm_fields"]
    if any(NAME_PLACEHOLDER in s for k in fields for s in flatten_text(doc.get(k))):
        return False, f"{NAME_PLACEHOLDER} placeholder leaked into the profile"
    substantive = sum(1 for k in ("about_headline", "about_bio", "services", "achievements", "technical_proficiency")
                      if len(_norm(" ".join(flatten_text(doc.get(k))))) >= 15)
    if substantive < 2:
        return False, f"only {substantive} substantive field(s) present, need >=2"
    return True, ""


def record_metrics(entity_type: str, doc: dict) -> dict:
    fields = ENTITY_CONFIG[entity_type]["llm_fields"]
    texts = {k: " ".join(flatten_text(doc.get(k))) for k in fields}
    texts = {k: v for k, v in texts.items() if v}
    return {
        "field_chars": {k: len(v) for k, v in texts.items()},
        "leftover_pronouns": len(LEFTOVER_PRONOUN_RE.findall(" ".join(texts.values()))),
    }


# ---------------------------------------------------------------------------
# CSV output
# ---------------------------------------------------------------------------

def csv_fields(entity_type: str) -> list:
    """source_file first, then CSV_COLUMNS (the v1 text columns derived by flat_columns(), plus a
    few structured fields), then bookkeeping. time_taken_by_model is the seconds spent
    extracting the row, including a hirer's review and repair and any retry waits.

    The roll_* tail is this entity type's style rolls from extract_variations.json, so the CSV
    shows which wording variant produced each row. Adding a roll there adds its column here
    (and changes the header, see check_csv_headers).

    INDUSTRY_FIELDS come from industry.py's manifest, so the CSVs can be split by industry
    without a join. TAG_FIELDS are the SkillsFuture tags: flat " | "-joined columns plus
    tags_json, the nested form."""
    return (["source_file", *CSV_COLUMNS[entity_type]]
            + ["classify_label", *INDUSTRY_FIELDS, *TAG_FIELDS, "extracted_at", "time_taken_by_model"]
            + [f"roll_{k}" for k in VARIATIONS.get(entity_type, {})])


def finalize_record(entity_type: str, doc: dict, tags: dict) -> dict:
    """The full v2 record (ML_*_schema_v2.json) for a finished extraction: the LLM-written
    fields, the ones code fills, and the tags block, in schema order and validated against the
    schema. Raises if it doesn't validate, which would be a bug here, not a bad reply."""
    cfg = ENTITY_CONFIG[entity_type]
    rec = {}
    for k, prop in cfg["props"].items():
        if k == "tags":
            rec[k] = tags or taxonomy.nest([], [])
        elif k in doc:
            rec[k] = doc[k]
        else:
            rec[k] = [] if "array" in _types(prop) else None
    if entity_type == "HIRER":
        rec["duration_weeks_min"], rec["duration_weeks_max"] = parse_duration_weeks(rec["short_description"])
    errors = [e.message[:200] for e in cfg["validator"].iter_errors(rec)]
    if errors:
        raise ValueError(f"final record doesn't match its schema: {errors[0]}")
    return rec


def _experience_text(rec: dict):
    """The v1 relevant_experience text from a provider record: the tenure as a sentence, the
    achievements, then the credentials."""
    parts = []
    if rec.get("years_experience"):
        parts.append(f"{rec['years_experience']} years of experience.")
    parts += rec.get("achievements") or []
    if rec.get("credentials"):
        parts.append("Credentials: " + "; ".join(rec["credentials"]) + ".")
    return " ".join(parts) or None


def flat_columns(entity_type: str, rec: dict) -> dict:
    """The CSV_COLUMNS values for a v2 record: the v1 text columns derived from the new fields
    (so the enricher, labeller and ranker import don't change) plus the structured extras."""
    if entity_type == "HIRER":
        return {
            "extracted_by_model": rec["extracted_by_model"],
            "source_company": rec.get("source_company"),
            "source_company_team": rec.get("source_company_team"),
            "hire_title": rec["gig_title"],
            "hire_description": rec["short_description"],
            "hire_description_additional_notes": rec.get("additional_notes"),
            "hirer_ref": rec["hirer_ref"],
            "duration_weeks_min": rec.get("duration_weeks_min"),
            "duration_weeks_max": rec.get("duration_weeks_max"),
        }
    services = rec["services"]
    return {
        "extracted_by_model": rec["extracted_by_model"],
        "about_title": rec.get("about_headline"),
        "about_description": rec.get("about_bio"),
        "services_offered_title": services[0]["service_title"],
        # one service reads as before; several are all kept, each under its title, so the
        # text the ranker matches on holds every service the profile offers
        "services_offered_description": (services[0]["service_detail"] if len(services) == 1 else
                                         " ".join(f"{s['service_title']}: {s['service_detail']}" for s in services)),
        "relevant_experience": _experience_text(rec),
        "years_experience": rec.get("years_experience"),
    }


def append_jsonl(path: Path, rec: dict) -> None:
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")


def export_json() -> None:
    """Collect each entity type's .jsonl of v2 records into a .json array next to it
    (hirers.json, providers.json), one record per source file with the latest winning. Runs at
    the end of every extraction and on its own with --export-json."""
    for entity_type, cfg in ENTITY_CONFIG.items():
        src = cfg["jsonl"]
        if not src.exists():
            continue
        records = {}
        for line in src.read_text(encoding="utf-8").splitlines():
            if line.strip():
                rec = json.loads(line)
                records[rec["source_file"]] = rec
        dest = src.with_suffix(".json")
        dest.write_text(json.dumps(list(records.values()), ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"{dest.name}: {len(records)} {entity_type.lower()} records", flush=True)


def _csv_safe(v):
    """Guards against CSV-formula injection if the file is opened in Excel or Sheets, since
    scraped text is untrusted. "-" is excluded because itemised fields are joined as "- " lines
    and would otherwise get a stray apostrophe."""
    s = "" if v is None else str(v)
    return "'" + s if s[:1] in ("=", "+", "@", "\t", "\r") else s


def append_csv_row(path: Path, fieldnames: list, row: dict) -> None:
    is_new = not path.exists()
    with path.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        if is_new:
            writer.writeheader()
        writer.writerow({k: _csv_safe(row.get(k)) for k in fieldnames})


def check_csv_headers() -> None:
    """A schema edit changes the columns; appending to a CSV written under the
    old schema would silently misalign every row after it."""
    for entity_type, cfg in ENTITY_CONFIG.items():
        if cfg["csv"].exists():
            with cfg["csv"].open(newline="", encoding="utf-8") as f:
                header = next(csv.reader(f), [])
            if header != csv_fields(entity_type):
                if set(header) < set(csv_fields(entity_type)):
                    missing = [c for c in csv_fields(entity_type) if c not in header]
                    raise SystemExit(
                        f"{cfg['csv'].name} predates some of the current columns ({', '.join(missing)}). "
                        f"Run extract.py --backfill-industries once to migrate it in place.")
                raise SystemExit(
                    f"{cfg['csv'].name} was written under a different schema (columns differ from "
                    f"{cfg['schema'].name}). Move it and {EXTRACT_MANIFEST_PATH.name} aside and rerun."
                )


def backfill_industries() -> None:
    """Rewrites both CSVs with the current industry tags, joined on source_file, with no LLM
    calls. Also adds columns that newer code fills (blank unless filled here). Refuses a CSV
    with columns the code doesn't know, since that means a schema change. The first rewrite
    keeps a copy as <name>.pre_industry.bak."""
    industries = load_industries()
    for entity_type, cfg in ENTITY_CONFIG.items():
        path, fields = cfg["csv"], csv_fields(entity_type)
        if not path.exists():
            continue
        with path.open(newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            header, rows = reader.fieldnames or [], list(reader)
        unknown = [c for c in header if c not in fields]
        if unknown:
            raise SystemExit(f"{path.name} has columns this code doesn't know ({', '.join(unknown)}); "
                             f"that's a schema change, not something to backfill.")
        filled = 0
        for row in rows:
            tag = industries.get(row["source_file"])
            if tag:
                row.update({k: tag.get(k) or "" for k in INDUSTRY_FIELDS})
                filled += 1
        backup = path.with_name(path.name + ".pre_industry.bak")
        if not backup.exists():
            backup.write_bytes(path.read_bytes())
        tmp = path.with_name(path.name + ".tmp")
        with tmp.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()
            writer.writerows({k: row.get(k) or "" for k in fields} for row in rows)
        tmp.replace(path)
        print(f"{path.name}: {filled}/{len(rows)} rows have an industry tag", flush=True)


# ---------------------------------------------------------------------------
# Manifest / progress tracking
# ---------------------------------------------------------------------------

def load_classified_files() -> list:
    """Every (file, label) worth extracting from classify.py's manifest,
    re-read fresh each call so --watch mode picks up files classify.py
    appends while this keeps running."""
    items = []
    if not CLASSIFY_MANIFEST_PATH.exists():
        return items
    with CLASSIFY_MANIFEST_PATH.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            record = json.loads(line)
            if record.get("status") != "ok":
                continue
            label = record.get("label")
            if label in ENTITY_TYPE_FOR_LABEL:
                items.append((record["file"], label))
    return items


def load_industries() -> dict:
    """{filename: industry record} from industry.py's manifest, the latest
    record per file winning. Re-read on each call like the others, so
    --watch picks up files industry.py tags while this keeps running."""
    industries = {}
    if not INDUSTRY_MANIFEST_PATH.exists():
        return industries
    with INDUSTRY_MANIFEST_PATH.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            record = json.loads(line)
            if record.get("status") == "ok" and record.get("industry"):
                industries[record["file"]] = record
    return industries


def balance_pending(pending: list, per_cell: int = None) -> list:
    """Reorder `pending` so extraction spends its calls evenly across (entity_type, industry)
    cells instead of following manifest order, which is dominated by the domains that produced
    the most pages (kroll, bcg and alvarezandmarsal are about 47% of everything extractable).

    Files are grouped by cell and taken round-robin, one per cell; a cell that runs out drops
    out of the rotation. `per_cell` caps how many files one cell contributes this run, and the
    rest stay pending. Files industry.py hasn't tagged go in an "(untagged)" cell so extraction
    doesn't stall. Order within a cell is unchanged, so a rerun gives the same order."""
    industries = load_industries()
    cells = {}
    for fname, label in pending:
        key = (ENTITY_TYPE_FOR_LABEL[label], industries.get(fname, {}).get("industry", "(untagged)"))
        cells.setdefault(key, []).append((fname, label))

    if per_cell is not None:
        cells = {k: v[:per_cell] for k, v in cells.items()}

    ordered = []
    queues = list(cells.values())
    while queues:
        for q in queues:
            ordered.append(q.pop(0))
        queues = [q for q in queues if q]
    return ordered


def load_extract_progress() -> dict:
    done = {}
    if EXTRACT_MANIFEST_PATH.exists():
        with EXTRACT_MANIFEST_PATH.open("r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                record = json.loads(line)
                if record.get("status") == "error":
                    continue  # retryable, not "done"
                done[record["file"]] = record
    return done


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def process_file(fname: str, label: str, industry: dict = None) -> tuple:
    """Extracts one file and returns (manifest record, CSV row or None, log line). Writes
    nothing itself, so several can run at once (--workers) while main() stays the only writer.
    `industry` is the file's record from data/manifests/industry.jsonl, if any."""
    entity_type = ENTITY_TYPE_FOR_LABEL[label]
    cfg = ENTITY_CONFIG[entity_type]
    bucket = label.lower()
    src = BUCKET_DIRS[label] / fname
    timestamp = datetime.now().isoformat(timespec="seconds")

    if not src.exists():
        record = {"file": fname, "status": "error", "reason": "source file missing", "timestamp": timestamp}
        return record, None, f"{bucket}/{fname} -> ERROR (source file missing)"

    text = src.read_text(encoding="utf-8", errors="ignore")
    model = model_for_file(fname, "extract")
    start = time.perf_counter()

    try:
        doc, usage, meta = extract_entity(text, entity_type, model, fname)
    except ContentRejected as e:  # still refused after the retries: not retryable, so rejected
        elapsed = round(time.perf_counter() - start, 2)
        record = {"file": fname, "entity_type": entity_type, "model": model, "elapsed": elapsed,
                  "status": "rejected", "reason": f"content check, after retries: {e}", "timestamp": timestamp}
        return record, None, f"{bucket}/{fname} ({model}) -> REJECTED  ({record['reason']})"
    except Exception as e:
        record = {
            "file": fname, "entity_type": entity_type, "model": model,
            "status": "error", "reason": f"api_error: {e}", "timestamp": timestamp,
        }
        return record, None, f"{bucket}/{fname} ({model}) -> ERROR  ({e})"

    elapsed = round(time.perf_counter() - start, 2)
    base = {
        "file": fname, "entity_type": entity_type, "model": model, "usage": usage,
        "elapsed": elapsed, **meta, "timestamp": timestamp,
    }
    if doc is None:
        ok = False
        if meta.get("review_after_repair", {}).get("decision") == "retry":
            reason = f"still flagged after repair: {meta['review_after_repair']['reason']}"
        elif meta.get("repaired"):
            reason = "repair judged the page non-qualifying (model returned {})"
        else:
            reason = "page doesn't qualify (model returned {})"
    else:
        ok, reason = quality_check(entity_type, doc)
    note = f" [repaired after review: {meta['review']['reason']}]" if meta.get("repaired") else ""

    if ok:
        try:
            rec = finalize_record(entity_type, doc, meta.get("tags"))
        except Exception as e:  # a bug here, not a bad reply: error the file so it is redone
            record = {**base, "status": "error", "reason": f"api_error: {e}"}
            return record, None, f"{bucket}/{fname} ({model}) -> ERROR  ({e})"
        # "_v2" is the nested record for the .jsonl; the CSV writer ignores it
        row = {**flat_columns(entity_type, rec), "source_file": fname, "classify_label": label,
               "extracted_at": timestamp, "time_taken_by_model": elapsed,
               **{k: (industry or {}).get(k) for k in INDUSTRY_FIELDS},
               **taxonomy.csv_columns(meta.get("tags")),
               **{f"roll_{k}": v for k, v in (meta.get("rolls") or {}).items()},
               "_v2": rec}
        title = doc.get(cfg["title_field"])
        record = {**base, "status": "written", "title": title, "metrics": record_metrics(entity_type, doc)}
        return record, row, f"{bucket}/{fname} ({model}) -> WRITTEN ({entity_type}: {title}){note}"
    record = {**base, "status": "rejected", "reason": reason}
    return record, None, f"{bucket}/{fname} ({model}) -> REJECTED  ({reason}){note}"


def _results(pending: list, workers: int):
    """Yields process_file() results: in file order with one worker, else in
    completion order from a thread pool. Closing the generator early cancels
    files not started yet; ones already in flight finish unwritten and are
    simply redone next run."""
    industries = load_industries()
    if workers <= 1:
        for fname, label in pending:
            yield process_file(fname, label, industries.get(fname))
        return
    ex = ThreadPoolExecutor(max_workers=workers)
    futures = [ex.submit(process_file, fname, label, industries.get(fname)) for fname, label in pending]
    try:
        for fut in as_completed(futures):
            yield fut.result()
    finally:
        ex.shutdown(wait=True, cancel_futures=True)


def use_out_tag(tag: str) -> None:
    """Point every output (both CSVs, the nested .jsonl / .json records and the progress
    manifest) at a tagged copy, e.g. "v2" -> data/output/hirers_v2.csv and
    data/manifests/extract_v2.jsonl. Progress is tracked per tag, so a tagged run re-extracts
    every file whatever the untagged run did."""
    global PROVIDERS_CSV, HIRERS_CSV, PROVIDERS_JSONL, HIRERS_JSONL, EXTRACT_MANIFEST_PATH
    PROVIDERS_CSV = OUTPUT_DIR / f"providers_{tag}.csv"
    HIRERS_CSV = OUTPUT_DIR / f"hirers_{tag}.csv"
    PROVIDERS_JSONL = OUTPUT_DIR / f"providers_{tag}.jsonl"
    HIRERS_JSONL = OUTPUT_DIR / f"hirers_{tag}.jsonl"
    EXTRACT_MANIFEST_PATH = MANIFESTS_DIR / f"extract_{tag}.jsonl"
    ENTITY_CONFIG["PROVIDER"]["csv"] = PROVIDERS_CSV
    ENTITY_CONFIG["HIRER"]["csv"] = HIRERS_CSV
    ENTITY_CONFIG["PROVIDER"]["jsonl"] = PROVIDERS_JSONL
    ENTITY_CONFIG["HIRER"]["jsonl"] = HIRERS_JSONL


def ping() -> None:
    for model in MODEL_POOL:
        start = time.perf_counter()
        try:
            raw, _, reasoning = _call_llm(model, "Reply with exactly: OK", json_mode=False)
            note = "  (reasoned before answering)" if reasoning else ""
            print(f"{model}: OK in {time.perf_counter() - start:.1f}s -> {raw.strip()!r}{note}", flush=True)
        except Exception as e:
            print(f"{model}: FAILED after {time.perf_counter() - start:.1f}s -- {type(e).__name__}: {e}", flush=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--watch", action="store_true",
        help="keep running after the initial backlog is extracted, checking for new "
             "qualifying files as classify.py appends to its manifest",
    )
    parser.add_argument(
        "--poll-interval", type=float, default=10.0,
        help="seconds to wait between rescans in --watch mode when nothing new was found (default: 10)",
    )
    parser.add_argument(
        "--limit", type=int, default=None,
        help="process at most this many files then stop (with --entity, of that type)",
    )
    parser.add_argument(
        "--balance", action="store_true",
        help="spend extraction calls evenly across (entity_type, industry) cells instead of in "
             "manifest order, so the CSVs don't inherit the corpus's skew toward a few domains. "
             "Needs data/manifests/industry.jsonl (classifier_extractor/industry.py)",
    )
    parser.add_argument(
        "--per-cell", type=int, default=None,
        help="with --balance, cap how many files any one (entity_type, industry) cell contributes "
             "this run; over-cap files stay pending rather than being spent",
    )
    parser.add_argument(
        "--entity", choices=["hirer", "provider"], default=None,
        help="extract only hirer pages (-> hirers.csv) or only provider pages, i.e. PROVIDER and "
             "UNCERTAIN (-> providers.csv). Default: both",
    )
    parser.add_argument("--ping", action="store_true", help="check every pool model responds, then exit")
    parser.add_argument("--workers", type=int, default=4, help="files to extract at once (default: 4)")
    parser.add_argument(
        "--rps", type=float, default=1.0,
        help="cap on requests/second across all workers (SOCLAAS sustains ~1/s per key, shared "
             "with anything else running on it; default: 1, 0 for no cap)",
    )
    parser.add_argument(
        "--backfill-industries", action="store_true",
        help="rewrite both CSVs with the current industry tags from data/manifests/industry.jsonl "
             "(no LLM calls), migrating a CSV that predates the industry columns, then exit",
    )
    parser.add_argument(
        "--out-tag", default=None,
        help="write to data/output/hirers_TAG.csv, providers_TAG.csv, the matching .jsonl / .json records "
             "and data/manifests/extract_TAG.jsonl instead of the untagged files, with progress tracked separately "
             "(e.g. --out-tag v2)",
    )
    parser.add_argument(
        "--export-json", action="store_true",
        help="rebuild hirers.json / providers.json (JSON arrays) from the .jsonl records written so far "
             "(no LLM calls), then exit; a normal run does this at its end",
    )
    args = parser.parse_args()
    global _PACER
    _PACER = Pacer(args.rps) if args.rps else None
    if args.out_tag:
        use_out_tag(args.out_tag)

    if args.ping:
        ping()
        return
    if args.export_json:
        export_json()
        return
    if args.backfill_industries:
        backfill_industries()
        return

    check_csv_headers()
    if _NLP is None:
        raise SystemExit(
            "spaCy/en_core_web_sm isn't installed, so person names on provider pages can't be masked. "
            "Install it first: pip install spacy && python -m spacy download en_core_web_sm"
        )

    LOGS_DIR.mkdir(exist_ok=True)
    PID_PATH.write_text(str(os.getpid()), encoding="utf-8")
    try:
        run(args)
    finally:
        if PID_PATH.exists() and PID_PATH.read_text(encoding="utf-8").strip() == str(os.getpid()):
            PID_PATH.unlink()  # leave another instance's PID file alone


def run(args) -> None:
    already_done = load_extract_progress()
    consecutive_errors = 0
    aborted = False
    processed_this_run = 0
    idle_announced = False  # log "waiting" once per idle stretch, not every poll

    with EXTRACT_MANIFEST_PATH.open("a", encoding="utf-8") as manifest:
      while True:
        all_items = load_classified_files()
        if args.entity:
            # Before --balance and --limit, so both apply within the chosen entity type.
            all_items = [it for it in all_items if ENTITY_TYPE_FOR_LABEL[it[1]] == args.entity.upper()]
        pending = [it for it in all_items if it[0] not in already_done]
        if args.balance:
            # Before --limit, so a limited run still draws evenly across cells
            # rather than taking its whole quota from the first one.
            pending = balance_pending(pending, args.per_cell)
        if args.limit is not None:
            pending = pending[: max(0, args.limit - processed_this_run)]

        if not pending:
            if not args.watch or (args.limit is not None and processed_this_run >= args.limit):
                print(f"{len(all_items)} qualifying files total; {len(already_done)} already processed", flush=True)
                break
            if not idle_announced:
                print(f"  [WATCH] idle ({len(already_done)} done) -- waiting for new files from classify.py...", flush=True)
                idle_announced = True
            time.sleep(args.poll_interval)
            continue

        idle_announced = False
        print(f"{len(pending)} new file(s) to extract ({len(already_done)} already done)", flush=True)

        results = _results(pending, args.workers)
        try:
            for i, (record, row, line) in enumerate(results, 1):
                if row is not None:  # CSV and .jsonl before manifest, so the manifest never claims an unwritten row
                    entity_type = record["entity_type"]
                    append_csv_row(ENTITY_CONFIG[entity_type]["csv"], csv_fields(entity_type), row)
                    append_jsonl(ENTITY_CONFIG[entity_type]["jsonl"], row["_v2"])
                manifest.write(json.dumps(record) + "\n")
                manifest.flush()
                print(f"[{i}/{len(pending)}] {line}", flush=True)

                if record["status"] == "error" and record["reason"].startswith("api_error"):
                    consecutive_errors += 1  # retryable, so not marked done
                    if consecutive_errors >= MAX_CONSECUTIVE_ERRORS:
                        print(
                            f"\n[ABORT] {consecutive_errors} extraction errors in a row -- stopping so the "
                            f"remaining {len(pending) - i} files aren't ground through blindly. Fix the "
                            f"underlying issue and rerun; already-processed files are untouched.",
                            flush=True,
                        )
                        aborted = True
                        break
                    continue
                consecutive_errors = 0
                already_done[record["file"]] = record
                processed_this_run += 1

                if args.limit is not None and processed_this_run >= args.limit:
                    break
        finally:
            results.close()

        if aborted or (args.limit is not None and processed_this_run >= args.limit):
            break

    written = {t: sum(1 for r in already_done.values() if r.get("status") == "written" and r.get("entity_type") == t)
               for t in ENTITY_CONFIG}
    rejected = sum(1 for r in already_done.values() if r.get("status") == "rejected")
    print(f"\nDone. {PROVIDERS_CSV.name}: {written['PROVIDER']} rows, {HIRERS_CSV.name}: {written['HIRER']} rows, "
          f"rejected: {rejected}. Manifest: {EXTRACT_MANIFEST_PATH}")
    export_json()


if __name__ == "__main__":
    main()
