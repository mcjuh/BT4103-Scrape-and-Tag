# -*- coding: utf-8 -*-
"""
The "monitor" role: a centralised web dashboard over every other
role in the pipeline, laid out as the pipeline itself --

    Crawl  ->  Classify  ->  Industry  ->  Extract  ->  Label
  crawl.py   classify.py  industry.py  extract.py   label.py

Every stage answers the same three questions, in the same place, in the same
shape: is it RUNNING, how many documents has it PROCESSED, and how many are
QUEUED waiting for it. The number between two stage cards is the handoff --
documents that have cleared the left stage and are waiting on the right one.
That's the thing you actually want at a glance; per-model chips, token
counts and the raw tables are secondary and sit below.

It never writes to any role's data -- it reads logs/crawl.log,
data/pages/unprocessed/*.md, data/manifests/{classify,industry,extract}.jsonl,
data/manifests/crawl_state.json, data/output/providers.csv,
data/output/hirers.csv, data/manifests/relevance_labels.jsonl,
data/output/relevance_scores.csv and logs/<stage>.pid.

Each stage card also has Start/Stop buttons. They run only the fixed
commands in LAUNCHABLE (never a command line from the page), append to
logs/<stage>.log (the same file run.py writes), and need a per-session token
that only the page itself carries. A started run is its own process: closing the
dashboard doesn't stop it. Stop removes the stage's PID file, since a hard
stop skips the script's own cleanup. Crawl refuses to start with less than
CRAWL_MIN_FREE_GB of RAM free (BACKLOG A2).

    python monitor/dashboard.py [--port 8765]

Then open http://localhost:8765 in a browser. Ctrl+C to stop the server.
"""

import argparse
import csv
import json
import os
import re
import secrets
import signal
import subprocess
import sys
import threading
import time
from collections import Counter
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT_DIR = SCRIPT_DIR.parent  # monitor/ sits one level below the project root
DATA_DIR = ROOT_DIR / "data"  # shared data lake every role reads/writes into
MANIFESTS_DIR = DATA_DIR / "manifests"
OUTPUT_DIR = DATA_DIR / "output"
UNPROCESSED_DIR = DATA_DIR / "pages" / "unprocessed"
SEEDS_PATH = ROOT_DIR / "scraper" / "seeds.md"  # read-only; the authority on how many seeds exist
MANIFEST_PATH = MANIFESTS_DIR / "classify.jsonl"
INDUSTRY_MANIFEST_PATH = MANIFESTS_DIR / "industry.jsonl"
EXTRACT_MANIFEST_PATH = MANIFESTS_DIR / "extract.jsonl"
STATE_PATH = MANIFESTS_DIR / "crawl_state.json"
PROVIDERS_CSV = OUTPUT_DIR / "providers.csv"
HIRERS_CSV = OUTPUT_DIR / "hirers.csv"
LABELS_PATH = MANIFESTS_DIR / "relevance_labels.jsonl"
SCORES_CSV = OUTPUT_DIR / "relevance_scores.csv"
LOGS_DIR = ROOT_DIR / "logs"  # one log per stage (logs/<stage>.log, appended) and the PID files
RUN_MARK = "----- run "  # starts each run in a stage log; same marker as run.py

MANIFEST_RECORD_LIMIT = 300  # how many manifest rows the dashboard shows at once

# Labels that go on to the industry and extract stages. IGNORE stops at
# classify, so it is not part of either stage's queue.
DOWNSTREAM_LABELS = ("PROVIDER", "HIRER", "UNCERTAIN")

SEED_RE = re.compile(r"^=== \[(.*?)\] (\S+)", re.MULTILINE)
SAVED_LINE_RE = re.compile(r"^  \[SAVED\] (\S+)", re.MULTILINE)
SEED_URL_RE = re.compile(r"https?://\S+")


def _last_run(text: str) -> str:
    """The latest run in an appended stage log: everything after the last
    RUN_MARK line, so counts and the done/stopped check describe the current
    run, not every run the log has ever held."""
    cut = text.rfind("\n" + RUN_MARK)
    return text[cut + 1:] if cut >= 0 else text


def _total_seeds() -> int:
    """Seed count straight from seeds.md, which is the actual input config,
    rather than a "Loaded N total seed URLs" line in whichever log happens to
    be newest. Adding seeds to the file should move this number immediately,
    without waiting for a crawl to start."""
    return len(SEED_URL_RE.findall(_read_text(SEEDS_PATH)))


def _read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="ignore")
    except FileNotFoundError:
        return ""


def _read_jsonl(path: Path) -> list:
    """Every parseable record in a .jsonl. A half-written final line (a
    script flushing mid-append while this reads) is skipped rather than
    raising -- the dashboard must never fall over because a writer was
    mid-write."""
    records = []
    if not path.exists():
        return records
    with path.open("r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return records


def _pid_alive(pid: int) -> bool:
    if os.name == "nt":
        # os.kill(pid, 0) on Windows sends CTRL_C_EVENT rather than probing,
        # so ask the OS directly whether the process is still active.
        import ctypes
        kernel32 = ctypes.windll.kernel32
        handle = kernel32.OpenProcess(0x1000, False, pid)  # PROCESS_QUERY_LIMITED_INFORMATION
        if not handle:
            return False
        code = ctypes.c_ulong()
        ok = kernel32.GetExitCodeProcess(handle, ctypes.byref(code))
        kernel32.CloseHandle(handle)
        return bool(ok) and code.value == 259  # STILL_ACTIVE
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    return True


def _script_alive(pid_path: Path) -> bool:
    """Is the PID a script wrote at startup still alive? Every pipeline
    script writes logs/<stage>.pid and removes it on exit. It's the only
    reliable "running" signal: the crawl log can go silent for a whole seed
    (up to 30 min), an LLM stage can sit on one slow call for minutes, and a
    crash or Ctrl+C never writes a closing line. A hard kill leaves a stale
    PID file behind, which the liveness check handles."""
    try:
        pid = int(pid_path.read_text(encoding="utf-8").strip())
    except (OSError, ValueError):
        return False
    return _pid_alive(pid)


def _run_state(pid_name: str) -> str:
    # A script launched from here counts as running from the moment it starts,
    # not only once it has written its PID file -- extract.py loads spaCy and
    # crawl.py imports crawl4ai first, and a second click in that gap would
    # otherwise launch it twice.
    proc = LAUNCHED.get(pid_name)
    if proc is not None and proc.poll() is None:
        return "running"
    return "running" if _script_alive(LOGS_DIR / f"{pid_name}.pid") else "idle"


# ---------------------------------------------------------------------------
# Launching / stopping scripts from the page
# ---------------------------------------------------------------------------

# The only commands the page can run. It sends a stage key and option values,
# never a command line: the script and fixed flags come from here, every
# option is a positive integer parsed server-side before it becomes an
# argument, and every choice must be one of the values listed here. Nothing
# goes through a shell.
LAUNCHABLE = {
    "crawl": {"script": "scraper/crawl.py", "fixed": ["--concurrency", "1"], "options": {}},
    "classify": {"script": "classifier_extractor/classify.py", "fixed": [], "options": {}},
    "industry": {"script": "classifier_extractor/industry.py", "fixed": [],
                "options": {"limit": "--limit"}},
    "extract": {"script": "classifier_extractor/extract.py", "fixed": ["--balance"],
                "options": {"limit": "--limit", "per_cell": "--per-cell"},
                "choices": {"entity": ("--entity", ["hirer", "provider"])}},
    "label": {"script": "labeller/label.py", "fixed": [],
              "options": {"max_pairs": "--max-pairs"}},
}
LAUNCHED = {}  # stage -> Popen, for scripts started by this dashboard process
LAUNCH_LOCK = threading.Lock()
# crawl4ai's memory dispatcher silently throttles to zero pages below this
# (BACKLOG A2: a run at 0.3 GB free saved nothing from 98 of 121 seeds).
CRAWL_MIN_FREE_GB = 8.0
# Required on every launch/stop request. It's only ever sent inside the page
# itself, which another site's script can't read, so a random web page can't
# POST to localhost and start a run.
TOKEN = secrets.token_urlsafe(24)


def _free_ram_gb():
    """Available physical memory in GB, or None if it can't be read."""
    try:
        if os.name == "nt":
            import ctypes

            class MEMORYSTATUSEX(ctypes.Structure):
                _fields_ = [("dwLength", ctypes.c_ulong), ("dwMemoryLoad", ctypes.c_ulong),
                            ("ullTotalPhys", ctypes.c_ulonglong), ("ullAvailPhys", ctypes.c_ulonglong),
                            ("ullTotalPageFile", ctypes.c_ulonglong), ("ullAvailPageFile", ctypes.c_ulonglong),
                            ("ullTotalVirtual", ctypes.c_ulonglong), ("ullAvailVirtual", ctypes.c_ulonglong),
                            ("ullAvailExtendedVirtual", ctypes.c_ulonglong)]
            stat = MEMORYSTATUSEX()
            stat.dwLength = ctypes.sizeof(stat)
            if not ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(stat)):
                return None
            return stat.ullAvailPhys / 1e9
        for line in Path("/proc/meminfo").read_text().splitlines():
            if line.startswith("MemAvailable:"):
                return int(line.split()[1]) * 1024 / 1e9
    except (OSError, ValueError, AttributeError):
        pass
    return None


def _pid_is_python(pid: int) -> bool:
    """Guards Stop against a stale PID file whose number Windows has since
    handed to some unrelated process: only a Python process gets killed."""
    if os.name != "nt":
        return True
    import ctypes
    kernel32 = ctypes.windll.kernel32
    handle = kernel32.OpenProcess(0x1000, False, pid)  # PROCESS_QUERY_LIMITED_INFORMATION
    if not handle:
        return False
    try:
        buf = ctypes.create_unicode_buffer(1024)
        size = ctypes.c_ulong(len(buf))
        if not kernel32.QueryFullProcessImageNameW(handle, 0, buf, ctypes.byref(size)):
            return False
        name = Path(buf.value).name.lower()
        return name.startswith("python") or name in ("py.exe", "pyw.exe")
    finally:
        kernel32.CloseHandle(handle)


def _log_tail(stage: str, n: int = 4) -> list:
    lines = [l for l in _read_text(LOGS_DIR / f"{stage}.log").splitlines() if l.strip()]
    return [l[:220] for l in lines[-n:]]


def launch(stage: str, options: dict) -> tuple:
    """Starts a stage's script in the background. Returns (ok, message)."""
    spec = LAUNCHABLE.get(stage)
    if spec is None:
        return False, f"unknown stage {stage!r}"
    args = []
    for name, flag in spec["options"].items():
        raw = str(options.get(name) or "").strip()
        if not raw:
            continue
        if not raw.isdigit() or int(raw) <= 0:
            return False, f"{name} must be a positive whole number"
        args += [flag, str(int(raw))]
    for name, (flag, allowed) in spec.get("choices", {}).items():
        raw = str(options.get(name) or "").strip()
        if not raw:
            continue  # blank = the script's default (for extract: both types)
        if raw not in allowed:
            return False, f"{name} must be one of: {', '.join(allowed)}"
        args += [flag, raw]
    if stage == "crawl":
        free = _free_ram_gb()
        if free is not None and free < CRAWL_MIN_FREE_GB:
            return False, (f"only {free:.1f} GB RAM free -- the crawler saves nothing below "
                           f"~{CRAWL_MIN_FREE_GB:.0f} GB (BACKLOG A2). Free memory and retry.")
    with LAUNCH_LOCK:
        if _run_state(stage) == "running":
            return False, f"{stage} is already running"
        LOGS_DIR.mkdir(exist_ok=True)
        log_path = LOGS_DIR / f"{stage}.log"
        cmd = [sys.executable, "-u", str(ROOT_DIR / spec["script"]), *spec["fixed"], *args]
        # utf-8 output: page titles are printed and would crash a cp1252 console encoder
        env = {**os.environ, "PYTHONIOENCODING": "utf-8", "PYTHONUNBUFFERED": "1"}
        # Own process group, no console: the run survives the dashboard being
        # closed, and a Ctrl+C in the dashboard's window doesn't reach it.
        flags = (subprocess.CREATE_NEW_PROCESS_GROUP | subprocess.CREATE_NO_WINDOW) if os.name == "nt" else 0
        with log_path.open("a", encoding="utf-8") as log:
            log.write(f"\n{RUN_MARK}{time.strftime('%Y-%m-%d %H:%M:%S')}: {' '.join(cmd)}\n")
            log.flush()
            LAUNCHED[stage] = subprocess.Popen(
                cmd, cwd=ROOT_DIR, stdout=log, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL,
                env=env, creationflags=flags, start_new_session=(os.name != "nt"))
    return True, f"started {spec['script']} -> logs/{log_path.name}"


def stop(stage: str) -> tuple:
    """Stops a running stage. Every script is safe to stop mid-run: finished
    files are already in its manifest, and in-flight ones are redone next run."""
    if stage not in LAUNCHABLE:
        return False, f"unknown stage {stage!r}"
    pid_path = LOGS_DIR / f"{stage}.pid"
    pids = set()
    try:
        pids.add(int(pid_path.read_text(encoding="utf-8").strip()))
    except (OSError, ValueError):
        pass
    proc = LAUNCHED.get(stage)
    if proc is not None and proc.poll() is None:
        pids.add(proc.pid)
    pids = {p for p in pids if _pid_alive(p) and _pid_is_python(p)}
    if not pids:
        return False, f"{stage} isn't running"
    for pid in pids:
        try:
            os.kill(pid, signal.SIGTERM)  # TerminateProcess on Windows
        except OSError as e:
            return False, f"couldn't stop PID {pid}: {e}"
    # A hard stop skips the script's own cleanup, so remove its PID file here.
    pid_path.unlink(missing_ok=True)
    return True, f"stopped {stage} (PID {', '.join(map(str, sorted(pids)))})"


def _csv_row_count(path: Path) -> int:
    if not path.exists():
        return 0
    with path.open("r", encoding="utf-8", newline="") as f:
        return max(0, sum(1 for _ in csv.reader(f)) - 1)  # minus header row


def _counted(records: list, key: str) -> dict:
    counts = {}
    for r in records:
        v = r.get(key) or "legacy (pre-multi-LLM)"
        counts[v] = counts.get(v, 0) + 1
    return counts


def _stage(key, name, script, state, processed, queue, **extra) -> dict:
    """One pipeline stage in the shape the UI renders. `processed` and
    `queue` are the two numbers every stage must be able to answer with;
    everything else is optional detail."""
    stage = {
        "key": key, "name": name, "script": script, "state": state,
        "processed": processed, "queue": queue,
        "total": processed + queue,
        "errors": 0, "chips": [], "rows": [], "note": None,
    }
    stage.update(extra)
    return stage


# ---------------------------------------------------------------------------
# Per-stage status
# ---------------------------------------------------------------------------

def crawl_state() -> list:
    """Raw per-seed results from data/manifests/crawl_state.json: crawl.py's own
    structured record of every seed it has finished (or given up on),
    independent of what's still in the text log. Each entry is
    [label, url, status, note, saved_count]."""
    if not STATE_PATH.exists():
        return []
    try:
        return json.loads(STATE_PATH.read_text(encoding="utf-8", errors="ignore"))
    except (json.JSONDecodeError, OSError):
        return []


def crawl_stage(state: list) -> dict:
    """Seeds, not pages, are the crawler's unit of work.

    A seed counts as PROCESSED only if it actually saved something. That
    matches crawl.py's own rule -- it retries any seed with saved_count == 0
    rather than treating it as done -- and it stops the dashboard reporting
    a green 86/86 while 63 of those seeds have never produced a page, which
    is exactly what it used to do."""
    content = _last_run(_read_text(LOGS_DIR / "crawl.log"))
    if _run_state("crawl") == "running":
        run_state = "running"
    elif content.rfind("Batch done.") > content.rfind("total seed URLs"):
        run_state = "done"  # the latest run in the log reached its end
    elif content:
        run_state = "stopped"  # crashed, killed, or Ctrl+C'd mid-run
    else:
        run_state = "idle"

    productive = [e for e in state if len(e) > 4 and e[4] > 0]
    barren = [e for e in state if len(e) > 4 and e[4] == 0]
    total_seeds = _total_seeds() or len(state)
    # Seeds never attempted at all, plus the ones that came back with nothing
    # and so will be retried -- both are still owed work.
    queue = max(0, total_seeds - len(productive))

    seed_matches = list(SEED_RE.finditer(content))
    current = f"{seed_matches[-1].group(1)} -- {seed_matches[-1].group(2)}" if seed_matches else None
    pages_saved = sum(e[4] for e in productive)

    chips = [("saved", pages_saved), ("blocked", content.count("  [BLOCKED]")),
             ("skipped", content.count("  [SKIP]")), ("failed", content.count("  [FAIL]"))]
    note = f"{len(barren)} seed(s) have saved 0 pages and will be retried" if barren else None
    return _stage(
        "crawl", "Crawl", "scraper/crawl.py", run_state,
        processed=len(productive), queue=queue,
        unit="seeds", output=pages_saved, output_unit="pages saved",
        current=current, chips=chips, note=note,
        recent=SAVED_LINE_RE.findall(content)[-6:],
    )


def classify_stage(records: list) -> dict:
    """Queue = whatever is physically sitting in data/pages/unprocessed/. That
    folder is exactly "crawled, not yet classified" -- classify.py moves each
    file out as it goes -- so the directory listing is the queue, no
    bookkeeping needed."""
    ok = [r for r in records if r.get("status") != "error"]
    errors = sum(1 for r in records if r.get("status") == "error")
    queue = len(list(UNPROCESSED_DIR.glob("*.md"))) if UNPROCESSED_DIR.exists() else 0

    labels = _counted(ok, "label")
    usage_in = sum((r.get("usage") or {}).get("prompt_tokens") or 0 for r in records)
    usage_out = sum((r.get("usage") or {}).get("completion_tokens") or 0 for r in records)

    return _stage(
        "classify", "Classify", "classify.py --watch",
        _run_state("classify"),
        processed=len(ok), queue=queue, unit="docs", errors=errors,
        chips=[(k, labels.get(k, 0)) for k in ("PROVIDER", "HIRER", "IGNORE", "UNCERTAIN")],
        models=_counted(ok, "model"),
        tokens={"prompt": usage_in, "completion": usage_out},
        output=sum(labels.get(k, 0) for k in DOWNSTREAM_LABELS),
        output_unit="docs to downstream stages",
        recent=[f"{r['file']} -> {'ERROR' if r.get('status') == 'error' else r.get('label', '?')}"
                for r in records[-6:]],
    )


def industry_stage(downstream_files: set) -> dict:
    """Stage 3: the industry tag. Its queue is every PROVIDER/HIRER/UNCERTAIN
    file classify.py has produced that it hasn't tagged yet -- the same set
    extract.py works from, which is why the two stages show the same total
    and can be read against each other."""
    records = _read_jsonl(INDUSTRY_MANIFEST_PATH)
    ok = [r for r in records if r.get("status") == "ok"]
    errors = sum(1 for r in records if r.get("status") == "error")
    tagged = {r["file"] for r in ok}

    industries = _counted(ok, "industry")
    top = sorted(industries.items(), key=lambda kv: -kv[1])[:6]
    taxonomy = ok[-1].get("taxonomy_version") if ok else None

    # The full spread for the Industry panel: every industry in the taxonomy,
    # including ones with no pages yet (those are the seeding targets), split
    # by which CSV a page would feed. UNCERTAIN extracts as a provider.
    names = _taxonomy_industries()
    names += sorted(n for n in industries if n not in names)  # a label the taxonomy no longer has
    side = {"PROVIDER": "provider", "UNCERTAIN": "provider", "HIRER": "hirer"}
    spread = {n: {"name": n, "total": 0, "provider": 0, "hirer": 0} for n in names}
    for r in ok:
        row = spread.get(r.get("industry") or "OTHER")
        if row is None:
            continue
        row["total"] += 1
        row[side.get(r.get("classify_label"), "provider")] += 1
    other_named = Counter(r["other_industry"] for r in ok if r.get("other_industry")).most_common(8)

    return _stage(
        "industry", "Industry", "industry.py",
        _run_state("industry"),
        processed=len(ok), queue=len(downstream_files - tagged), unit="docs", errors=errors,
        chips=top, models=_counted(ok, "model"),
        note=f"taxonomy {taxonomy}" if taxonomy else None,
        output=len(industries), output_unit="distinct industries seen",
        recent=[f"{r['file']} -> {r.get('industry', '?')}" for r in ok[-6:]],
        spread=list(spread.values()), other_named=other_named,
    )


# Not real sectors: shown under a divider at the bottom of the spread.
INDUSTRY_CATCHALLS = ("Cross-industry", "OTHER")


def _taxonomy_industries() -> list:
    """Industry names in taxonomy order, straight from industry.py's
    taxonomy file (its input config, like seeds.md for the crawl), so an
    industry with no pages yet still shows up as a zero."""
    try:
        data = json.loads(_read_text(ROOT_DIR / "classifier_extractor" / "prompts" / "industry_taxonomy.json"))
        return [i["name"] for i in data["industries"]]
    except (ValueError, KeyError, TypeError):
        return []


def extract_stage(downstream_files: set) -> dict:
    """Queue is the same downstream set as the industry stage, minus whatever
    already has a terminal extract record. "Processed" counts rejected rows
    too -- a page the model judged non-qualifying is finished work, not
    backlog, and lumping it into the queue would make the stage look
    permanently behind."""
    records = _read_jsonl(EXTRACT_MANIFEST_PATH)
    done = {r["file"] for r in records if r.get("status") in ("written", "rejected")}
    written = sum(1 for r in records if r.get("status") == "written")
    rejected = sum(1 for r in records if r.get("status") == "rejected")
    errors = sum(1 for r in records if r.get("status") == "error")

    recent = []
    for r in records[-6:]:
        if r.get("status") == "written":
            recent.append(f"{r['file']} -> WRITTEN ({r.get('title') or r.get('entity_type', '?')})")
        elif r.get("status") == "rejected":
            recent.append(f"{r['file']} -> REJECTED ({r.get('reason', '')})")
        else:
            recent.append(f"{r['file']} -> ERROR")

    providers, hirers = _csv_row_count(PROVIDERS_CSV), _csv_row_count(HIRERS_CSV)
    return _stage(
        "extract", "Extract", "extract.py --watch",
        _run_state("extract"),
        processed=len(done), queue=len(downstream_files - done), unit="docs", errors=errors,
        chips=[("written", written), ("rejected", rejected),
               ("providers.csv", providers), ("hirers.csv", hirers)],
        models=_counted([r for r in records if r.get("status") in ("written", "rejected")], "model"),
        output=providers + hirers, output_unit="rows in the CSVs",
        recent=recent,
    )


def label_stage(providers: int, hirers: int) -> dict:
    """The labeller's unit is the (gig, provider) pair, and its queue is
    every pair the two CSVs imply but which hasn't been scored -- which is
    why this number jumps every time extract.py writes a row."""
    records = _read_jsonl(LABELS_PATH)
    ok = [r for r in records if r.get("status") == "ok"]
    errors = len(records) - len(ok)
    pairs = {(r["hirer"], r["provider"]) for r in ok}
    possible = providers * hirers

    return _stage(
        "label", "Label", "labeller/label.py",
        _run_state("label"),
        processed=len(pairs), queue=max(0, possible - len(pairs)), unit="pairs", errors=errors,
        chips=sorted(_counted(ok, "approach").items(), key=lambda kv: -kv[1]),
        output=_csv_row_count(SCORES_CSV), output_unit="rows in relevance_scores.csv",
        note=f"{providers} providers x {hirers} gigs" if possible else "needs rows in both CSVs",
        recent=[],
    )


def pipeline() -> dict:
    classify_records = _read_jsonl(MANIFEST_PATH)
    downstream_files = {
        r["file"] for r in classify_records
        if r.get("status") != "error" and r.get("label") in DOWNSTREAM_LABELS
    }
    state = crawl_state()
    ex = extract_stage(downstream_files)
    stages = [
        crawl_stage(state),
        classify_stage(classify_records),
        industry_stage(downstream_files),
        ex,
        label_stage(_csv_row_count(PROVIDERS_CSV), _csv_row_count(HIRERS_CSV)),
    ]
    for s in stages:
        spec = LAUNCHABLE[s["key"]]
        s["launch"] = {
            "command": " ".join([spec["script"], *spec["fixed"]]),
            "options": list(spec["options"]),
            "choices": {k: allowed for k, (_, allowed) in spec.get("choices", {}).items()},
            "log": _log_tail(s["key"]),
            "log_file": f"logs/{s['key']}.log",
        }
    free = _free_ram_gb()
    return {
        "stages": stages,
        "free_ram_gb": round(free, 1) if free is not None else None,
        "crawl_min_free_gb": CRAWL_MIN_FREE_GB,
        "crawl_state": state,
        # newest first, capped so a huge manifest doesn't balloon every response
        "records": list(reversed(classify_records[-MANIFEST_RECORD_LIMIT:])),
    }


PAGE = """<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Pipeline Dashboard</title>
<style>
  :root {
    color-scheme: dark;
    --bg: #0f1115; --panel: #171a21; --border: #2a2f3a; --text: #e6e8eb;
    --muted: #8b93a1; --accent: #5b9dff; --green: #3ecf8e; --yellow: #e8b339;
    --red: #ef5d5d; --magenta: #c792ea; --cyan: #56d4dd;
  }
  * { box-sizing: border-box; }
  body {
    margin: 0; padding: 24px; background: var(--bg); color: var(--text);
    font: 14px/1.5 -apple-system, "Segoe UI", Roboto, sans-serif;
  }
  header { display: flex; align-items: baseline; gap: 12px; margin-bottom: 4px; }
  h1 { font-size: 18px; margin: 0; }
  .subtitle { color: var(--muted); font-size: 12.5px; margin-bottom: 20px; }

  /* ---- pipeline ---- */
  .pipeline { display: flex; align-items: stretch; gap: 0; overflow-x: auto; padding-bottom: 6px; }
  .stage {
    flex: 1 1 0; min-width: 190px; background: var(--panel); border: 1px solid var(--border);
    border-radius: 10px; padding: 14px 16px; display: flex; flex-direction: column;
  }
  .stage.is-running { border-color: rgba(232,179,57,.55); box-shadow: 0 0 0 1px rgba(232,179,57,.15); }
  .stage.has-queue .queue-n { color: var(--yellow); }
  .stage-head { display: flex; justify-content: space-between; align-items: center; gap: 8px; }
  .stage-name { font-size: 14px; font-weight: 700; }
  .stage-script {
    font-family: ui-monospace, SFMono-Regular, Consolas, monospace; font-size: 10.5px;
    color: var(--muted); margin: 2px 0 12px; overflow-wrap: anywhere;
  }
  .counts { display: flex; gap: 14px; margin-bottom: 10px; }
  .count { flex: 1; }
  .count .n { font-size: 22px; font-weight: 700; line-height: 1.1; font-variant-numeric: tabular-nums; }
  .count .l { font-size: 10.5px; text-transform: uppercase; letter-spacing: .05em; color: var(--muted); }
  .bar-track { background: #23262f; border-radius: 6px; height: 6px; overflow: hidden; margin: 2px 0 10px; }
  .bar-fill { height: 100%; background: var(--accent); transition: width .4s ease; }
  .stage-foot { margin-top: auto; }
  .stage .out { font-size: 11.5px; color: var(--muted); margin-top: 8px; }
  .stage .out b { color: var(--text); }
  .stage .note { font-size: 11px; color: var(--yellow); margin-top: 8px; }
  .stage .err { font-size: 11.5px; color: var(--red); margin-top: 6px; }
  .arrow {
    flex: 0 0 auto; align-self: center; padding: 0 6px; text-align: center; min-width: 58px;
  }
  .arrow .n { font-size: 12px; font-weight: 700; font-variant-numeric: tabular-nums; }
  .arrow .g { color: var(--muted); font-size: 16px; line-height: 1; }

  .badge { display: inline-block; padding: 2px 9px; border-radius: 999px; font-size: 10px; font-weight: 700; letter-spacing: .05em; }
  .badge.running { background: rgba(232,179,57,.15); color: var(--yellow); }
  .badge.done { background: rgba(62,207,142,.15); color: var(--green); }
  .badge.stopped { background: rgba(239,93,93,.15); color: var(--red); }
  .badge.idle { background: rgba(139,147,161,.15); color: var(--muted); }

  .labels { display: flex; flex-wrap: wrap; gap: 6px; margin-top: 10px; }
  .chip { font-size: 11px; padding: 3px 8px; border-radius: 7px; background: #1f232c; border: 1px solid var(--border); color: var(--muted); }
  .chip b { color: var(--text); }
  .chip.model { border-color: rgba(199,146,234,.35); }

  /* ---- secondary ---- */
  details.more { margin-top: 18px; }
  details.more > summary {
    cursor: pointer; color: var(--muted); font-size: 12px; text-transform: uppercase;
    letter-spacing: .06em; font-weight: 600; padding: 8px 0; list-style: none;
  }
  details.more > summary::before { content: "\\25B8  "; }
  details.more[open] > summary::before { content: "\\25BE  "; }
  .wide-panel {
    background: var(--panel); border: 1px solid var(--border); border-radius: 10px;
    padding: 14px 18px; margin-bottom: 16px;
  }
  .wide-panel h2 { font-size: 12px; text-transform: uppercase; letter-spacing: .06em; color: var(--muted); margin: 0 0 12px; display: inline-block; }
  .table-scroll { max-height: 340px; overflow-y: auto; border-radius: 6px; }
  table { width: 100%; border-collapse: collapse; font-size: 12.5px; }
  thead th {
    position: sticky; top: 0; background: #1c2029; text-align: left; color: var(--muted);
    font-weight: 600; padding: 6px 10px; border-bottom: 1px solid var(--border);
  }
  tbody td { padding: 5px 10px; border-bottom: 1px solid #1e222b; vertical-align: top; overflow-wrap: anywhere; }
  tbody tr:hover { background: #1b1f28; }
  .status-ok { color: var(--green); }
  .status-fail { color: var(--red); }
  .status-skip { color: var(--muted); }
  .mono { font-family: ui-monospace, SFMono-Regular, Consolas, monospace; font-size: 11.5px; }
  .muted { color: var(--muted); }
  .feed-line { font-size: 12.5px; padding: 3px 0; font-family: ui-monospace, SFMono-Regular, Consolas, monospace; white-space: pre-wrap; overflow-wrap: anywhere; }
  .tag { display: inline-block; width: 76px; font-weight: 700; font-size: 11px; }
  .tag.crawl { color: var(--cyan); }
  .tag.classify { color: var(--magenta); }
  .tag.industry { color: var(--accent); }
  .tag.extract { color: var(--green); }
  .filters { float: right; display: flex; gap: 6px; }
  .filter-btn {
    background: #1f232c; border: 1px solid var(--border); color: var(--muted); font-size: 11px;
    padding: 3px 10px; border-radius: 6px; cursor: pointer;
  }
  .filter-btn.active { background: var(--accent); color: #0f1115; border-color: var(--accent); font-weight: 700; }
  .updated { color: var(--muted); font-size: 11.5px; margin-top: 18px; text-align: right; }

  /* ---- industry spread ---- */
  #industry-panel { margin-top: 16px; }
  .spread { display: grid; grid-template-columns: minmax(120px, 210px) 1fr 52px 50px 64px 52px;
            column-gap: 12px; align-items: center; font-size: 12.5px; }
  .spread .hd { font-size: 10.5px; text-transform: uppercase; letter-spacing: .05em; color: var(--muted);
                padding-bottom: 6px; border-bottom: 1px solid var(--border); margin-bottom: 4px; }
  .spread .num { text-align: right; font-variant-numeric: tabular-nums; }
  .spread .row { display: contents; }
  .spread .row > div { padding: 3px 0; }
  .spread .row:hover > div { background: #1b1f28; }
  .spread .row.zero > div { color: var(--muted); }
  .spread .track { height: 10px; position: relative; }
  .spread .fill { position: absolute; left: 0; top: 0; bottom: 0; background: var(--accent);
                  border-radius: 0 4px 4px 0; min-width: 2px; }
  .spread .fill.catchall { background: var(--muted); }
  .spread .divider { grid-column: 1 / -1; border-top: 1px dashed var(--border); margin: 6px 0 3px; }
  .spread-foot { font-size: 11.5px; color: var(--muted); margin-top: 10px; }
  @media (max-width: 640px) {
    body { padding: 16px; }
    header { flex-wrap: wrap; }
    .spread { grid-template-columns: minmax(0, 1fr) 56px 36px 50px 38px; column-gap: 8px; font-size: 12px; }
    .spread .share { display: none; }  /* still in the hover tooltip */
  }
  #tip { position: fixed; pointer-events: none; background: #0f1115; border: 1px solid var(--border);
         border-radius: 6px; padding: 6px 9px; font-size: 12px; display: none; z-index: 20; white-space: nowrap; }
  #tip b { color: var(--text); }

  /* ---- launch controls ---- */
  .controls { border-top: 1px solid var(--border); margin-top: 12px; padding-top: 10px; }
  .opts { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 8px; }
  .opts label { font-size: 10.5px; color: var(--muted); display: flex; flex-direction: column; gap: 2px; }
  .opts input, .opts select {
    width: 76px; background: #0f1115; color: var(--text); border: 1px solid var(--border);
    border-radius: 5px; padding: 3px 6px; font: inherit; font-size: 12px;
  }
  .btn {
    border: 1px solid var(--border); border-radius: 6px; padding: 4px 12px; font: inherit;
    font-size: 12px; font-weight: 600; cursor: pointer; background: #1f232c; color: var(--text);
  }
  .btn.start { border-color: rgba(62,207,142,.5); color: var(--green); }
  .btn.stop { border-color: rgba(239,93,93,.5); color: var(--red); }
  .btn:disabled { opacity: .4; cursor: not-allowed; }
  .btn:not(:disabled):hover { background: #262b35; }
  .ctl-note { font-size: 11px; color: var(--muted); margin-top: 6px; }
  .ctl-note.warn { color: var(--yellow); }
  .log {
    margin-top: 8px; background: #0f1115; border: 1px solid var(--border); border-radius: 6px;
    padding: 5px 7px; font-family: ui-monospace, SFMono-Regular, Consolas, monospace;
    font-size: 10.5px; color: var(--muted); white-space: pre-wrap; overflow-wrap: anywhere;
    max-height: 92px; overflow-y: auto;
  }
  #toast {
    position: fixed; bottom: 18px; left: 50%; transform: translateX(-50%); padding: 8px 14px;
    border-radius: 8px; font-size: 12.5px; background: var(--panel); border: 1px solid var(--border);
    display: none; max-width: min(640px, calc(100vw - 32px)); z-index: 10;
  }
  #toast.ok { display: block; border-color: rgba(62,207,142,.6); }
  #toast.fail { display: block; border-color: rgba(239,93,93,.6); color: var(--red); }
</style>
</head>
<body>
  <header><h1>Pipeline</h1><span id="headline" class="muted"></span></header>
  <div class="subtitle">RUNNING comes from each script&#39;s PID file (logs/&lt;stage&gt;.pid), so it is exact. Start/Stop run the fixed command shown on each card; output is appended to logs/&lt;stage&gt;.log. Runs keep going if this dashboard is closed.</div>

  <div class="pipeline" id="pipeline"></div>
  <div class="wide-panel" id="industry-panel"></div>
  <div id="tip"></div>

  <details class="more" id="more-detail">
    <summary>Detail &mdash; seeds, manifest, activity</summary>
    <div class="wide-panel" id="models-panel"></div>
    <div class="wide-panel" id="seeds-panel"></div>
    <div class="wide-panel" id="manifest-panel"></div>
    <div class="wide-panel" id="feed-panel"></div>
  </details>

  <div class="updated" id="updated"></div>
  <div id="toast"></div>

<script>
function esc(s) {
  return String(s).replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
}
const fmt = n => (n == null ? '-' : Number(n).toLocaleString());

const TOKEN = '__TOKEN__';
const OPTION_LABELS = {limit: 'limit', per_cell: 'per cell', max_pairs: 'max pairs', entity: 'extract'};
const optValues = {};  // stage -> {option: value}, kept here so a re-render doesn't wipe typing
let ram = {free: null, min: 8};

function renderControls(s) {
  const l = s.launch || {};
  const running = s.state === 'running';
  const vals = optValues[s.key] || {};
  const inputs = (l.options || []).map(o => `
      <label>${esc(OPTION_LABELS[o] || o)}
        <input type="number" min="1" step="1" placeholder="all" data-stage="${s.key}" data-opt="${o}"
               value="${esc(vals[o] || '')}" ${running ? 'disabled' : ''}></label>`).join('')
    + Object.entries(l.choices || {}).map(([o, allowed]) => `
      <label>${esc(OPTION_LABELS[o] || o)}
        <select data-stage="${s.key}" data-opt="${o}" ${running ? 'disabled' : ''}>
          <option value="">both</option>
          ${allowed.map(a => `<option value="${esc(a)}" ${vals[o] === a ? 'selected' : ''}>${esc(a)}s only</option>`).join('')}
        </select></label>`).join('');
  let note = `<div class="ctl-note mono">${esc(l.command || '')}</div>`;
  let blocked = false;
  if (s.key === 'crawl' && ram.free != null && ram.free < ram.min && !running) {
    blocked = true;
    note += `<div class="ctl-note warn">${ram.free} GB RAM free; crawl needs ${ram.min} GB+</div>`;
  }
  const log = (l.log || []).length
    ? `<div class="log" title="${esc(l.log_file || '')}">${l.log.map(esc).join('\\n')}</div>` : '';
  return `
    <div class="controls">
      ${inputs ? `<div class="opts">${inputs}</div>` : ''}
      ${running
        ? `<button class="btn stop" data-action="stop" data-stage="${s.key}">Stop</button>`
        : `<button class="btn start" data-action="launch" data-stage="${s.key}" ${blocked ? 'disabled' : ''}>Start</button>`}
      ${note}
      ${log}
    </div>`;
}

const CATCHALLS = ['Cross-industry', 'OTHER'];

function renderSpread(stage) {
  const rows = (stage && stage.spread) || [];
  const total = rows.reduce((a, r) => a + r.total, 0);
  if (!total) {
    return `<h2>Industry spread</h2><div class="muted">No pages tagged yet. Start the Industry stage.</div>`;
  }
  const real = rows.filter(r => !CATCHALLS.includes(r.name)).sort((a, b) => b.total - a.total || a.name.localeCompare(b.name));
  const catch_ = rows.filter(r => CATCHALLS.includes(r.name));
  const max = Math.max(...rows.map(r => r.total), 1);
  const pct = n => (100 * n / total).toFixed(1) + '%';
  const row = r => {
    const tip = `<b>${esc(r.name)}</b><br>${fmt(r.total)} pages (${pct(r.total)})<br>` +
                `${fmt(r.provider)} provider &middot; ${fmt(r.hirer)} hirer`;
    return `<div class="row ${r.total ? '' : 'zero'}" data-tip="${esc(tip)}">
      <div>${esc(r.name)}</div>
      <div class="track">${r.total ? `<div class="fill ${CATCHALLS.includes(r.name) ? 'catchall' : ''}"
           style="width:${(100 * r.total / max).toFixed(2)}%"></div>` : ''}</div>
      <div class="num">${fmt(r.total)}</div>
      <div class="num share">${pct(r.total)}</div>
      <div class="num">${fmt(r.provider)}</div>
      <div class="num">${fmt(r.hirer)}</div>
    </div>`;
  };
  const empty = real.filter(r => !r.total).map(r => r.name);
  const named = (stage.other_named || []).map(([k, v]) => `${esc(k)} (${fmt(v)})`).join(', ');
  return `
    <h2>Industry spread &mdash; ${fmt(total)} pages tagged</h2>
    <div class="spread">
      <div class="hd">Industry</div><div class="hd"></div><div class="hd num">Pages</div>
      <div class="hd num share">Share</div><div class="hd num">Provider</div><div class="hd num">Hirer</div>
      ${real.map(row).join('')}
      <div class="divider"></div>
      ${catch_.map(row).join('')}
    </div>
    <div class="spread-foot">
      ${empty.length ? `No pages yet: ${esc(empty.join(', '))}. ` : ''}
      ${named ? `OTHER named: ${named}.` : ''}
    </div>`;
}

function wireTips() {
  const tip = document.getElementById('tip');
  document.addEventListener('mousemove', e => {
    const row = e.target.closest && e.target.closest('[data-tip]');
    if (!row) { tip.style.display = 'none'; return; }
    tip.innerHTML = row.dataset.tip;
    tip.style.display = 'block';
    const x = Math.min(e.clientX + 14, window.innerWidth - tip.offsetWidth - 8);
    tip.style.left = x + 'px';
    tip.style.top = (e.clientY + 14) + 'px';
  });
}

function toast(msg, ok) {
  const t = document.getElementById('toast');
  t.textContent = msg;
  t.className = ok ? 'ok' : 'fail';
  clearTimeout(toast._t);
  toast._t = setTimeout(() => { t.className = ''; }, 6000);
}

async function act(action, stage) {
  if (action === 'stop' && !confirm(`Stop ${stage}? Finished files are kept; in-flight ones are redone next run.`)) return;
  try {
    const res = await fetch(`/api/${action}`, {
      method: 'POST',
      headers: {'Content-Type': 'application/json', 'X-Token': TOKEN},
      body: JSON.stringify({stage, options: optValues[stage] || {}}),
    });
    const data = await res.json().catch(() => ({ok: false, message: `HTTP ${res.status}`}));
    toast(data.message, data.ok);
  } catch (e) {
    toast(String(e), false);
  }
  refresh();
}

function renderStage(s) {
  const pct = s.total ? Math.min(100, 100 * s.processed / s.total) : 0;
  const cls = ['stage', s.state === 'running' ? 'is-running' : '', s.queue > 0 ? 'has-queue' : ''].join(' ');
  return `
    <div class="${cls}">
      <div class="stage-head">
        <span class="stage-name">${esc(s.name)}</span>
        <span class="badge ${s.state}">${s.state.toUpperCase()}</span>
      </div>
      <div class="stage-script">${esc(s.script)}</div>
      <div class="counts">
        <div class="count"><div class="n">${fmt(s.processed)}</div><div class="l">processed</div></div>
        <div class="count"><div class="n queue-n">${fmt(s.queue)}</div><div class="l">queued</div></div>
      </div>
      <div class="bar-track"><div class="bar-fill" style="width:${pct}%"></div></div>
      <div class="stage-foot">
        <div class="out">${fmt(s.processed)} / ${fmt(s.total)} ${esc(s.unit || 'docs')}</div>
        ${s.output != null ? `<div class="out"><b>${fmt(s.output)}</b> ${esc(s.output_unit || '')}</div>` : ''}
        ${s.current ? `<div class="out">at ${esc(s.current)}</div>` : ''}
        ${s.errors ? `<div class="err">${fmt(s.errors)} error(s)</div>` : ''}
        ${s.note ? `<div class="note">${esc(s.note)}</div>` : ''}
        ${(s.chips || []).length ? `<div class="labels">${s.chips.map(([k, v]) =>
            `<span class="chip">${esc(k)} <b>${fmt(v)}</b></span>`).join('')}</div>` : ''}
        ${renderControls(s)}
      </div>
    </div>`;
}

function renderPipeline(stages) {
  const parts = [];
  stages.forEach((s, i) => {
    parts.push(renderStage(s));
    if (i < stages.length - 1) {
      const next = stages[i + 1];
      parts.push(`<div class="arrow"><div class="g">&#9656;</div><div class="n">${fmt(next.queue)}</div><div class="l muted" style="font-size:10px">waiting</div></div>`);
    }
  });
  return parts.join('');
}

function renderHeadline(stages) {
  const running = stages.filter(s => s.state === 'running').map(s => s.name);
  const queued = stages.reduce((a, s) => a + (s.queue || 0), 0);
  const errs = stages.reduce((a, s) => a + (s.errors || 0), 0);
  const bits = [running.length ? `running: ${running.join(', ')}` : 'nothing running',
                `${fmt(queued)} queued across all stages`];
  if (errs) bits.push(`${fmt(errs)} errors`);
  return bits.join('  &middot;  ');
}

function renderModels(stages) {
  const blocks = stages.filter(s => s.models && Object.keys(s.models).length).map(s => {
    const chips = Object.entries(s.models).sort((a, b) => b[1] - a[1])
      .map(([m, n]) => `<span class="chip model">${esc(m)} <b>${fmt(n)}</b></span>`).join('');
    const tok = s.tokens ? `<span class="muted" style="font-size:11.5px">
        ${fmt(s.tokens.prompt)} prompt + ${fmt(s.tokens.completion)} completion tokens</span>` : '';
    return `<div style="margin-bottom:12px"><div class="muted" style="font-size:11.5px;margin-bottom:4px">
       ${esc(s.name)} ${tok}</div><div class="labels">${chips}</div></div>`;
  }).join('');
  return `<h2>Model routing per stage</h2>${blocks || '<div class="muted">No model-attributed records yet.</div>'}`;
}

const STATUS_CLASS = s => s.startsWith('OK') ? 'status-ok' : s.startsWith('FAILED') ? 'status-fail' : 'status-skip';

function renderSeeds(state) {
  const barren = state.filter(e => e[4] === 0).length;
  const rows = state.map(([label, url, status, note, saved]) => `
    <tr>
      <td>${esc(label)}</td>
      <td class="mono">${esc(url)}</td>
      <td class="${STATUS_CLASS(status)}">${esc(status)}</td>
      <td>${fmt(saved)}</td>
      <td class="muted">${esc(note || '')}</td>
    </tr>`).join('');
  return `
    <h2>Seeds &mdash; ${state.length} recorded, ${barren} with 0 pages saved</h2>
    <div class="table-scroll"><table>
      <thead><tr><th>Label</th><th>Seed URL</th><th>Status</th><th>Saved</th><th>Note</th></tr></thead>
      <tbody>${rows || '<tr><td colspan="5" class="muted">(no seeds recorded yet)</td></tr>'}</tbody>
    </table></div>`;
}

let manifestFilter = 'ALL';

function renderManifest(records) {
  const labels = ['ALL', 'PROVIDER', 'HIRER', 'IGNORE', 'UNCERTAIN', 'ERROR'];
  const filterBtns = labels.map(l =>
    `<span class="filter-btn ${manifestFilter === l ? 'active' : ''}" data-label="${l}">${l}</span>`).join('');
  const filtered = records.filter(r => {
    if (manifestFilter === 'ALL') return true;
    if (manifestFilter === 'ERROR') return r.status === 'error';
    return r.label === manifestFilter;
  });
  const rows = filtered.slice(0, 150).map(r => {
    const label = r.status === 'error' ? 'ERROR' : (r.label || '?');
    const u = r.usage || {};
    const tok = (u.prompt_tokens || u.completion_tokens) ? `${u.prompt_tokens||0}+${u.completion_tokens||0}` : '';
    return `
    <tr>
      <td class="mono">${esc(r.file)}</td>
      <td class="${label === 'ERROR' ? 'status-fail' : ''}">${esc(label)}</td>
      <td class="muted">${esc(r.reason || '')}</td>
      <td>${r.elapsed != null ? r.elapsed + 's' : ''}</td>
      <td class="muted">${tok}</td>
      <td class="muted mono">${esc(r.timestamp || '')}</td>
    </tr>`;
  }).join('');
  return `
    <h2>Classify manifest &mdash; ${records.length} shown, newest first</h2>
    <div class="filters">${filterBtns}</div><div style="clear:both"></div>
    <div class="table-scroll"><table>
      <thead><tr><th>File</th><th>Label</th><th>Reason</th><th>Elapsed</th><th>Tokens</th><th>Timestamp</th></tr></thead>
      <tbody>${rows || '<tr><td colspan="6" class="muted">(nothing classified yet)</td></tr>'}</tbody>
    </table></div>`;
}

function wireManifestFilters() {
  document.querySelectorAll('.filter-btn').forEach(btn => {
    btn.onclick = () => {
      manifestFilter = btn.dataset.label;
      const scroller = document.querySelector('#manifest-panel .table-scroll');
      if (scroller) scroller.scrollTop = 0;
      refresh();
    };
  });
}

function renderFeed(stages) {
  const lines = [];
  for (const s of stages) {
    for (const line of (s.recent || [])) {
      lines.push(`<span class="tag ${s.key}">${s.name.toUpperCase()}</span>${esc(line)}`);
    }
  }
  const html = lines.length ? lines.map(l => `<div class="feed-line">${l}</div>`).join('')
                            : '<div class="feed-line muted">(nothing yet)</div>';
  return `<h2>Recent activity</h2>${html}`;
}

// Replace a panel's HTML only when it actually changed, and carry over the
// scroll position of any inner .table-scroll so polling doesn't jump the
// user back to the top of the seeds/manifest tables.
function setPanel(id, html) {
  const el = document.getElementById(id);
  if (el._html === html) return false;
  const scrolls = [...el.querySelectorAll('.table-scroll')].map(s => s.scrollTop);
  el.innerHTML = html;
  el._html = html;
  el.querySelectorAll('.table-scroll').forEach((s, i) => { if (scrolls[i] != null) s.scrollTop = scrolls[i]; });
  return true;
}

async function refresh() {
  try {
    const res = await fetch('/api/status');
    const data = await res.json();
    const stages = data.stages || [];
    ram = {free: data.free_ram_gb, min: data.crawl_min_free_gb};
    // Don't re-render the cards under someone typing into an option box.
    if (!document.getElementById('pipeline').contains(document.activeElement)
        || !['INPUT', 'SELECT'].includes(document.activeElement.tagName)) {
      setPanel('pipeline', renderPipeline(stages));
    }
    setPanel('industry-panel', renderSpread(stages.find(s => s.key === 'industry')));
    document.getElementById('headline').innerHTML = renderHeadline(stages);
    if (document.getElementById('more-detail').open) {
      setPanel('models-panel', renderModels(stages));
      setPanel('seeds-panel', renderSeeds(data.crawl_state || []));
      if (setPanel('manifest-panel', renderManifest(data.records || []))) wireManifestFilters();
      setPanel('feed-panel', renderFeed(stages));
    }
    document.getElementById('updated').textContent = 'Updated ' + new Date().toLocaleTimeString();
  } catch (e) {
    document.getElementById('updated').textContent = 'Refresh error: ' + e;
  }
}

// Delegated, so the handlers survive the cards being re-rendered every poll.
const pipelineEl = document.getElementById('pipeline');
pipelineEl.addEventListener('click', e => {
  const btn = e.target.closest('button[data-action]');
  if (btn && !btn.disabled) { btn.disabled = true; act(btn.dataset.action, btn.dataset.stage); }
});
const rememberOpt = e => {
  const el = e.target;
  if (el.dataset && el.dataset.opt) {
    (optValues[el.dataset.stage] = optValues[el.dataset.stage] || {})[el.dataset.opt] = el.value;
  }
};
pipelineEl.addEventListener('input', rememberOpt);
pipelineEl.addEventListener('change', rememberOpt);
pipelineEl.addEventListener('focusout', () => setTimeout(refresh, 0));

wireTips();
document.getElementById('more-detail').addEventListener('toggle', refresh);
refresh();
setInterval(refresh, 5000);
</script>
</body>
</html>
"""


class Handler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        pass  # keep stdout quiet -- errors still surface via exceptions

    def _send(self, code, body: bytes, content_type: str):
        self.send_response(code)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def _host_ok(self) -> bool:
        """Only answer requests addressed to this machine by name. Stops DNS
        rebinding, where an outside page points its own hostname at 127.0.0.1
        to read the page (and so the token)."""
        host = (self.headers.get("Host") or "").rsplit(":", 1)[0].strip("[]").lower()
        return host in ("localhost", "127.0.0.1")

    def do_GET(self):
        if not self._host_ok():
            self._send(403, b"forbidden", "text/plain")
        elif self.path in ("/", "/index.html"):
            self._send(200, PAGE.replace("__TOKEN__", TOKEN).encode("utf-8"), "text/html; charset=utf-8")
        elif self.path == "/api/status":
            self._send(200, json.dumps(pipeline()).encode("utf-8"), "application/json")
        else:
            self._send(404, b"not found", "text/plain")

    def do_POST(self):
        if not self._host_ok() or not secrets.compare_digest(self.headers.get("X-Token") or "", TOKEN):
            self._send(403, b"forbidden", "text/plain")
            return
        try:
            length = min(int(self.headers.get("Content-Length") or 0), 10_000)
            body = json.loads(self.rfile.read(length) or b"{}")
            if not isinstance(body, dict):
                raise ValueError
        except ValueError:
            self._send(400, b"bad request", "text/plain")
            return
        stage = str(body.get("stage") or "")
        if self.path == "/api/launch":
            options = body.get("options") if isinstance(body.get("options"), dict) else {}
            ok, message = launch(stage, options)
        elif self.path == "/api/stop":
            ok, message = stop(stage)
        else:
            self._send(404, b"not found", "text/plain")
            return
        self._send(200 if ok else 409, json.dumps({"ok": ok, "message": message}).encode("utf-8"),
                   "application/json")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=8765)
    args = parser.parse_args()
    server = ThreadingHTTPServer(("127.0.0.1", args.port), Handler)
    print(f"Dashboard at http://localhost:{args.port}  (Ctrl+C to stop)", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
