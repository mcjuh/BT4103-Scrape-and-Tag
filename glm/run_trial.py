# -*- coding: utf-8 -*-
"""Runs the GLM pilot of docs/GLM-TRIAL.md: design, make, validate, retry, write, grade, regenerate, compare.

    python glm/run_trial.py                    # the pilot: 5 gigs x 8 providers
    python glm/run_trial.py --n 10             # more gigs
    python glm/run_trial.py --skip-grade       # generate only
    python glm/run_trial.py --report-only      # just the comparison tables

Reruns reuse what is already in data/output/glm_trial/ (a gig or provider is only made if missing), so a
stopped run resumes. Every attempt is logged in attempts.jsonl.
"""

import argparse
import csv
import json
import statistics
import subprocess
import sys
import threading
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import design  # noqa: E402
import make  # noqa: E402
import validate  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "output" / "glm_trial"
BASE = ROOT / "data" / "output" / "crafted_gigs"
GRADE_LOG = ROOT / "data" / "manifests" / "gig_grades.jsonl"
GRADE_VERSION = "rubric_01.v5"
GRADER = "qwen3.8:27b"
WORKERS = 8  # --workers
SAVE_EVERY = 10
_lock = threading.Lock()


def load_json(path: Path, default):
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else default


def save_json(path: Path, data) -> None:
    path.write_text(json.dumps(data, indent=1, ensure_ascii=False), encoding="utf-8")


def save_csv(path: Path, rows: list) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)


def log_attempt(kind: str, key: str, tries: int, errors: list) -> None:
    line = {"time": datetime.now().isoformat(timespec="seconds"), "kind": kind, "key": key, "tries": tries,
            "ok": not errors, "errors": errors}
    with _lock, (OUT / "attempts.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps(line, ensure_ascii=False) + "\n")


# ---------------------------------------------------------------------------
# Generate
# ---------------------------------------------------------------------------

def generate(n: int) -> None:
    gig_rows = design.design_gigs(n)
    prov_rows = {g["gig"]: design.design_providers(g) for g in gig_rows}
    save_csv(OUT / "design.csv", [{k: v for k, v in g.items()} for g in gig_rows])
    save_csv(OUT / "providers_design.csv", [p for ps in prov_rows.values() for p in ps])

    gigs = load_json(OUT / "gigs_by_id.json", {})
    todo = [r for r in gig_rows if r["gig"] not in gigs]
    print(f"gigs: {len(gigs)} done, {len(todo)} to make", flush=True)

    def one_gig(row):
        rec, tries, errors = make.make_gig(row)
        log_attempt("gig", row["gig"], tries, errors)
        print(f"  gig {row['gig']}: {'ok' if not errors else 'FAILED'} in {tries} tr{'y' if tries == 1 else 'ies'} {errors[:2] if errors else ''}", flush=True)
        return row["gig"], rec, errors

    with ThreadPoolExecutor(WORKERS) as ex:
        for k, fut in enumerate(as_completed([ex.submit(one_gig, r) for r in todo]), 1):
            gid, rec, errors = fut.result()
            if not errors:
                gigs[gid] = rec
            if k % SAVE_EVERY == 0:
                save_json(OUT / "gigs_by_id.json", gigs)
    save_json(OUT / "gigs_by_id.json", gigs)

    provs = load_json(OUT / "providers_by_file.json", {})
    jobs = [(p, gigs[g["gig"]]) for g in gig_rows if g["gig"] in gigs for p in prov_rows[g["gig"]]
            if p["provider"] not in provs and not any(v.get("replaces") == p["provider"] for v in provs.values())]
    print(f"providers: {len(provs)} done, {len(jobs)} to make", flush=True)

    def one_provider(job):
        prow, gig = job
        rec, tries, errors = make.make_provider(prow, gig)
        log_attempt("provider", prow["provider"], tries, errors)
        print(f"  {prow['provider']} (target {prow['target_grade']}, {prow['route']}): {'ok' if not errors else 'FAILED'} in {tries}"
              f"{' ' + str(errors[:2]) if errors else ''}", flush=True)
        return prow["provider"], rec, errors

    with ThreadPoolExecutor(WORKERS) as ex:
        for k, fut in enumerate(as_completed([ex.submit(one_provider, j) for j in jobs]), 1):
            pid, rec, errors = fut.result()
            if not errors:
                provs[pid] = rec
            if k % SAVE_EVERY == 0:
                save_json(OUT / "providers_by_file.json", provs)
    save_json(OUT / "providers_by_file.json", provs)
    write_outputs(gig_rows, prov_rows, gigs, provs)


def write_outputs(gig_rows, prov_rows, gigs, provs) -> None:
    """hirers.json, providers.json and pairs.json from what has been made (the shapes of crafted_gigs/)."""
    hirers = [gigs[g["gig"]] for g in gig_rows if g["gig"] in gigs]
    providers, pairs = [], {}
    for g in gig_rows:
        if g["gig"] not in gigs:
            continue
        for p in prov_rows[g["gig"]]:
            rec = provs.get(p["provider"])
            if rec:
                providers.append(rec)
                pairs.setdefault(gigs[g["gig"]]["source_file"], []).append(rec["source_file"])
    save_json(OUT / "hirers.json", hirers)
    save_json(OUT / "providers.json", providers)
    save_json(OUT / "pairs.json", pairs)
    print(f"wrote {len(hirers)} gigs, {len(providers)} providers, {sum(map(len, pairs.values()))} pairs to {OUT}", flush=True)


# ---------------------------------------------------------------------------
# Grade, regenerate
# ---------------------------------------------------------------------------

def grade() -> None:
    cmd = [sys.executable, str(ROOT / "run.py"), "grade", "--gigs-csv", str(OUT / "hirers.json"),
           "--providers-csv", str(OUT / "providers.json"), "--pairs", str(OUT / "pairs.json")]
    subprocess.run(cmd, cwd=ROOT, check=True)


def grades(prefix: str) -> dict:
    """{(gig source_file, provider source_file): grade} for this grader and rubric, latest line winning."""
    out = {}
    for line in GRADE_LOG.read_text(encoding="utf-8").splitlines():
        r = json.loads(line)
        if r.get("status") == "ok" and r["model"] == GRADER and r["prompt_version"] == GRADE_VERSION \
                and r["provider_id"].startswith(prefix):
            out[(r["gig_id"], r["provider_id"])] = r["grade"]
    return out


def regenerate_far(n: int) -> bool:
    """One regeneration for each provider whose Qwen grade is 2 or more from the target. The new record is
    saved under a new id (-r1) so the grader sees it as a new pair; the old one is kept in replaced.json."""
    gig_rows = design.design_gigs(n)
    prov_rows = {g["gig"]: design.design_providers(g) for g in gig_rows}
    gigs = load_json(OUT / "gigs_by_id.json", {})
    provs = load_json(OUT / "providers_by_file.json", {})
    replaced = load_json(OUT / "replaced.json", [])
    got = grades("glm-provider__")
    todo = []
    for g in gig_rows:
        gig = gigs.get(g["gig"])
        for p in prov_rows[g["gig"]]:
            rec = provs.get(p["provider"])
            if gig and rec and (gig["source_file"], p["provider"]) in got \
                    and abs(got[(gig["source_file"], p["provider"])] - p["target_grade"]) >= 2:
                todo.append((p, gig, rec, got[(gig["source_file"], p["provider"])]))
    print(f"regenerating {len(todo)} provider(s) graded 2+ from target", flush=True)
    if not todo:
        return False

    def one(job):
        prow, gig, old, qgrade = job
        rec, tries, errors = make.make_provider(prow, gig)
        log_attempt("provider-regen", prow["provider"], tries, errors)
        return prow, old, qgrade, rec, errors

    with ThreadPoolExecutor(WORKERS) as ex:
        for prow, old, qgrade, rec, errors in ex.map(one, todo):
            if errors:
                print(f"  {prow['provider']}: regeneration FAILED {errors[:2]}; kept the first", flush=True)
                continue
            new_id = prow["provider"].replace(".md", "-r1.md")
            rec["source_file"] = new_id
            rec["replaces"] = prow["provider"]
            replaced.append({"provider": prow["provider"], "target_grade": prow["target_grade"], "qwen_grade": qgrade, "record": old})
            del provs[prow["provider"]]
            provs[new_id] = rec
    save_json(OUT / "providers_by_file.json", provs)
    save_json(OUT / "replaced.json", replaced)
    # rebuild the outputs with the replacements in place of the originals
    swap = {r["replaces"]: r for r in provs.values() if r.get("replaces")}
    providers, pairs = [], {}
    for g in gig_rows:
        gig = gigs.get(g["gig"])
        for p in prov_rows[g["gig"]]:
            rec = provs.get(p["provider"]) or next((v for v in swap.values() if v["replaces"] == p["provider"]), None)
            if gig and rec:
                providers.append({k: v for k, v in rec.items() if k != "replaces"})
                pairs.setdefault(gig["source_file"], []).append(rec["source_file"])
    save_json(OUT / "providers.json", providers)
    save_json(OUT / "pairs.json", pairs)
    return True


# ---------------------------------------------------------------------------
# Compare
# ---------------------------------------------------------------------------

def profile_words(p: dict) -> int:
    n = validate.words(p.get("about_bio")) + validate.words(p.get("how_i_work"))
    n += sum(validate.words(s.get("service_detail")) for s in p.get("services") or [])
    n += sum(validate.words(a) for a in p.get("achievements") or [])
    return n


def table(pairs: list, title: str) -> None:
    """pairs: [(target, qwen_grade)]. Rows are targets, columns Qwen grades."""
    print(f"\n{title}  (rows: target grade, columns: Qwen grade; n={len(pairs)})")
    c = Counter(pairs)
    print("  target |    0    1    2    3 | exact  within 1")
    for t in (3, 2, 1, 0):
        row = [c[(t, q)] for q in range(4)]
        tot = sum(row) or 1
        print(f"     {t}   | " + " ".join(f"{x:4d}" for x in row) + f" | {row[t] / tot:5.0%}  {sum(row[max(0, t - 1):t + 2]) / tot:5.0%}")
    n = len(pairs) or 1
    print(f"  all    | exact {sum(c[(t, t)] for t in range(4)) / n:.0%}, "
          f"2+ away {sum(v for (t, q), v in c.items() if abs(t - q) >= 2)}")


def report(n: int) -> None:
    gig_rows = design.design_gigs(n)
    gigs = load_json(OUT / "gigs_by_id.json", {})
    provs = load_json(OUT / "providers_by_file.json", {})
    attempts = [json.loads(l) for l in (OUT / "attempts.jsonl").read_text(encoding="utf-8").splitlines()] \
        if (OUT / "attempts.jsonl").exists() else []
    latest = {}
    for a in attempts:  # a rerun of a failed key replaces its earlier line
        if a["kind"] in ("gig", "provider"):
            latest[a["key"]] = a
    first = list(latest.values())
    print(f"\n=== validation: {sum(a['ok'] for a in first)}/{len(first)} outputs passed within 3 tries "
          f"({Counter(a['tries'] for a in first if a['ok'])} by tries used) ===")
    for a in first:
        if not a["ok"]:
            print(f"  FAILED {a['key']}: {a['errors'][:3]}")

    prov_design = {r["provider"]: r for r in csv.DictReader((OUT / "providers_design.csv").open(encoding="utf-8"))}
    got = grades("glm-provider__")
    gig_file = {k: v["source_file"] for k, v in gigs.items()}
    g_pairs = []
    for pid, rec in provs.items():
        orig = rec.get("replaces") or pid
        d = prov_design.get(orig)
        g = next((x for x in gig_file.values() if x.startswith(f"glm-gig__{int(orig.split('__')[1].split('_')[0]):02d}_")), None)
        if d and g and (g, pid) in got:
            g_pairs.append((int(d["target_grade"]), got[(g, pid)]))
    table(g_pairs, "GLM pilot")

    b_design = list(csv.DictReader((BASE / "providers_design.csv").open(encoding="utf-8")))
    b_got = grades("crafted-provider__")
    gmap = {f"{int(r['gig'][1:]):02d}": r["source_file"] for r in csv.DictReader((BASE / "design.csv").open(encoding="utf-8"))}
    b_pairs = []
    for d in b_design:
        num = d["provider"].split("__")[1][:2]
        if (gmap[num], d["provider"]) in b_got:
            b_pairs.append((int(d["target_grade"]), b_got[(gmap[num], d["provider"])]))
    table(b_pairs, "Base set (Claude-written, 800)")

    print("\n=== style: GLM vs base ===")
    base = json.loads((BASE / "providers_crafted.json").read_text(encoding="utf-8"))
    for label, recs in (("GLM", list(provs.values())), ("base", base)):
        w = [profile_words(p) for p in recs]
        a = [len(p.get("achievements") or []) for p in recs]
        c = [len(p.get("credentials") or []) for p in recs]
        print(f"  {label:5s} n={len(recs):3d}  words mean {statistics.mean(w):.0f} (sd {statistics.pstdev(w):.0f}, "
              f"range {min(w)}-{max(w)})  achievements {statistics.mean(a):.1f}  credentials {statistics.mean(c):.1f}")
    by_grade = {}
    for pid, rec in provs.items():
        d = prov_design.get(rec.get("replaces") or pid)
        if d:
            by_grade.setdefault(int(d["target_grade"]), []).append(profile_words(rec))
    print("  GLM words by target grade: " + ", ".join(f"{g}: {statistics.mean(v):.0f}" for g, v in sorted(by_grade.items(), reverse=True)))
    gw = [validate.words(g["short_description"]) for g in gigs.values()]
    bw = [validate.words(g["short_description"]) for g in json.loads((BASE / "hirers_crafted.json").read_text(encoding="utf-8"))]
    print(f"  gig words: GLM mean {statistics.mean(gw):.0f} ({min(gw)}-{max(gw)}), base mean {statistics.mean(bw):.0f} ({min(bw)}-{max(bw)})")


def main() -> None:
    global WORKERS
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--n", type=int, default=5, help="number of gigs (default: 5, the pilot)")
    ap.add_argument("--workers", type=int, default=WORKERS, help="parallel GLM calls (default: %(default)s)")
    ap.add_argument("--skip-grade", action="store_true")
    ap.add_argument("--report-only", action="store_true")
    args = ap.parse_args()
    WORKERS = args.workers
    OUT.mkdir(parents=True, exist_ok=True)
    if not args.report_only:
        generate(args.n)
        if not args.skip_grade:
            grade()
            if regenerate_far(args.n):
                grade()
    report(args.n)


if __name__ == "__main__":
    main()
