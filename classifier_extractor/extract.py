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
                      en_core_web_sm; skipped with a warning if missing)
                      and gendered pronouns -> neutral ones.

HIRER records then get a grounding review (from review_gig_content.py and
gig_repair.py): a DIFFERENT pool model (llm_pool.reviewer_for_file) reads
the source and the record and answers keep/retry, flagging only clear
defects (unsupported scope, catch-all roles, invented requirements). On
retry the extracting model redoes its pass once, given the reviewer's
reason and its previous record (prompts/repair_hirer.md); that result is
final. The verdict is kept in the manifest. A review that fails outright
errors the whole file, so it's retried from scratch next run.

Either prompt may return {} when the page doesn't qualify (no concrete gig
/ not one individual); that's recorded as "rejected", never written.

Also carried over from gig.py/showcase.py:
- Per-file style rolls (prompts/extract_variations.json): hirer detail
  tier; provider title style, achievement grammar, and a rare deliberate
  prose imperfection -- so synthetic records don't all converge on one
  voice. Seeded by file name, so a rerun rolls the same way.
- A per-record flag (hidden_reasoning) for whether the model reasoned
  before answering. Thinking mode itself is left on for every model.
- The OpenAI client's own retries are off; the loop here is the only one.
  --ping checks every pool model responds.
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
import time
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

MAX_CHARS = 24000
MAX_RETRIES = 3
RETRY_BACKOFF_S = 2  # doubles each retry: 2s, 4s
MAX_CONSECUTIVE_ERRORS = 5

GENERIC_TITLE_BLOCKLIST = {
    "our services", "contact us", "get in touch", "learn more", "services",
    "about us", "who we are", "what we do",
}

load_dotenv(ENV_PATH)

client = OpenAI(
    base_url=os.environ["SOCLAAS_BASE_URL"],
    api_key=os.environ["SOCLAAS_API_KEY"],
    timeout=180,  # thinking is left on, which slows some pool models down
    max_retries=0,  # _call_with_retries is the only retry loop
)


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
    _NLP = None  # pronouns are still neutralised; names just aren't masked

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


def anonymise(text: str) -> str:
    if _NLP is not None:
        names = {ent.text for ent in _NLP(text).ents if ent.label_ == "PERSON"}
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


def _call_llm(model: str, content: str) -> tuple:
    response = client.chat.completions.create(model=model, messages=[{"role": "user", "content": content}])
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


def _entity_doc(data: dict, entity_type: str, fname: str, model: str):
    """A parsed extraction response -> schema-valid document, or None for {}.
    Raises on a schema mismatch, so the caller retries it like any failure."""
    if data == {}:
        return None
    cfg = ENTITY_CONFIG[entity_type]
    code_values = {"source_file": fname, "extracted_by_model": model}
    # blank -> null, so a blank optional field reads as "not stated" and a
    # blank required one fails the schema check instead of being written
    data = {k: (None if isinstance(v, str) and not v.strip() else v) for k, v in data.items()}
    doc = {**data, **{k: v for k, v in code_values.items() if k in cfg["properties"]}}
    errors = [e.message for e in cfg["validator"].iter_errors(doc)]
    if errors:
        raise ValueError(f"schema mismatch: {errors[0]}")
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
    review prompt, the grounding review and at most one repair. Returns
    (document or None if the page doesn't qualify, the extracting model's
    usage, meta). The reviewer's own usage is kept in meta["review"]."""
    cfg = ENTITY_CONFIG[entity_type]
    rolls, picked = roll_variations(entity_type, fname)
    kwargs = prompt_kwargs(entity_type, fname, rolls)
    if cfg["anonymise"]:
        text = anonymise(text)
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
        record = _record_json(entity_type, doc)
        verdict, usage = call(
            reviewer,
            f"{cfg['review_template'].format(**kwargs)}\n\n{source}\n\nGENERATED RECORD:\n```json\n{record}\n```",
            _review_verdict,
        )
        meta["review"] = {"model": reviewer, **verdict, "usage": usage}
        if verdict["decision"] == "retry":
            repair = cfg["repair_template"].format(**kwargs, review_reason=verdict["reason"], previous_record=record)
            doc = extract_call(f"{cfg['templates'][0].format(**kwargs)}\n\n{repair}\n\n{source}")
            meta["repaired"] = True
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
    call for it (a hirer's review and repair included) plus any retry waits."""
    props = ENTITY_CONFIG[entity_type]["properties"]
    return (["source_file"] + [k for k in props if k != "source_file"]
            + ["classify_label", "extracted_at", "time_taken_by_model"])


def _csv_safe(v):
    """Guard against CSV-formula injection if this is ever opened in Excel/
    Sheets straight off disk -- a page's scraped text is untrusted input."""
    s = "" if v is None else str(v)
    return "'" + s if s[:1] in ("=", "+", "-", "@", "\t", "\r") else s


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
                raise SystemExit(
                    f"{cfg['csv'].name} was written under a different schema (columns differ from "
                    f"{cfg['schema'].name}). Move it and docs/extract_manifest.jsonl aside and rerun."
                )


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

def ping() -> None:
    for model in MODEL_POOL:
        start = time.perf_counter()
        try:
            raw, _, reasoning = _call_llm(model, "Reply with exactly: OK")
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
        help="process at most this many files then stop (for testing)",
    )
    parser.add_argument("--ping", action="store_true", help="check every pool model responds, then exit")
    args = parser.parse_args()

    if args.ping:
        ping()
        return

    check_csv_headers()
    if _NLP is None:
        print(
            "NOTE: spaCy/en_core_web_sm not installed -- provider pages get pronoun neutralisation "
            "only, names are not masked (pip install spacy && python -m spacy download en_core_web_sm)",
            flush=True,
        )

    already_done = load_extract_progress()
    consecutive_errors = 0
    aborted = False
    processed_this_run = 0
    idle_announced = False  # log "waiting" once per idle stretch, not every poll

    with EXTRACT_MANIFEST_PATH.open("a", encoding="utf-8") as manifest:
      while True:
        all_items = load_classified_files()
        pending = [it for it in all_items if it[0] not in already_done]
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

        for i, (fname, label) in enumerate(pending, 1):
            entity_type = ENTITY_TYPE_FOR_LABEL[label]
            cfg = ENTITY_CONFIG[entity_type]
            bucket = label.lower()
            src = BUCKET_DIRS[label] / fname
            timestamp = datetime.now().isoformat(timespec="seconds")

            if not src.exists():
                record = {"file": fname, "status": "error", "reason": "source file missing", "timestamp": timestamp}
                manifest.write(json.dumps(record) + "\n")
                manifest.flush()
                print(f"[{i}/{len(pending)}] {bucket}/{fname} -> ERROR (source file missing)", flush=True)
                already_done[fname] = record
                processed_this_run += 1
                continue

            text = src.read_text(encoding="utf-8", errors="ignore")
            model = model_for_file(fname, "extract")
            start = time.perf_counter()

            try:
                doc, usage, meta = extract_entity(text, entity_type, model, fname)
                consecutive_errors = 0
            except Exception as e:
                consecutive_errors += 1
                record = {
                    "file": fname, "entity_type": entity_type, "model": model,
                    "status": "error", "reason": f"api_error: {e}", "timestamp": timestamp,
                }
                manifest.write(json.dumps(record) + "\n")
                manifest.flush()
                print(f"[{i}/{len(pending)}] {bucket}/{fname} ({model}) -> ERROR  ({e})", flush=True)
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

            elapsed = round(time.perf_counter() - start, 2)
            base = {
                "file": fname, "entity_type": entity_type, "model": model, "usage": usage,
                "elapsed": elapsed, **meta, "timestamp": timestamp,
            }
            if doc is None:
                ok, reason = False, ("repair judged the page non-qualifying (model returned {})" if meta.get("repaired")
                                     else "page doesn't qualify (model returned {})")
            else:
                ok, reason = quality_check(entity_type, doc)
            note = f" [repaired after review: {meta['review']['reason']}]" if meta.get("repaired") else ""

            if ok:
                row = {**doc, "source_file": fname, "classify_label": label, "extracted_at": timestamp,
                       "time_taken_by_model": elapsed}
                append_csv_row(cfg["csv"], csv_fields(entity_type), row)
                title = doc.get(cfg["title_field"])
                record = {**base, "status": "written", "title": title, "metrics": record_metrics(entity_type, doc)}
                print(f"[{i}/{len(pending)}] {bucket}/{fname} ({model}) -> WRITTEN ({entity_type}: {title}){note}", flush=True)
            else:
                record = {**base, "status": "rejected", "reason": reason}
                print(f"[{i}/{len(pending)}] {bucket}/{fname} ({model}) -> REJECTED  ({reason}){note}", flush=True)

            manifest.write(json.dumps(record) + "\n")
            manifest.flush()
            already_done[fname] = record
            processed_this_run += 1

            if args.limit is not None and processed_this_run >= args.limit:
                break

        if aborted or (args.limit is not None and processed_this_run >= args.limit):
            break

    written = {t: sum(1 for r in already_done.values() if r.get("status") == "written" and r.get("entity_type") == t)
               for t in ENTITY_CONFIG}
    rejected = sum(1 for r in already_done.values() if r.get("status") == "rejected")
    print(f"\nDone. {PROVIDERS_CSV.name}: {written['PROVIDER']} rows, {HIRERS_CSV.name}: {written['HIRER']} rows, "
          f"rejected: {rejected}. Manifest: {EXTRACT_MANIFEST_PATH}")


if __name__ == "__main__":
    main()
