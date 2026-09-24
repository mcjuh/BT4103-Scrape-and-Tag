# -*- coding: utf-8 -*-
"""
Second half of the classifier/extractor role: classify.py sorts pages into
docs/provider/, docs/hirer/, docs/ignore/, docs/uncertain/; this script
reads classify.py's docs/manifest.jsonl to find pages worth extracting
(PROVIDER, HIRER, UNCERTAIN) and turns each into ONE record shaped exactly
like the ML schemas next to this file:

    ML_provider_schema_v1.json  -> ProviderDocument -> docs/providers.csv
    ML_hirer_schema_v1.json     -> HireDocument     -> docs/hirers.csv

The schemas are the single source of truth: each prompt's field list and
JSON skeleton are generated from them, and every LLM response is validated
against them (jsonschema) before anything is written -- a response that
doesn't match is retried like any other failure. source_file and
extracted_by_model are filled in here, not by the LLM, which can't know
either.

Providers and hirers run through the same code path; what differs is the
prompts (prompts/, never inline here) and the per-type settings in
ENTITY_CONFIG:

  HIRER     1 pass:   extract_hirer.md reframes a case study as the gig
                      its original hirer could have posted (from gig.py).
  PROVIDER  2 passes: extract_provider_facts.md extracts neutral facts,
                      then extract_provider_style.md restyles them into a
                      first-person profile, so styling can't add facts
                      (from showcase.py). The source is anonymised first:
                      names -> [CANDIDATE_NAME] (needs spaCy +
                      en_core_web_sm; extract.py won't start without it)
                      and gendered pronouns -> neutral ones.

HIRER records then get a grounding review (from review_gig_content.py and
gig_repair.py): a DIFFERENT pool model (llm_pool.reviewer_for_file) reads
the source and the record and answers keep/retry, flagging only clear
defects (unsupported scope, catch-all roles, invented requirements, named
organisations). On retry the extracting model redoes its pass once, given
the reviewer's reason and its previous record (prompts/repair_hirer.md);
the same reviewer checks the rewrite once more, and a rewrite that's still
flagged is rejected. The verdict is kept in the manifest. A review that fails outright
errors the whole file, so it's retried from scratch next run.

Either prompt may return {} when the page doesn't qualify (no concrete gig
/ not one individual); that's recorded as "rejected", never written.

Also carried over from gig.py/showcase.py:
- Per-file style rolls (prompts/extract_variations.json): hirer detail
  tier and voice/opening; provider title style, achievement grammar, and a rare deliberate
  prose imperfection -- so synthetic records don't all converge on one
  voice. Seeded by file name, so a rerun rolls the same way.
- A per-record flag (hidden_reasoning) for whether the model reasoned
  before answering. Thinking mode is switched off (NO_THINKING); the flag
  is what keeps records from before and after that change comparable.
- The OpenAI client's own retries are off; the loop here is the only one.
  --ping checks every pool model responds.
- --entity hirer|provider extracts only one type (provider = PROVIDER and
  UNCERTAIN pages); --balance and --limit then apply within that type.
- --workers N extracts N files at once (default 4; one at a time is
  latency-bound); --rps caps requests/second across all workers (default
  1). SOCLAAS sustains only ~1 request/s, shared by every script on the
  key, and past that returns bare 429s. The tagging stage ran 2,894 pages
  at 4 workers / 1 rps cleanly. Only the main thread writes the CSVs and the
  manifest.
- industry / secondary_industry / taxonomy_version columns are copied in
  from industry.py's docs/industry_manifest.jsonl by code, never asked of
  the LLM. --backfill-industries rewrites both CSVs with the current tags
  (joined on source_file), which is also how a CSV written before these
  columns existed is migrated.
- Per-record quality metrics in the manifest (field lengths, leftover
  gendered pronouns).

Each file is extracted by one model from llm_pool.MODEL_POOL.
Read-only against docs/<bucket>/. Progress is tracked in
docs/extract_manifest.jsonl, so reruns skip written/rejected files and
retry only errors.
"""

import argparse
import csv
import functools
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

from llm_pool import MODEL_POOL, model_for_file, reviewer_for_file

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT_DIR = SCRIPT_DIR.parent  # classifier_extractor/ sits one level below the project root
DOCS_DIR = ROOT_DIR / "docs"  # shared data lake every role reads/writes into
ENV_PATH = ROOT_DIR / ".env"
PROMPTS_DIR = SCRIPT_DIR / "prompts"

CLASSIFY_MANIFEST_PATH = DOCS_DIR / "manifest.jsonl"
INDUSTRY_MANIFEST_PATH = DOCS_DIR / "industry_manifest.jsonl"  # industry.py's output, read for --balance
EXTRACT_MANIFEST_PATH = DOCS_DIR / "extract_manifest.jsonl"
PROVIDERS_CSV = DOCS_DIR / "providers.csv"
HIRERS_CSV = DOCS_DIR / "hirers.csv"

BUCKET_DIRS = {
    "PROVIDER": DOCS_DIR / "provider",
    "HIRER": DOCS_DIR / "hirer",
    "UNCERTAIN": DOCS_DIR / "uncertain",
}
# UNCERTAIN is, by classify.py's own definition, "a genuine PROVIDER profile
# that also carries explicit HIRER signals" -- so it's a provider candidate,
# not a hirer one.
ENTITY_TYPE_FOR_LABEL = {
    "PROVIDER": "PROVIDER",
    "UNCERTAIN": "PROVIDER",
    "HIRER": "HIRER",
}

# Everything that differs between the two entity types. "prompts" run in
# order: the first reads the page, each later one reads the previous
# pass's JSON. "review"/"repair" are optional; a repair reruns the first
# pass, so only give them to single-pass entity types.
ENTITY_CONFIG = {
    "PROVIDER": {
        "schema": SCRIPT_DIR / "ML_provider_schema_v1.json",
        "prompts": ["extract_provider_facts.md", "extract_provider_style.md"],
        "anonymise": True,
        "csv": PROVIDERS_CSV,
        "title_field": "about_title",
        "review": None,
        "repair": None,
    },
    "HIRER": {
        "schema": SCRIPT_DIR / "ML_hirer_schema_v1.json",
        "prompts": ["extract_hirer.md"],
        "anonymise": False,
        "csv": HIRERS_CSV,
        "title_field": "hire_title",
        "review": "review_hirer.md",
        "repair": "repair_hirer.md",
    },
}
CODE_FIELDS = ("source_file", "extracted_by_model")  # filled in here, never asked of the LLM
# Copied from industry.py's manifest, never asked of the LLM either. A file
# industry.py hadn't tagged when it was extracted gets blanks until the next
# --backfill-industries.
INDUSTRY_FIELDS = ("industry", "secondary_industry", "taxonomy_version")
PID_PATH = DOCS_DIR / "_extract.pid"  # read by monitor/dashboard.py for an exact RUNNING state

MAX_CHARS = 24000
MAX_RETRIES = 3
RETRY_BACKOFF_S = 2  # doubles each retry: 2s, 4s
MAX_CONSECUTIVE_ERRORS = 5
# Per call, a guard against a model developing qwen3.8:27b's runaway output
# again (11,832 median completion tokens with thinking on). Thinking off, the
# largest record seen was 655 tokens across BOTH provider passes, and a
# review is ~125. A reply cut off here fails loudly rather than as bad JSON.
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
    _cfg["validator"] = Draft7Validator(_schema)
    _cfg["properties"] = list(_schema["properties"])
    _cfg["llm_fields"] = {
        k: v.get("description", "") for k, v in _schema["properties"].items() if k not in CODE_FIELDS
    }
    _cfg["templates"] = [(PROMPTS_DIR / p).read_text(encoding="utf-8").strip() for p in _cfg["prompts"]]
    for _key in ("review", "repair"):
        _cfg[f"{_key}_template"] = (PROMPTS_DIR / _cfg[_key]).read_text(encoding="utf-8").strip() if _cfg[_key] else None

VARIATIONS = json.loads((PROMPTS_DIR / "extract_variations.json").read_text(encoding="utf-8"))


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


def prompt_kwargs(entity_type: str, fname: str, rolls: dict) -> dict:
    fields = ENTITY_CONFIG[entity_type]["llm_fields"]
    return {
        **rolls,
        "field_block": "\n".join(f'- "{k}": {d}' for k, d in fields.items()),
        "skeleton": json.dumps({k: None for k in fields}, indent=2),
        "source_file": fname,
    }


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
    """Swap the publishing firm's names (its domain stem plus
    PUBLISHER_ALIASES) for "the firm" before the model reads the page. A bio
    names its firm in nearly every sentence, so asking the model to leave it
    out isn't enough on its own.

    Also swallows up to two capitalised words right after the name (e.g.
    "PwC Canada", "BCG Institute", "Alvarez & Marsal GmbH"): otherwise only
    the name is replaced and the qualifier is left dangling ("the firm
    Canada"), which reads as broken grammar and leaks exactly the kind of
    detail this masking exists to hide. The extension is case-sensitive
    (unlike the name match) so it only grabs genuine proper-noun
    continuations, not ordinary words that happen to follow."""
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
    """Whether the model reasoned ("thinking") before answering. Thinking is
    left on, so this is recorded per record rather than suppressed."""
    message = response.choices[0].message
    content = message.content or ""
    extra = message.model_dump() if hasattr(message, "model_dump") else {}
    return "<think" in content.lower() or bool(extra.get("reasoning_content") or extra.get("reasoning"))


# Thinking off, as labeller/label.py already does. It was left on here
# deliberately, but the cost turned out to be carried almost entirely by one
# model: qwen3.8:27b reasoned on 100% of its extract calls, emitting a median
# 11,832 completion tokens against ~350 for the other three, at a median
# 171.2s per record versus 4.0-10.8s -- p90 378s, max 734s. Routed a quarter
# of all files, it was ~85-90% of total extraction wall clock. Measured A/B on
# one page: 19.6s/1,389 tokens with thinking on, 2.5s/126 tokens off; the
# other models are unaffected either way (qwen3.6:35b: 1.4s vs 2.4s).
# `hidden_reasoning` is still recorded per record, so the ON-era rows remain
# comparable against the OFF-era ones. Checked 21 Sep on a 200-file OFF-era
# run: no quality drop (qwen3.8:27b hirer first-review keep 88.6% -> 95.7%,
# providers written 100% in both eras; small n -- see BACKLOG.md item G).
NO_THINKING = {"chat_template_kwargs": {"enable_thinking": False}}


def _call_llm(model: str, content: str, json_mode: bool = True) -> tuple:
    # JSON mode stops malformed JSON (llama3.1 otherwise drops commas and
    # quotes); every pool model accepts it. Only --ping asks for plain text.
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
    """Takes the outermost {...} rather than the whole reply: some models
    (llama3.1) wrap the JSON in a preamble and a code fence despite being
    told not to. strict=False accepts raw newlines inside strings, which
    the same models emit in multi-paragraph descriptions."""
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
# copied an example instead of the source (seen: llama3.1 pasted the example
# patent numbers and $5M insurance engagement into a real person's profile).
PROMPT_EXAMPLE_LEAKS = (
    "9921894", "10203941", "USPTO patents", "European insurance carrier",
    "Computer Weekly", "40 services off mainframe", "from 3 days to 4 hours",
)

# Records are anonymised: the text a gig or profile shows must not name the
# firm that published the page. A domain's own stem (e.g. "kroll") is always
# checked; these are the other names a publisher goes by.
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
ORG_FIELDS = ("source_company", "source_company_team")  # metadata, allowed to name the publisher


def _join_items(items: list):
    """Models often itemise a multi-line field (relevant_experience) as a
    JSON list or dict; the schema wants one string, so join it as "- "
    lines. For a dict: filled values become "key: value" lines; with no
    values, keys are kept only if they read as items (sentences, e.g.
    {"- Chaired a charity committee.": {}}), not labels (e.g.
    {"budget": null, "timeline": null} -> None)."""
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
    text = " ".join(v for k, v in doc.items()
                    if isinstance(v, str) and k not in ORG_FIELDS and k not in CODE_FIELDS)
    for name in names:
        name = name.strip()
        if name and re.search(rf"(?<!\w){re.escape(name)}(?!\w)", text, re.IGNORECASE):
            return name
    return None


def _entity_doc(data: dict, entity_type: str, fname: str, model: str):
    """A parsed extraction response -> schema-valid document, or None for {}.
    Raises on a schema mismatch, so the caller retries it like any failure."""
    if data == {}:
        return None
    cfg = ENTITY_CONFIG[entity_type]
    code_values = {"source_file": fname, "extracted_by_model": model}
    data = {k: (_join_items(v) if isinstance(v, (list, dict)) else v) for k, v in data.items()}
    # blank -> null, so a blank optional field reads as "not stated" and a
    # blank required one fails the schema check instead of being written
    data = {k: (None if isinstance(v, str) and not v.strip() else v) for k, v in data.items()}
    doc = {**data, **{k: v for k, v in code_values.items() if k in cfg["properties"]}}
    errors = [e.message for e in cfg["validator"].iter_errors(doc)]
    if errors:
        raise ValueError(f"schema mismatch: {errors[0]}")
    text = " ".join(v for v in doc.values() if isinstance(v, str)).lower()
    leak = next((s for s in PROMPT_EXAMPLE_LEAKS if s.lower() in text), None)
    if leak:
        raise ValueError(f"copied a prompt example ({leak!r}) instead of the source")
    org = _named_org(fname, doc)
    if org:
        raise ValueError(f"names {org!r}; organisations must be described generically")
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


def _call_with_retries(model: str, content: str, validate) -> tuple:
    """Returns (validate(parsed JSON), usage, hidden_reasoning). A parse or
    validation failure is retried just like an API error. `model` stays
    fixed for every retry -- falling back to another would break the
    deterministic file->model assignment llm_pool.py relies on."""
    last_err = None
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            raw_output, usage, reasoning = _call_llm(model, content)
            return validate(_parse_json(raw_output)), usage, reasoning
        except Exception as e:
            last_err = e
            if attempt < MAX_RETRIES:
                wait_s = RETRY_BACKOFF_S * (2 ** (attempt - 1))
                print(f"    [RETRY] attempt {attempt}/{MAX_RETRIES} failed ({e}); retrying in {wait_s}s", flush=True)
                time.sleep(wait_s)
    raise last_err


def _record_json(entity_type: str, doc: dict) -> str:
    """The LLM-written part of a record, as handed to a later pass."""
    fields = ENTITY_CONFIG[entity_type]["llm_fields"]
    return json.dumps({k: doc.get(k) for k in fields}, ensure_ascii=False, indent=2)


def extract_entity(text: str, entity_type: str, model: str, fname: str) -> tuple:
    """Runs the entity type's prompt passes in order, then, if it has a
    review prompt, the grounding review, at most one repair, and a second
    review of that repair. Returns
    (document or None if the page doesn't qualify, the extracting model's
    usage, meta). The reviewer's own usage is kept in meta["review"]."""
    cfg = ENTITY_CONFIG[entity_type]
    rolls, picked = roll_variations(entity_type, fname)
    kwargs = prompt_kwargs(entity_type, fname, rolls)
    if cfg["anonymise"]:
        text = anonymise(mask_publisher(text, fname))
    validate = functools.partial(_entity_doc, entity_type=entity_type, fname=fname, model=model)

    source = f"SOURCE MATERIAL:\n```\n{text[:MAX_CHARS]}\n```"
    usage_total = {"prompt_tokens": 0, "completion_tokens": 0}
    meta = {"rolls": picked, "hidden_reasoning": False}

    def call(call_model: str, content: str, check) -> tuple:
        result, usage, reasoning = _call_with_retries(call_model, content, check)
        meta["hidden_reasoning"] = meta["hidden_reasoning"] or reasoning
        return result, usage

    def extract_call(content: str):
        doc, usage = call(model, content, validate)
        for k in usage_total:
            usage_total[k] += usage.get(k) or 0
        return doc

    doc, payload = None, source
    for template in cfg["templates"]:
        doc = extract_call(f"{template.format(**kwargs)}\n\n{payload}")
        if doc is None:
            break
        payload = f"INPUT RECORD:\n```json\n{_record_json(entity_type, doc)}\n```"

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
    return doc, usage_total, meta


# ---------------------------------------------------------------------------
# Quality checks (independent of what the LLM claims)
# ---------------------------------------------------------------------------

def _norm(s) -> str:
    return re.sub(r"\s+", " ", s.strip()) if isinstance(s, str) else ""


def quality_check(entity_type: str, doc: dict) -> tuple:
    if entity_type == "HIRER":
        title = _norm(doc.get("hire_title"))
        desc = _norm(doc.get("hire_description"))
        if not title or title.lower() in GENERIC_TITLE_BLOCKLIST:
            return False, f"no credible gig title (got {title!r})"
        if len(desc) < 30:
            return False, f"hire_description too short ({len(desc)} chars, need >=30)"
        return True, ""

    fields = ENTITY_CONFIG["PROVIDER"]["llm_fields"]
    if any(NAME_PLACEHOLDER in _norm(doc.get(k)) for k in fields):
        return False, f"{NAME_PLACEHOLDER} placeholder leaked into the profile"
    substantive = sum(1 for k in fields if len(_norm(doc.get(k))) >= 15)
    if substantive < 2:
        return False, f"only {substantive} substantive field(s) present, need >=2"
    return True, ""


def record_metrics(entity_type: str, doc: dict) -> dict:
    fields = ENTITY_CONFIG[entity_type]["llm_fields"]
    texts = {k: doc[k] for k in fields if isinstance(doc.get(k), str)}
    return {
        "field_chars": {k: len(v) for k, v in texts.items()},
        "leftover_pronouns": len(LEFTOVER_PRONOUN_RE.findall(" ".join(texts.values()))),
    }


# ---------------------------------------------------------------------------
# CSV output
# ---------------------------------------------------------------------------

def csv_fields(entity_type: str) -> list:
    """source_file first, then the schema's own fields in schema order, then
    bookkeeping -- so the columns follow the schema file automatically.
    time_taken_by_model is the seconds spent extracting the row: every model
    call for it (a hirer's review and repair included) plus any retry waits.

    The roll_* tail is this entity type's style rolls from
    extract_variations.json -- which wording variant produced this row. They
    were only in extract_manifest.jsonl before, which meant anyone reading
    the CSV on its own couldn't tell a "Minimal"-detail gig from a
    "Standard" one, or check whether a variant correlates with weaker rows.
    Column names come from the variations file, so adding a roll there adds
    its column here (and, as ever, changes the header -- see
    check_csv_headers).

    INDUSTRY_FIELDS come from industry.py's manifest, so the CSVs can be
    split or balanced by industry without a join (see backfill_industries)."""
    props = ENTITY_CONFIG[entity_type]["properties"]
    return (["source_file"] + [k for k in props if k != "source_file"]
            + ["classify_label", *INDUSTRY_FIELDS, "extracted_at", "time_taken_by_model"]
            + [f"roll_{k}" for k in VARIATIONS.get(entity_type, {})])


def _csv_safe(v):
    """Guard against CSV-formula injection if this is ever opened in Excel/
    Sheets straight off disk -- a page's scraped text is untrusted input.
    "-" is excluded: _join_items() always starts relevant_experience with
    "- ", so guarding it would prepend a stray apostrophe onto nearly every
    bulleted field instead of only ones a source could actually weaponise."""
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
                    f"{cfg['schema'].name}). Move it and docs/extract_manifest.jsonl aside and rerun."
                )


def backfill_industries() -> None:
    """Rewrites both CSVs with the current industry tags, joined on
    source_file -- no LLM calls, nothing re-extracted. Also migrates a CSV
    whose header predates newer code-filled columns (they're added, blank
    unless filled here). Refuses a CSV with columns the current code doesn't
    know, since that means a schema change, not a missing column. The first
    rewrite keeps a copy as <name>.pre_industry.bak."""
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
    """Reorder `pending` so extraction spends its calls evenly across
    (entity_type, industry) cells instead of working through the manifest in
    order.

    Manifest order is crawl order, which is dominated by whichever domains
    produced the most pages -- kroll, bcg and alvarezandmarsal are ~47% of
    everything extractable. Extracting in that order reproduces the
    imbalance in the output CSVs no matter how many rows get written.

    So: group by cell, then round-robin across cells, taking one file from
    each in turn. A cell that runs out simply drops out of the rotation --
    that costs nothing, because a rare industry with 3 files should still
    contribute all 3. `per_cell` additionally caps how many files any one
    cell may contribute this run; files over the cap stay pending rather
    than being spent, so raising the cap later picks up exactly where this
    left off.

    Files industry.py hasn't tagged yet go in their own "(untagged)" cell
    rather than being dropped -- extraction shouldn't stall just because
    tagging is still catching up -- but they're one cell among many, so they
    can't dominate the run either. Order within a cell is left as-is, so a
    rerun with the same inputs produces the same order."""
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
    """Extracts one file and returns (manifest record, CSV row or None, log
    line). Writes nothing itself, so several can run at once (--workers)
    while main() stays the only writer. `industry` is the file's record from
    industry_manifest.jsonl, if it has one."""
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
        row = {**doc, "source_file": fname, "classify_label": label, "extracted_at": timestamp,
               "time_taken_by_model": elapsed,
               **{k: (industry or {}).get(k) for k in INDUSTRY_FIELDS},
               **{f"roll_{k}": v for k, v in (meta.get("rolls") or {}).items()}}
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
             "Needs docs/industry_manifest.jsonl (classifier_extractor/industry.py)",
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
        help="rewrite both CSVs with the current industry tags from docs/industry_manifest.jsonl "
             "(no LLM calls), migrating a CSV that predates the industry columns, then exit",
    )
    args = parser.parse_args()
    global _PACER
    _PACER = Pacer(args.rps) if args.rps else None

    if args.ping:
        ping()
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
                if row is not None:  # CSV before manifest, so the manifest never claims an unwritten row
                    entity_type = record["entity_type"]
                    append_csv_row(ENTITY_CONFIG[entity_type]["csv"], csv_fields(entity_type), row)
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


if __name__ == "__main__":
    main()
