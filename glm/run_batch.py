# -*- coding: utf-8 -*-
"""GLM half of the comparison batch (100 gigs x 4 providers, one per grade) at low reasoning effort.

    python glm/run_batch.py              # make what is missing, then write hirers/providers/pairs.json
    python glm/run_batch.py --n 5        # a smoke test on the first 5 gigs

Output: data/output/compare_batch/glm/. Rerunning resumes: only a missing gig or provider is made, so a second run
retries the ones that failed validation. Generation only; nothing is graded here."""

import argparse
import json
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import batch_design  # noqa: E402
import llm  # noqa: E402
import make  # noqa: E402

OUT = batch_design.OUT / "glm"
WORKERS = 8
TRIES = 5  # low effort fails checks more often than default, but each retry costs seconds
_lock = threading.Lock()


def load(path, default):
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else default


def save(path, data):
    path.write_text(json.dumps(data, indent=1, ensure_ascii=False), encoding="utf-8")


def log(kind, key, tries, errors):
    line = {"time": datetime.now().isoformat(timespec="seconds"), "kind": kind, "key": key, "tries": tries,
            "ok": not errors, "errors": errors}
    with _lock, (OUT / "attempts.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps(line, ensure_ascii=False) + "\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=batch_design.N_GIGS)
    args = ap.parse_args()
    llm.REASONING_EFFORT = "low"
    make.TRIES = TRIES
    OUT.mkdir(parents=True, exist_ok=True)
    batch_design.save_design()
    rows = batch_design.gig_rows()[:args.n]
    prow = {g["gig"]: batch_design.provider_rows(g, "glm") for g in rows}
    t0 = time.time()

    gigs = load(OUT / "gigs_by_id.json", {})
    todo = [r for r in rows if r["gig"] not in gigs]
    print(f"gigs: {len(gigs)} done, {len(todo)} to make", flush=True)

    def one_gig(row):
        rec, tries, errors = make.make_gig(row)
        log("gig", row["gig"], tries, errors)
        print(f"  gig {row['gig']}: {'ok' if not errors else 'FAILED'} in {tries} {errors[:2] if errors else ''}", flush=True)
        return row["gig"], rec, errors

    with ThreadPoolExecutor(WORKERS) as ex:
        for fut in as_completed([ex.submit(one_gig, r) for r in todo]):
            gid, rec, errors = fut.result()
            if not errors:
                gigs[gid] = rec
    save(OUT / "gigs_by_id.json", gigs)

    provs = load(OUT / "providers_by_file.json", {})
    jobs = [(p, gigs[g["gig"]]) for g in rows if g["gig"] in gigs for p in prow[g["gig"]] if p["provider"] not in provs]
    print(f"providers: {len(provs)} done, {len(jobs)} to make", flush=True)

    def one_provider(job):
        p, gig = job
        rec, tries, errors = make.make_provider(p, gig)
        log("provider", p["provider"], tries, errors)
        print(f"  {p['provider']} (target {p['target_grade']}, {p['route']}): {'ok' if not errors else 'FAILED'} in {tries}"
              f"{' ' + str(errors[:2]) if errors else ''}", flush=True)
        return p["provider"], rec, errors

    with ThreadPoolExecutor(WORKERS) as ex:
        for k, fut in enumerate(as_completed([ex.submit(one_provider, j) for j in jobs]), 1):
            pid, rec, errors = fut.result()
            if not errors:
                provs[pid] = rec
            if k % 10 == 0:
                save(OUT / "providers_by_file.json", provs)
    save(OUT / "providers_by_file.json", provs)

    hirers, providers, pairs = [], [], {}
    for g in rows:
        if g["gig"] not in gigs:
            continue
        hirers.append(gigs[g["gig"]])
        for p in prow[g["gig"]]:
            if p["provider"] in provs:
                providers.append(provs[p["provider"]])
                pairs.setdefault(gigs[g["gig"]]["source_file"], []).append(p["provider"])
    save(OUT / "hirers.json", hirers)
    save(OUT / "providers.json", providers)
    save(OUT / "pairs.json", pairs)
    print(f"wrote {len(hirers)}/{len(rows)} gigs, {len(providers)}/{4 * len(rows)} providers in {time.time() - t0:.0f}s", flush=True)


if __name__ == "__main__":
    main()
