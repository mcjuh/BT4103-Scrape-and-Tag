# -*- coding: utf-8 -*-
"""
Tag every already-classified page with the INDUSTRY the work is done for --
the third stage, between classify.py and extract.py.

The taxonomy comes from the client: the `industry` column of their test
workbook (data/reference/client_documents/20260917 Senseigigs_NUS_Test_Dataset_Team31.xlsx,
30 gigs), collapsed into groups, plus a few sectors the crawled corpus needs
(Energy & Resources, Public Sector, Education) so they don't all land in
OTHER. It lives in prompts/industry_taxonomy.json, versioned, and the prompt's
industry list is generated from it (same arrangement as extract.py's
schema-generated {field_block}), so the taxonomy file stays the one place that
defines the labels.

It replaced subject.py (the academic-subject taxonomy, subject_v1): tagged on
the client's own 30 gigs, that put 21 into Mathematics, Accountancy or Law, so
it couldn't separate the work the client actually cares about. Industry does.

WHY ITS OWN STAGE, rather than a field on either neighbour:
- Not in extract.py's schemas: by the time an extract call returns, the call
  is already paid for. Balancing the dataset means knowing a page's industry
  BEFORE deciding whether to spend an extraction on it, so it has to be known
  one stage earlier.
- Not folded into classify_triage.md: classify.py only globs
  data/pages/unprocessed/, so the 12k already-labelled pages could not be re-run
  through it without moving them all back, and editing that prompt would
  perturb a PROVIDER/HIRER/IGNORE boundary that already has 12k rows behind it.

So this reads classify.py's data/manifests/classify.jsonl (not its code, per the
project's one-way data-lake rule), reads each qualifying page out of its
bucket folder, and appends one record per file to
data/manifests/industry.jsonl. Nothing is moved: industry is a second,
orthogonal axis on the same files.

By default only PROVIDER/HIRER/UNCERTAIN are tagged -- the IGNORE pages never
reach extract.py. --include-ignore overrides that.

Each file is routed to one pool model by model_for_file(fname, "industry"),
a stage salt of its own, for the reason llm_pool.py documents: these labels
are synthetic data, and a single generative source narrows the corpus's
distribution.

    py -3 classifier_extractor/industry.py --workers 4 --rps 1
    py -3 classifier_extractor/industry.py --report
"""

import argparse
import json
import os
import threading
import time
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

from llm_pool import model_for_file

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT_DIR = SCRIPT_DIR.parent  # classifier_extractor/ sits one level below the project root
DATA_DIR = ROOT_DIR / "data"  # shared data lake every role reads/writes into
PAGES_DIR = DATA_DIR / "pages"
MANIFESTS_DIR = DATA_DIR / "manifests"
LOGS_DIR = ROOT_DIR / "logs"
ENV_PATH = ROOT_DIR / ".env"
PROMPTS_DIR = SCRIPT_DIR / "prompts"

CLASSIFY_MANIFEST_PATH = MANIFESTS_DIR / "classify.jsonl"
INDUSTRY_MANIFEST_PATH = MANIFESTS_DIR / "industry.jsonl"

# Where classify.py put each label's files. A page is read from here; it is
# never moved -- industry is an extra axis on the existing buckets.
BUCKET_DIRS = {
    "PROVIDER": PAGES_DIR / "provider",
    "HIRER": PAGES_DIR / "hirer",
    "IGNORE": PAGES_DIR / "ignore",
    "UNCERTAIN": PAGES_DIR / "uncertain",
}
DEFAULT_LABELS = ("PROVIDER", "HIRER", "UNCERTAIN")

MAX_CHARS = 24000  # same cap as classify.py/extract.py; truncation is from the front
MAX_RETRIES = 3
RETRY_BACKOFF_S = 2  # doubles each retry: 2s, 4s
MAX_CONSECUTIVE_ERRORS = 5
# The answer is one line of JSON (41-75 completion tokens per page under the
# subject taxonomy, thinking off). The cap is a guard against runaway output,
# not a limit a normal answer comes near.
MAX_COMPLETION_TOKENS = 300
PID_PATH = LOGS_DIR / "industry.pid"  # read by monitor/dashboard.py for an exact RUNNING state

load_dotenv(ENV_PATH)

client = OpenAI(
    base_url=os.environ["SOCLAAS_BASE_URL"],
    api_key=os.environ["SOCLAAS_API_KEY"],
    timeout=180,  # generous: calls take ~1-3s with thinking off
    max_retries=0,  # classify_industry() is the only retry loop
)

TAXONOMY = json.loads((PROMPTS_DIR / "industry_taxonomy.json").read_text(encoding="utf-8"))
TAXONOMY_VERSION = TAXONOMY["taxonomy_version"]
INDUSTRIES = [i["name"] for i in TAXONOMY["industries"]]
VALID_INDUSTRIES = set(INDUSTRIES)


def _industry_block() -> str:
    """The prompt's industry list, generated from industry_taxonomy.json so
    the taxonomy file is the only place a label is defined -- the same reason
    extract.py generates its {field_block} from the JSON schemas."""
    lines = []
    for i in TAXONOMY["industries"]:
        lines.append(f"**{i['name']}** -- {i['gist']}")
        if i["client_labels"]:
            lines.append(f"  e.g. {'; '.join(i['client_labels'])}")
        lines.append("")
    return "\n".join(lines).strip()


INDUSTRY_PROMPT = (
    (PROMPTS_DIR / "classify_industry.md").read_text(encoding="utf-8").strip()
    .replace("{industry_block}", _industry_block())
)


class Pacer:
    """Spaces requests evenly across worker threads (--rps), same as extract.py's."""

    def __init__(self, rps: float):
        self.gap, self.next_at, self.lock = 1.0 / rps, time.monotonic(), threading.Lock()

    def wait(self):
        with self.lock:
            now = time.monotonic()
            slot = max(now, self.next_at)
            self.next_at = slot + self.gap
        time.sleep(max(0.0, slot - now))


_PACER = None  # set by main() when --rps is given


def _match(name: str):
    """A taxonomy name matching `name` up to case/spacing drift, or None."""
    name = (name or "").strip().lower()
    return next((i for i in INDUSTRIES if i.lower() == name), None)


def parse_industry(raw_output: str) -> dict:
    """Pull the industry fields out of the model's response. Never raises: an
    unparseable or out-of-taxonomy answer becomes OTHER with the problem in
    `reason`, so a malformed response is visible in the report as an OTHER
    rather than silently vanishing or crashing the run."""
    text = raw_output.strip()
    if text.startswith("```"):
        text = text.strip("`")
        if text.lower().startswith("json"):
            text = text[4:]
        text = text.strip()

    try:
        data = json.loads(text)
    except (json.JSONDecodeError, AttributeError) as e:
        return {"industry": "OTHER", "secondary_industry": None, "other_industry": None,
                "reason": f"parse_error: {e}", "parsed": False}

    industry = _match(str(data.get("industry") or ""))
    reason = str(data.get("reason") or "")
    if industry is None:
        return {"industry": "OTHER", "secondary_industry": None, "other_industry": None,
                "reason": f"unrecognized industry: {data.get('industry')!r}", "parsed": False}

    secondary = _match(str(data.get("secondary_industry") or ""))
    if secondary == industry:
        secondary = None

    other = str(data.get("other_industry") or "").strip() or None
    if industry != "OTHER":
        other = None

    return {"industry": industry, "secondary_industry": secondary, "other_industry": other,
            "reason": reason, "parsed": True}


# Thinking off, matching extract.py and labeller/label.py -- see the note in
# extract.py for the measurements (qwen3.8:27b was the outlier on every stage).
NO_THINKING = {"chat_template_kwargs": {"enable_thinking": False}}


def _call_llm(text: str, model: str) -> tuple:
    if _PACER:
        _PACER.wait()
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": f"{INDUSTRY_PROMPT}\n\nPAGE TEXT:\n{text[:MAX_CHARS]}"}],
        max_completion_tokens=MAX_COMPLETION_TOKENS,
        extra_body=NO_THINKING,
    )
    if response.choices[0].finish_reason == "length":
        # an error to retry, not an OTHER: the page wasn't ambiguous, the reply was cut off
        raise ValueError(f"reply hit the {MAX_COMPLETION_TOKENS}-token cap (runaway output?)")
    usage = {}
    if response.usage:
        usage = {
            "prompt_tokens": response.usage.prompt_tokens,
            "completion_tokens": response.usage.completion_tokens,
        }
    return response.choices[0].message.content, usage


def classify_industry(text: str, model: str) -> tuple:
    """Tag with retries for transient failures. Raises only once MAX_RETRIES
    attempts all fail -- that is a hard error (the tagger failed), not an
    OTHER (the page was ambiguous). `model` is fixed across retries so a
    transient failure can't silently break the deterministic file->model
    assignment llm_pool.py relies on."""
    last_err = None
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            raw_output, usage = _call_llm(text, model)
            return parse_industry(raw_output), usage, raw_output
        except Exception as e:
            last_err = e
            if attempt < MAX_RETRIES:
                wait_s = RETRY_BACKOFF_S * (2 ** (attempt - 1))
                print(f"    [RETRY] attempt {attempt}/{MAX_RETRIES} failed ({e}); retrying in {wait_s}s", flush=True)
                time.sleep(wait_s)
    raise last_err


def load_classified_files(labels: tuple) -> list:
    """Every (file, label) from classify.py's manifest worth tagging, re-read
    fresh on each call so --watch picks up what classify.py appends while
    this keeps running."""
    items = []
    if not CLASSIFY_MANIFEST_PATH.exists():
        return items
    seen = set()
    with CLASSIFY_MANIFEST_PATH.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            record = json.loads(line)
            if record.get("status") != "ok" or record.get("label") not in labels:
                continue
            if record["file"] in seen:
                continue
            seen.add(record["file"])
            items.append((record["file"], record["label"]))
    return items


def load_progress() -> dict:
    """Files already tagged. "error" records are excluded so a rerun retries
    them instead of skipping them forever."""
    done = {}
    if INDUSTRY_MANIFEST_PATH.exists():
        with INDUSTRY_MANIFEST_PATH.open("r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                record = json.loads(line)
                if record.get("status") == "error":
                    continue
                done[record["file"]] = record
    return done


def process_file(fname: str, label: str) -> tuple:
    """Tags one file and returns (manifest record, log line). Pure apart from
    the LLM call, so it is safe to run in a thread pool -- only the main
    thread writes the manifest."""
    model = model_for_file(fname, "industry")
    path = BUCKET_DIRS[label] / fname
    if not path.exists():
        return ({"file": fname, "status": "error", "classify_label": label,
                 "reason": f"file not found in {BUCKET_DIRS[label].name}/",
                 "timestamp": datetime.now().isoformat(timespec="seconds")},
                f"{fname} -> ERROR (missing from {BUCKET_DIRS[label].name}/)")

    text = path.read_text(encoding="utf-8", errors="ignore")
    if len(text.strip()) < 100:
        # classify.py labels these IGNORE without a call; one that still
        # reached here is not worth an LLM call either.
        record = {"file": fname, "status": "ok", "classify_label": label, "industry": "Cross-industry",
                  "secondary_industry": None, "other_industry": None,
                  "reason": "too little text content", "model": None,
                  "taxonomy_version": TAXONOMY_VERSION, "elapsed": 0.0, "usage": {},
                  "timestamp": datetime.now().isoformat(timespec="seconds")}
        return record, f"{fname} -> Cross-industry (too little text content)"

    start = time.perf_counter()
    try:
        parsed, usage, raw_output = classify_industry(text, model)
    except Exception as e:
        return ({"file": fname, "status": "error", "classify_label": label, "model": model,
                 "reason": f"api_error: {e}",
                 "timestamp": datetime.now().isoformat(timespec="seconds")},
                f"{fname} ({model}) -> ERROR  ({e})")

    record = {
        "file": fname,
        "status": "ok",
        "classify_label": label,
        "industry": parsed["industry"],
        "secondary_industry": parsed["secondary_industry"],
        "other_industry": parsed["other_industry"],
        "reason": parsed["reason"],
        "model": model,
        "taxonomy_version": TAXONOMY_VERSION,
        "elapsed": round(time.perf_counter() - start, 2),
        "usage": usage,
        "timestamp": datetime.now().isoformat(timespec="seconds"),
    }
    if not parsed["parsed"]:
        record["raw_output"] = raw_output  # only kept when the parse actually failed
    secondary = f" / {parsed['secondary_industry']}" if parsed["secondary_industry"] else ""
    other = f" [{parsed['other_industry']}]" if parsed["other_industry"] else ""
    return record, f"{fname} ({model}) -> {parsed['industry']}{secondary}{other}  ({parsed['reason']})"


def _results(pending: list, workers: int):
    """Yields process_file() results: in file order with one worker, else in
    completion order from a thread pool."""
    if workers <= 1:
        for fname, label in pending:
            yield process_file(fname, label)
        return
    ex = ThreadPoolExecutor(max_workers=workers)
    futures = [ex.submit(process_file, fname, label) for fname, label in pending]
    try:
        for fut in as_completed(futures):
            yield fut.result()
    finally:
        ex.shutdown(wait=True, cancel_futures=True)


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------

def _bar(n: int, top: int, width: int = 32) -> str:
    return "#" * max(1, round(width * n / top)) if n else ""


def report() -> None:
    """Print the industry distribution from data/manifests/industry.jsonl.
    Read-only, no LLM calls -- safe to run while a tagging run is going."""
    if not INDUSTRY_MANIFEST_PATH.exists():
        print(f"No {INDUSTRY_MANIFEST_PATH.name} yet -- run industry.py first.")
        return
    records = [r for r in (json.loads(l) for l in INDUSTRY_MANIFEST_PATH.read_text(encoding="utf-8").splitlines() if l.strip())
               if r.get("status") == "ok"]
    if not records:
        print(f"No completed records in {INDUSTRY_MANIFEST_PATH}")
        return

    by_label = Counter(r["classify_label"] for r in records)
    print(f"\n{len(records)} page(s) tagged  ({', '.join(f'{k} {v}' for k, v in sorted(by_label.items()))})"
          f"  taxonomy: {records[-1].get('taxonomy_version')}")

    print("\n=== Primary industry ===")
    counts = Counter(r["industry"] for r in records)
    top = counts.most_common(1)[0][1]
    for name in INDUSTRIES:
        n = counts.get(name, 0)
        pct = 100 * n / len(records)
        print(f"  {name:<30} {n:>5}  {pct:>5.1f}%  {_bar(n, top)}")
    empty = [i for i in INDUSTRIES if not counts.get(i)]
    if empty:
        print(f"\n  Industries with no pages at all ({len(empty)}): {', '.join(empty)}")

    print("\n=== Primary industry x classify label ===")
    labels = sorted(by_label)
    print(f"  {'':<30}" + "".join(f"{l:>12}" for l in labels))
    for name in INDUSTRIES:
        row = [sum(1 for r in records if r["industry"] == name and r["classify_label"] == l) for l in labels]
        if any(row):
            print(f"  {name:<30}" + "".join(f"{v:>12}" for v in row))

    print("\n=== Industry incl. secondary (a page can count twice) ===")
    both = Counter(r["industry"] for r in records)
    both.update(r["secondary_industry"] for r in records if r.get("secondary_industry"))
    for name, n in both.most_common():
        print(f"  {name:<30} {n:>5}   (primary {counts.get(name, 0)}, secondary {n - counts.get(name, 0)})")

    others = Counter(r["other_industry"] for r in records if r.get("other_industry"))
    if others:
        print("\n=== OTHER: sectors the model named (taxonomy gaps) ===")
        for name, n in others.most_common(20):
            print(f"  {name:<48} {n:>5}")

    print("\n=== Per model (watch for one model's labels skewing the corpus) ===")
    for model in sorted({r["model"] for r in records if r.get("model")}):
        rows = [r for r in records if r.get("model") == model]
        top3 = Counter(r["industry"] for r in rows).most_common(3)
        print(f"  {model:<16} {len(rows):>5} pages   top: {', '.join(f'{k} {v}' for k, v in top3)}")

    print("\n=== Per source domain (top 12) ===")
    for dom, n in Counter(r["file"].split("__")[0] for r in records).most_common(12):
        rows = [r for r in records if r["file"].split("__")[0] == dom]
        top3 = Counter(r["industry"] for r in rows).most_common(3)
        print(f"  {dom:<28} {n:>5}   top: {', '.join(f'{k} {v}' for k, v in top3)}")
    print()


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--report", action="store_true",
                        help="print the industry distribution from the manifest and exit (no LLM calls)")
    parser.add_argument("--include-ignore", action="store_true",
                        help="also tag the IGNORE bucket (~9.4k pages that never reach extract.py)")
    parser.add_argument("--limit", type=int, default=None, help="tag at most this many files then stop")
    parser.add_argument("--workers", type=int, default=4, help="files to tag at once (default: 4)")
    parser.add_argument("--rps", type=float, default=1.0,
                        help="cap on requests/second across all workers (SOCLAAS sustains ~1/s per key; "
                             "default: 1, 0 for no cap)")
    parser.add_argument("--watch", action="store_true",
                        help="keep running, tagging new files as classify.py appends to its manifest")
    parser.add_argument("--poll-interval", type=float, default=10.0,
                        help="seconds between rescans in --watch mode when nothing new was found (default: 10)")
    args = parser.parse_args()

    if args.report:
        report()
        return

    global _PACER
    _PACER = Pacer(args.rps) if args.rps else None

    LOGS_DIR.mkdir(exist_ok=True)
    PID_PATH.write_text(str(os.getpid()), encoding="utf-8")
    try:
        run(args)
    finally:
        if PID_PATH.exists() and PID_PATH.read_text(encoding="utf-8").strip() == str(os.getpid()):
            PID_PATH.unlink()  # leave another instance's PID file alone


def run(args) -> None:
    labels = tuple(BUCKET_DIRS) if args.include_ignore else DEFAULT_LABELS
    already_done = load_progress()
    consecutive_errors = 0
    aborted = False
    processed_this_run = 0
    idle_announced = False

    with INDUSTRY_MANIFEST_PATH.open("a", encoding="utf-8") as manifest:
      while True:
        all_items = load_classified_files(labels)
        pending = [it for it in all_items if it[0] not in already_done]
        if args.limit is not None:
            pending = pending[: max(0, args.limit - processed_this_run)]

        if not pending:
            if not args.watch or (args.limit is not None and processed_this_run >= args.limit):
                print(f"{len(all_items)} qualifying file(s) total; {len(already_done)} already tagged", flush=True)
                break
            if not idle_announced:
                print(f"  [WATCH] idle ({len(already_done)} done) -- waiting for new files from classify.py...", flush=True)
                idle_announced = True
            time.sleep(args.poll_interval)
            continue

        idle_announced = False
        print(f"{len(pending)} new file(s) to tag ({len(already_done)} already done)", flush=True)

        results = _results(pending, args.workers)
        try:
            for i, (record, line) in enumerate(results, 1):
                manifest.write(json.dumps(record) + "\n")
                manifest.flush()
                print(f"[{i}/{len(pending)}] {line}", flush=True)

                if record["status"] == "error":
                    consecutive_errors += 1
                    if consecutive_errors >= MAX_CONSECUTIVE_ERRORS:
                        print(f"\n[ABORT] {consecutive_errors} errors in a row -- stopping rather than "
                              f"grinding through the remaining {len(pending) - i} files. Fix the cause "
                              f"and rerun; tagged files are untouched.", flush=True)
                        aborted = True
                        break
                else:
                    consecutive_errors = 0
                    already_done[record["file"]] = record
                processed_this_run += 1
        finally:
            results.close()

        if aborted:
            break

    print(f"\nDone. Manifest: {INDUSTRY_MANIFEST_PATH}")
    print("Run with --report for the distribution.")


if __name__ == "__main__":
    main()
