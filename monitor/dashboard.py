# -*- coding: utf-8 -*-
"""
The "monitor" role: a centralised, read-only web dashboard over every other
role in the pipeline --

    scrapper (../scrapper/crawl.py)
    classifier/extractor (../classifier_extractor/classify.py + extract.py)
    labeller (../labeller/label.py)

It never writes to any role's files -- only reads crawl_run.log,
docs/*.md, docs/manifest.jsonl, docs/extract_manifest.jsonl,
docs/providers.csv, docs/hirers.csv, docs/_crawl_state.json,
docs/_crawl.pid, docs/relevance_labels.jsonl, and docs/relevance_scores.csv -- so it's
safe to start, stop, or restart independently of every other script.

    python monitor/dashboard.py [--port 8765]

Then open http://localhost:8765 in a browser. Ctrl+C to stop the server.
"""

import argparse
import csv
import json
import os
import re
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT_DIR = SCRIPT_DIR.parent  # monitor/ sits one level below the project root
DOCS_DIR = ROOT_DIR / "docs"  # shared data lake every role reads/writes into
UNPROCESSED_DIR = DOCS_DIR / "unprocessed"
CRAWL_LOG = ROOT_DIR / "crawl_run.log"
MANIFEST_PATH = DOCS_DIR / "manifest.jsonl"
STATE_PATH = DOCS_DIR / "_crawl_state.json"
PID_PATH = DOCS_DIR / "_crawl.pid"  # written by crawl.py at start, removed on exit
EXTRACT_MANIFEST_PATH = DOCS_DIR / "extract_manifest.jsonl"
PROVIDERS_CSV = DOCS_DIR / "providers.csv"
HIRERS_CSV = DOCS_DIR / "hirers.csv"
LABELS_PATH = DOCS_DIR / "relevance_labels.jsonl"
SCORES_CSV = DOCS_DIR / "relevance_scores.csv"
MANIFEST_RECORD_LIMIT = 300  # how many manifest rows the dashboard shows at once

SEED_RE = re.compile(r"^=== \[(.*?)\] (\S+)", re.MULTILINE)
TOTAL_SEEDS_RE = re.compile(r"Loaded (\d+) total seed URLs")
SAVED_LINE_RE = re.compile(r"^  \[SAVED\] (\S+)", re.MULTILINE)


def _read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="ignore")
    except FileNotFoundError:
        return ""


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


def _crawl_alive() -> bool:
    """The only reliable "running" signal: is the PID crawl.py wrote at
    startup still alive? The log can go silent for a whole seed (up to 30
    min), and a crash or Ctrl+C never writes "Batch done.", so the log alone
    can't answer this. A hard kill leaves a stale PID file behind, which
    the liveness check handles."""
    try:
        pid = int(PID_PATH.read_text(encoding="utf-8").strip())
    except (OSError, ValueError):
        return False
    return _pid_alive(pid)


def crawl_status() -> dict:
    content = _read_text(CRAWL_LOG)
    if _crawl_alive():
        state = "running"
    elif content.rfind("Batch done.") > content.rfind("total seed URLs"):
        state = "done"  # the latest run in the log reached its end
    elif content:
        state = "stopped"  # crashed, killed, or Ctrl+C'd mid-run
    else:
        state = "idle"
    total_m = TOTAL_SEEDS_RE.search(content)
    seed_matches = list(SEED_RE.finditer(content))

    current_label, current_url = (seed_matches[-1].groups() if seed_matches else (None, None))
    saved_lines = SAVED_LINE_RE.findall(content)

    return {
        "total_seeds": int(total_m.group(1)) if total_m else None,
        "seeds_started": len(seed_matches),
        "current_seed": f"{current_label} -- {current_url}" if current_label else None,
        "saved": content.count("  [SAVED]"),
        "blocked": content.count("  [BLOCKED]"),
        "skipped": content.count("  [SKIP]"),
        "failed": content.count("  [FAIL]"),
        "state": state,
        "recent": saved_lines[-6:],
    }


def crawl_state() -> list:
    """Raw per-seed results from docs/_crawl_state.json: crawl.py's own
    structured record of every seed it has finished (or given up on),
    independent of what's still in the text log. Each entry is
    [label, url, status, note, saved_count]."""
    if not STATE_PATH.exists():
        return []
    try:
        return json.loads(STATE_PATH.read_text(encoding="utf-8", errors="ignore"))
    except (json.JSONDecodeError, OSError):
        return []


def classify_status(record_limit: int = MANIFEST_RECORD_LIMIT) -> dict:
    label_counts = {}
    model_counts = {}
    error_count = 0
    prompt_tokens = 0
    completion_tokens = 0
    recent = []
    all_records = []

    if MANIFEST_PATH.exists():
        with MANIFEST_PATH.open("r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError:
                    continue
                all_records.append(record)
                model = record.get("model") or "legacy (pre-multi-LLM)"
                model_counts[model] = model_counts.get(model, 0) + 1
                if record.get("status") == "error":
                    error_count += 1
                    recent.append(f"{record['file']} -> ERROR")
                else:
                    label = record.get("label", "?")
                    label_counts[label] = label_counts.get(label, 0) + 1
                    recent.append(f"{record['file']} -> {label}")
                    usage = record.get("usage") or {}
                    prompt_tokens += usage.get("prompt_tokens") or 0
                    completion_tokens += usage.get("completion_tokens") or 0

    pending_now = len(list(UNPROCESSED_DIR.glob("*.md"))) if UNPROCESSED_DIR.exists() else 0
    classified = sum(label_counts.values())
    # "ever crawled" = still-pending + already sorted into a bucket (each
    # file lives in exactly one place at a time now that classify.py moves
    # rather than copies, so this doesn't double-count).
    total_pages = pending_now + classified

    return {
        "total_pages": total_pages,
        "classified": classified,
        "pending": pending_now,
        "errors": error_count,
        "labels": label_counts,
        "models": model_counts,
        "recent": recent[-6:],
        "prompt_tokens": prompt_tokens,
        "completion_tokens": completion_tokens,
        # newest first, capped so a huge manifest doesn't balloon every response
        "records": list(reversed(all_records[-record_limit:])),
    }


def _csv_row_count(path: Path) -> int:
    if not path.exists():
        return 0
    with path.open("r", encoding="utf-8", newline="") as f:
        return max(0, sum(1 for _ in csv.reader(f)) - 1)  # minus header row


def extract_status() -> dict:
    written = rejected = errors = 0
    model_counts = {}
    recent = []

    if EXTRACT_MANIFEST_PATH.exists():
        with EXTRACT_MANIFEST_PATH.open("r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError:
                    continue
                model = record.get("model") or "legacy (pre-multi-LLM)"
                model_counts[model] = model_counts.get(model, 0) + 1
                status = record.get("status")
                if status == "written":
                    written += 1
                    label = record.get("title") or record.get("entity_type", "?")
                    recent.append(f"{record['file']} -> WRITTEN ({label})")
                elif status == "rejected":
                    rejected += 1
                    recent.append(f"{record['file']} -> REJECTED ({record.get('reason', '')})")
                elif status == "error":
                    errors += 1
                    recent.append(f"{record['file']} -> ERROR")

    return {
        "written": written,
        "rejected": rejected,
        "errors": errors,
        "models": model_counts,
        "providers_rows": _csv_row_count(PROVIDERS_CSV),
        "hirers_rows": _csv_row_count(HIRERS_CSV),
        "recent": recent[-6:],
    }

def labeller_status() -> dict:
    calls = {}
    errors = 0
    pairs = set()
    if LABELS_PATH.exists():
        with LABELS_PATH.open("r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if record.get("status") != "ok":
                    errors += 1
                    continue
                calls[record["approach"]] = calls.get(record["approach"], 0) + 1
                pairs.add((record["hirer"], record["provider"]))
    return {
        "pairs": len(pairs),
        "calls": calls,
        "errors": errors,
        "scores_rows": _csv_row_count(SCORES_CSV),
    }


PAGE = """<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Scrapper Agent Dashboard</title>
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
  h1 { font-size: 18px; margin: 0 0 20px; color: var(--text); }
  h1 .dot { display: inline-block; width: 8px; height: 8px; border-radius: 50%; margin-right: 8px; background: var(--green); }
  .grid { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 16px; margin-bottom: 16px; }
  @media (max-width: 1100px) { .grid { grid-template-columns: 1fr 1fr; } }
  @media (max-width: 700px) { .grid { grid-template-columns: 1fr; } }
  .panel {
    background: var(--panel); border: 1px solid var(--border); border-radius: 10px;
    padding: 16px 18px;
  }
  .panel h2 {
    font-size: 12px; text-transform: uppercase; letter-spacing: .06em;
    color: var(--muted); margin: 0 0 14px; font-weight: 600;
  }
  .row { display: flex; justify-content: space-between; align-items: baseline; margin: 8px 0; gap: 12px; }
  .row .k { color: var(--muted); font-size: 12.5px; white-space: nowrap; }
  .row .v { font-weight: 600; text-align: right; overflow-wrap: anywhere; }
  .badge { display: inline-block; padding: 2px 10px; border-radius: 999px; font-size: 11px; font-weight: 700; letter-spacing: .04em; }
  .badge.running { background: rgba(232,179,57,.15); color: var(--yellow); }
  .badge.done { background: rgba(62,207,142,.15); color: var(--green); }
  .badge.stopped { background: rgba(239,93,93,.15); color: var(--red); }
  .bar-track { background: #23262f; border-radius: 6px; height: 8px; overflow: hidden; margin-top: 6px; }
  .bar-fill { height: 100%; background: var(--accent); transition: width .4s ease; }
  .labels { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 10px; }
  .chip { font-size: 11.5px; padding: 4px 10px; border-radius: 8px; background: #1f232c; border: 1px solid var(--border); }
  .chip b { color: var(--text); }
  .chip.provider { border-color: rgba(91,157,255,.4); }
  .chip.hirer { border-color: rgba(62,207,142,.4); }
  .chip.model { border-color: rgba(199,146,234,.4); }
  .chip.ignore { border-color: rgba(139,147,161,.3); }
  .chip.uncertain { border-color: rgba(232,179,57,.4); }
  .feed {
    background: var(--panel); border: 1px solid var(--border); border-radius: 10px;
    padding: 14px 18px; max-height: 320px; overflow-y: auto;
  }
  .feed h2 { font-size: 12px; text-transform: uppercase; letter-spacing: .06em; color: var(--muted); margin: 0 0 10px; }
  .feed-line { font-size: 12.5px; padding: 3px 0; font-family: ui-monospace, SFMono-Regular, Consolas, monospace; white-space: pre-wrap; overflow-wrap: anywhere; }
  .tag { display: inline-block; width: 66px; font-weight: 700; font-size: 11px; }
  .tag.crawl { color: var(--cyan); }
  .tag.classify { color: var(--magenta); }
  .tag.extract { color: var(--green); }
  .muted { color: var(--muted); }
  .placeholder { color: var(--muted); font-style: italic; padding: 6px 0; }
  .badge.future { background: rgba(139,147,161,.15); color: var(--muted); }
  .updated { color: var(--muted); font-size: 11.5px; margin-top: 18px; text-align: right; }
  .wide-panel {
    background: var(--panel); border: 1px solid var(--border); border-radius: 10px;
    padding: 14px 18px; margin-bottom: 16px;
  }
  .wide-panel h2 { font-size: 12px; text-transform: uppercase; letter-spacing: .06em; color: var(--muted); margin: 0 0 12px; display: inline-block; }
  .table-scroll { max-height: 360px; overflow-y: auto; border-radius: 6px; }
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
  .filters { float: right; display: flex; gap: 6px; }
  .filter-btn {
    background: #1f232c; border: 1px solid var(--border); color: var(--muted); font-size: 11px;
    padding: 3px 10px; border-radius: 6px; cursor: pointer;
  }
  .filter-btn.active { background: var(--accent); color: #0f1115; border-color: var(--accent); font-weight: 700; }
  .tokens { color: var(--muted); font-size: 11.5px; font-weight: 400; margin-left: 10px; }
</style>
</head>
<body>
  <h1><span class="dot" id="statusdot"></span>Scrapper Agent Dashboard</h1>
  <div class="grid">
    <div class="panel" id="crawl-panel"></div>
    <div class="panel" id="classify-panel"></div>
    <div class="panel" id="extract-panel"></div>
  </div>
  <div class="wide-panel" id="seeds-panel"></div>
  <div class="wide-panel" id="manifest-panel"></div>
  <div class="wide-panel" id="labeller-panel"></div>
  <div class="feed" id="feed-panel"></div>
  <div class="updated" id="updated"></div>

<script>
function esc(s) {
  return String(s).replace(/[&<>]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]));
}

const CRAWL_BADGES = {
  running: '<span class="badge running">RUNNING</span>',
  done: '<span class="badge done">DONE</span>',
  stopped: '<span class="badge stopped">STOPPED</span>',
  idle: '<span class="badge future">NOT RUNNING</span>',
};
const CRAWL_DOT = { running: '#e8b339', done: '#3ecf8e', stopped: '#ef5d5d', idle: '#8b93a1' };

function renderCrawl(c) {
  const seeds = c.total_seeds != null ? `${c.seeds_started} / ${c.total_seeds}` : `${c.seeds_started}`;
  const pct = c.total_seeds ? Math.min(100, 100 * c.seeds_started / c.total_seeds) : 0;
  const badge = CRAWL_BADGES[c.state] || CRAWL_BADGES.idle;
  return `
    <h2>Crawl &mdash; crawl.py</h2>
    <div class="row"><span class="k">Status</span><span class="v">${badge}</span></div>
    <div class="row"><span class="k">Seeds</span><span class="v">${seeds}</span></div>
    <div class="bar-track"><div class="bar-fill" style="width:${pct}%"></div></div>
    <div class="row"><span class="k">${c.state === 'running' ? 'Current seed' : 'Last seed'}</span><span class="v">${esc(c.current_seed || '(not started)')}</span></div>
    <div class="row"><span class="k">Pages saved</span><span class="v">${c.saved}</span></div>
    <div class="row"><span class="k">Blocked / Skipped / Failed</span><span class="v">${c.blocked} / ${c.skipped} / ${c.failed}</span></div>
  `;
}

function renderModelChips(models) {
  const entries = Object.entries(models || {}).sort((a, b) => b[1] - a[1]);
  if (!entries.length) return '';
  const chips = entries.map(([m, n]) => `<span class="chip model">${esc(m)} <b>${n}</b></span>`).join('');
  return `<div class="labels">${chips}</div>`;
}

function renderClassify(cl) {
  const pct = cl.total_pages ? Math.min(100, 100 * cl.classified / cl.total_pages) : 0;
  const l = cl.labels || {};
  const tokens = (cl.prompt_tokens || cl.completion_tokens)
    ? `<span class="tokens">${(cl.prompt_tokens||0).toLocaleString()} prompt + ${(cl.completion_tokens||0).toLocaleString()} completion tokens</span>`
    : '';
  return `
    <h2>Classify &mdash; classify.py --watch</h2>${tokens}
    <div class="row"><span class="k">Classified / Total</span><span class="v">${cl.classified} / ${cl.total_pages}</span></div>
    <div class="bar-track"><div class="bar-fill" style="width:${pct}%"></div></div>
    <div class="row"><span class="k">Pending in unprocessed/</span><span class="v">${cl.pending}</span></div>
    <div class="row"><span class="k">Errors</span><span class="v">${cl.errors}</span></div>
    <div class="labels">
      <span class="chip provider">PROVIDER <b>${l.PROVIDER || 0}</b></span>
      <span class="chip hirer">HIRER <b>${l.HIRER || 0}</b></span>
      <span class="chip ignore">IGNORE <b>${l.IGNORE || 0}</b></span>
      <span class="chip uncertain">UNCERTAIN <b>${l.UNCERTAIN || 0}</b></span>
    </div>
    ${renderModelChips(cl.models)}
  `;
}

function renderExtract(ex) {
  return `
    <h2>Extract &mdash; classifier_extractor/extract.py --watch</h2>
    <div class="row"><span class="k">Written</span><span class="v">${ex.written}</span></div>
    <div class="row"><span class="k">Rejected / Errors</span><span class="v">${ex.rejected} / ${ex.errors}</span></div>
    <div class="row"><span class="k">providers.csv rows</span><span class="v">${ex.providers_rows}</span></div>
    <div class="row"><span class="k">hirers.csv rows</span><span class="v">${ex.hirers_rows}</span></div>
    ${renderModelChips(ex.models)}
  `;
}

function renderLabeller(lb) {
  const chips = Object.entries(lb.calls || {})
    .map(([a, n]) => `<span class="chip model">${esc(a)} <b>${n}</b></span>`).join('');
  return `
    <h2>Labeller &mdash; labeller/label.py</h2>
    <div class="row"><span class="k">Pairs scored</span><span class="v">${lb.pairs}</span></div>
    <div class="row"><span class="k">relevance_scores.csv rows</span><span class="v">${lb.scores_rows}</span></div>
    <div class="row"><span class="k">Failed calls</span><span class="v">${lb.errors}</span></div>
    ${chips ? `<div class="labels">${chips}</div>` : '<div class="placeholder">No relevance labels yet.</div>'}
  `;
}

const STATUS_CLASS = s => s.startsWith('OK') ? 'status-ok' : s.startsWith('FAILED') ? 'status-fail' : 'status-skip';

function renderSeeds(state) {
  const rows = state.map(([label, url, status, note, saved]) => `
    <tr>
      <td>${esc(label)}</td>
      <td class="mono">${esc(url)}</td>
      <td class="${STATUS_CLASS(status)}">${esc(status)}</td>
      <td>${saved}</td>
      <td class="muted">${esc(note || '')}</td>
    </tr>`).join('');
  return `
    <h2>Seeds &mdash; docs/_crawl_state.json (${state.length} recorded)</h2>
    <div class="table-scroll"><table>
      <thead><tr><th>Label</th><th>Seed URL</th><th>Status</th><th>Saved</th><th>Note</th></tr></thead>
      <tbody>${rows || '<tr><td colspan="5" class="muted">(no seeds recorded yet)</td></tr>'}</tbody>
    </table></div>
  `;
}

let manifestFilter = 'ALL';

function renderManifest(records) {
  const labels = ['ALL', 'PROVIDER', 'HIRER', 'IGNORE', 'UNCERTAIN', 'ERROR'];
  const filterBtns = labels.map(l =>
    `<span class="filter-btn ${manifestFilter === l ? 'active' : ''}" data-label="${l}">${l}</span>`
  ).join('');

  const filtered = records.filter(r => {
    if (manifestFilter === 'ALL') return true;
    if (manifestFilter === 'ERROR') return r.status === 'error';
    return r.label === manifestFilter;
  });

  const rows = filtered.slice(0, 150).map(r => {
    const label = r.status === 'error' ? 'ERROR' : (r.label || '?');
    const usage = r.usage || {};
    const tok = (usage.prompt_tokens || usage.completion_tokens)
      ? `${usage.prompt_tokens||0}+${usage.completion_tokens||0}` : '';
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
    <h2>Manifest &mdash; docs/manifest.jsonl (${records.length} shown, newest first)</h2>
    <div class="filters">${filterBtns}</div>
    <div style="clear:both"></div>
    <div class="table-scroll"><table>
      <thead><tr><th>File</th><th>Label</th><th>Reason</th><th>Elapsed</th><th>Tokens</th><th>Timestamp</th></tr></thead>
      <tbody>${rows || '<tr><td colspan="6" class="muted">(nothing classified yet)</td></tr>'}</tbody>
    </table></div>
  `;
}

function wireManifestFilters() {
  document.querySelectorAll('.filter-btn').forEach(btn => {
    btn.onclick = () => {
      manifestFilter = btn.dataset.label;
      // a new filter is a different list, so start it from the top
      const scroller = document.querySelector('#manifest-panel .table-scroll');
      if (scroller) scroller.scrollTop = 0;
      refresh();
    };
  });
}

function renderFeed(c, cl, ex) {
  const lines = [];
  for (const line of c.recent) lines.push(`<span class="tag crawl">CRAWL</span>${esc(line)}`);
  for (const line of cl.recent) lines.push(`<span class="tag classify">CLASSIFY</span>${esc(line)}`);
  for (const line of ex.recent) lines.push(`<span class="tag extract">EXTRACT</span>${esc(line)}`);
  const html = lines.length
    ? lines.map(l => `<div class="feed-line">${l}</div>`).join('')
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
    setPanel('crawl-panel', renderCrawl(data.crawl));
    setPanel('classify-panel', renderClassify(data.classify));
    setPanel('extract-panel', renderExtract(data.extract));
    setPanel('seeds-panel', renderSeeds(data.crawl_state || []));
    if (setPanel('manifest-panel', renderManifest(data.classify.records || []))) wireManifestFilters();
    setPanel('labeller-panel', renderLabeller(data.labeller));
    setPanel('feed-panel', renderFeed(data.crawl, data.classify, data.extract));
    document.getElementById('statusdot').style.background = CRAWL_DOT[data.crawl.state] || CRAWL_DOT.idle;
    document.getElementById('updated').textContent = 'Updated ' + new Date().toLocaleTimeString();
  } catch (e) {
    document.getElementById('updated').textContent = 'Refresh error: ' + e;
  }
}

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

    def do_GET(self):
        if self.path in ("/", "/index.html"):
            self._send(200, PAGE.encode("utf-8"), "text/html; charset=utf-8")
        elif self.path == "/api/status":
            data = {
                "crawl": crawl_status(),
                "classify": classify_status(),
                "extract": extract_status(),
                "crawl_state": crawl_state(),
                "labeller": labeller_status(),
            }
            self._send(200, json.dumps(data).encode("utf-8"), "application/json")
        else:
            self._send(404, b"not found", "text/plain")


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
