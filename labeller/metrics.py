# -*- coding: utf-8 -*-
"""
Ranking metrics shared by evaluate.py and experiments/analyze.py.

For one gig, `scores` is {provider: predicted score} (higher = more relevant)
and `grades` is {provider: gold grade 0-3}; a provider missing from `grades`
counts as grade 0.

NDCG uses linear gains (as trec_eval, which the Beyond Yes and No paper
reports) and is the expectation over random tie-breaking, so tied scores
aren't rewarded by a lucky input order. Intervals and p-values are taken over
gigs: a percentile bootstrap, and a paired sign-flip permutation test.
"""

import math
import random
import statistics as st

TIE_SHUFFLES = 50


def _dcg(grades: list, k: int) -> float:
    return sum(g / math.log2(i + 2) for i, g in enumerate(grades[:k]))


def ndcg(scores: dict, grades: dict, k: int, seed: int = 0) -> float:
    items = sorted(scores)
    idcg = _dcg(sorted((grades.get(p, 0) for p in items), reverse=True), k)
    if not idcg:
        return float("nan")  # nothing relevant among the scored providers
    tied = len(set(scores.values())) < len(scores)
    rng, total, n = random.Random(seed), 0.0, (TIE_SHUFFLES if tied else 1)
    for _ in range(n):
        rng.shuffle(items)
        ranked = sorted(items, key=lambda p: -scores[p])  # stable sort: ties fall in random order
        total += _dcg([grades.get(p, 0) for p in ranked], k)
    return total / n / idcg


def tau_b(x: list, y: list) -> float:
    conc = disc = tx = ty = 0
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            dx, dy = x[i] - x[j], y[i] - y[j]
            if dx == 0 and dy == 0:
                continue
            if dx == 0:
                tx += 1
            elif dy == 0:
                ty += 1
            elif (dx > 0) == (dy > 0):
                conc += 1
            else:
                disc += 1
    denom = math.sqrt((conc + disc + tx) * (conc + disc + ty))
    return (conc - disc) / denom if denom else float("nan")


def auc(scores: dict, grades: dict, min_grade: int = 2) -> float:
    pos = [s for p, s in scores.items() if grades.get(p, 0) >= min_grade]
    neg = [s for p, s in scores.items() if grades.get(p, 0) < min_grade]
    if not pos or not neg:
        return float("nan")
    wins = sum((a > b) + 0.5 * (a == b) for a in pos for b in neg)
    return wins / (len(pos) * len(neg))


def avg_ranks(values: list) -> list:
    order = sorted(range(len(values)), key=lambda i: values[i])
    ranks = [0.0] * len(values)
    i = 0
    while i < len(order):
        j = i
        while j + 1 < len(order) and values[order[j + 1]] == values[order[i]]:
            j += 1
        for k in range(i, j + 1):
            ranks[order[k]] = (i + j) / 2 + 1
        i = j + 1
    return ranks


def spearman(x: list, y: list) -> float:
    if len(x) < 2:
        return float("nan")
    rx, ry = avg_ranks(x), avg_ranks(y)
    mx, my = st.mean(rx), st.mean(ry)
    num = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    den = math.sqrt(sum((a - mx) ** 2 for a in rx) * sum((b - my) ** 2 for b in ry))
    return num / den if den else float("nan")


def gig_metrics(scores: dict, grades: dict) -> dict:
    items = sorted(scores)
    return {
        "ndcg10": ndcg(scores, grades, 10),
        "ndcg5": ndcg(scores, grades, 5),
        "tau": tau_b([scores[p] for p in items], [grades.get(p, 0) for p in items]),
        "auc": auc(scores, grades),
        "distinct": len(set(scores.values())) / len(scores),
    }


def mean_ci(vals: list, boot: int = 5000, seed: int = 1):
    vals = [v for v in vals if not math.isnan(v)]
    if not vals:
        return float("nan"), float("nan"), float("nan")
    rng = random.Random(seed)
    boots = sorted(st.mean(rng.choices(vals, k=len(vals))) for _ in range(boot))
    return st.mean(vals), boots[int(0.025 * boot)], boots[int(0.975 * boot) - 1]


def paired_p(a: list, b: list, perm: int = 20000, seed: int = 2) -> float:
    d = [x - y for x, y in zip(a, b) if not (math.isnan(x) or math.isnan(y))]
    if not d:
        return float("nan")
    obs = abs(sum(d))
    rng = random.Random(seed)
    hits = sum(abs(sum(x if rng.random() < 0.5 else -x for x in d)) >= obs - 1e-12 for _ in range(perm))
    return (hits + 1) / (perm + 1)
