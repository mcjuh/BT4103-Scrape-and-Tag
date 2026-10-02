# -*- coding: utf-8 -*-
"""
Grades gig/provider pairs for content fit, on the platform sample format
(docs/platform_sample/hirers_sample.csv and providers_sample.csv).

This is the grader for the new standard format. It is self-contained: it does
not import label.py or judge_pools.py, which grade the older hirers.csv /
providers.csv format and are left as they are.

What the model sees (prompts/rubric_01_v4.md)
  gig       gig_title, short_gig_description, and the extractor's "Engagement duration"
            estimate (shown on its own line, as the gig's estimated duration)
  provider  title, about_headline, about_bio, services_i_offer, relevant_achievements,
            technical_proficiency, credentials, how_i_work, then availability and rate
  Never shown: name, links, localisation_changes, source_*, review_flag. The sample has no
  structured budget, seniority or start date on the gig side, and no seniority on the
  provider side, so the prompt has the model work those out from the text (the way
  enricher/ did with an LLM judge) and apply v3's tolerances to the provider's own
  availability and rate. category / specialisation are the SkillsFuture tags the extractor
  assigned from the same text, so they are left out by default (a grade that read them would
  partly echo the tagger); --with-tags adds them for an ablation and records the run under a
  different prompt_version.

How a pair is scored
  The model answers "<grade> <score>", e.g. "2 0.62": a band (0-3) and a score inside
  that band. The answer position's logprobs give the probability of each band, so:
    grade  = the most probable band. A tie goes to the lower grade.
    score  = the expectation over bands, where the band the model chose contributes the
             score it wrote and every other band contributes its midpoint, then clipped
             into the grade's range. So the score ranks pairs finely, the grade is never
             a rounded average that falls between bands, and the two always agree:
             round(score * 3) == grade for every score this script can emit, which is
             the rule judge_pools.py's export and the ranker's grade_from_score() apply.
  Ranges: 0 = 0.00-0.16, 1 = 0.17-0.49, 2 = 0.50-0.83, 3 = 0.84-0.99.
  Treat the score's second decimal as noise; the band is the trustworthy part.

One model grades each run (--model, default qwen3.8:27b: the grader of the ranker's labels,
see ranker/pipeline/label.md). Calls are logged per model and prompt version, so runs on
other models can sit in the same log; this script does not combine them.

    python labeller/grade_pairs.py --dry-run                                # show a prompt
    python labeller/grade_pairs.py --max-pairs 20                           # smoke test
    python labeller/grade_pairs.py --gigs 1-10                              # chosen gigs
    python labeller/grade_pairs.py --pairs docs/platform_sample/pilot_pairs.json   # the pilot
    python labeller/grade_pairs.py                                          # every pair
    python labeller/grade_pairs.py --export                                 # log -> CSV

Pairs default to every gig x every provider. --pairs takes a JSON file
{"G001": ["P004", "P007"], ...} to grade a chosen set (e.g. a judging pool).
Reruns skip pairs already graded by that model and prompt, so a stopped run resumes.
Needs SOCLAAS_BASE_URL and SOCLAAS_API_KEY (in .env at the repo root).
"""

import argparse
import csv
import json
import math
import os
import re
import time
from collections import Counter
from datetime import datetime
from functools import lru_cache
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT_DIR = SCRIPT_DIR.parent
DOCS_DIR = ROOT_DIR / "docs"
SAMPLE_DIR = DOCS_DIR / "platform_sample"
PROMPT_PATH = SCRIPT_DIR / "prompts" / "rubric_01_v4.md"

GIGS_CSV = SAMPLE_DIR / "hirers_sample.csv"
PROVIDERS_CSV = SAMPLE_DIR / "providers_sample.csv"
LOG_PATH = DOCS_DIR / "gig_grades.jsonl"  # one line per call; the source of truth
OUT_CSV = DOCS_DIR / "gig_grades.csv"  # one row per (pair, model, prompt), from --export
PROMPT_VERSION = "rubric_01.v4.1"  # v4.1: terms (seniority, budget, availability) are graded again

# Same pool as classifier_extractor/llm_pool.py. Duplicated, not imported: roles only
# talk to each other through docs/.
MODEL_POOL = ["qwen3.8:27b", "qwen3.6:35b", "qwen3-vl:32b"]
DEFAULT_MODEL = "qwen3.8:27b"  # graded the ranker's 22k labels (ranker/pipeline/label.md)

GIG_FIELDS = [("gig_title", "Title"), ("short_gig_description", "Scope")]
PROVIDER_FIELDS = [
    ("title", "Title"),
    ("about_headline", "Headline"),
    ("about_bio", "About"),
    ("services_i_offer", "Services"),
    ("relevant_achievements", "Achievements"),
    ("technical_proficiency", "Technical proficiency"),
    ("credentials", "Credentials"),
    ("how_i_work", "How they work"),
]
TERMS_FIELDS = [("availability", "Availability"), ("rate", "Rate")]  # shown after the content fields
TAG_FIELDS = [("category", "Category"), ("specialisation", "Specialisation")]

FIELD_CHARS = 1500  # per-field cap on the text shown
TOP_LOGPROBS = 20
MAX_TOKENS = 12  # "2 0.62" is about 6 tokens; the cap just stops a model that rambles
MAX_RETRIES = 5  # SOCLAAS rate-limits (429) bursts of short calls
RETRY_BACKOFF_S = 2  # doubles each retry: 2s, 4s, 8s, 16s
MAX_CONSECUTIVE_ERRORS = 5
# A model that "thinks" first would make the scored first token reasoning text, not the grade.
NO_THINKING = {"chat_template_kwargs": {"enable_thinking": False}}

# Each grade's score range. Its edges are the points where round(score * 3) changes, so
# a score inside a grade's range always maps back to that grade.
BANDS = {0: (0.00, 0.16), 1: (0.17, 0.49), 2: (0.50, 0.83), 3: (0.84, 0.99)}
MIDPOINT = {g: round((lo + hi) / 2, 2) for g, (lo, hi) in BANDS.items()}

# "<grade> <score>". The grade digit must not be followed by "." or another digit, so a
# bare "0.62" (the old v3 format) is rejected rather than read as grade 0.
REPLY_RE = re.compile(r"^\W*([0-3])(?![\d.])[\s,:;|/-]*(1(?:\.0+)?|0?\.\d+|0(?![\d.]))?")
DURATION_RE = re.compile(r"\s*Engagement duration:\s*([^.\n]*(?:\.\d[^.\n]*)*)\.?", re.I)


# ---------------------------------------------------------------------------
# Input text
# ---------------------------------------------------------------------------

def _clean(value) -> str:
    """Collapse spaces, keep line breaks (bullets and 'Label: items' lines carry meaning)."""
    s = re.sub(r"[ \t]+", " ", str(value or "").replace("\r", "")).strip()
    s = re.sub(r"\s*\n\s*", "\n", s)
    return s if len(s) <= FIELD_CHARS else s[:FIELD_CHARS].rstrip() + "..."


def gig_duration(row: dict) -> str:
    """The extractor's 'Engagement duration: 4-6 weeks.' estimate, e.g. '4-6 weeks', or ''."""
    m = DURATION_RE.search(str(row.get("short_gig_description") or ""))
    return _clean(m.group(1)) if m else ""


def describe(row: dict, fields: list) -> str:
    """'Label: text' per non-empty field; a multi-line value starts on its own line. The
    gig's duration sentence is taken out of its Scope (render() shows it on its own line)."""
    out = []
    for key, label in fields:
        text = _clean(row.get(key))
        if key == "short_gig_description":
            text = _clean(DURATION_RE.sub("", text))
        if text:
            out.append(f"{label}:\n{text}" if "\n" in text else f"{label}: {text}")
    return "\n".join(out)


def render(template: str, gig: dict, provider: dict, with_tags: bool = False) -> str:
    tags = TAG_FIELDS if with_tags else []
    query = describe(gig, GIG_FIELDS + tags)
    if gig_duration(gig):
        query += f"\nEstimated duration: {gig_duration(gig)}"
    document = describe(provider, PROVIDER_FIELDS + tags + TERMS_FIELDS)
    return template.format(query=query, document=document)


def load_rows(path: Path, id_col: str) -> dict:
    csv.field_size_limit(10 ** 9)
    with path.open(newline="", encoding="utf-8-sig") as f:
        return {r[id_col]: r for r in csv.DictReader(f) if r.get(id_col)}


def _num(identifier: str) -> int:
    return int(re.sub(r"\D", "", identifier) or -1)


def parse_gigs(spec: str, gig_ids: list) -> list:
    """"1-10" or "3,7,10-12" -> the gig ids (G001...) whose number is in that set."""
    wanted = set()
    for part in spec.split(","):
        lo, _, hi = part.strip().partition("-")
        wanted.update(range(int(lo), int(hi or lo) + 1))
    return [g for g in gig_ids if _num(g) in wanted]


def build_pairs(gigs: dict, providers: dict, pairs_path: Path = None, only: list = None) -> dict:
    """{gig_id: [provider_id, ...]}: every gig x every provider, or a --pairs file."""
    if pairs_path:
        pairs = json.loads(pairs_path.read_text(encoding="utf-8"))
        unknown = sorted({g for g in pairs if g not in gigs} | {p for ps in pairs.values() for p in ps if p not in providers})
        if unknown:
            raise SystemExit(f"--pairs names ids that are not in the sample: {unknown[:10]}")
    else:
        pairs = {g: list(providers) for g in gigs}
    return {g: ps for g, ps in pairs.items() if only is None or g in only}


# ---------------------------------------------------------------------------
# Model call and scoring
# ---------------------------------------------------------------------------

@lru_cache(maxsize=1)
def get_client():
    from dotenv import load_dotenv
    from openai import OpenAI
    load_dotenv(ROOT_DIR / ".env")
    return OpenAI(base_url=os.environ["SOCLAAS_BASE_URL"], api_key=os.environ["SOCLAAS_API_KEY"], timeout=50)


def complete(prompt: str, model: str):
    """One greedy, no-thinking call with top-k logprobs. `model` stays fixed across retries:
    falling back to another would silently change which model the record claims."""
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            return get_client().chat.completions.create(
                model=model, messages=[{"role": "user", "content": prompt}], max_tokens=MAX_TOKENS,
                temperature=0, logprobs=True, top_logprobs=TOP_LOGPROBS, extra_body=NO_THINKING)
        except Exception as e:
            if attempt == MAX_RETRIES:
                raise
            wait_s = RETRY_BACKOFF_S * 2 ** (attempt - 1)
            print(f"    [RETRY] attempt {attempt}/{MAX_RETRIES} failed ({e}); retrying in {wait_s}s", flush=True)
            time.sleep(wait_s)


def _bare(token: str) -> str:
    return token.strip().strip("\"'*`").lower()


def grade_probs(content: list):
    """P(grade 0..3) at the answer position (the first token that isn't whitespace or
    quotes), renormalised over the four grade digits in the top-k. None if none appear."""
    for tok in content:
        if not _bare(tok.token):
            continue
        mass = [0.0] * 4
        for cand in tok.top_logprobs:
            if _bare(cand.token) in ("0", "1", "2", "3"):
                mass[int(_bare(cand.token))] += math.exp(cand.logprob)
        total = sum(mass)
        return [m / total for m in mass] if total > 0 else None
    return None


def _clip(x: float, grade: int) -> float:
    lo, hi = BANDS[grade]
    return min(max(x, lo), hi)


def score_reply(text: str, content: list) -> dict:
    """The model's reply and its logprobs -> grade, score and the evidence behind them.
    Raises ValueError for a reply that isn't '<grade> <score>'."""
    m = REPLY_RE.match(text or "")
    if not m:
        raise ValueError(f"reply is not '<grade> <score>': {text!r}")
    said_grade = int(m.group(1))
    flags = []

    if m.group(2) is None:
        said_score, flags = MIDPOINT[said_grade], flags + ["score_missing"]
    else:
        said_score = float(m.group(2))
        if not BANDS[said_grade][0] <= said_score <= BANDS[said_grade][1]:
            said_score, flags = _clip(said_score, said_grade), flags + ["score_out_of_band"]

    probs = grade_probs(content)
    scoring = "logprobs"
    if probs is None:
        probs, scoring = [1.0 if g == said_grade else 0.0 for g in range(4)], "parsed"

    raw = probs[said_grade] * said_score + sum(p * MIDPOINT[g] for g, p in enumerate(probs) if g != said_grade)
    grade = max(range(4), key=lambda g: probs[g])  # max() keeps the first, i.e. lowest, on a tie
    return {
        "grade": grade,
        "score": round(_clip(raw, grade), 4),
        "score_raw": round(raw, 4),
        "said_grade": said_grade,
        "said_score": said_score,
        "grade_probs": [round(p, 4) for p in probs],
        "scoring": scoring,
        "flags": flags,
    }


def grade_pair(prompt: str, model: str) -> dict:
    response = complete(prompt, model)
    choice = response.choices[0]
    text = choice.message.content or ""
    content = choice.logprobs.content if choice.logprobs and choice.logprobs.content else []
    result = score_reply(text, content)
    result["generated"] = text.strip()
    if response.usage:
        result["usage"] = {"prompt_tokens": response.usage.prompt_tokens,
                           "completion_tokens": response.usage.completion_tokens}
    return result


# ---------------------------------------------------------------------------
# Log and export
# ---------------------------------------------------------------------------

def load_ok(path: Path, model: str = None, version: str = None) -> dict:
    """(gig_id, provider_id, model, prompt_version) -> the latest successful record."""
    out = {}
    if path.exists():
        with path.open(encoding="utf-8") as f:
            for line in f:
                if not line.strip():
                    continue
                r = json.loads(line)
                if r.get("status") == "ok" and (model is None or r["model"] == model) \
                        and (version is None or r["prompt_version"] == version):
                    out[(r["gig_id"], r["provider_id"], r["model"], r["prompt_version"])] = r
    return out


EXPORT_FIELDS = ["gig_id", "hirer_id", "provider_id", "model", "prompt_version", "grade", "score",
                 "p0", "p1", "p2", "p3", "scoring", "flags", "timestamp"]


def export(log_path: Path, out_path: Path) -> int:
    done = load_ok(log_path)
    with out_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=EXPORT_FIELDS)
        w.writeheader()
        for key in sorted(done, key=lambda k: (_num(k[0]), _num(k[1]), k[2], k[3])):
            r = done[key]
            w.writerow({**{k: r.get(k, "") for k in ("gig_id", "hirer_id", "provider_id", "model",
                                                    "prompt_version", "grade", "score", "scoring", "timestamp")},
                        **{f"p{g}": p for g, p in enumerate(r["grade_probs"])},
                        "flags": ";".join(r.get("flags") or [])})
    dist = Counter((k[2], r["grade"]) for k, r in done.items())
    print(f"exported {len(done)} graded pairs to {out_path}; (model, grade) counts: {dict(sorted(dist.items()))}")
    return len(done)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--model", choices=MODEL_POOL, default=DEFAULT_MODEL, help="the model that grades this run (default: %(default)s)")
    ap.add_argument("--gigs-csv", type=Path, default=GIGS_CSV)
    ap.add_argument("--providers-csv", type=Path, default=PROVIDERS_CSV)
    ap.add_argument("--pairs", type=Path, default=None, help='JSON {"G001": ["P004", ...]} instead of every pair')
    ap.add_argument("--gigs", default=None, help='grade only these gigs by number, e.g. "1-10" or "3,7,10-12"')
    ap.add_argument("--max-pairs", type=int, default=0, help="stop after N new calls (smoke test)")
    ap.add_argument("--with-tags", action="store_true", help="also show category / specialisation (ablation)")
    ap.add_argument("--rps", type=float, default=1.0, help="max calls per second (default: 1)")
    ap.add_argument("--dry-run", action="store_true", help="print the first prompt and the call count, call nothing")
    ap.add_argument("--export", action="store_true", help=f"write {OUT_CSV.name} from the log and exit")
    args = ap.parse_args()

    if args.export:
        export(LOG_PATH, OUT_CSV)
        return

    version = PROMPT_VERSION + ("+tags" if args.with_tags else "")
    template = PROMPT_PATH.read_text(encoding="utf-8").strip()
    gigs = load_rows(args.gigs_csv, "gig_id")
    providers = load_rows(args.providers_csv, "provider_id")
    only = parse_gigs(args.gigs, list(gigs)) if args.gigs else None
    pairs = build_pairs(gigs, providers, args.pairs, only)
    model = args.model
    done = load_ok(LOG_PATH, args.model, version)
    jobs = [(g, p) for g, ps in pairs.items() for p in ps if (g, p, model, version) not in done]
    if args.max_pairs:
        jobs = jobs[:args.max_pairs]
    print(f"{len(pairs)} gigs, {sum(len(v) for v in pairs.values())} pairs; {len(jobs)} call(s) to make "
          f"on {model}, prompt {version}", flush=True)

    if args.dry_run:
        if jobs:
            g, p = jobs[0]
            print(f"\n----- prompt for {g} x {p} -----\n{render(template, gigs[g], providers[p], args.with_tags)}")
        return

    errors, next_call, graded = 0, 0.0, []
    with LOG_PATH.open("a", encoding="utf-8") as out:
        for i, (g, p) in enumerate(jobs, 1):
            record = {"gig_id": g, "hirer_id": gigs[g].get("hirer_id", ""), "provider_id": p, "model": model,
                      "prompt_version": version, "timestamp": datetime.now().isoformat(timespec="seconds")}
            time.sleep(max(0.0, next_call - time.time()))
            t0 = time.time()
            next_call = t0 + 1.0 / args.rps
            try:
                r = grade_pair(render(template, gigs[g], providers[p], args.with_tags), model)
                record.update(status="ok", elapsed=round(time.time() - t0, 2), **r)
                graded.append(r["grade"])
                errors = 0
                note = f"  [{','.join(r['flags'])}]" if r["flags"] else ""
                print(f"[{i}/{len(jobs)}] {g} <- {p}  grade {r['grade']}  score {r['score']:.2f}  "
                      f"p={r['grade_probs']}{note}", flush=True)
            except Exception as e:
                errors += 1
                record.update(status="error", reason=str(e)[:300])
                print(f"[{i}/{len(jobs)}] {g} <- {p}  ERROR ({e})", flush=True)
            out.write(json.dumps(record) + "\n")
            out.flush()
            if errors >= MAX_CONSECUTIVE_ERRORS:
                print(f"\n[ABORT] {errors} errors in a row; fix and rerun. Graded pairs are kept and skipped.", flush=True)
                break
    print(f"\nDone. grades this run: {dict(sorted(Counter(graded).items()))}. "
          f"Run with --export to write {OUT_CSV.name}.")


if __name__ == "__main__":
    main()
