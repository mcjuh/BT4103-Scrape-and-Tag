# -*- coding: utf-8 -*-
"""
Pick a fixed, good-quality sample of gigs and provider profiles for a full
cross-product labelling run (every sampled gig x every sampled provider).

    python labeller/sample.py [--n 100] [--seed 4103]
    python run.py label --hirers data/output/sample/hirers_sample.csv \
        --providers data/output/sample/providers_sample.csv --max-pairs 10000

"Good" means:
  gigs       the first-pass grounding review kept it (no repair needed), it is in
             the current prompt's format (ends in an Engagement duration: line), it has a
             real industry tag (not OTHER), no additional notes, a unique title,
             and a description of 300-1200 chars once the engagement line is gone.
  providers  classify.py called it PROVIDER (not UNCERTAIN), all five profile
             fields are filled, no leftover pronouns after anonymisation, a real
             industry tag, and an About section of at least 200 chars.

The sample is spread evenly: round-robin over industries, and within an
industry round-robin over source firms, so one firm (bcg.com, kroll.com) or one
industry (Financial Services) can't fill it. Gigs and providers are drawn over
the same industries so every gig has in-industry providers to rank.

The "Engagement duration: ..." sentence extract_hirer.md appends to every gig
description is stripped: it says how long the work runs, not what it needs,
and every gig has one, so it only adds noise to a relevance judgement.
"""

import argparse
import csv
import json
import random
import re
from collections import defaultdict
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_DIR = SCRIPT_DIR.parent / "data"
HIRERS_CSV = DATA_DIR / "output" / "hirers.csv"
PROVIDERS_CSV = DATA_DIR / "output" / "providers.csv"
MANIFEST = DATA_DIR / "manifests" / "extract.jsonl"
OUT_DIR = DATA_DIR / "output" / "sample"

PROFILE_FIELDS = ["about_title", "about_description", "services_offered_title",
                  "services_offered_description", "relevant_experience"]
ENGAGEMENT_RE = re.compile(r"\s*Engagement duration:[^\n]*$", re.IGNORECASE)

csv.field_size_limit(10**9)


def load_rows(path: Path) -> tuple:
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return reader.fieldnames, list(reader)


def latest_written(entity_type: str) -> dict:
    """source_file -> the manifest entry of the attempt that wrote its CSV row."""
    out = {}
    with MANIFEST.open(encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            r = json.loads(line)
            if r.get("entity_type") == entity_type and r.get("status") == "written":
                out[r["file"]] = r
    return out


def strip_engagement(desc: str) -> str:
    return ENGAGEMENT_RE.sub("", desc.strip()).strip()


def good_hirers(rows: list) -> list:
    manifest = latest_written("HIRER")
    seen_titles, keep = set(), []
    for r in rows:
        m = manifest.get(r["source_file"], {})
        desc = strip_engagement(r["hire_description"])
        notes = r["hire_description_additional_notes"].strip()
        title = r["hire_title"].strip().lower()
        if ((m.get("review") or {}).get("decision") != "keep" or m.get("repaired")
                or not ENGAGEMENT_RE.search(r["hire_description"].strip())
                or r["industry"] in ("", "OTHER")
                or notes not in ("", "null")
                or not 300 <= len(desc) <= 1200
                or title in seen_titles):
            continue
        seen_titles.add(title)
        keep.append({**r, "hire_description": desc, "hire_description_additional_notes": ""})
    return keep


def good_providers(rows: list) -> list:
    manifest = latest_written("PROVIDER")
    return [
        r for r in rows
        if r["classify_label"] == "PROVIDER"
        and all(r[k].strip() for k in PROFILE_FIELDS)
        and (manifest.get(r["source_file"], {}).get("metrics") or {}).get("leftover_pronouns", 0) == 0
        and r["industry"] not in ("", "OTHER")
        and len(r["about_description"]) >= 200
    ]


def firm(row: dict) -> str:
    return row["source_file"].split("__")[0]


def spread(rows: list, n: int, industries: list, rng: random.Random) -> list:
    """Round-robin over industries, and over firms within each industry."""
    queues = {}
    for ind in industries:
        by_firm = defaultdict(list)
        for r in rows:
            if r["industry"] == ind:
                by_firm[firm(r)].append(r)
        firms = sorted(by_firm)
        rng.shuffle(firms)
        for f in firms:
            rng.shuffle(by_firm[f])
        # interleave firms: one from each firm, then the next from each, ...
        order = []
        while any(by_firm[f] for f in firms):
            order += [by_firm[f].pop() for f in firms if by_firm[f]]
        queues[ind] = order

    picked = []
    while len(picked) < n and any(queues.values()):
        for ind in industries:
            if queues[ind] and len(picked) < n:
                picked.append(queues[ind].pop(0))
    return picked


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=100, help="gigs and providers each (default: 100)")
    parser.add_argument("--seed", type=int, default=4103)
    args = parser.parse_args()

    h_fields, hirers = load_rows(HIRERS_CSV)
    p_fields, providers = load_rows(PROVIDERS_CSV)
    hirers, providers = good_hirers(hirers), good_providers(providers)

    # industries both sides have, so no gig is sampled with no in-industry provider
    industries = sorted({r["industry"] for r in hirers} & {r["industry"] for r in providers})
    rng = random.Random(args.seed)
    h_pick = spread([r for r in hirers if r["industry"] in industries], args.n, industries, rng)
    p_pick = spread([r for r in providers if r["industry"] in industries], args.n, industries, rng)

    OUT_DIR.mkdir(exist_ok=True)
    for name, fields, picked in [("hirers_sample.csv", h_fields, h_pick),
                                 ("providers_sample.csv", p_fields, p_pick)]:
        with (OUT_DIR / name).open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=fields)
            w.writeheader()
            w.writerows(picked)

    print(f"eligible: {len(hirers)} gigs, {len(providers)} providers")
    print(f"sampled:  {len(h_pick)} gigs, {len(p_pick)} providers -> {len(h_pick) * len(p_pick)} pairs")
    print(f"\n{'industry':<30} gigs  providers")
    for ind in industries:
        print(f"{ind:<30} {sum(r['industry'] == ind for r in h_pick):>4}  "
              f"{sum(r['industry'] == ind for r in p_pick):>9}")
    print(f"\ngig firms:      {len({firm(r) for r in h_pick})}"
          f"\nprovider firms: {len({firm(r) for r in p_pick})}")
    print(f"written to {OUT_DIR}")


if __name__ == "__main__":
    main()
