# -*- coding: utf-8 -*-
"""
The labeller role: zero-shot LLM relevance labels between hirer gigs
(docs/hirers.csv) and provider profiles (docs/providers.csv), both produced
by classifier_extractor/extract.py.

Method: Zhuang et al., "Beyond Yes and No: Improving Zero-Shot LLM Rankers
via Scoring Fine-Grained Relevance Labels" (arXiv:2310.14122). Pointwise --
each (gig, provider) pair is one prompt, with the gig as the paper's
"query" and the provider profile as its "document". Instead of a binary
Yes/No, the model chooses among fine-grained relevance labels, and the
score is the EXPECTED RELEVANCE computed from the log-likelihood the model
assigns to every label -- not the one label it happens to generate, which
the paper shows produces ties and ranks worse (kept here only as a
fallback when logprobs are missing).

Five approaches:
  rg_2l        "Not Relevant" / "Relevant"                              paper RG-2L
  rg_3l        + "Somewhat Relevant" / "Highly Relevant"                paper RG-3L
  rg_4l        + "Perfectly Relevant"                                   paper RG-4L
  rg_s04       "From a scale of 0 to 4 ..."                             paper RG-S(0,4)
  rg_3l_multi  rg_3l scored by EVERY model in MODEL_POOL, averaged      (not in paper)

rg_3l is the base for rg_3l_multi because it tied with rg_s04 as the
paper's best variant. Approaches 1-4 use the pair's one routed model (a
hash of the pair, same idea as classifier_extractor/llm_pool.py), so the
four prompts are compared on the same model for any given pair while the
corpus as a whole still spreads across the whole pool. rg_3l_multi reuses
the routed model's rg_3l call and adds the other three models -- 7 calls
per pair in total, not 8.

Every score is normalised to 0-1 (expected relevance / highest label
value) so the five approaches are directly comparable.

    py -3 labeller/label.py [--max-pairs 50]

Pairs are taken hirer-major (all providers for the first gig, then the
next gig, ...), so a small --max-pairs yields a complete ranking for the
first gig(s) rather than a thin slice of every gig. Reruns skip calls
already recorded in docs/relevance_labels.jsonl, so raising --max-pairs
only pays for the new pairs.
"""

import argparse
import csv
import hashlib
import json
import math
import os
import re
import time
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT_DIR = SCRIPT_DIR.parent  # labeller/ sits one level below the project root
DOCS_DIR = ROOT_DIR / "docs"  # shared data lake every role reads/writes into
ENV_PATH = ROOT_DIR / ".env"
PROMPTS_DIR = SCRIPT_DIR / "prompts"

PROVIDERS_CSV = DOCS_DIR / "providers.csv"
HIRERS_CSV = DOCS_DIR / "hirers.csv"
LABELS_PATH = DOCS_DIR / "relevance_labels.jsonl"  # one line per LLM call
SCORES_CSV = DOCS_DIR / "relevance_scores.csv"  # one row per pair, rebuilt each run

# Same pool as classifier_extractor/llm_pool.py (see its docstring for why
# these four). Duplicated rather than imported: roles only talk to each
# other through docs/, never through Python imports across role folders.
MODEL_POOL = ["llama3.1:8b", "qwen3.8:27b", "qwen3.6:35b", "qwen3-vl:32b"]

LABEL_TEMPLATE = (PROMPTS_DIR / "rg_labels.md").read_text(encoding="utf-8").strip()
SCALE_TEMPLATE = (PROMPTS_DIR / "rg_scale.md").read_text(encoding="utf-8").strip()

# name -> (template kind, labels in ascending relevance; label i is worth i).
# Word labels are chosen so each starts with a different first token, since
# a label is scored by its first token's log-likelihood.
APPROACHES = {
    "rg_2l": ("labels", ["Not Relevant", "Relevant"]),
    "rg_3l": ("labels", ["Not Relevant", "Somewhat Relevant", "Highly Relevant"]),
    "rg_4l": ("labels", ["Not Relevant", "Somewhat Relevant", "Highly Relevant", "Perfectly Relevant"]),
    "rg_s04": ("scale", ["0", "1", "2", "3", "4"]),
}
MULTI_BASE = "rg_3l"

FIELD_CHARS = 1500  # per-field cap when building the query/document text
TOP_LOGPROBS = 20
MAX_RETRIES = 3
RETRY_BACKOFF_S = 2  # doubles each retry: 2s, 4s
MAX_CONSECUTIVE_ERRORS = 5
# Models that "think" first would otherwise make the first output token --
# the one whose logprobs get scored -- reasoning text, not the label.
# Probed: with this flag all four pool models emit the label as token 0
# with a real distribution over the alternatives.
NO_THINKING = {"chat_template_kwargs": {"enable_thinking": False}}

load_dotenv(ENV_PATH)

client = OpenAI(
    base_url=os.environ["SOCLAAS_BASE_URL"],
    api_key=os.environ["SOCLAAS_API_KEY"],
    timeout=50,
)


def model_for_pair(hirer_file: str, provider_file: str) -> str:
    digest = hashlib.sha256(f"label:{hirer_file}|{provider_file}".encode("utf-8")).hexdigest()
    return MODEL_POOL[int(digest, 16) % len(MODEL_POOL)]


# ---------------------------------------------------------------------------
# Query (gig) / document (provider profile) text
# ---------------------------------------------------------------------------

# Content fields of classifier_extractor/ML_*_schema_v1.json. source_company is
# left out of the gig on purpose: it's the firm that published the page, not
# part of what the gig needs.
GIG_FIELDS = [
    ("hire_title", "Gig"),
    ("hire_description", "Scope"),
    ("hire_description_additional_notes", "Notes"),
]
PROFILE_FIELDS = [
    ("about_title", "Headline"),
    ("about_description", "About"),
    ("services_offered_title", "Service"),
    ("services_offered_description", "Service details"),
    ("relevant_experience", "Experience"),
]


def _clean(v) -> str:
    s = (v or "").strip()
    if s[:1] == "'" and s[1:2] in ("=", "+", "-", "@", "\t", "\r"):
        s = s[1:]  # undo extract.py's CSV-formula guard
    s = re.sub(r"\s+", " ", s)
    return s if len(s) <= FIELD_CHARS else s[:FIELD_CHARS].rstrip() + "..."


def _describe(row: dict, fields: list) -> str:
    return "\n".join(f"{label}: {_clean(row.get(k))}" for k, label in fields if _clean(row.get(k)))


def build_prompt(approach: str, query: str, document: str) -> str:
    kind, labels = APPROACHES[approach]
    if kind == "scale":
        return SCALE_TEMPLATE.format(k=len(labels) - 1, query=query, document=document)
    quoted = [f'"{l}"' for l in labels]
    options = " or ".join(quoted) if len(quoted) == 2 else ", ".join(quoted[:-1]) + ", or " + quoted[-1]
    return LABEL_TEMPLATE.format(label_options=options, query=query, document=document)


# ---------------------------------------------------------------------------
# Scoring (paper section 3: expected relevance from label log-likelihoods)
# ---------------------------------------------------------------------------

def _bare(token: str) -> str:
    return token.strip().strip("\"'*`").lower()


def _label_for_token(token: str, labels: list):
    t = _bare(token)
    if not t:
        return None
    hits = [i for i, l in enumerate(labels) if l.lower().startswith(t)]
    return hits[0] if len(hits) == 1 else None


def label_logprobs(content: list, labels: list):
    """Log-likelihood of each label at the answer position -- the first
    output token that isn't whitespace/quotes/markdown. A label missing from
    the top-k there gets a floor just below the lowest logprob seen. Returns
    None if no label appears in the top-k at all."""
    for tok in content:
        if not _bare(tok.token):
            continue
        best = {}
        for cand in tok.top_logprobs:
            i = _label_for_token(cand.token, labels)
            if i is not None and cand.logprob > best.get(i, -math.inf):
                best[i] = cand.logprob
        if not best:
            return None
        floor = min(c.logprob for c in tok.top_logprobs) - 1.0
        return [best.get(i, floor) for i in range(len(labels))]
    return None


def parse_generated(text: str, labels: list):
    t = (text or "").lower()
    for i in sorted(range(len(labels)), key=lambda i: -len(labels[i])):
        if re.search(rf"\b{re.escape(labels[i].lower())}\b", t):
            return i
    return None


def judge(approach: str, model: str, query: str, document: str) -> dict:
    """`model` is fixed for every retry -- falling back to another model
    would silently change which model the record claims produced it."""
    _, labels = APPROACHES[approach]
    prompt = build_prompt(approach, query, document)

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=10,
                temperature=0,
                logprobs=True,
                top_logprobs=TOP_LOGPROBS,
                extra_body=NO_THINKING,
            )
            break
        except Exception as e:
            if attempt == MAX_RETRIES:
                raise
            wait_s = RETRY_BACKOFF_S * (2 ** (attempt - 1))
            print(f"    [RETRY] attempt {attempt}/{MAX_RETRIES} failed ({e}); retrying in {wait_s}s", flush=True)
            time.sleep(wait_s)

    choice = response.choices[0]
    text = choice.message.content or ""
    content = choice.logprobs.content if choice.logprobs and choice.logprobs.content else []
    generated = parse_generated(text, labels)
    s = label_logprobs(content, labels)

    if s is not None:
        top = max(s)
        exps = [math.exp(x - top) for x in s]
        probs = [e / sum(exps) for e in exps]
        er = sum(p * i for i, p in enumerate(probs))
        pr = s[-1]  # paper's peak relevance: log-likelihood of the top label
        scoring = "logprobs"
    elif generated is not None:
        probs = [1.0 if i == generated else 0.0 for i in range(len(labels))]
        er, pr, scoring = float(generated), None, "parsed"
    else:
        raise ValueError(f"no relevance label in output {text!r}")

    usage = {}
    if response.usage:
        usage = {"prompt_tokens": response.usage.prompt_tokens, "completion_tokens": response.usage.completion_tokens}
    return {
        "generated": labels[generated] if generated is not None else None,
        "probs": [round(p, 4) for p in probs],
        "expected_relevance": round(er, 4),
        "score": round(er / (len(labels) - 1), 4),
        "peak_relevance": round(pr, 4) if pr is not None else None,
        "scoring": scoring,
        "usage": usage,
    }


# ---------------------------------------------------------------------------
# Inputs / outputs
# ---------------------------------------------------------------------------

def load_rows(path: Path) -> list:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def load_ok_records() -> list:
    records = []
    if LABELS_PATH.exists():
        with LABELS_PATH.open(encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    r = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if r.get("status") == "ok":
                    records.append(r)
    return records


SCORE_FIELDS = [
    "hirer_file", "hire_title", "provider_file", "about_title", "routed_model",
    *APPROACHES, "rg_3l_multi",
]


def write_scores(hirers: list, providers: list) -> int:
    titles = {h["source_file"]: _clean(h.get("hire_title")) for h in hirers}
    headlines = {p["source_file"]: _clean(p.get("about_title")) for p in providers}

    got = {}  # (hirer, provider) -> {(approach, model): score}
    for r in load_ok_records():
        got.setdefault((r["hirer"], r["provider"]), {})[(r["approach"], r["model"])] = r["score"]

    rows = []
    for (h, p), scores in got.items():
        routed = model_for_pair(h, p)
        row = {
            "hirer_file": h, "hire_title": titles.get(h, ""),
            "provider_file": p, "about_title": headlines.get(p, ""), "routed_model": routed,
        }
        for a in APPROACHES:
            row[a] = scores.get((a, routed), "")
        multi = [scores[(MULTI_BASE, m)] for m in MODEL_POOL if (MULTI_BASE, m) in scores]
        # only a full set of models counts -- a partial average isn't the same measure
        row["rg_3l_multi"] = round(sum(multi) / len(multi), 4) if len(multi) == len(MODEL_POOL) else ""
        rows.append(row)

    rows.sort(key=lambda r: (r["hirer_file"], -(r["rg_3l_multi"] if r["rg_3l_multi"] != "" else -1)))
    with SCORES_CSV.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=SCORE_FIELDS)
        writer.writeheader()
        writer.writerows(rows)
    return len(rows)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--max-pairs", type=int, default=50,
        help="score at most this many (gig, provider) pairs, hirer-major (default: 50). "
             "Each pair costs up to 7 LLM calls; already-recorded calls are skipped.",
    )
    args = parser.parse_args()

    hirers = load_rows(HIRERS_CSV)
    providers = load_rows(PROVIDERS_CSV)
    if not hirers or not providers:
        print(
            f"Need rows in both {HIRERS_CSV.name} ({len(hirers)}) and {PROVIDERS_CSV.name} "
            f"({len(providers)}) -- run classifier_extractor/extract.py first.",
            flush=True,
        )
        return

    done = {(r["hirer"], r["provider"], r["approach"], r["model"]) for r in load_ok_records()}
    pairs = [(h, p) for h in hirers for p in providers][: args.max_pairs]
    jobs = []
    for h, p in pairs:
        routed = model_for_pair(h["source_file"], p["source_file"])
        calls = [(a, routed) for a in APPROACHES] + [(MULTI_BASE, m) for m in MODEL_POOL if m != routed]
        jobs += [(h, p, a, m) for a, m in calls if (h["source_file"], p["source_file"], a, m) not in done]

    print(
        f"{len(hirers)} gigs x {len(providers)} providers; scoring {len(pairs)} pair(s) "
        f"-> {len(jobs)} LLM call(s) to make",
        flush=True,
    )

    consecutive_errors = 0
    with LABELS_PATH.open("a", encoding="utf-8") as out:
        for i, (h, p, approach, model) in enumerate(jobs, 1):
            hf, pf = h["source_file"], p["source_file"]
            record = {
                "hirer": hf, "provider": pf, "approach": approach, "model": model,
                "timestamp": datetime.now().isoformat(timespec="seconds"),
            }
            try:
                record.update(status="ok", **judge(approach, model, _describe(h, GIG_FIELDS), _describe(p, PROFILE_FIELDS)))
                consecutive_errors = 0
                print(f"[{i}/{len(jobs)}] {approach:<6} {model:<14} {record['score']:.2f}  {hf} <- {pf}", flush=True)
            except Exception as e:
                consecutive_errors += 1
                record.update(status="error", reason=str(e)[:300])
                print(f"[{i}/{len(jobs)}] {approach:<6} {model:<14} ERROR ({e})", flush=True)
            out.write(json.dumps(record) + "\n")
            out.flush()
            if consecutive_errors >= MAX_CONSECUTIVE_ERRORS:
                print(
                    f"\n[ABORT] {consecutive_errors} errors in a row -- stopping. Fix the underlying "
                    f"issue and rerun; recorded calls are kept and skipped next time.",
                    flush=True,
                )
                break

    n = write_scores(hirers, providers)
    print(f"\nDone. {n} scored pair(s) in {SCORES_CSV}")


if __name__ == "__main__":
    main()
