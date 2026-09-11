# -*- coding: utf-8 -*-
"""
Classify the pruned Markdown pages saved in docs/ (by crawl.py) using the
SOC LLM. Each page is labeled by one of three models (see llm_pool.py for
which three and why) -- model_for_file() decides which, deterministically,
per file.

Based on marcus' triage.py (marcus' files/triage.py) -- same 4-way taxonomy
and prompt, including its KEY RULE that a page about a deal/case study/team
achievement is IGNORE even if it names or quotes an individual, unless that
person's own career is the actual subject of the page. Kept from this
script's own earlier version: retry-with-backoff on transient failures, a
circuit breaker that aborts after too many errors in a row instead of
grinding through a systemic outage, and a MAX_CHARS cap on what's sent to
the LLM.

- PROVIDER: the page's primary subject is one named person's own
  career/background/expertise -- a bio, profile, or portfolio. Named to
  match providers.sql / the ProviderDocument ML schema, since that's
  exactly what this label feeds.
- HIRER: a request for work with a defined scope/deliverable/budget/deadline.
  Named to match hirers.sql / the HireDocument ML schema.
- IGNORE: company/team pages, marketing, case studies, deal summaries,
  boilerplate -- anything that isn't one person's own bio or a concrete
  work request.
- UNCERTAIN: a genuine PROVIDER that also carries explicit HIRER signals,
  or the model's response didn't parse cleanly. Not a dumping ground for
  merely low-value pages -- those are IGNORE.

crawl.py saves new pages into docs/unprocessed/ -- this script drains that
folder, moving (not copying) each file into docs/provider/, docs/hirer/,
docs/ignore/, or docs/uncertain/ once classified, so docs/unprocessed/ is
always exactly "crawled, not yet classified" and nothing sits duplicated
in two places. A file only leaves unprocessed/ after its bucket copy
succeeds -- if that fails, it stays put and is retried next time rather
than being lost. Progress is tracked in docs/manifest.jsonl; reruns skip
files already successfully classified but retry ones that previously
hard-errored.
"""

import argparse
import json
import os
import shutil
import time
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

from llm_pool import model_for_file

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT_DIR = SCRIPT_DIR.parent  # classifier_extractor/ sits one level below the project root
DOCS_DIR = ROOT_DIR / "docs"  # shared data lake -- every role reads/writes here, not its own folder
UNPROCESSED_DIR = DOCS_DIR / "unprocessed"
ENV_PATH = ROOT_DIR / ".env"
PROMPTS_DIR = SCRIPT_DIR / "prompts"

BUCKET_DIRS = {
    "PROVIDER": DOCS_DIR / "provider",
    "HIRER": DOCS_DIR / "hirer",
    "IGNORE": DOCS_DIR / "ignore",
    "UNCERTAIN": DOCS_DIR / "uncertain",
}
VALID_LABELS = set(BUCKET_DIRS)

MAX_CHARS = 24000  # cap page text sent to the LLM; crawl.py's strip_link_farms
# already removes most boilerplate runs, this is just a defense-in-depth
# margin in case a page still has an unusually long preamble before the
# real content starts (truncation is from the front)
MAX_RETRIES = 3
RETRY_BACKOFF_S = 2  # doubles each retry: 2s, 4s, 8s
# If this many classifications in a row hard-error, stop the run instead of
# grinding through the rest of the files -- a systemic problem (bad API
# key, endpoint down, quota exhausted) would otherwise burn through the
# whole batch one failure at a time before anyone notices.
MAX_CONSECUTIVE_ERRORS = 5

load_dotenv(ENV_PATH)

client = OpenAI(
    base_url=os.environ["SOCLAAS_BASE_URL"],
    api_key=os.environ["SOCLAAS_API_KEY"],
    timeout=50,
)
# No single MODEL constant -- which model classifies a given page comes from
# llm_pool.model_for_file(), one of three per MODEL_POOL. SOCLAAS_MODEL in
# .env is no longer read here (kept in .env for other tooling/reference).

# Prompt text lives in prompts/classify_triage.md, not inline here -- editing the taxonomy
# or trying a reworded prompt is then a plain-text diff/swap, not a Python code change, and
# the prompt's own history is a normal file history instead of being buried inside this
# script's.
TRIAGE_PROMPT = (PROMPTS_DIR / "classify_triage.md").read_text(encoding="utf-8").strip()


def parse_label(raw_output: str) -> dict:
    """Pull {label, reason} out of the model's response. Never raises --
    anything that doesn't parse cleanly gets routed to UNCERTAIN for manual
    review, same as triage.py."""
    text = raw_output.strip()
    if text.startswith("```"):
        text = text.strip("`")
        if text.lower().startswith("json"):
            text = text[4:]
        text = text.strip()

    try:
        data = json.loads(text)
        label = str(data.get("label", "UNCERTAIN")).upper()
        reason = data.get("reason", "")
        if label not in VALID_LABELS:
            label, reason = "UNCERTAIN", f"unrecognized label: {label}"
        return {"label": label, "reason": reason}
    except (json.JSONDecodeError, AttributeError) as e:
        return {"label": "UNCERTAIN", "reason": f"parse_error: {e}"}


def _call_llm(text: str, model: str) -> tuple:
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": f"{TRIAGE_PROMPT}\n\nPAGE TEXT:\n{text[:MAX_CHARS]}"}],
    )
    usage = {}
    if response.usage:
        usage = {
            "prompt_tokens": response.usage.prompt_tokens,
            "completion_tokens": response.usage.completion_tokens,
        }
    return response.choices[0].message.content, usage


def classify_page(text: str, model: str) -> tuple:
    """Classify with retries for transient failures (rate limits, timeouts).
    Raises only once MAX_RETRIES attempts all fail -- callers treat that as
    a hard error, not UNCERTAIN, since it means the classifier itself
    failed, not that the page was ambiguous. `model` is fixed for the
    whole call (all retries reuse it) -- a transient failure on one model
    doesn't fall back to a different one, since that would silently break
    the deterministic file->model assignment llm_pool.py relies on."""
    last_err = None
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            raw_output, usage = _call_llm(text, model)
            return parse_label(raw_output), usage, raw_output
        except Exception as e:
            last_err = e
            if attempt < MAX_RETRIES:
                wait_s = RETRY_BACKOFF_S * (2 ** (attempt - 1))
                print(f"    [RETRY] attempt {attempt}/{MAX_RETRIES} failed ({e}); retrying in {wait_s}s", flush=True)
                time.sleep(wait_s)
    raise last_err


def load_manifest(manifest_path: Path) -> dict:
    """Files already successfully classified. Records with status "error"
    are excluded so a rerun retries them instead of skipping them
    permanently -- a hard error means the classifier failed, not that the
    file is done."""
    done = {}
    if manifest_path.exists():
        with manifest_path.open("r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                record = json.loads(line)
                if record.get("status") == "error":
                    continue
                done[record["file"]] = record
    return done


def _pending_files(already_done: dict) -> list:
    """Files in docs/unprocessed/ not yet in the manifest. Re-globbed on
    every call so --watch mode picks up files crawl.py saves while this
    keeps running. A file already in the manifest but still physically
    present here (a prior bucket-move that failed) is treated as done --
    load_manifest already excludes hard errors, so this only happens for a
    successful classification whose file-move hiccuped, and forcing a
    re-classification of it would waste an LLM call for no reason."""
    md_files = sorted(UNPROCESSED_DIR.glob("*.md"))
    return md_files, [f for f in md_files if f.name not in already_done]


def _drain_stuck_moves(already_done: dict) -> None:
    """A file can be classified successfully (recorded "ok" in the
    manifest) and then fail the shutil.move into its bucket right
    afterward -- OS hiccup, the process getting killed mid-move, etc.
    _pending_files() treats anything in the manifest as done and never
    looks at it again, so without this such a file is stuck in
    unprocessed/ forever: correctly labeled, but never relocated and never
    retried. Run once at startup to relocate any of these before the main
    loop starts, using the label already on record -- no LLM call needed,
    the classification itself was never in question."""
    stuck = 0
    for fpath in sorted(UNPROCESSED_DIR.glob("*.md")):
        record = already_done.get(fpath.name)
        if not record or record.get("status") != "ok":
            continue
        dest_dir = BUCKET_DIRS.get(record.get("label"))
        if not dest_dir:
            continue
        try:
            shutil.move(str(fpath), str(dest_dir / fpath.name))
            stuck += 1
        except OSError as e:
            print(f"  WARNING: still could not move {fpath.name} out of unprocessed/: {e}", flush=True)
    if stuck:
        print(f"Relocated {stuck} already-classified file(s) that were stuck in unprocessed/ from a prior run", flush=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--watch", action="store_true",
        help="keep running after the initial backlog is classified, checking for and "
             "classifying new files as they appear -- for running alongside a still-active "
             "crawl.py instead of waiting for it to finish first",
    )
    parser.add_argument(
        "--poll-interval", type=float, default=5.0,
        help="seconds to wait between rescans in --watch mode when nothing new was found (default: 5)",
    )
    args = parser.parse_args()

    UNPROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    for d in BUCKET_DIRS.values():
        d.mkdir(parents=True, exist_ok=True)

    manifest_path = DOCS_DIR / "manifest.jsonl"
    already_done = load_manifest(manifest_path)
    _drain_stuck_moves(already_done)

    consecutive_errors = 0
    aborted = False
    idle_announced = False  # log "waiting" once per idle stretch, not every poll
    with manifest_path.open("a", encoding="utf-8") as manifest:
      while True:
        md_files, pending = _pending_files(already_done)

        if not pending:
            if not args.watch:
                print(f"Found {len(md_files)} Markdown files; {len(already_done)} already in manifest", flush=True)
                break
            if not idle_announced:
                print(f"  [WATCH] idle ({len(already_done)} done) -- waiting for new files from crawl.py...", flush=True)
                idle_announced = True
            time.sleep(args.poll_interval)
            continue

        idle_announced = False
        print(f"{len(pending)} new Markdown file(s) to classify ({len(already_done)} already done)", flush=True)

        for i, fpath in enumerate(pending, 1):
            text = fpath.read_text(encoding="utf-8", errors="ignore")
            model = model_for_file(fpath.name, "classify")

            if len(text.strip()) < 100:
                parsed = {"label": "IGNORE", "reason": "too little text content"}
                usage, elapsed, raw_output = {}, 0.0, None
                model = None  # no LLM call made, so no model to attribute this to
                consecutive_errors = 0
            else:
                start = time.perf_counter()
                try:
                    parsed, usage, raw_output = classify_page(text, model)
                    elapsed = time.perf_counter() - start
                    consecutive_errors = 0
                except Exception as e:
                    consecutive_errors += 1
                    record = {
                        "file": fpath.name,
                        "status": "error",
                        "model": model,
                        "reason": f"api_error: {e}",
                        "timestamp": datetime.now().isoformat(timespec="seconds"),
                    }
                    manifest.write(json.dumps(record) + "\n")
                    manifest.flush()
                    print(f"[{i}/{len(pending)}] {fpath.name} ({model}) -> ERROR (left in place)  ({e})", flush=True)
                    if consecutive_errors >= MAX_CONSECUTIVE_ERRORS:
                        print(
                            f"\n[ABORT] {consecutive_errors} classification errors in a row -- "
                            f"stopping so the remaining {len(pending) - i} files aren't ground through "
                            f"blindly. Fix the underlying issue and rerun; already-classified files are "
                            f"untouched.",
                            flush=True,
                        )
                        aborted = True
                        break
                    continue

            record = {
                "file": fpath.name,
                "status": "ok",
                "label": parsed["label"],
                "reason": parsed["reason"],
                "model": model,
                "elapsed": round(elapsed, 2),
                "usage": usage,
                "timestamp": datetime.now().isoformat(timespec="seconds"),
            }
            if parsed["reason"].startswith(("parse_error", "unrecognized label")):
                record["raw_output"] = raw_output  # only keep this when the parse actually failed
            manifest.write(json.dumps(record) + "\n")
            manifest.flush()

            try:
                dest = BUCKET_DIRS[parsed["label"]] / fpath.name
                shutil.move(str(fpath), str(dest))  # drains unprocessed/ as things get classified
            except OSError as e:
                print(f"  WARNING: could not move {fpath.name} out of unprocessed/: {e}", flush=True)

            already_done[fpath.name] = record
            print(f"[{i}/{len(pending)}] {fpath.name} ({model}) -> {parsed['label']}  ({parsed['reason']})", flush=True)

        if aborted:
            break

    counts = {k: len(list(v.glob("*.md"))) for k, v in BUCKET_DIRS.items()}
    print(f"\nDone. Manifest: {manifest_path}")
    print(f"Counts: {counts}")
    print(f"Check {BUCKET_DIRS['UNCERTAIN']} + the manifest's 'reason' field for manual review.")


if __name__ == "__main__":
    main()
