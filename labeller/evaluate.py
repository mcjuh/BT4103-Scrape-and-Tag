# -*- coding: utf-8 -*-
"""
Score relevance predictions against the graded gold labels
(experiments/gold.json: the client's 30 gigs, one intended showcase each, graded 0-3
from the client's four bands; every other showcase counts as grade 0).

    py -3 labeller/evaluate.py docs/relevance_scores.csv rg_3l
    py -3 labeller/evaluate.py predictions.csv rg_2l rg_3l rg_3l_multi --per-gig per_gig.csv

predictions.csv has one row per (gig, provider) pair:
  gig column       hirer_file | gig | hirer      (the source_file in hirers.csv)
  provider column  provider_file | provider      (the source_file in providers.csv)
and each labelling method's score (higher = more relevant) in either layout:
  wide   a column named after the method -- label.py's docs/relevance_scores.csv
         (rg_2l, rg_3l, rg_4l, rg_s04, rg_3l_multi) is already in this shape
  long   a method | approach | cond column naming the method, plus a score column
Blank scores are skipped (e.g. rg_3l_multi for a pair where a model call failed).

Only gigs in the gold file count. Each is scored over the providers the
predictions scored for it (the re-ranking setting), with gold providers the
predictions didn't score ignored and scored providers missing from gold
counted as grade 0. "relevant scored" reports how many of a gig's gold
grade>=2 providers the predictions scored at all: NDCG over a candidate set
that left the right providers out can still look high.

With several methods, p is a paired permutation test against the first one
over the gigs both scored.
"""

import argparse
import csv
import json
import math
import statistics as st
import sys
from collections import Counter, defaultdict
from pathlib import Path

from metrics import gig_metrics, mean_ci, paired_p, spearman

SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_GOLD = SCRIPT_DIR / "experiments" / "gold.json"

GIG_COLS = ("hirer_file", "gig", "hirer")
PROVIDER_COLS = ("provider_file", "provider")
METHOD_COLS = ("method", "approach", "cond")
SCORE_COL = "score"


def _pick(fields: list, options: tuple, what: str, path: Path) -> str:
    for c in options:
        if c in fields:
            return c
    sys.exit(f"{path} has no {what} column (expected one of: {', '.join(options)}). Columns: {fields}")


def load_predictions(path: Path, methods: list):
    """-> ({method: {gig: {provider: score}}}, {method: blank count}, {method: duplicate count})"""
    csv.field_size_limit(10**9)
    with path.open(newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        rows, fields = list(reader), reader.fieldnames or []
    gcol = _pick(fields, GIG_COLS, "gig", path)
    pcol = _pick(fields, PROVIDER_COLS, "provider", path)
    mcol = next((c for c in METHOD_COLS if c in fields), None)
    long_ok = mcol is not None and SCORE_COL in fields
    for m in methods:
        if m not in fields and not long_ok:
            sys.exit(f"{path}: no '{m}' column, and no {'/'.join(METHOD_COLS)} + {SCORE_COL} columns for "
                     f"the long layout. Columns: {fields}")

    preds = {m: defaultdict(dict) for m in methods}
    blank, dupes = Counter(), Counter()
    for line, r in enumerate(rows, 2):
        for m in methods:
            if m in fields:          # wide
                v = r[m]
            elif r[mcol] == m:       # long
                v = r[SCORE_COL]
            else:
                continue
            if v is None or not v.strip():
                blank[m] += 1
                continue
            try:
                score = float(v)
            except ValueError:
                sys.exit(f"{path}:{line}: {m} score {v!r} isn't a number")
            if r[pcol] in preds[m][r[gcol]]:
                dupes[m] += 1  # last one wins
            preds[m][r[gcol]][r[pcol]] = score
    return preds, blank, dupes


def evaluate(by_gig: dict, gold: dict) -> dict:
    per_gig, xs, ys = {}, [], []
    for gig, scores in by_gig.items():
        if gig not in gold["gigs"] or len(scores) < 2:
            continue
        grades = gold["gigs"][gig]["grades"]
        mt = gig_metrics(scores, grades)
        relevant = [p for p, g in grades.items() if g >= 2]
        mt["relevant_scored"] = sum(p in scores for p in relevant) / len(relevant) if relevant else float("nan")
        mt["n"] = len(scores)
        per_gig[gig] = mt
        for p, s in scores.items():
            xs.append(s)
            ys.append(grades.get(p, 0))
    return {"per_gig": per_gig, "pooled_spearman": spearman(xs, ys), "pairs": len(xs)}


def _mean(vals: list) -> float:
    vals = [v for v in vals if not math.isnan(v)]
    return st.mean(vals) if vals else float("nan")


def main():
    parser = argparse.ArgumentParser(description="Score relevance predictions against gold labels.")
    parser.add_argument("predictions", type=Path, help="predictions CSV (see module docstring for the layout)")
    parser.add_argument("methods", nargs="+", help="labelling method(s) to score, e.g. rg_3l")
    parser.add_argument("--gold", type=Path, default=DEFAULT_GOLD, help=f"gold labels (default: {DEFAULT_GOLD.name})")
    parser.add_argument("--per-gig", type=Path, help="also write per-gig metrics to this CSV")
    args = parser.parse_args()

    gold = json.loads(args.gold.read_text(encoding="utf-8"))
    preds, blank, dupes = load_predictions(args.predictions, args.methods)
    results = {m: evaluate(preds[m], gold) for m in args.methods}

    print(f"Predictions: {args.predictions}")
    print(f"Gold:        {args.gold} ({len(gold['gigs'])} gigs)")
    for m in args.methods:
        outside = sum(g not in gold["gigs"] for g in preds[m])
        notes = [f"{len(preds[m])} gig(s) in predictions, {outside} not in gold"]
        no_rel = [gold["gigs"][g]["id"] for g, v in results[m]["per_gig"].items() if math.isnan(v["ndcg10"])]
        if no_rel:
            notes.append(f"{len(no_rel)} gig(s) with no gold-relevant provider among the scored ones "
                         f"({', '.join(no_rel)}) -- nothing to rank, so NDCG/tau/AUC are undefined and left out")
        if blank[m]:
            notes.append(f"{blank[m]} blank score(s) skipped")
        if dupes[m]:
            notes.append(f"{dupes[m]} duplicate pair(s), last kept")
        print(f"  {m}: " + "; ".join(notes))
    print()

    header = ["method", "gigs", "pairs", "NDCG@10 [95% CI]", "NDCG@5", "tau-b", "AUC", "relevant scored",
              "pooled Spearman"] + (["p vs " + args.methods[0]] if len(args.methods) > 1 else [])
    rows = []
    base = results[args.methods[0]]["per_gig"]
    for m in args.methods:
        pg = results[m]["per_gig"]
        mean, lo, hi = mean_ci([v["ndcg10"] for v in pg.values()])
        row = [m, str(len(pg)), str(results[m]["pairs"]), f"{mean:.3f} [{lo:.3f}, {hi:.3f}]"]
        row += [f"{_mean([v[k] for v in pg.values()]):.3f}" for k in ("ndcg5", "tau", "auc", "relevant_scored")]
        row.append(f"{results[m]['pooled_spearman']:.3f}")
        if len(args.methods) > 1:
            common = [g for g in pg if g in base]
            row.append("-" if m == args.methods[0] else
                       f"{paired_p([pg[g]['ndcg10'] for g in common], [base[g]['ndcg10'] for g in common]):.3f}"
                       f" ({len(common)} gigs)")
        rows.append(row)
    widths = [max(len(r[i]) for r in rows + [header]) for i in range(len(header))]
    for r in [header, ["-" * w for w in widths]] + rows:
        print("  ".join(c.ljust(w) for c, w in zip(r, widths)))
    if any(len(results[m]["per_gig"]) < 5 for m in args.methods):
        print("\nFewer than 5 gigs scored: the interval and p-value are not meaningful yet.")

    if args.per_gig:
        with args.per_gig.open("w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["method", "gig_id", "gig_title", "n_scored", "ndcg10", "ndcg5", "tau", "auc",
                        "relevant_scored"])
            for m in args.methods:
                for g, v in results[m]["per_gig"].items():
                    info = gold["gigs"][g]
                    w.writerow([m, info["id"], info["title"], v["n"]] +
                               [round(v[k], 4) for k in ("ndcg10", "ndcg5", "tau", "auc", "relevant_scored")])
        print(f"\nWrote {args.per_gig}")


if __name__ == "__main__":
    main()
