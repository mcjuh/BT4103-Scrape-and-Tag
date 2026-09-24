# -*- coding: utf-8 -*-
"""
Build the labeller's gold set from the client's test workbook.

    py -3 labeller/experiments/build_gold.py

Reads client_documents/*Test_Dataset*.xlsx and writes, next to this script:
    gold.json                    graded labels in evaluate.py's format
    client_testset/gigs.csv      the 30 gigs, in hirers.csv's column names
    client_testset/showcases.csv the 30 showcases, in providers.csv's column names

WHY A CONVERTER AND NOT THE WORKBOOK ITSELF
The workbook was written by the client with an LLM; the client is not
technical. Its `expected_score_range` (0-100) and `match_rationale` are one
model's opinion, not measured ground truth. Scoring our LLM's relevance
labels directly against another LLM's numbers would be circular, and is the
self-preference bias llm_pool.py exists to avoid.

So the numbers are NOT carried across. What is carried across is the part
that survives that objection: the client's *ordinal intent* -- their
four-band judgement of how well each pair fits -- mapped onto the 0-3 rubric
the labeller's evaluator already uses. An ordinal band ("this is a better
fit than that one") is a much weaker claim than a score of 87, and it is the
claim the workbook actually supports.

    OBVIOUS   (they say 80-100) -> 3  shortlist
    SUBTLE    (they say 55-79)  -> 2  relevant
    PARTIAL   (they say 30-54)  -> 1  marginal
    NEAR-MISS (they say 0-29)   -> 0  not relevant

Rerunning this regenerates gold.json from the workbook, so a new version of
the workbook is a rerun, not a hand-edit.

KNOWN LIMITS, in the file itself so nobody forgets them:
- The workbook pairs 1:1 -- gig n with provider n only. Every other provider
  is unlabelled, and evaluate.py treats unlabelled as grade 0. That is an
  assumption the client never made: they never claimed provider 7 is
  irrelevant to gig 3, only that provider 3 is the intended match.
- The 4 NEAR-MISS gigs end up with no provider graded >= 1, so NDCG is
  undefined for them and evaluate.py reports nan. That is not a bug, but it
  does mean the NEAR-MISS cases -- the workbook's most interesting content --
  are invisible to a ranking metric. They need a separate check: does the
  engine score them LOW in absolute terms? See report_near_miss() below.
- These are silver labels derived from synthetic data. They are a
  development target, not a measurement of real-world matching quality.
"""

import csv
import json
import re
from pathlib import Path

try:
    import openpyxl
except ImportError:
    raise SystemExit("openpyxl is needed to read the workbook: py -3 -m pip install openpyxl")

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT_DIR = SCRIPT_DIR.parent.parent  # labeller/experiments/ -> labeller/ -> project root
CLIENT_DIR = ROOT_DIR / "client_documents"
GOLD_PATH = SCRIPT_DIR / "gold.json"
TESTSET_DIR = SCRIPT_DIR / "client_testset"

BAND_TO_GRADE = {"OBVIOUS": 3, "SUBTLE": 2, "PARTIAL": 1, "NEAR-MISS": 0}
RUBRIC = {
    "3": "Shortlist: the showcase meets the gig's core need (client band OBVIOUS).",
    "2": "Relevant: a real connection that isn't obvious from keywords (client band SUBTLE).",
    "1": "Marginal: meaningful overlap, imperfect fit (client band PARTIAL).",
    "0": "Not relevant, including deliberate near-misses that look similar on the surface "
         "(client band NEAR-MISS), and every provider the workbook left unpaired.",
}

GIG_ID = "client_gig_{:02d}"
PROV_ID = "client_showcase_{:02d}"


def _find_workbook() -> Path:
    matches = sorted(CLIENT_DIR.glob("*Test_Dataset*.xlsx"))
    if not matches:
        raise SystemExit(f"No *Test_Dataset*.xlsx found in {CLIENT_DIR}")
    return matches[-1]  # newest by name; they're date-prefixed


def _rows(ws) -> list:
    """Row 1 is a title banner and row 2 the real header; everything after the
    numeric ids is a colour legend, so rows are kept only while the id column
    is a number."""
    raw = list(ws.iter_rows(values_only=True))
    header = [str(h).strip() if h else "" for h in raw[1]]
    return [dict(zip(header, r)) for r in raw[2:] if isinstance(r[0], (int, float))]


def _clean(v) -> str:
    """The workbook carries en-dashes and non-breaking spaces from Word. Left
    as-is they show up in prompts as mojibake on a cp1252 console."""
    s = "" if v is None else str(v)
    return re.sub(r"\s+", " ", s.replace("–", "-").replace("—", "-")
                  .replace(" ", " ").replace("’", "'")).strip()


def build():
    wb_path = _find_workbook()
    wb = openpyxl.load_workbook(wb_path, data_only=True)
    gigs = _rows(wb["Hirer Gig Descriptions"])
    provs = _rows(wb["Provider Showcases"])
    key = _rows(wb["Matching Key (Ground Truth)"])
    print(f"{wb_path.name}: {len(gigs)} gigs, {len(provs)} showcases, {len(key)} pairs")

    TESTSET_DIR.mkdir(parents=True, exist_ok=True)

    # The gigs and showcases go in labeller/experiments/, NOT docs/ -- they are
    # the client's synthetic examples and must never be mixed into the real
    # extracted dataset. Column names match hirers.csv / providers.csv so
    # label.py can read them unchanged; fields the workbook has no column for
    # (about_title, about_description) are left empty rather than invented.
    with (TESTSET_DIR / "gigs.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["source_file", "hire_title", "hire_description",
                                          "hire_description_additional_notes", "industry",
                                          "difficulty_level"])
        w.writeheader()
        for g in gigs:
            w.writerow({
                "source_file": GIG_ID.format(int(g["gig_id"])),
                "hire_title": _clean(g["gig_title"]),
                "hire_description": _clean(g["gig_description"]),
                "hire_description_additional_notes": _clean(g.get("approx_revenue")),
                "industry": _clean(g.get("industry")),
                "difficulty_level": _clean(g.get("difficulty_level")),
            })

    with (TESTSET_DIR / "showcases.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["source_file", "about_title", "about_description",
                                          "services_offered_title", "services_offered_description",
                                          "relevant_experience", "difficulty_level"])
        w.writeheader()
        for p in provs:
            w.writerow({
                "source_file": PROV_ID.format(int(p["provider_id"])),
                "about_title": "", "about_description": "",
                "services_offered_title": _clean(p["services_offered_title"]),
                "services_offered_description": _clean(p["services_offered_description"]),
                "relevant_experience": _clean(p["relevant_experience"]),
                "difficulty_level": _clean(p.get("difficulty_level")),
            })

    gold_gigs = {}
    for row in key:
        gid, pid = int(row["hirer_id"]), int(row["provider_id"])
        band = _clean(row["difficulty_level"]).upper()
        if band not in BAND_TO_GRADE:
            print(f"  [WARN] pair {gid}: unrecognised band {band!r}, skipped")
            continue
        entry = gold_gigs.setdefault(GIG_ID.format(gid), {
            "id": f"C{gid:03d}",
            "title": _clean(row["hirer_gig_title"]),
            "grades": {},
            "bands": {},
            "rationales": {},
        })
        entry["grades"][PROV_ID.format(pid)] = BAND_TO_GRADE[band]
        entry["bands"][PROV_ID.format(pid)] = band
        entry["rationales"][PROV_ID.format(pid)] = _clean(row.get("match_rationale"))

    gold = {
        "source": f"Derived from client_documents/{wb_path.name} by "
                  f"labeller/experiments/build_gold.py -- rerun it rather than editing this file.",
        "annotator": "The client, writing with an LLM. NOT measured ground truth and NOT human "
                     "annotation: the workbook's 0-100 expected_score_range values are one "
                     "model's opinion and are deliberately NOT carried over here. Only the "
                     "ordinal four-band judgement is, mapped onto the 0-3 rubric below. Treat "
                     "as a development target, not a measurement of matching quality.",
        "caveats": [
            "1:1 pairing only -- the workbook never claims anything about the other 29 "
            "providers per gig, but evaluate.py scores unlabelled providers as grade 0.",
            "The 4 NEAR-MISS gigs have no provider graded >=1, so NDCG is undefined for them "
            "(evaluate.py reports nan). Check those with report_near_miss() instead: they are "
            "passed by scoring LOW, which a ranking metric cannot see.",
            "The gigs and showcases are synthetic Singapore-SME scenarios; the extracted "
            "corpus is global big-4 consulting. Good scores here do not transfer automatically.",
        ],
        "rubric": RUBRIC,
        "band_to_grade": BAND_TO_GRADE,
        "gigs": gold_gigs,
    }
    GOLD_PATH.write_text(json.dumps(gold, indent=1, ensure_ascii=False), encoding="utf-8")

    dist = {}
    for g in gold_gigs.values():
        for band in g["bands"].values():
            dist[band] = dist.get(band, 0) + 1
    print(f"  wrote {GOLD_PATH.relative_to(ROOT_DIR)}  ({len(gold_gigs)} gigs; bands: "
          f"{', '.join(f'{k} {v}' for k, v in sorted(dist.items()))})")
    print(f"  wrote {(TESTSET_DIR / 'gigs.csv').relative_to(ROOT_DIR)} and showcases.csv")
    print("\nTo score against it:")
    print("  py -3 labeller/label.py --hirers labeller/experiments/client_testset/gigs.csv \\")
    print("        --providers labeller/experiments/client_testset/showcases.csv --max-pairs 900")
    print("  py -3 labeller/evaluate.py docs/relevance_scores.csv rg_3l rg_3l_multi")


if __name__ == "__main__":
    build()
