# -*- coding: utf-8 -*-
"""Design rows for the GLM trial (docs/GLM-TRIAL.md, step 1): code decides what each gig is, and the
route of each provider, before any model is called. Variety comes from here, not from examples."""

import json
import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "classifier_extractor"))
import taxonomy  # noqa: E402

# Hirer industry pool (opt-in, see design_gigs): the named industries of classifier_extractor/prompts/industry_taxonomy.json,
# without the two catch-alls. Rolled on its own random stream, so switching it on leaves every other column unchanged.
USE_INDUSTRY = False
INDUSTRIES = {i["name"]: i["gist"] for i in json.loads(
    (ROOT / "classifier_extractor" / "prompts" / "industry_taxonomy.json").read_text(encoding="utf-8"))["industries"]
    if i["name"] not in ("Cross-industry", "OTHER")}

LEVELS = ("mid", "senior", "expert")
MODES = ("execution", "advisory", "mixed")
YEARS = {"mid": (6, 9), "senior": (12, 18), "expert": (22, 30)}

# Pilot rows cover all three levels, all three modes and (row 4) a generic gig. After that the nine
# level x mode combinations repeat in a shuffled order.
COMBOS = [(l, m) for l in LEVELS for m in MODES]
PILOT_COMBOS = [("mid", "execution"), ("senior", "advisory"), ("expert", "mixed"),
                ("mid", "advisory"), ("senior", "execution")]
PILOT_GENERIC = {3}

GENERIC_TASKS = [
    "proofreading and copy-editing a long document", "translating a document between English and Chinese",
    "cleaning up and restructuring an Excel workbook", "redesigning a slide deck", "clearing an admin or inbox backlog",
    "writing a set of job descriptions", "mystery shopping across several outlets", "transcribing and summarising recordings",
    "building a simple Power BI or Excel dashboard", "writing a staff handbook section", "data entry and tidy-up of a customer list",
]

OPENINGS = [
    "the organisation: start with a plain line on what it does",
    "the need: start with a plain statement of what is wanted",
    "first person singular: \"I run ...\" or \"I need ...\"",
    "first person plural: \"Our ...\" or \"We ...\"",
    "a third-person description of the organisation, then the ask",
    "the kind of specialist wanted: \"Looking for ...\"",
]

LEVEL_HINT = {
    "mid": "well-defined, lower-stakes work with a clear method (mapping a process, setting up a standard tool, routine documents)",
    "senior": "the specialist owns the outcome, advises management, handles some ambiguity or regulation (a compliance gap review, a cost-reduction study)",
    "expert": "high stakes, a scarce specialism or a formal opinion (an expert-witness report, M&A due diligence, a safety case for a regulator)",
}
MODE_HINT = {
    "execution": "hands-on production: the deliverable is finished documents, a working build or completed files, and the verbs are drafted, built, prepared, implemented, ran",
    "advisory": "judgement for management: the deliverable is an assessment, a recommendation, a roadmap or an opinion, and the verbs are review, diagnose, advise, recommend",
    "mixed": "clearly both: the specialist must produce something and also advise on it",
}

# The two routes per grade, as in data/output/crafted_gigs/README.md.
ROUTES = {
    "3a": (3, "the same work on the same kind of problem, in a similar setting"),
    "3b": (3, "the same work, built up in a different industry"),
    "2a": (2, "same discipline, a neighbouring sub-focus"),
    "2b": (2, "the right skills, mostly applied to a different kind of problem"),
    "1a": (1, "an adjacent area or a transferable skill"),
    "1b": (1, "a generic skill (project management, data analysis, admin) with no sign of the gig's domain"),
    "0a": (0, "shares only the gig's industry or setting, and none of its work"),
    "0b": (0, "shares only a tool, regulator or keyword with the gig, in unrelated work (e.g. \"mezzanine\" financing for a mezzanine floor)"),
}


def _row(i, sector, track, level, mode, generic, rng):
    return {
        "gig": f"G{i + 1:02d}", "n": i + 1, "sector": sector, "track": track, "level": level, "mode": mode,
        "specificity": "generic" if generic else "specific",
        "generic_task": rng.choice(GENERIC_TASKS) if generic else "",
        "words": rng.randint(60, 105), "weeks": rng.choice(["1-2", "2-3", "3-4", "4-6", "6-8", "2", "4"]),
        "opening": rng.choice(OPENINGS), "notes": rng.random() < 0.25,
    }


def design_gigs(n: int = 5, seed: int = 20261012, industry: bool = None) -> list:
    """n gig design rows. The first 5 are the pilot's, fixed whatever n is (see PILOT_COMBOS), so a bigger run
    extends the pilot instead of replacing it. Beyond them the nine level x mode combinations repeat in a
    shuffled order, about one gig in five is generic, sectors go round in a shuffled order (each sector
    appears before any repeats) and a sector's tracks are used before one repeats.

    industry=True (default: USE_INDUSTRY) adds an "industry" column, the kind of business the hirer runs, drawn
    from INDUSTRIES in shuffled rounds (each appears before any repeats) independently of the sector, so a field
    meets many kinds of hirer. Off, the rows are exactly what earlier runs produced."""
    if industry is None:
        industry = USE_INDUSTRY
    rng = random.Random(seed)
    tracks = taxonomy.load()["tracks"]
    sectors = list(tracks)
    rng.shuffle(sectors)
    rows = []
    for i in range(min(n, len(PILOT_COMBOS))):
        level, mode = PILOT_COMBOS[i]
        sector = sectors[i % len(sectors)]
        rows.append(_row(i, sector, rng.choice(tracks[sector]), level, mode, i in PILOT_GENERIC, rng))
    if n > len(PILOT_COMBOS):
        rng = random.Random(f"{seed}:extend")
        used = {(r["sector"], r["track"]) for r in rows}
        combos = []
        while len(combos) < n:
            batch = COMBOS[:]
            rng.shuffle(batch)
            combos += batch
        for i in range(len(PILOT_COMBOS), n):
            level, mode = combos[i]
            sector = sectors[i % len(sectors)]
            fresh = [t for t in tracks[sector] if (sector, t) not in used] or tracks[sector]
            track = rng.choice(fresh)
            used.add((sector, track))
            rows.append(_row(i, sector, track, level, mode, rng.random() < 0.2, rng))
    if industry:
        irng, order = random.Random(f"{seed}:industry"), []
        while len(order) < n:
            batch = list(INDUSTRIES)
            irng.shuffle(batch)
            order += batch
        for row, name in zip(rows, order):
            row["industry"] = name
    return rows


def design_providers(gig_row: dict, seed: int = 20261012) -> list:
    """Eight provider design rows for one gig: two per grade, one per route, the letters shuffled so the
    file name does not give away the grade. Level, mode and the years come from the gig row."""
    rng = random.Random(f"{seed}:{gig_row['gig']}")
    routes = list(ROUTES)
    rng.shuffle(routes)
    letters = "abcdefgh"
    lo, hi = YEARS[gig_row["level"]]
    rows = []
    for letter, route in zip(letters, routes):
        grade, meaning = ROUTES[route]
        rows.append({
            "provider": f"glm-provider__{gig_row['n']:02d}_{letter}.md", "gig": gig_row["gig"],
            "target_grade": grade, "route": route, "route_meaning": meaning,
            "seniority": gig_row["level"], "years_experience": rng.randint(lo, hi), "mode_of_work": gig_row["mode"],
        })
    return rows
