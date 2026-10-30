# -*- coding: utf-8 -*-
"""
Crawls the seed URLs listed in seeds.md with crawl4ai and saves each page
under data/pages/unprocessed/ as pruned Markdown. A PruningContentFilter
strips navigation, footers and cookie banners before the HTML-to-Markdown
step, so pages are small enough for classify.py to read cheaply. There is
no LLM call in the crawl.

Per seed:
- Best-first deep crawl on the seed's own domain, up to MAX_DEPTH and
  MAX_PAGES_PER_DOMAIN. Links are scored by keyword (LINK_KEYWORDS) so the
  crawler follows case-study, team and people pages first.
- A filter chain skips login, privacy, sitemap, newsletter and binary files.
- One attempt per URL with a timeout, wrapped so one failing site cannot
  stop the run. Sites with bot protection (McKinsey, BCG, Bain, Big 4) are
  expected to fail; failures go to the console and
  data/manifests/crawl_report.md.

seeds.md mixes people and team sites (possible providers) with gig and
case-study hubs (Toptal, Upwork, Catalant, ...). Both are saved the same
way.
"""

import argparse
import asyncio
import json
import os
import re
import traceback
from pathlib import Path
from urllib.parse import urlparse

from crawl4ai import (
    AsyncWebCrawler,
    BrowserConfig,
    CrawlerRunConfig,
    CacheMode,
)
from crawl4ai.content_filter_strategy import PruningContentFilter
from crawl4ai.deep_crawling import BestFirstCrawlingStrategy, FilterChain, KeywordRelevanceScorer, URLPatternFilter
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT_DIR = SCRIPT_DIR.parent  # scraper/ sits one level below the project root
WEBLINKS_PATH = SCRIPT_DIR / "seeds.md"  # scraper's own input config, not shared with other roles
DATA_DIR = ROOT_DIR / "data"  # shared data lake; every role reads/writes here, not its own folder
PAGES_DIR = DATA_DIR / "pages"  # crawled pages, one folder per classify.py bucket
MANIFESTS_DIR = DATA_DIR / "manifests"
# Crawled pages land here; classify.py moves each into its bucket once classified, so what
# is left here is what is still pending.
UNPROCESSED_DIR = PAGES_DIR / "unprocessed"
STATE_PATH = MANIFESTS_DIR / "crawl_state.json"
# Written at startup with this process's PID and deleted on exit, so monitor/dashboard.py
# can tell "running" from "crashed" by checking whether the PID is alive. The log alone
# can't, since a seed can sit silent for up to SEED_TIMEOUT_S.
PID_PATH = ROOT_DIR / "logs" / "crawl.pid"

MAX_DEPTH = 5
MAX_PAGES_PER_DOMAIN = 1000
PAGE_TIMEOUT_MS = 20_000  # 20s per page
SEED_TIMEOUT_S = 1800  # hard cap per seed (deep crawl of up to MAX_PAGES_PER_DOMAIN pages)
MD_PRUNE_THRESHOLD = 0.48  # PruningContentFilter score cutoff; crawl4ai's own default

# Links whose URL/anchor text look like these are prioritized by the
# best-first crawl strategy.
LINK_KEYWORDS = [
    "case-study", "case-studies", "case study", "success-story",
    "success-stories", "client-story", "client-stories", "our-people",
    "our-team", "leadership", "team", "who-we-are", "meet-the-team",
    "meet-our", "people", "achievement", "award", "portfolio",
    "engagement", "project", "expert", "consultant", "profile",
    # Industry/sector hub pages: not people or case-study pages themselves, but
    # waypoints that link to them.
    "industries", "industry", "sector", "sectors", "capabilities",
    "insights", "solutions", "services",
]

# Signals that a "successful" fetch landed on a bot-check or consent wall. Checked against
# each page's saved Markdown (lowercased) so blocked pages don't end up in data/pages/.
BLOCK_SIGNALS = [
    "just a moment...",  # Cloudflare interstitial
    "cf-chl-", "cf_chl_", "checking your browser",
    "captcha", "recaptcha", "h-captcha",
    "please verify you are a human", "verify you are human",
    "access denied", "request unsuccessful",
    "enable javascript to continue", "please enable javascript",
    "pardon our interruption",
    "perimeterx", "px-captcha",
]
MIN_TEXT_WORDS = 80  # below this word count, a page is almost certainly a shell/error page

# Junk paths to exclude so the crawl budget is not spent on login, pagination,
# tag, search or feed URLs.
EXCLUDE_PATTERNS = [
    "*/login*", "*/signin*", "*/sign-in*", "*/signup*", "*/sign-up*",
    "*/register*", "*cookie*", "*privacy*", "*terms-of*", "*sitemap*",
    "*newsletter*", "*subscribe*", "*/careers*", "*.pdf", "*.jpg",
    "*.jpeg", "*.png", "*.svg", "*.zip", "*.mp4",
    "*/tag/*", "*/tags/*", "*/page/*", "*?page=*", "*/search*",
    "*/rss*", "*/feed*", "*/wp-json/*", "*/print/*", "*/share*",
]


def read_seed_urls(path: Path):
    """Parse seeds.md into (label, url) for every markdown line containing a URL. Lines are
    expected as "Label: https://...". A "Label: www.example.com" with no scheme is also
    accepted: https:// is assumed and a warning is printed."""
    seeds = []
    url_re = re.compile(r"(https?://\S+)")
    # Optional per-seed page cap, e.g. "HKA: https://www.hka.com/people/ (max 300 pages)",
    # so a seed crawls only as much as the corpus needs from it.
    cap_re = re.compile(r"\(max (\d+) pages?\)", re.IGNORECASE)
    bare_domain_re = re.compile(r"^([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})(/\S*)?$")
    skipped = []
    for lineno, raw_line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = raw_line.strip()
        if not line:
            continue
        m = url_re.search(line)
        if m:
            url = m.group(1).rstrip(")\"'.,")
            label = line.split(":", 1)[0].strip() if ":" in line else url
            cap = cap_re.search(line)
            seeds.append((label, url, int(cap.group(1)) if cap else None))
            continue
        # No http(s) URL found; check for a "Label: bare-domain" line
        # (missing scheme) before giving up on it.
        if ":" in line:
            label, rest = line.split(":", 1)
            rest = rest.strip().rstrip(")\"'.,")
            if bare_domain_re.match(rest):
                url = f"https://{rest}"
                print(f"  [WARN] seeds.md line {lineno}: '{line}' has no scheme, assuming {url}", flush=True)
                seeds.append((label.strip(), url, None))
                continue
        # Section headers have no URL; only warn when the line looks like a seed
        # (contains a colon, i.e. "Label: something").
        if ":" in line:
            skipped.append((lineno, line))

    for lineno, line in skipped:
        print(f"  [WARN] seeds.md line {lineno}: could not parse a URL, seed skipped: '{line}'", flush=True)

    return seeds


def domain_of(url: str) -> str:
    """Normalize a URL to a domain key for dedup and file naming. Strips a leading www, www2,
    www3 ... so "www2.deloitte.com" and "www.deloitte.com" both become "deloitte.com"."""
    netloc = urlparse(url).netloc.lower()
    return re.sub(r"^www\d*\.", "", netloc)


def slugify(url: str) -> str:
    parsed = urlparse(url)
    slug = (parsed.path.strip("/") or "home").replace("/", "_")
    slug = re.sub(r"[^a-zA-Z0-9_\-]", "-", slug)
    slug = re.sub(r"-{2,}", "-", slug).strip("-_")
    if not slug:
        slug = "home"
    return slug[:120]


def safe_filename(domain: str, url: str) -> str:
    return f"{domain}__{slugify(url)}.md"


# A run of this many consecutive bare "[Text](url)" lines is dropped as a link farm (see
# strip_link_farms). A short list of featured links stays well under this.
LINK_FARM_MIN_RUN = 10
_BARE_LINK_LINE_RE = re.compile(r"^(?:[-*]\s*)?\[[^\]]+\]\([^)]+\)\s*$")


def strip_link_farms(text: str) -> str:
    """Drop long runs of consecutive bare-markdown-link lines, the signature of a navigation,
    footer or country-picker block (EY's country selector is 150+ lines of
    "[BotswanaEnglish](url)"). The pruning filter catches some of these but not all, so this
    backstop looks at the shape of the text. Left in, a big link farm can push classify.py's
    MAX_CHARS truncation past the real content."""
    lines = text.split("\n")
    out = []
    run = []

    def flush():
        if len(run) < LINK_FARM_MIN_RUN:
            out.extend(run)
        run.clear()

    for line in lines:
        if _BARE_LINK_LINE_RE.match(line.strip()):
            run.append(line)
        else:
            flush()
            out.append(line)
    flush()
    return "\n".join(out)


def block_reason(text: str) -> str | None:
    """Cheap check for a bot-check or consent wall instead of real content. Returns a short
    reason if the page looks blocked, else None. `text` is the already-pruned Markdown."""
    lowered = text.lower()
    for signal in BLOCK_SIGNALS:
        if signal in lowered:
            return f"block signal '{signal}'"
    word_count = len(text.split())
    if word_count < MIN_TEXT_WORDS:
        return f"too little text ({word_count} words)"
    return None


async def crawl_seed(crawler: AsyncWebCrawler, label: str, seed_url: str, report: list, max_pages: int = None):
    domain = domain_of(seed_url)
    max_pages = max_pages or MAX_PAGES_PER_DOMAIN
    print(f"\n=== [{label}] {seed_url}  (domain={domain}, max {max_pages} pages) ===", flush=True)

    filter_chain = FilterChain([
        URLPatternFilter(patterns=EXCLUDE_PATTERNS, reverse=True),
    ])

    deep_strategy = BestFirstCrawlingStrategy(
        max_depth=MAX_DEPTH,
        include_external=False,
        max_pages=max_pages,
        filter_chain=filter_chain,
        url_scorer=KeywordRelevanceScorer(keywords=LINK_KEYWORDS, weight=1.0),
    )

    run_config = CrawlerRunConfig(
        deep_crawl_strategy=deep_strategy,
        cache_mode=CacheMode.BYPASS,
        page_timeout=PAGE_TIMEOUT_MS,
        verbose=False,
        stream=True,
        wait_until="domcontentloaded",
        markdown_generator=DefaultMarkdownGenerator(
            content_filter=PruningContentFilter(threshold=MD_PRUNE_THRESHOLD, threshold_type="fixed")
        ),
    )

    saved_count = 0
    blocked_count = 0
    pages_seen = 0
    try:
        results = await crawler.arun(url=seed_url, config=run_config)
    except Exception as e:
        print(f"  [FAIL] deep crawl error for {seed_url}: {e}", flush=True)
        report.append((label, seed_url, "FAILED (deep crawl exception)", str(e)[:200], 0))
        return

    # Streaming: pages are saved as they arrive, so even a mid-crawl
    # timeout/cancellation at the call site keeps whatever was saved so far.
    async for r in results:
        if not getattr(r, "success", False):
            continue
        pages_seen += 1
        page_url = getattr(r, "url", seed_url)
        title = ""
        try:
            title = (r.metadata or {}).get("title", "") if hasattr(r, "metadata") else ""
        except Exception:
            title = ""

        # Prefer the pruned fit_markdown. Fall back to raw_markdown if pruning stripped
        # everything, and skip the page if neither exists.
        md_result = getattr(r, "markdown", None)
        fit_md = (getattr(md_result, "fit_markdown", None) or "").strip() if md_result else ""
        raw_md = (getattr(md_result, "raw_markdown", None) or "").strip() if md_result else ""
        content = fit_md if len(fit_md) >= 50 else raw_md
        if not content:
            continue
        content = strip_link_farms(content)
        if not content:
            continue

        reason = block_reason(content)
        if reason:
            blocked_count += 1
            print(f"  [BLOCKED] {page_url}  ({reason})", flush=True)
            continue

        fname = safe_filename(domain, page_url)
        fpath = UNPROCESSED_DIR / fname
        header = f"<!-- Source: {page_url} | Title: {title} | Seed: {seed_url} ({label}) -->\n\n"
        try:
            fpath.write_text(header + content, encoding="utf-8")
            saved_count += 1
            print(f"  [SAVED] {fname}  <- {page_url}  ({len(content)} chars)", flush=True)
        except Exception as e:
            print(f"  [FAIL] could not write {fname}: {e}", flush=True)

    status = f"OK ({pages_seen} pages crawled, {saved_count} saved)"
    note = f"{blocked_count} blocked (bot-check/consent wall)" if blocked_count else ""
    print(f"  -> {status}" + (f"  [{note}]" if note else ""), flush=True)
    report.append((label, seed_url, status, note, saved_count))


def load_state():
    if STATE_PATH.exists():
        try:
            return json.loads(STATE_PATH.read_text(encoding="utf-8"))
        except Exception:
            return []
    return []


def save_state(report):
    MANIFESTS_DIR.mkdir(parents=True, exist_ok=True)
    STATE_PATH.write_text(json.dumps(report, indent=2), encoding="utf-8")


def dedupe_report(report):
    """Keep only the most recent result per (label, url), since the state file accumulates
    across runs and a seed processed twice would otherwise appear twice in the report."""
    by_seed = {}
    for entry in report:
        by_seed[(entry[0], entry[1])] = entry
    return list(by_seed.values())


def write_report_md(report):
    report_path = MANIFESTS_DIR / "crawl_report.md"
    lines = ["# Crawl Report\n"]
    total_saved = sum(r[4] for r in report)
    lines.append(f"Total seeds processed: {len(report)}  |  Total files saved: {total_saved}\n")
    lines.append("| Label | Seed URL | Status | Saved | Notes |")
    lines.append("|---|---|---|---|---|")
    for label, url, status, note, saved in report:
        lines.append(f"| {label} | {url} | {status} | {saved} | {note} |")
    report_path.write_text("\n".join(lines), encoding="utf-8")
    return total_saved, report_path


async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=int, default=0, help="start index (inclusive) into seed list")
    parser.add_argument("--end", type=int, default=None, help="end index (exclusive) into seed list")
    parser.add_argument(
        "--force", action="store_true",
        help="crawl a seed even if its domain already has saved pages from a prior run "
             "(default: skip it -- a single deep crawl now covers a domain broadly, so "
             "reruns are incremental by default rather than re-fetching everything)",
    )
    parser.add_argument(
        "--concurrency", type=int, default=1,
        help="how many seeds to crawl at once (default: 1, sequential). Each seed already "
             "fetches multiple pages concurrently internally (crawl4ai's own dispatcher), so "
             "raising this multiplies peak browser/memory load roughly linearly -- only raise "
             "it when there's real memory headroom (crawl4ai's own MemoryAdaptiveDispatcher "
             "will throttle/crash under pressure regardless of this setting).",
    )
    args = parser.parse_args()

    MANIFESTS_DIR.mkdir(parents=True, exist_ok=True)
    UNPROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    all_seeds = read_seed_urls(WEBLINKS_PATH)
    end = args.end if args.end is not None else len(all_seeds)
    batch = all_seeds[args.start:end]
    print(f"Loaded {len(all_seeds)} total seed URLs; processing batch [{args.start}:{end}] = {len(batch)} seeds", flush=True)

    browser_config = BrowserConfig(
        headless=True,
        verbose=False,
        text_mode=True,
    )

    report = dedupe_report(load_state())  # cumulative across batches

    # Dedup is keyed on the exact (label, url) seed, not the domain, because one site
    # can need several seeds (e.g. separate /industries and /people hubs). A seed is
    # skipped only if it already ran successfully, unless --force is passed. A seed
    # that saved 0 pages does not count as done, since crawl4ai can throttle to zero
    # fetches under memory pressure without raising an error.
    already_done = {(entry[0], entry[1]) for entry in report if entry[4] > 0}

    # Resolve skips up front (all synchronous, no concurrency concerns) so
    # the concurrent workers below only ever see seeds that should actually run.
    to_run = []
    seen_this_run = set()
    for label, url, max_pages in batch:
        if (label, url) in seen_this_run:
            print(f"  [SKIP] {label} ({url}) -- duplicate seed entry within this run", flush=True)
            continue
        seen_this_run.add((label, url))
        if (label, url) in already_done and not args.force:
            print(
                f"  [SKIP] {label} ({url}) -- already crawled in a prior run "
                f"(use --force to re-crawl anyway)",
                flush=True,
            )
            continue
        to_run.append((label, url, max_pages))

    semaphore = asyncio.Semaphore(max(1, args.concurrency))

    async def run_one(crawler, label, url, max_pages):
        async with semaphore:
            domain = domain_of(url)
            before = len(list(UNPROCESSED_DIR.glob(f"{domain}__*.md")))
            try:
                await asyncio.wait_for(crawl_seed(crawler, label, url, report, max_pages), timeout=SEED_TIMEOUT_S)
            except asyncio.TimeoutError:
                after = len(list(UNPROCESSED_DIR.glob(f"{domain}__*.md")))
                saved_before_timeout = max(0, after - before)
                print(f"  [FAIL] TIMEOUT ({SEED_TIMEOUT_S}s) crawling {url} ({saved_before_timeout} saved before timeout)", flush=True)
                report.append((label, url, "FAILED (overall timeout)", "", saved_before_timeout))
            except Exception as e:
                print(f"  [FAIL] unexpected error on {url}: {e}", flush=True)
                traceback.print_exc()
                report.append((label, url, "FAILED (exception)", str(e)[:200], 0))
            # No awaits below, so other workers cannot interleave mid-update.
            report[:] = dedupe_report(report)
            save_state(report)  # persist after every seed so progress survives

    async with AsyncWebCrawler(config=browser_config) as crawler:
        await asyncio.gather(*(run_one(crawler, label, url, max_pages) for label, url, max_pages in to_run))

    total_saved, report_path = write_report_md(report)
    print(f"\nBatch done. Cumulative report written to {report_path}")
    print(f"Cumulative seeds processed: {len(report)}  |  Cumulative files saved: {total_saved}")


if __name__ == "__main__":
    PID_PATH.parent.mkdir(exist_ok=True)
    PID_PATH.write_text(str(os.getpid()), encoding="utf-8")
    try:
        asyncio.run(main())
    finally:
        PID_PATH.unlink(missing_ok=True)
