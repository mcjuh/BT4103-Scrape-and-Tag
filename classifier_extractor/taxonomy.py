# -*- coding: utf-8 -*-
"""
Singapore's SkillsFuture framework as the tag vocabulary for extract.py's tagging
step. Every gig and every provider profile gets:

    category        a SkillsFuture SECTOR            (data/reference/skillsfuture/sector.csv)
    specialisation  a TRACK inside that sector       (track.csv)
    skills          TSCs (technical skills and competencies) linked to the chosen
                    tracks                           (tsc.csv via job_role.csv + job_role_tsc.csv)

and the three nest: category -> specialisation -> skills, as the platform's
Category / Specialisation search tags do ("Tax (Accountancy)").

This module is only the vocabulary and the checking: it loads the CSVs, builds the
lists the prompts show, and turns a model's reply into valid, nested tags. It makes
no LLM calls (extract.py does, with the prompts in prompts/tag_*.md), so it can be
tested on its own.

Design choices, from the ranker repo's taxonomy-tower experiments:
- Skills are picked ONLY from the chosen tracks' own list, never from all 2,088 TSCs.
  That list is 3-112 titles per track, small enough to show in full. (The first
  taxonomy tower hopped provider -> job role -> every skill of that role, and 44% of
  strong matches then shared no skill; here the model reads the record and picks.)
- Tags are capped (MAX_*), and an empty result is allowed. In that experiment a
  provider tagged with 80 skills overlapped almost every gig, and wrong rare tags got
  the biggest weights, so a short accurate list beats a long one and a wrong tag is
  worse than none.
- Composite tracks ("A / B / C", 28 of the 247) are left out: each is an aggregate
  of tracks that are listed on their own, so picking one says nothing extra.
- Track names such as "Operations" and "Management" repeat across sectors, so a track
  is always handled as a (sector, track) pair, and a pair that isn't in the framework
  is rejected.

Bump TAXONOMY_VERSION when this logic or the framework files change what a tag means.
"""

import csv
import difflib
import json
import re
from functools import lru_cache
from pathlib import Path

SF_DIR = Path(__file__).resolve().parent.parent / "data" / "reference" / "skillsfuture"
TAXONOMY_VERSION = "sf_v1"
MAX_SECTORS, MAX_TRACKS, MAX_SKILLS = 2, 3, 8  # skills: 0 to MAX, see parse_skills
FUZZY_CUTOFF = 0.88  # a near-miss spelling is accepted; a different name is not
SEP = " | "

# Written to the CSVs by extract.py, one string each.
TAG_FIELDS = ("category", "specialisation", "skills", "tags_json", "tag_taxonomy_version")


def _read(name: str) -> list:
    with (SF_DIR / name).open(newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


@lru_cache(maxsize=1)
def load() -> dict:
    """{"tracks": {sector: [track, ...]}, "skills": {(sector, track): [tsc, ...]}},
    both in a stable (alphabetical) order, composite tracks left out."""
    sectors = {r["sector_id"]: r["name"].strip() for r in _read("sector.csv")}
    tsc_title = {r["tsc_id"]: r["title"].strip() for r in _read("tsc.csv")}
    track_of_role = {r["role_id"]: r["track_id"] for r in _read("job_role.csv")}
    skills_of_track = {}
    for r in _read("job_role_tsc.csv"):
        track_id, title = track_of_role.get(r["role_id"]), tsc_title.get(r["tsc_id"])
        if track_id and title:
            skills_of_track.setdefault(track_id, set()).add(title)

    tracks, skills = {}, {}
    for r in _read("track.csv"):
        name, sector = r["name"].strip(), sectors.get(r["sector_id"])
        if not sector or " / " in name or not skills_of_track.get(r["track_id"]):
            continue
        tracks.setdefault(sector, []).append(name)
        skills[(sector, name)] = sorted(skills_of_track[r["track_id"]], key=str.lower)
    return {"tracks": {s: sorted(t, key=str.lower) for s, t in sorted(tracks.items())}, "skills": skills}


def _key(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", str(s).lower().replace("&", " and ")).strip()


def _match(name, choices: list):
    """The listed choice `name` means, or None: same words ignoring case,
    punctuation and "&"/"and", else the single closest spelling."""
    if not isinstance(name, str):
        return None
    wanted = _key(name)
    by_key = {_key(c): c for c in choices}
    if wanted in by_key:
        return by_key[wanted]
    close = difflib.get_close_matches(wanted, list(by_key), n=1, cutoff=FUZZY_CUTOFF)
    return by_key[close[0]] if close else None


# ---------------------------------------------------------------------------
# What the prompts show
# ---------------------------------------------------------------------------

def sector_track_block() -> str:
    """One line per sector: "Sector: Track | Track | ..."."""
    return "\n".join(f"{sector}: {SEP.join(tracks)}" for sector, tracks in load()["tracks"].items())


def skills_block(pairs: list) -> str:
    """The skills linked to each chosen track, one block per track."""
    skills = load()["skills"]
    return "\n\n".join(f"{sector} > {track} ({len(skills[(sector, track)])} skills):\n"
                       f"{SEP.join(skills[(sector, track)])}" for sector, track in pairs)


# ---------------------------------------------------------------------------
# What a model's reply must be
# ---------------------------------------------------------------------------

def parse_specialisations(data: dict) -> list:
    """The reply to prompts/tag_specialisation.md -> [(sector, track), ...], best fit
    first, at most MAX_TRACKS tracks across at most MAX_SECTORS sectors. Empty is
    valid (nothing fit). Raises ValueError for a pair that isn't in the framework,
    so the caller retries it like any failure; extras beyond the caps are dropped,
    since the prompt puts the best fit first."""
    items = data.get("specialisations")
    if not isinstance(items, list):
        raise ValueError("'specialisations' must be a list (empty if nothing fits)")
    tracks = load()["tracks"]
    pairs, sectors = [], []
    for item in items:
        if isinstance(item, str) and ">" in item:  # "Sector > Track"
            sector_name, _, track_name = item.partition(">")
        elif isinstance(item, dict):
            sector_name, track_name = item.get("sector"), item.get("track")
        else:
            raise ValueError(f"specialisation must be {{sector, track}}, got {item!r}")
        sector = _match(sector_name.strip() if isinstance(sector_name, str) else sector_name, list(tracks))
        if sector is None:
            raise ValueError(f"unknown sector {sector_name!r}")
        track = _match(track_name.strip() if isinstance(track_name, str) else track_name, tracks[sector])
        if track is None:
            raise ValueError(f"track {track_name!r} is not listed under sector {sector!r}")
        if (sector, track) in pairs:
            continue
        if sector not in sectors and len(sectors) >= MAX_SECTORS:
            continue
        if len(pairs) >= MAX_TRACKS:
            continue
        pairs.append((sector, track))
        if sector not in sectors:
            sectors.append(sector)
    return pairs


def parse_skills(data: dict, pairs: list) -> tuple:
    """The reply to prompts/tag_skills.md -> ([skill title, ...], [dropped, ...]): up to
    MAX_SKILLS titles, each one listed under at least one of the chosen tracks. A title
    that isn't in those lists is dropped and reported rather than failing the record:
    small models name a plausible skill the framework doesn't have ("DevOps",
    "Value-Based Care"), and on a smoke test that was 3 of 5 errors and retrying the
    same prompt didn't change it. An empty result is valid too: the prompt lets the
    model leave out a skill the text doesn't clearly show, and a weak track's list
    otherwise gets padded with irrelevant skills (seen: "Clinical Support for Patient
    Service Associates" on a health-insurance strategist). Only a reply that isn't a
    list raises ValueError, so the caller retries it."""
    items = data.get("skills")
    if not isinstance(items, list):
        raise ValueError("'skills' must be a list of skill titles")
    pool = {}  # title -> first chosen track that lists it
    for pair in pairs:
        for title in load()["skills"][pair]:
            pool.setdefault(title, pair)
    chosen, dropped = [], []
    for item in items:
        if isinstance(item, dict):
            item = item.get("title") or item.get("skill")
        title = _match(item.strip() if isinstance(item, str) else item, list(pool))
        if title is None:
            dropped.append(str(item))
        elif title not in chosen:
            chosen.append(title)
    return chosen[:MAX_SKILLS], dropped


# ---------------------------------------------------------------------------
# Nesting and CSV columns
# ---------------------------------------------------------------------------

def nest(pairs: list, skills: list) -> dict:
    """The `tags` block of the v2 record schemas (ML_*_schema_v2.json): category ->
    specialisation -> skills. A skill listed under several chosen tracks sits under the
    first of them. `group` (the platform's Industry / Function / Subject / Others heading)
    is always None here: it is populated afterwards, outside the LLM, from the platform's
    own category list. No pairs gives an empty `categories` list, the valid "nothing fit"."""
    owner = {}
    for pair in pairs:
        for title in load()["skills"][pair]:
            owner.setdefault(title, pair)
    categories = []
    for sector, track in pairs:
        entry = {"name": track, "search_tag": f"{track} ({sector})",
                 "skills": [s for s in skills if owner.get(s) == (sector, track)]}
        for cat in categories:
            if cat["name"] == sector:
                cat["specialisations"].append(entry)
                break
        else:
            categories.append({"name": sector, "group": None, "specialisations": [entry]})
    return {"taxonomy_version": TAXONOMY_VERSION, "categories": categories}


def csv_columns(tags: dict = None) -> dict:
    """The TAG_FIELDS strings for a record's `tags` block (blank when nothing fit)."""
    categories = (tags or {}).get("categories") or []
    if not categories:
        return {k: "" for k in TAG_FIELDS}
    specs = [sp for cat in categories for sp in cat["specialisations"]]
    return {
        "category": SEP.join(cat["name"] for cat in categories),
        "specialisation": SEP.join(sp["search_tag"] for sp in specs),
        "skills": SEP.join(s for sp in specs for s in sp["skills"]),
        "tags_json": json.dumps(categories, ensure_ascii=False),
        "tag_taxonomy_version": tags.get("taxonomy_version", TAXONOMY_VERSION),
    }
