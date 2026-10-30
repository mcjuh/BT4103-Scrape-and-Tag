# -*- coding: utf-8 -*-
"""TEMPORARY. Brings the existing GLM trial records in line with the updated prompts and validator
(16OCT_TODO.md, section 6) without regenerating them. Delete this file and glm_trial/_pre_mend/ once the mended
files are committed and the report is clean.

    python glm/mend_tmp.py --dry-run          # counts only, nothing written, no GLM calls
    python glm/mend_tmp.py [--limit N]        # mend into glm_trial/_mended/ (resumable), report, samples
    python glm/mend_tmp.py --apply            # back up the live files to _pre_mend/, copy _mended/ over them

Stage 1 (dashes) is rule based (dashes.py) and needs no model. Stage 2 (verb mix) asks GLM to rewrite only the
opening verb of one or two achievements of a provider whose achievements all open with one kind of verb.
Each stage is checked per record against the original; a record that fails a check keeps its previous text and
is listed in mend_report.json. Nothing is edited in place: the live files change only under --apply, after a
backup that is never overwritten.
"""

import argparse
import csv
import difflib
import json
import random
import re
import shutil
import sys
import threading
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import dashes  # noqa: E402
import make  # noqa: E402
import run_trial  # noqa: E402
import validate  # noqa: E402

OUT = run_trial.OUT
MENDED = OUT / "_mended"
BACKUP = OUT / "_pre_mend"
FILES = ("gigs_by_id.json", "providers_by_file.json", "hirers.json", "providers.json", "pairs.json")
MAX_CHANGED_WORDS = 6  # per rewritten achievement
WORKERS = 8
_lock = threading.Lock()

REWRITE_PROMPT = """You are editing test data for a Singapore gig marketplace. Below are the achievements of a fictional freelance specialist whose mode of work is <<mode>>. Every one of them opens with <<have>> verb, which makes the profile read like a template.

ACHIEVEMENTS
<<achievements>>

Rewrite exactly <<n>> of them (pick the ones where it reads most naturally) so that the achievement opens with <<want>>. Change as few words as possible: the opening verb and only the words that must change with it. Keep the same facts, the same figures, the same kind of client and the same outcome. Each stays ONE sentence of at most 20 words. Leave the other achievements exactly as they are, word for word. Never use em dashes or en dashes.

Return ONLY a JSON object: {"achievements": [ ...all of them, in the same order... ]}"""
WANT = {"production": "a verb for hands-on work (Wrote, Built, Prepared, Ran, Drafted, Implemented, Configured)",
        "advisory": "a verb for advising or leading (Advised, Reviewed, Led, Recommended, Assessed, Guided)"}
HAVE = {"production": "a hands-on production", "advisory": "an advisory"}


def words(s) -> list:
    return re.findall(r"[a-z0-9$%']+", str(s).lower())


def changed_words(a: str, b: str) -> int:
    ops = difflib.SequenceMatcher(None, words(a), words(b)).get_opcodes()
    return sum(max(i2 - i1, j2 - j1) for tag, i1, i2, j1, j2 in ops if tag != "equal")


def load_inputs():
    gigs = run_trial.load_json(OUT / "gigs_by_id.json", {})
    provs = run_trial.load_json(OUT / "providers_by_file.json", {})
    gd, pd = {}, {}
    with (OUT / "design.csv").open(encoding="utf-8") as f:
        for r in csv.DictReader(f):
            r["words"], r["n"] = int(r["words"]), int(r["n"])
            r["notes"] = r["notes"] in ("True", "true", "1")
            gd[r["gig"]] = r
    with (OUT / "providers_design.csv").open(encoding="utf-8") as f:
        for r in csv.DictReader(f):
            r["years_experience"], r["target_grade"] = int(r["years_experience"]), int(r["target_grade"])
            pd[r["provider"]] = r
    return gigs, provs, gd, pd


# ---------------------------------------------------------------------------
# Checks: what must not change
# ---------------------------------------------------------------------------

def same_design(old: dict, new: dict, skip: tuple = ()) -> list:
    """Every field except those in skip has the same words (dashes may have become punctuation); identifiers,
    numbers and nulls are compared exactly."""
    errs = []
    if set(old) != set(new):
        errs.append(f"fields changed: {sorted(set(old) ^ set(new))}")
    for k in old:
        if k in skip or k not in new:
            continue
        a, b = old[k], new[k]
        if isinstance(a, (str, list, dict)) and k not in ("source_file", "hirer_ref", "replaces", "extracted_by_model"):
            if words(json.dumps(a, ensure_ascii=False)) != words(json.dumps(b, ensure_ascii=False)):
                errs.append(f"{k}: wording changed")
        elif a != b:
            errs.append(f"{k}: {a!r} -> {b!r}")
    return errs


def new_errors(old_errs: list, new_errs: list) -> list:
    """Errors the new record has that the old one did not (digits ignored, so "102 words" and "103 words" are one)."""
    kind = lambda e: re.sub(r"\d+", "#", e)  # noqa: E731
    return [e for e in new_errs if kind(e) not in {kind(o) for o in old_errs}]


def provider_check_rec(rec: dict) -> dict:
    return {k: v for k, v in rec.items() if k != "replaces"}


# ---------------------------------------------------------------------------
# Stage 1: dashes
# ---------------------------------------------------------------------------

def mend_gig(rec: dict, row: dict):
    """(record, errors, dash notes). errors empty = the dash-free record passes every check."""
    notes = []
    new = dashes.apply_to_record(rec, notes)
    if new == rec:
        return rec, [], notes
    errs = same_design(rec, new)
    errs += new_errors(validate.gig_errors(rec, row), validate.gig_errors(new, row))
    return (new, [], notes) if not errs else (rec, errs, notes)


def mend_dashes(rec: dict, row: dict, gig: dict):
    notes = []
    new = dashes.apply_to_record(rec, notes)
    if new == rec:
        return rec, [], notes
    errs = same_design(rec, new)
    errs += new_errors(validate.provider_errors(provider_check_rec(rec), row, gig),
                       validate.provider_errors(provider_check_rec(new), row, gig))
    return (new, [], notes) if not errs else (rec, errs, notes)


# ---------------------------------------------------------------------------
# Stage 2: verb mix
# ---------------------------------------------------------------------------

def mend_verbs(rec: dict, row: dict, gig: dict):
    """(record, tries, errors). Rewrites the opening verb of one or two achievements; rec is unchanged on failure."""
    ach = rec["achievements"]
    have = validate.single_verb_class(ach)
    want = "advisory" if have == "production" else "production"
    prompt = (make._fill(REWRITE_PROMPT, mode=row["mode_of_work"], have=HAVE[have], want=WANT[want],
                         n="one or two", achievements="\n".join(f"{i + 1}. {a}" for i, a in enumerate(ach))))
    baseline = validate.provider_errors(provider_check_rec(rec), row, gig)

    def build(reply):
        new_ach = reply.get("achievements")
        if not isinstance(new_ach, list) or len(new_ach) != len(ach) or not all(isinstance(a, str) for a in new_ach):
            raise ValueError(f"achievements must be a list of {len(ach)} strings")
        return dashes.apply_to_record({**rec, "achievements": [a.strip() for a in new_ach]})

    def check(new):
        errs = []
        diff = [i for i, (a, b) in enumerate(zip(ach, new["achievements"])) if a != b]
        if not 1 <= len(diff) <= 2:
            errs.append(f"change one or two achievements, not {len(diff)}; leave the rest word for word")
        for i in diff:
            a, b = ach[i], new["achievements"][i]
            if Counter(re.findall(r"\d+", a)) != Counter(re.findall(r"\d+", b)):
                errs.append(f'achievement {i + 1} must keep every figure of the original: "{a}"')
            if changed_words(a, b) > MAX_CHANGED_WORDS:
                errs.append(f"achievement {i + 1} changed more than {MAX_CHANGED_WORDS} words; change only the opening")
        if diff and not any(validate.verb_class(new["achievements"][i]) == want for i in diff):
            errs.append(f"a rewritten achievement must open with {WANT[want]}")
        errs += same_design(rec, new, skip=("achievements",))
        errs += new_errors(baseline, validate.provider_errors(provider_check_rec(new), row, gig))
        return errs

    return make._attempt(prompt, build, check)


# ---------------------------------------------------------------------------
# Run
# ---------------------------------------------------------------------------

def rows_for(provs: dict, gigs: dict, pd: dict, key: str):
    row = pd[provs[key].get("replaces") or key]
    return row, gigs[row["gig"]]


def run(args) -> None:
    gigs, provs, gd, pd = load_inputs()
    report = {"gigs": {"checked": len(gigs), "with_dashes": 0, "mended": 0, "rolled_back": {}},
              "providers": {"checked": len(provs), "with_dashes": 0, "dashes_mended": 0, "dashes_rolled_back": {},
                            "single_verb_class": 0, "verbs_mended": 0, "verbs_failed": {}}}

    new_gigs = {}
    for gid, rec in gigs.items():
        report["gigs"]["with_dashes"] += dashes.has_dash(rec)
        new, errs, _ = mend_gig(rec, gd[gid])
        new_gigs[gid] = new
        if errs:
            report["gigs"]["rolled_back"][gid] = errs
        elif new != rec:
            report["gigs"]["mended"] += 1

    new_provs, need_verbs = {}, []
    for key, rec in provs.items():
        row, gig = rows_for(provs, new_gigs, pd, key)
        report["providers"]["with_dashes"] += dashes.has_dash(rec)
        new, errs, _ = mend_dashes(rec, row, gig)
        new_provs[key] = new
        if errs:
            report["providers"]["dashes_rolled_back"][key] = errs
        elif new != rec:
            report["providers"]["dashes_mended"] += 1
        if validate.single_verb_class(new.get("achievements")):
            need_verbs.append(key)
    report["providers"]["single_verb_class"] = len(need_verbs)
    print(f"gigs: {report['gigs']['with_dashes']} with dashes, {report['gigs']['mended']} mended, "
          f"{len(report['gigs']['rolled_back'])} rolled back", flush=True)
    print(f"providers: {report['providers']['with_dashes']} with dashes, {report['providers']['dashes_mended']} mended, "
          f"{len(report['providers']['dashes_rolled_back'])} rolled back; {len(need_verbs)} need a verb fix", flush=True)
    if args.dry_run:
        return

    MENDED.mkdir(exist_ok=True)
    cache_path = MENDED / "verb_cache.json"
    cache = run_trial.load_json(cache_path, {})  # key -> mended record, or {"failed": errors}
    todo = [k for k in need_verbs if k not in cache][: args.limit or None]
    print(f"verb rewrites: {len(cache)} cached, {len(todo)} to make", flush=True)

    def one(key):
        row, gig = rows_for(provs, new_gigs, pd, key)
        rec, tries, errs = mend_verbs(new_provs[key], row, gig)
        run_trial.log_attempt("mend", key, tries, errs)
        print(f"  {key}: {'ok' if not errs else 'FAILED'} in {tries} {errs[:1] if errs else ''}", flush=True)
        return key, rec, errs

    with ThreadPoolExecutor(WORKERS) as ex:
        for k, (key, rec, errs) in enumerate(ex.map(one, todo), 1):
            cache[key] = {"failed": errs} if errs else rec
            if k % 10 == 0:
                run_trial.save_json(cache_path, cache)
    run_trial.save_json(cache_path, cache)

    before_verbs = {}
    for key in need_verbs:
        c = cache.get(key)
        if c is None:
            continue
        if "failed" in c and "source_file" not in c:
            report["providers"]["verbs_failed"][key] = c["failed"]
        else:
            before_verbs[key] = new_provs[key]
            new_provs[key] = c
            report["providers"]["verbs_mended"] += 1
    report["providers"]["verbs_not_attempted"] = [k for k in need_verbs if k not in cache]

    # Outputs in the shapes of crafted_gigs/: reuse run_trial.write_outputs against the mended dicts.
    gig_rows = [{"gig": g} for g in gd]
    prov_rows = {}
    for p in pd.values():
        prov_rows.setdefault(p["gig"], []).append(p)
    saved = run_trial.OUT
    run_trial.OUT = MENDED
    try:
        run_trial.write_outputs(gig_rows, prov_rows, new_gigs, new_provs)
    finally:
        run_trial.OUT = saved
    run_trial.save_json(MENDED / "gigs_by_id.json", new_gigs)
    run_trial.save_json(MENDED / "providers_by_file.json", new_provs)
    run_trial.save_json(MENDED / "mend_report.json", report)

    rng = random.Random(1)
    lines = ["# Dash changes (every changed string)\n"]
    for key, rec in {**gigs, **provs}.items():
        n = []
        dashes.apply_to_record(rec, n)
        for field, b, a in n:
            lines.append(f"- `{key}` {field}\n  - before: {b}\n  - after:  {a}")
    lines.append("\n# Verb rewrites (30 sampled)\n")
    for key in rng.sample(list(before_verbs), min(30, len(before_verbs))):
        for b, a in zip(before_verbs[key]["achievements"], new_provs[key]["achievements"]):
            if a != b:
                lines.append(f"- `{key}`\n  - before: {b}\n  - after:  {a}")
    (MENDED / "mend_samples.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"\nwrote {MENDED}: mend_report.json, mend_samples.md. verbs mended "
          f"{report['providers']['verbs_mended']}, failed {len(report['providers']['verbs_failed'])}, "
          f"not attempted {len(report['providers']['verbs_not_attempted'])}", flush=True)


def apply() -> None:
    if not (MENDED / "mend_report.json").exists():
        raise SystemExit("run the mend first (no _mended/mend_report.json)")
    if BACKUP.exists():
        raise SystemExit(f"{BACKUP} already exists; refusing to overwrite a backup")
    BACKUP.mkdir()
    for name in FILES:
        shutil.copy2(OUT / name, BACKUP / name)
    for name in FILES:
        shutil.copy2(MENDED / name, OUT / name)
    print(f"backed up to {BACKUP}; copied the mended files over the live ones")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--limit", type=int, default=0, help="at most N verb rewrites this run (resumable)")
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()
    apply() if args.apply else run(args)


if __name__ == "__main__":
    main()
