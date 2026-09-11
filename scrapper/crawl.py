# -*- coding: utf-8 -*-
"""
Crawl the seed URLs listed in seeds.md using crawl4ai and save each page
visited under docs/ as pruned, dense Markdown (not raw HTML) -- a
PruningContentFilter strips nav/footer/cookie-banner/script boilerplate
before the HTML-to-Markdown conversion, so a ~150-600KB raw page typically
comes out as a few KB of on-topic text with links preserved. This keeps
docs/ token-cheap for classify.py and any other future agent reading these
files, without losing the content that actually matters. No LLM extraction
in the crawl loop -- that happens as a separate later step (classify.py)
over the downloaded Markdown.

seeds.md includes both individual/team-oriented sites (candidate gig
providers) and gig/case-study hubs (Consultport, Toptal, Catalant,
Business Talent Group, MBO Partners, GLG, Upwork) whose listing pages can
themselves represent a gig -- both kinds of pages are saved the same way.

Design notes / judgment calls:
- Best-first deep crawl per seed (not plain BFS): links are scored by
  keyword relevance (KeywordRelevanceScorer over LINK_KEYWORDS) so the
  crawler prioritizes following links that look like case-study/team/
  people/achievement pages instead of wandering into nav boilerplate.
  max_depth=MAX_DEPTH, max_pages=MAX_PAGES_PER_DOMAIN per domain, same-domain only.
- A FilterChain excludes obvious junk paths (login/signup, cookie/privacy/
  terms, sitemap, newsletter/subscribe, and binary assets) so crawl budget
  isn't wasted on them.
- One attempt per URL, generous but bounded timeout, wrapped in
  try/except so a single failing/blocking site does not kill the run.
- Many big consulting sites (McKinsey, BCG, Bain, Big 4) run bot
  protection / heavy JS / consent walls -- failures there are expected
  and are logged to the console and to docs/_crawl_report.md.
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
ROOT_DIR = SCRIPT_DIR.parent  # scrapper/ sits one level below the project root
WEBLINKS_PATH = SCRIPT_DIR / "seeds.md"  # scrapper's own input config, not shared with other roles
DOCS_DIR = ROOT_DIR / "docs"  # shared data lake -- every role reads/writes here, not its own folder
# Crawled-but-not-yet-classified pages land here, not loose in DOCS_DIR --
# classify.py drains this folder (moving each file into its bucket once
# classified) so DOCS_DIR's root stays just bookkeeping + bucket folders,
# and it's obvious at a glance what's still pending.
UNPROCESSED_DIR = DOCS_DIR / "unprocessed"
STATE_PATH = DOCS_DIR / "_crawl_state.json"
# Written once at startup with this process's PID and deleted on exit, so
# monitor/dashboard.py can tell "running" from "crashed/stopped" by checking
# whether that PID is still alive -- the log alone can't (a seed can sit
# silent for up to SEED_TIMEOUT_S, and a hard kill leaves no trace in it).
PID_PATH = DOCS_DIR / "_crawl.pid"

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
    # Industry/sector hub pages -- not people/case-study pages themselves,
    # but at MAX_DEPTH=5 they're valuable waypoints (e.g. an industries
    # landing page links out to per-industry pages, which in turn link to
    # that industry's case studies and experts) and are relevant gig_listing
    # / candidate_profile context in their own right.
    "industries", "industry", "sector", "sectors", "capabilities",
    "insights", "solutions", "services",
]

# Signals that a "successful" fetch actually landed on a bot-check/consent
# wall rather than real content. Checked against the saved Markdown
# (lowercased) of every page so blocked pages don't silently pollute docs/
# (and burn classify.py's LLM budget on junk).
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

# Junk paths to exclude entirely so crawl budget isn't wasted on them. At
# MAX_DEPTH=2 these barely mattered (the crawl never got deep enough to
# reach them); at MAX_DEPTH=5 / MAX_PAGES_PER_DOMAIN=200 the crawler will
# actually wander into pagination/tag/search/feed URLs, so it's worth
# excluding them before they eat budget that could go to real content.
EXCLUDE_PATTERNS = [
    "*/login*", "*/signin*", "*/sign-in*", "*/signup*", "*/sign-up*",
    "*/register*", "*cookie*", "*privacy*", "*terms-of*", "*sitemap*",
    "*newsletter*", "*subscribe*", "*/careers*", "*.pdf", "*.jpg",
    "*.jpeg", "*.png", "*.svg", "*.zip", "*.mp4",
    "*/tag/*", "*/tags/*", "*/page/*", "*?page=*", "*/search*",
    "*/rss*", "*/feed*", "*/wp-json/*", "*/print/*", "*/share*",
]


def read_seed_urls(path: Path):
    """Parse seeds.md, pulling out (label, url) for every markdown line
    containing a URL. Lines are expected as "Label: https://...", but a
    "Label: www.example.com" (no scheme) is also accepted -- https:// is
    assumed and a warning is printed, rather than silently dropping the
    seed (this is how the Upwork entry used to go missing)."""
    seeds = []
    url_re = re.compile(r"(https?://\S+)")
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
            seeds.append((label, url))
            continue
        # No http(s) URL found -- check for a "Label: bare-domain" line
        # (missing scheme) before giving up on it.
        if ":" in line:
            label, rest = line.split(":", 1)
            rest = rest.strip().rstrip(")\"'.,")
            if bare_domain_re.match(rest):
                url = f"https://{rest}"
                print(f"  [WARN] seeds.md line {lineno}: '{line}' has no scheme, assuming {url}", flush=True)
                seeds.append((label.strip(), url))
                continue
        # Section headers and other non-seed lines are expected to have no
        # URL at all -- only warn when the line looks like it was meant to
        # be a seed (contains a colon, i.e. "Label: something").
        if ":" in line:
            skipped.append((lineno, line))

    for lineno, line in skipped:
        print(f"  [WARN] seeds.md line {lineno}: could not parse a URL, seed skipped: '{line}'", flush=True)

    return seeds


def domain_of(url: str) -> str:
    """Normalize a URL to a domain key for dedup/file-naming purposes.
    Strips a leading www / www2 / www3 ... label so "www2.deloitte.com" and
    "www.deloitte.com" collapse to the same "deloitte.com" -- otherwise
    they're treated as unrelated domains, which broke seed-level dedup
    (seeds.md had both forms pointing at the same real site)."""
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


# A run of this many (or more) consecutive bare "[Text](url)" lines gets
# dropped as a link farm (nav/footer/country-language-picker) -- see
# strip_link_farms. A short list of a few featured links is legitimate
# content and stays well under this.
LINK_FARM_MIN_RUN = 10
_BARE_LINK_LINE_RE = re.compile(r"^(?:[-*]\s*)?\[[^\]]+\]\([^)]+\)\s*$")


def strip_link_farms(text: str) -> str:
    """Drop long runs of consecutive bare-markdown-link lines. This is the
    signature of a nav/footer/country-language-picker block (e.g. EY's
    country selector renders as 150+ lines of "[BotswanaEnglish](url)",
    one link per line, no surrounding prose). PruningContentFilter's
    general boilerplate heuristic catches this on some sites (it did for
    Bain's near-identical office list) but not others, so this backstop
    doesn't depend on the heuristic -- it just looks at the shape of the
    text. Without it, a big enough link farm at the top of a page can push
    classify.py's MAX_CHARS truncation past the real content entirely."""
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
    """Cheap heuristic check for a bot-check/consent wall instead of real
    content. Returns a short reason string if the page looks blocked, else
    None. Not perfect, but catches the common cases so junk doesn't eat
    classify.py's LLM budget. `text` is the already-pruned Markdown, so no
    HTML-tag stripping is needed here."""
    lowered = text.lower()
    for signal in BLOCK_SIGNALS:
        if signal in lowered:
            return f"block signal '{signal}'"
    word_count = len(text.split())
    if word_count < MIN_TEXT_WORDS:
        return f"too little text ({word_count} words)"
    return None


async def crawl_seed(crawler: AsyncWebCrawler, label: str, seed_url: str, report: list):
    domain = domain_of(seed_url)
    print(f"\n=== [{label}] {seed_url}  (domain={domain}) ===", flush=True)

    filter_chain = FilterChain([
        URLPatternFilter(patterns=EXCLUDE_PATTERNS, reverse=True),
    ])

    deep_strategy = BestFirstCrawlingStrategy(
        max_depth=MAX_DEPTH,
        include_external=False,
        max_pages=MAX_PAGES_PER_DOMAIN,
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

        # No LLM extraction here -- just the pruned Markdown conversion,
        # already computed by crawl4ai per run_config.markdown_generator.
        # Prefer the pruned fit_markdown; fall back to the unpruned
        # raw_markdown if pruning stripped everything (e.g. a page that's
        # almost entirely a single content block crawl4ai scored as
        # boilerplate), and skip the page entirely if neither exists.
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
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    STATE_PATH.write_text(json.dumps(report, indent=2), encoding="utf-8")


def dedupe_report(report):
    """Keep only the most recent result per (label, url). The state file
    accumulates across separate invocations (batches, reruns, smoke tests)
    against the same docs/ dir, so a seed processed twice would otherwise
    show up twice in the final report."""
    by_seed = {}
    for entry in report:
        by_seed[(entry[0], entry[1])] = entry
    return list(by_seed.values())


def write_report_md(report):
    report_path = DOCS_DIR / "_crawl_report.md"
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

    DOCS_DIR.mkdir(parents=True, exist_ok=True)
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

    # A domain can legitimately need more than one seed -- e.g. a firm's
    # /industries hub and its /people hub are often disconnected content
    # trees, so one seed alone misses the other. Dedup is therefore keyed
    # on the exact (label, url) seed, not the domain: skip a seed only if
    # this specific seed already ran successfully in a prior run, unless
    # --force is passed. Two different seeds sharing a domain both run.
    #
    # A seed that "completed" with saved_count == 0 does NOT count as done,
    # even though it's not an exception/timeout. crawl4ai's own memory
    # dispatcher can throttle a seed down to zero real fetches under memory
    # pressure without ever raising -- that's indistinguishable from a
    # genuine 0-result seed except it produced nothing useful, so it's
    # always worth retrying rather than being silently skipped forever.
    already_done = {(entry[0], entry[1]) for entry in report if entry[4] > 0}

    # Resolve skips up front (all synchronous, no concurrency concerns) so
    # the concurrent workers below only ever see seeds that should actually run.
    to_run = []
    seen_this_run = set()
    for label, url in batch:
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
        to_run.append((label, url))

    semaphore = asyncio.Semaphore(max(1, args.concurrency))

    async def run_one(crawler, label, url):
        async with semaphore:
            domain = domain_of(url)
            before = len(list(UNPROCESSED_DIR.glob(f"{domain}__*.md")))
            try:
                await asyncio.wait_for(crawl_seed(crawler, label, url, report), timeout=SEED_TIMEOUT_S)
            except asyncio.TimeoutError:
                after = len(list(UNPROCESSED_DIR.glob(f"{domain}__*.md")))
                saved_before_timeout = max(0, after - before)
                print(f"  [FAIL] TIMEOUT ({SEED_TIMEOUT_S}s) crawling {url} ({saved_before_timeout} saved before timeout)", flush=True)
                report.append((label, url, "FAILED (overall timeout)", "", saved_before_timeout))
            except Exception as e:
                print(f"  [FAIL] unexpected error on {url}: {e}", flush=True)
                traceback.print_exc()
                report.append((label, url, "FAILED (exception)", str(e)[:200], 0))
            # Both of these are synchronous (no awaits inside), so this is
            # safe against other concurrent workers interleaving mid-update
            # even without an explicit lock -- asyncio only switches tasks
            # at an await point.
            report[:] = dedupe_report(report)
            save_state(report)  # persist after every seed so progress survives

    async with AsyncWebCrawler(config=browser_config) as crawler:
        await asyncio.gather(*(run_one(crawler, label, url) for label, url in to_run))

    total_saved, report_path = write_report_md(report)
    print(f"\nBatch done. Cumulative report written to {report_path}")
    print(f"Cumulative seeds processed: {len(report)}  |  Cumulative files saved: {total_saved}")


if __name__ == "__main__":
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    PID_PATH.write_text(str(os.getpid()), encoding="utf-8")
    try:
        asyncio.run(main())
    finally:
        PID_PATH.unlink(missing_ok=True)
