# -*- coding: utf-8 -*-
"""
Fetches an explicit list of URLs (no link-following) into docs/unprocessed/,
with the same Markdown pruning, link-farm stripping, block detection and file
naming as crawl.py.

    py -3 scrapper/fetch_urls.py scrapper/topup_urls_20260929.tsv

Input: one URL per line, optionally "label<TAB>url". Pages already saved in
any docs/ bucket are skipped.

Why this exists: crawl.py's best-first deep crawl can hang on some sites (it
saved a handful of pages and then went silent until the 30-minute seed
timeout on HKA, Secretariat, Brookes Bell, Diales, Chartis and Huron). Their
sitemaps list every bio page directly, so fetching that list is both faster
and bounded: exactly the pages chosen, no more.
"""

import asyncio
import importlib.util
import sys
from pathlib import Path

from crawl4ai import AsyncWebCrawler, BrowserConfig, CacheMode, CrawlerRunConfig
from crawl4ai.content_filter_strategy import PruningContentFilter
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator

_spec = importlib.util.spec_from_file_location("crawl", Path(__file__).with_name("crawl.py"))
crawl = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(crawl)

BATCH = 20  # URLs handed to crawl4ai at once; each batch is bounded by its own timeout
BATCH_TIMEOUT_S = 300


def read_list(path: Path) -> list:
    items = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        label, _, url = line.rpartition("\t")
        items.append((label or "fetch_urls", url))
    return items


def already_saved() -> set:
    return {f.name for d in ("unprocessed", "provider", "hirer", "uncertain", "ignore")
            for f in (crawl.DOCS_DIR / d).glob("*.md")}


def save(r, label: str) -> str:
    """Mirrors crawl.crawl_seed's per-page handling. Returns an outcome tag."""
    if not getattr(r, "success", False):
        return "failed"
    url = r.url
    md = getattr(r, "markdown", None)
    fit = (getattr(md, "fit_markdown", None) or "").strip() if md else ""
    raw = (getattr(md, "raw_markdown", None) or "").strip() if md else ""
    content = crawl.strip_link_farms(fit if len(fit) >= 50 else raw)
    if not content:
        return "empty"
    reason = crawl.block_reason(content)
    if reason:
        print(f"  [BLOCKED] {url}  ({reason})", flush=True)
        return "blocked"
    fname = crawl.safe_filename(crawl.domain_of(url), url)
    title = (r.metadata or {}).get("title", "") if getattr(r, "metadata", None) else ""
    header = f"<!-- Source: {url} | Title: {title} | Seed: {url} ({label}, fetch_urls) -->\n\n"
    (crawl.UNPROCESSED_DIR / fname).write_text(header + content, encoding="utf-8")
    print(f"  [SAVED] {fname}  <- {url}  ({len(content)} chars)", flush=True)
    return "saved"


async def main(path: Path):
    crawl.UNPROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    done = already_saved()
    items = [(lab, u) for lab, u in read_list(path)
             if crawl.safe_filename(crawl.domain_of(u), u) not in done]
    print(f"{len(items)} URL(s) to fetch", flush=True)
    config = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS, page_timeout=crawl.PAGE_TIMEOUT_MS, verbose=False,
        wait_until="domcontentloaded",
        markdown_generator=DefaultMarkdownGenerator(
            content_filter=PruningContentFilter(threshold=crawl.MD_PRUNE_THRESHOLD, threshold_type="fixed")),
    )
    labels = dict((u, lab) for lab, u in items)
    counts = {}
    async with AsyncWebCrawler(config=BrowserConfig(headless=True, verbose=False, text_mode=True)) as crawler:
        for i in range(0, len(items), BATCH):
            urls = [u for _, u in items[i:i + BATCH]]
            try:
                results = await asyncio.wait_for(crawler.arun_many(urls=urls, config=config), BATCH_TIMEOUT_S)
            except Exception as e:
                print(f"  [FAIL] batch {i // BATCH + 1}: {e}", flush=True)
                counts["batch_failed"] = counts.get("batch_failed", 0) + len(urls)
                continue
            for r in results:
                tag = save(r, labels.get(r.url, "fetch_urls"))
                counts[tag] = counts.get(tag, 0) + 1
            print(f"[{min(i + BATCH, len(items))}/{len(items)}] {counts}", flush=True)
    print(f"Done. {counts}", flush=True)


if __name__ == "__main__":
    asyncio.run(main(Path(sys.argv[1])))
