# -*- coding: utf-8 -*-
"""
Prompt experiment for the labeller: every prompt variant x every pool model
over a fixed candidate set per evaluation gig. analyze.py then scores the
rankings against the graded gold labels in gold.json.

    py -3 labeller/experiments/run_grid.py [--workers 8] [--candidates 40]

Candidates per gig = every gold-graded provider (grade >= 1) plus seeded
random grade-0 providers up to --candidates in total -- the paper's
re-ranking setting (it re-ranks BM25's top 100). The set is saved to
results/candidates.json the first time, so reruns and analyze.py see the
same one. Calls already recorded ok in results/grid.jsonl are skipped.

Conditions: the paper's four prompts from label.py, its Yes/No baseline,
plus three ablations -- RG-3L with the labels listed least relevant first
(the order label.py used before), a 0-2 scale, and RG-3L reworded for the
domain ("gig" / "provider profile" instead of "query" / "document").
"""

import argparse
import json
import random
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

EXP_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(EXP_DIR.parent))
import label as L  # noqa: E402  (same role folder, so importing is fine)

GOLD_PATH = EXP_DIR / "gold.json"
RESULTS_DIR = EXP_DIR / "results"
GRID_PATH = RESULTS_DIR / "grid.jsonl"
CANDIDATES_PATH = RESULTS_DIR / "candidates.json"
PROMPTS_DIR = EXP_DIR / "prompts"

YN_TEMPLATE = (PROMPTS_DIR / "rg_yn.md").read_text(encoding="utf-8").strip()
GIG_TEMPLATE = (PROMPTS_DIR / "rg_labels_gig.md").read_text(encoding="utf-8").strip()
SEED = 4103


def _options(labels_in_prompt_order: list) -> str:
    quoted = [f'"{l}"' for l in labels_in_prompt_order]
    return ", ".join(quoted[:-1]) + ", or " + quoted[-1]


RG3 = L.APPROACHES["rg_3l"][1]

# id -> (labels in ascending relevance, render(query, document) -> prompt)
CONDITIONS = {
    "yn": (["No", "Yes"], lambda q, d: YN_TEMPLATE.format(query=q, document=d)),
    "rg_2l": (L.APPROACHES["rg_2l"][1], lambda q, d: L.build_prompt("rg_2l", q, d)),
    "rg_3l": (RG3, lambda q, d: L.build_prompt("rg_3l", q, d)),
    "rg_4l": (L.APPROACHES["rg_4l"][1], lambda q, d: L.build_prompt("rg_4l", q, d)),
    "rg_s02": (["0", "1", "2"], lambda q, d: L.SCALE_TEMPLATE.format(k=2, query=q, document=d)),
    "rg_s04": (L.APPROACHES["rg_s04"][1], lambda q, d: L.build_prompt("rg_s04", q, d)),
    "rg_3l_asc": (RG3, lambda q, d: L.LABEL_TEMPLATE.format(label_options=_options(RG3), query=q, document=d)),
    "rg_3l_gig": (RG3, lambda q, d: GIG_TEMPLATE.format(label_options=_options(RG3[::-1]), query=q, document=d)),
}


class Pacer:
    """Spaces requests evenly across all worker threads. SOCLAAS returns a bare
    429 with no rate-limit headers; measured, it lets a burst of ~60 through and
    then sustains only ~1 request/s, so unpaced workers retry in lockstep and
    most of the budget goes to 429s."""

    def __init__(self, rps: float):
        self.gap, self.next_at, self.lock = 1.0 / rps, time.monotonic(), threading.Lock()

    def wait(self):
        with self.lock:
            now = time.monotonic()
            slot = max(now, self.next_at)
            self.next_at = slot + self.gap
        time.sleep(max(0.0, slot - now))


def pace_client(rps: float):
    """Route every request label.py makes (retries included) through one Pacer,
    and turn off the OpenAI client's own hidden 429 retries so each attempt is
    paced exactly once."""
    pacer = Pacer(rps)
    L.client = L.client.with_options(max_retries=0)
    create = L.client.chat.completions.create

    def paced_create(*args, **kwargs):
        pacer.wait()
        return create(*args, **kwargs)

    L.client.chat.completions.create = paced_create


def build_candidates(gold: dict, provider_ids: list, n_total: int) -> dict:
    cands = {}
    for gig, info in gold["gigs"].items():
        pos = sorted(info["grades"])
        neg = sorted(set(provider_ids) - set(pos))
        rng = random.Random(f"{SEED}:{gig}")
        chosen = pos + rng.sample(neg, max(0, n_total - len(pos)))
        rng.shuffle(chosen)
        cands[gig] = chosen
    return cands


def load_done() -> set:
    done = set()
    if GRID_PATH.exists():
        with GRID_PATH.open(encoding="utf-8") as f:
            for line in f:
                try:
                    r = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if r.get("status") == "ok":
                    done.add((r["gig"], r["provider"], r["cond"], r["model"]))
    return done


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=8, help="parallel calls in flight")
    parser.add_argument("--rps", type=float, default=1.0, help="requests/second across all workers (SOCLAAS sustains ~1)")
    parser.add_argument("--candidates", type=int, default=40, help="providers per gig (gold positives + random negatives)")
    parser.add_argument("--conds", nargs="*", default=list(CONDITIONS), help="subset of conditions to run")
    parser.add_argument("--models", nargs="*", default=L.MODEL_POOL, help="subset of models to run")
    parser.add_argument("--max-gigs", type=int, default=None, help="only the first N gigs (smoke test)")
    args = parser.parse_args()
    pace_client(args.rps)

    gold = json.loads(GOLD_PATH.read_text(encoding="utf-8"))
    hirers = {h["source_file"]: h for h in L.load_rows(L.HIRERS_CSV)}
    providers = {p["source_file"]: p for p in L.load_rows(L.PROVIDERS_CSV)}
    missing = [g for g in gold["gigs"] if g not in hirers] + \
              [p for v in gold["gigs"].values() for p in v["grades"] if p not in providers]
    if missing:
        sys.exit(f"gold.json names rows no longer in the CSVs: {missing[:5]}")

    RESULTS_DIR.mkdir(exist_ok=True)
    if CANDIDATES_PATH.exists():
        cands = json.loads(CANDIDATES_PATH.read_text(encoding="utf-8"))
    else:
        cands = build_candidates(gold, sorted(providers), args.candidates)
        CANDIDATES_PATH.write_text(json.dumps(cands, indent=1), encoding="utf-8")

    gigs = list(cands)[: args.max_gigs]
    query = {g: L._describe(hirers[g], L.GIG_FIELDS) for g in gigs}
    doc = {p: L._describe(providers[p], L.PROFILE_FIELDS) for g in gigs for p in cands[g]}
    done = load_done()
    jobs = [(g, p, c, m) for g in gigs for p in cands[g] for c in args.conds for m in args.models
            if (g, p, c, m) not in done]
    print(f"{len(gigs)} gigs x {args.candidates} candidates x {len(args.conds)} conditions x "
          f"{len(args.models)} models -> {len(jobs)} call(s) to make ({len(done)} already done)", flush=True)

    def run(job):
        g, p, c, m = job
        labels, render = CONDITIONS[c]
        rec = {"gig": g, "provider": p, "cond": c, "model": m}
        t = time.time()
        try:
            out = L.judge_prompt(render(query[g], doc[p]), labels, m)
            gen = out["generated"]
            rec.update(status="ok", gen_value=labels.index(gen) / (len(labels) - 1) if gen else None, **out)
        except Exception as e:
            rec.update(status="error", reason=str(e)[:300])
        rec["latency_s"] = round(time.time() - t, 3)
        return rec

    lock = threading.Lock()
    start, n_ok, n_err, recent_errs = time.time(), 0, 0, []
    with GRID_PATH.open("a", encoding="utf-8") as out, ThreadPoolExecutor(args.workers) as ex:
        futures = [ex.submit(run, j) for j in jobs]
        for i, fut in enumerate(as_completed(futures), 1):
            rec = fut.result()
            with lock:
                out.write(json.dumps(rec) + "\n")
                out.flush()
            ok = rec["status"] == "ok"
            n_ok += ok
            n_err += not ok
            recent_errs = (recent_errs + [not ok])[-100:]
            if i % 500 == 0 or i == len(jobs):
                rate = i / (time.time() - start)
                eta = (len(jobs) - i) / rate / 60 if rate else 0
                print(f"[{i}/{len(jobs)}] ok={n_ok} err={n_err} {rate:.1f} calls/s ETA {eta:.0f} min", flush=True)
            if len(recent_errs) == 100 and sum(recent_errs) > 50:
                print("[ABORT] >50% of the last 100 calls failed -- stopping; rerun to resume.", flush=True)
                ex.shutdown(wait=False, cancel_futures=True)
                break
    print(f"Done: ok={n_ok} err={n_err} in {(time.time() - start) / 60:.1f} min -> {GRID_PATH}")


if __name__ == "__main__":
    main()
