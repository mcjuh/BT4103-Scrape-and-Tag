# -*- coding: utf-8 -*-
"""
Scores the prompt experiment (run_grid.py output) against gold.json.

    py -3 labeller/experiments/analyze.py

Writes results/report.md (the tables) and results/per_gig.csv (every
ranker's per-gig metrics). Rankers:
  single    one (condition, model) with one scoring method:
              er  = expected relevance over the label probabilities (paper, label.py's score)
              pr  = peak relevance, log-likelihood of the top label (paper's alternative)
              gen = the label the model actually generated (the paper's argument against it: ties)
  routed    label.py's production setup: each gig judged by its hashed model (model_for_gig), er
  ens_*     one condition's er scores from all four models combined per gig, by mean score,
            mean rank, or mean per-model z-score

Primary metric is NDCG@10 with linear gains (the paper's metric, as in trec_eval), taken as the
expectation over random tie-breaking so tied scores aren't rewarded by a lucky input order.
Uncertainty: 95% bootstrap intervals over gigs; p-values are paired sign-flip permutation tests over gigs.
"""

import csv
import json
import math
import statistics as st
import sys
from collections import defaultdict
from pathlib import Path

EXP_DIR = Path(__file__).resolve().parent
sys.path[:0] = [str(EXP_DIR), str(EXP_DIR.parent)]
import run_grid as R  # noqa: E402
from metrics import avg_ranks, gig_metrics, mean_ci, paired_p, spearman  # noqa: E402
L = R.L

GOLD = json.loads(R.GOLD_PATH.read_text(encoding="utf-8"))
CANDS = json.loads(R.CANDIDATES_PATH.read_text(encoding="utf-8"))
REPORT_PATH = R.RESULTS_DIR / "report.md"
PER_GIG_PATH = R.RESULTS_DIR / "per_gig.csv"

CONDS = list(R.CONDITIONS)
MODELS = L.MODEL_POOL
GIGS = list(CANDS)  # narrowed in main() to the gigs whose grid is complete
SCORINGS = ["er", "pr", "gen"]


# ---------------------------------------------------------------------------
# Rankers
# ---------------------------------------------------------------------------

def load_records() -> dict:
    recs = {}  # (cond, model, gig, provider) -> latest ok record
    with R.GRID_PATH.open(encoding="utf-8") as f:
        for line in f:
            r = json.loads(line)
            if r.get("status") == "ok":
                recs[(r["cond"], r["model"], r["gig"], r["provider"])] = r
    return recs


def single_scores(recs, cond, model, gig, scoring):
    field = {"er": "score", "pr": "peak_relevance", "gen": "gen_value"}[scoring]
    out = {}
    for p in CANDS[gig]:
        r = recs.get((cond, model, gig, p))
        if r is None or r.get(field) is None:
            return None  # incomplete -- this gig is dropped for this ranker
        out[p] = r[field]
    return out


def ensemble_scores(recs, cond, gig, how):
    per_model = [single_scores(recs, cond, m, gig, "er") for m in MODELS]
    if any(s is None for s in per_model):
        return None
    items = CANDS[gig]
    cols = []
    for s in per_model:
        v = [s[p] for p in items]
        if how == "mean":
            cols.append(v)
        elif how == "rank":
            cols.append(avg_ranks(v))
        else:  # z
            mu, sd = st.mean(v), st.pstdev(v)
            cols.append([(x - mu) / sd if sd else 0.0 for x in v])
    return {p: st.mean(c[i] for c in cols) for i, p in enumerate(items)}


def build_rankers(recs) -> dict:
    """name -> {gig: metrics}"""
    rankers = {}
    for c in CONDS:
        for m in MODELS:
            for s in SCORINGS:
                rankers[("single", c, m, s)] = {}
        rankers[("routed", c, "-", "er")] = {}
        for how in ("mean", "rank", "z"):
            rankers[(f"ens_{how}", c, "all", "er")] = {}
    for g in GIGS:
        grades = GOLD["gigs"][g]["grades"]
        for key in rankers:
            kind, c, m, s = key
            if kind == "single":
                sc = single_scores(recs, c, m, g, s)
            elif kind == "routed":
                sc = single_scores(recs, c, L.model_for_gig(g), g, "er")
            else:
                sc = ensemble_scores(recs, c, g, kind[4:])
            if sc is not None:
                rankers[key][g] = gig_metrics(sc, grades)
    return rankers


def per_gig(rankers, key, metric="ndcg10") -> list:
    return [rankers[key].get(g, {}).get(metric, float("nan")) for g in GIGS]


def model_avg(rankers, cond, scoring, metric="ndcg10") -> list:
    """Per gig, the mean over the four single-model rankers -- 'how good is this prompt on a typical model'."""
    out = []
    for g in GIGS:
        vals = [rankers[("single", cond, m, scoring)].get(g, {}).get(metric, float("nan")) for m in MODELS]
        vals = [v for v in vals if not math.isnan(v)]
        out.append(st.mean(vals) if vals else float("nan"))
    return out


# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------

def fmt_ci(vals):
    m, lo, hi = mean_ci(vals)
    return f"{m:.3f} [{lo:.3f}, {hi:.3f}]"


def table(header, rows):
    lines = ["| " + " | ".join(header) + " |", "|" + "|".join("---" for _ in header) + "|"]
    lines += ["| " + " | ".join(str(x) for x in r) + " |" for r in rows]
    return "\n".join(lines)


def main():
    global GIGS
    recs = load_records()
    # Only gigs with every (condition, model, candidate) call present, so every ranker is compared
    # on the same gigs -- lets the report run on a partial grid while run_grid.py is still going.
    GIGS = [g for g in CANDS if all((c, m, g, p) in recs for c in CONDS for m in MODELS for p in CANDS[g])]
    if len(GIGS) < 2:
        sys.exit(f"Only {len(GIGS)} gig(s) fully scored so far -- need at least 2 for intervals.")
    rankers = build_rankers(recs)
    out = []
    n_expected = sum(len(CANDS[g]) for g in CANDS) * len(CONDS) * len(MODELS)
    parsed = sum(r.get("scoring") == "parsed" for r in recs.values())
    out.append("# Labeller prompt experiment\n")
    out.append(f"{len(GIGS)} of {len(CANDS)} gigs fully scored, {len(next(iter(CANDS.values())))} candidate "
               f"providers each, {len(CONDS)} conditions x {len(MODELS)} models. Calls recorded ok: "
               f"{len(recs)}/{n_expected} ({parsed} scored by parsing instead of logprobs).\n")
    out.append(f"Gold: {GOLD['annotator']}\n")
    out.append("NDCG@10 is the mean over gigs with a 95% bootstrap CI. p is a paired permutation test over gigs.\n")

    # 1. Prompt comparison (er, averaged over models)
    base = model_avg(rankers, "rg_2l", "er")
    rows = []
    for c in CONDS:
        v = model_avg(rankers, c, "er")
        rows.append([f"`{c}`", fmt_ci(v), f"{st.mean(v) - st.mean(base):+.3f}",
                     f"{paired_p(v, base):.3f}" if c != "rg_2l" else "-",
                     f"{st.mean(model_avg(rankers, c, 'er', 'ndcg5')):.3f}",
                     f"{st.mean(model_avg(rankers, c, 'er', 'tau')):.3f}",
                     f"{st.mean(model_avg(rankers, c, 'er', 'auc')):.3f}"])
    rows.sort(key=lambda r: -float(r[1].split()[0]))
    out.append("## 1. Which prompt ranks best (expected-relevance scoring, averaged over the 4 models)\n")
    out.append(table(["condition", "NDCG@10 [95% CI]", "vs rg_2l", "p vs rg_2l", "NDCG@5", "Kendall tau-b",
                      "AUC (grade>=2)"], rows) + "\n")

    # 2. Scoring method
    rows = []
    for c in CONDS:
        er, pr, gen = (model_avg(rankers, c, s) for s in SCORINGS)
        dist = {s: st.mean(model_avg(rankers, c, s, "distinct")) for s in SCORINGS}
        rows.append([f"`{c}`", f"{st.mean(er):.3f}", f"{st.mean(pr):.3f}", f"{st.mean(gen):.3f}",
                     f"{paired_p(er, gen):.3f}", f"{dist['er']:.2f}", f"{dist['gen']:.2f}"])
    out.append("## 2. Scoring method: expected relevance vs peak relevance vs generated label\n")
    out.append(table(["condition", "ER", "PR", "generated label", "p ER vs generated",
                      "distinct scores ER", "distinct scores generated"], rows) + "\n")

    # 3. Prompt x model
    rows = []
    for c in CONDS:
        rows.append([f"`{c}`"] + [f"{st.mean(per_gig(rankers, ('single', c, m, 'er'))):.3f}" for m in MODELS])
    rows.append(["**model mean**"] + [f"**{st.mean(st.mean(per_gig(rankers, ('single', c, m, 'er'))) for c in CONDS):.3f}**"
                                      for m in MODELS])
    out.append("## 3. NDCG@10 by prompt and model (ER)\n")
    out.append(table(["condition"] + [f"`{m}`" for m in MODELS], rows) + "\n")

    # 4. Several judges vs one
    rows = []
    for c in CONDS:
        single_means = {m: st.mean(per_gig(rankers, ("single", c, m, "er"))) for m in MODELS}
        best_m = max(single_means, key=single_means.get)
        avg1 = model_avg(rankers, c, "er")
        routed = per_gig(rankers, ("routed", c, "-", "er"))
        ens = {h: per_gig(rankers, (f"ens_{h}", c, "all", "er")) for h in ("mean", "rank", "z")}
        best = per_gig(rankers, ("single", c, best_m, "er"))
        rows.append([f"`{c}`", f"{st.mean(routed):.3f}", f"{st.mean(avg1):.3f}",
                     f"{single_means[best_m]:.3f} ({best_m})",
                     f"{st.mean(ens['mean']):.3f}", f"{st.mean(ens['rank']):.3f}", f"{st.mean(ens['z']):.3f}",
                     f"{paired_p(ens['mean'], routed):.3f}", f"{paired_p(ens['z'], best):.3f}"])
    out.append("## 4. Several judges vs one (NDCG@10, ER)\n")
    out.append("`routed` = label.py's production setup (one hashed model per gig). `mean single` = the average "
               "model. `best single` is picked with hindsight on this same data, so it's optimistic.\n")
    out.append(table(["condition", "routed (1 model)", "mean single", "best single", "ens: mean score",
                      "ens: mean rank", "ens: mean z-score", "p ens-mean vs routed", "p ens-z vs best single"],
                     rows) + "\n")

    # 5. Calibration: mean ER score by gold grade
    rows = []
    for c in ["rg_2l", "rg_3l", "rg_s04", "yn"]:
        for m in MODELS:
            by_grade = defaultdict(list)
            xs, ys = [], []
            for g in GIGS:
                grades = GOLD["gigs"][g]["grades"]
                for p in CANDS[g]:
                    r = recs.get((c, m, g, p))
                    if r:
                        by_grade[grades.get(p, 0)].append(r["score"])
                        xs.append(r["score"])
                        ys.append(grades.get(p, 0))
            rows.append([f"`{c}`", f"`{m}`"] + [f"{st.mean(by_grade[k]):.3f}" if by_grade[k] else "-"
                                                 for k in (0, 1, 2, 3)] + [f"{spearman(xs, ys):.3f}"])
    out.append("## 5. Calibration: mean score by gold grade, and Spearman over all pairs pooled across gigs\n")
    out.append("Pooled correlation matters if scores are compared across gigs or thresholded "
               "(e.g. 'show matches above 0.5'), not just ranked within a gig.\n")
    out.append(table(["condition", "model", "grade 0", "grade 1", "grade 2", "grade 3", "Spearman"], rows) + "\n")

    # 6. Cost
    rows = []
    for m in MODELS:
        lat = [r["latency_s"] for k, r in recs.items() if k[1] == m and "latency_s" in r]
        rows.append([f"`{m}`", f"{st.median(lat):.2f}", f"{st.mean(lat):.2f}"])
    out.append("## 6. Latency per call (s, measured at 8 parallel workers)\n")
    out.append(table(["model", "median", "mean"], rows) + "\n")
    rows = []
    for c in CONDS:
        pt = [r["usage"]["prompt_tokens"] for k, r in recs.items() if k[0] == c and r.get("usage")]
        rows.append([f"`{c}`", f"{st.mean(pt):.0f}" if pt else "-"])
    out.append(table(["condition", "mean prompt tokens"], rows) + "\n")

    # 7. Per-gig view for the headline comparison
    rows = []
    for g in GIGS:
        info = GOLD["gigs"][g]
        rows.append([info["id"], info["title"][:60],
                     f"{st.mean([rankers[('single', 'rg_2l', m, 'er')].get(g, {}).get('ndcg10', float('nan')) for m in MODELS]):.3f}",
                     f"{st.mean([rankers[('single', 'rg_3l', m, 'er')].get(g, {}).get('ndcg10', float('nan')) for m in MODELS]):.3f}",
                     f"{rankers[('ens_z', 'rg_3l', 'all', 'er')].get(g, {}).get('ndcg10', float('nan')):.3f}"])
    out.append("## 7. Per gig: NDCG@10\n")
    out.append(table(["gig", "title", "rg_2l (model avg)", "rg_3l (model avg)", "rg_3l ens z"], rows) + "\n")

    REPORT_PATH.write_text("\n".join(out), encoding="utf-8")
    with PER_GIG_PATH.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["kind", "cond", "model", "scoring", "gig", "ndcg10", "ndcg5", "tau", "auc", "distinct"])
        for (kind, c, m, s), by_gig in rankers.items():
            for g, mt in by_gig.items():
                w.writerow([kind, c, m, s, GOLD["gigs"][g]["id"]] +
                           [round(mt[k], 4) for k in ("ndcg10", "ndcg5", "tau", "auc", "distinct")])
    sys.stdout.reconfigure(encoding="utf-8")
    print("\n".join(out))
    print(f"\nWrote {REPORT_PATH} and {PER_GIG_PATH}")


if __name__ == "__main__":
    main()
