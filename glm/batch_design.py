# -*- coding: utf-8 -*-
"""Design rows for the comparison batch: the same 100 gigs and the same 4 providers per gig (one per grade 3, 2, 1, 0)
for both the GLM run (run_batch.py) and the Claude run (claude_batch.py), so the two sets differ only in the author.

A new seed, so none of these gigs repeats the 200 of the GLM trial; the hirer-industry pool is on."""

import csv
import os
import random
from pathlib import Path

import design

ROOT = Path(__file__).resolve().parent.parent
# COMPARE_BATCH=2 selects the second sample (own seed, own folder); unset keeps the first.
BATCH = os.environ.get("COMPARE_BATCH", "1")
OUT = ROOT / "data" / "output" / ("compare_batch" if BATCH == "1" else f"compare_batch_{BATCH}")
SEED = 20261027 if BATCH == "1" else int(f"2026102{BATCH}") + 7919 * int(BATCH)
N_GIGS = 100


def gig_rows() -> list:
    return design.design_gigs(N_GIGS, seed=SEED, industry=True)


def provider_rows(gig_row: dict, prefix: str) -> list:
    """Four design rows for one gig, one per grade (route a or b drawn per grade), the letters a-d shuffled so the
    file name does not give away the grade. `prefix` is "glm" or "crafted"; everything else is identical."""
    eight = design.design_providers(gig_row, seed=SEED)
    rng = random.Random(f"{SEED}:{gig_row['gig']}:pick")
    picked = [rng.choice([r for r in eight if r["target_grade"] == grade]) for grade in (3, 2, 1, 0)]
    rng.shuffle(picked)
    rows = []
    for letter, r in zip("abcd", picked):
        rows.append({**r, "provider": f"{prefix}-provider__{gig_row['n']:02d}_{letter}.md"})
    return rows


def save_design() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    rows = gig_rows()
    with (OUT / "design.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    prows = [{**p, "provider": p["provider"].split("__", 1)[1]} for g in rows for p in provider_rows(g, "x")]
    with (OUT / "providers_design.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(prows[0]))
        w.writeheader()
        w.writerows(prows)


if __name__ == "__main__":
    save_design()
    print(f"wrote {OUT / 'design.csv'} and providers_design.csv")
