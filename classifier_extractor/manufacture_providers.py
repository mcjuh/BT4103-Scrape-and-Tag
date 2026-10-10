# -*- coding: utf-8 -*-
"""
Manufactures provider profiles for gigs the corpus has no good match for, and
adds them to the extracted dataset, clearly marked as synthetic.

    python run.py manufacture --counts data/archive/2026-10-06/hirer_relevance_counts.csv
    python run.py manufacture --counts ... --limit 4        # a trial: the first two gigs

Why: in the ranker's judging pools on the 29 Sep dataset (rubric_0_3.v2), 474
of 1,023 gigs had no provider graded 2 or 3, so the ranker has no positive
example to learn from for them. --counts is the per-gig count file built from
those judgments (columns source_file and v2_grade_2_or_3); every gig with a
count of 0 is a target. Each target is written against the gig's CURRENT
wording (data/output/hirers.jsonl, matched on source_file); a gig whose page
has no current gig is skipped.

Two providers per target gig, each in two steps:
1. A pool model (its own "manufacture" salt) invents a fictional specialist
   and writes their profile PAGE (prompts/manufacture_provider_v2.md): "direct"
   is aimed at grade 3 (core expertise is exactly this work), "adjacent" at
   grade 2 (same field, neighbouring focus). The model first reads the gig's
   seniority and mode of work as rubric_01.v5 defines them, and both variants
   match the gig on those terms, so content fit is the only thing that varies.
   v1 of the prompt (manufacture_provider.md) is kept for the providers it made.
2. That page goes through extract.py's own provider extraction (facts pass,
   style pass, Singapore check, SkillsFuture tags), so the record has the same
   shape, style rolls and checks as one extracted from a crawled page.

They are written to data/output/providers.jsonl and providers.csv (and
providers.json is rebuilt), marked so they can always be told apart or
filtered out:
- source_file is "synthetic-provider__<target gig's hirer_ref>__<variant>.md"
  (not "synthetic__": extract.py treats the part before "__" as the
  publisher's name and masks or rejects that word in the text);
- extracted_by_model is "synthetic:<generator model>/<extraction model>".
classify_label stays PROVIDER so the ranker import keeps them; the industry
columns are copied from the target gig. They have not been graded: whether
they score 2 or 3 is only known once the judge runs over them.

Progress is in data/manifests/manufacture.jsonl, one line per attempt with the
generated page, so a rerun skips providers already written and retries the
rest. data/output/manufactured_providers.txt lists every written one and is
rebuilt at the end of each run.
"""

import argparse
import csv
import json
import os
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path

import extract as X
import taxonomy
from llm_pool import model_for_file

PROMPT = (X.PROMPTS_DIR / "manufacture_provider_v2.md").read_text(encoding="utf-8").strip()
PROMPT_VERSION = "manufacture_provider.v2"  # v1 (manufacture_provider.md) made the records with no prompt_version
GIG_LEVELS = ("mid", "senior", "expert")  # rubric_01.v5's seniority levels
GIG_MODES = ("execution", "advisory", "mixed")  # and its modes of work
MANIFEST_PATH = X.MANIFESTS_DIR / "manufacture.jsonl"
LIST_PATH = X.OUTPUT_DIR / "manufactured_providers.txt"
PID_PATH = X.LOGS_DIR / "manufacture.pid"
PREFIX = "synthetic-provider__"
MIN_PAGE_WORDS = 120

# variant -> (grade it is aimed at under rubric_01.v5, who the generator invents). The prompt makes
# both match the gig's seniority and mode of work, so only the content fit differs.
VARIANTS = {
    "direct": (3, "A specialist whose core expertise is exactly this kind of work on this kind of "
                  "problem, built up in the same industry or setting. A client reading the profile "
                  "would shortlist them for this gig straight away."),
    "adjacent": (2, "A specialist in the same field who is a good but not a perfect fit: their core "
                    "skills clearly apply, but their main focus is a neighbouring sub-specialism, or "
                    "the same kind of work done mostly in a different sector. They match the gig's "
                    "level and mode of work, so the content alone is what keeps them from being the "
                    "first choice."),
}

csv.field_size_limit(10**9)


def load_targets(counts_path: Path) -> tuple:
    """([(current gig record, its hirers.csv row)], number of zero-count gigs in the file)."""
    with counts_path.open(newline="", encoding="utf-8") as f:
        zero = [r["source_file"] for r in csv.DictReader(f) if r["v2_grade_2_or_3"].strip() == "0"]
    gigs = {}
    with X.HIRERS_JSONL.open(encoding="utf-8") as f:
        for line in f:
            if line.strip():
                rec = json.loads(line)
                gigs[rec["source_file"]] = rec  # the latest record per page wins, as in export_json
    with X.HIRERS_CSV.open(newline="", encoding="utf-8") as f:
        rows = {r["source_file"]: r for r in csv.DictReader(f)}
    return [(gigs[sf], rows.get(sf, {})) for sf in zero if sf in gigs], len(zero)


def provider_file(gig: dict, variant: str) -> str:
    return f"{PREFIX}{gig['hirer_ref']}__{variant}.md"


def gig_text(gig: dict) -> str:
    parts = [f"Title: {gig['gig_title']}", gig["short_description"]]
    if gig.get("additional_notes"):
        parts.append(f"Notes: {gig['additional_notes']}")
    return "\n".join(parts)


def check_reply(data: dict) -> tuple:
    """(page, gig_level, gig_mode) from the generator's JSON; ValueError makes the call retry."""
    page = data.get("profile_page")
    if not isinstance(page, str) or len(page.split()) < MIN_PAGE_WORDS:
        raise ValueError(f"profile_page missing or under {MIN_PAGE_WORDS} words")
    level, mode = data.get("gig_level"), data.get("gig_mode")
    if level not in GIG_LEVELS:
        raise ValueError(f"gig_level {level!r} is not one of {GIG_LEVELS}")
    if mode not in GIG_MODES:
        raise ValueError(f"gig_mode {mode!r} is not one of {GIG_MODES}")
    return page.strip(), level, mode


def generate_page(fname: str, gig: dict, variant: str) -> tuple:
    """(profile page text, gig_level, gig_mode, generator model, usage)."""
    model = model_for_file(fname, "manufacture")
    content = PROMPT.format(variant_instruction=VARIANTS[variant][1], gig=gig_text(gig))
    (page, level, mode), usage, _ = X._call_with_retries(model, content, check_reply)
    return page, level, mode, model, usage


def make_provider(gig: dict, gig_row: dict, variant: str) -> tuple:
    """Makes one provider. Returns (manifest record, (CSV row, v2 record) or None, log line).
    Writes nothing itself, so several can run at once."""
    fname = provider_file(gig, variant)
    timestamp = datetime.now().isoformat(timespec="seconds")
    base = {"file": fname, "variant": variant, "aimed_grade": VARIANTS[variant][0],
            "target_gig": gig["source_file"], "target_hirer_ref": gig["hirer_ref"],
            "target_title": gig["gig_title"], "prompt_version": PROMPT_VERSION, "timestamp": timestamp}
    start = time.perf_counter()
    try:
        page, level, mode, generator, gen_usage = generate_page(fname, gig, variant)
        base.update(generator=generator, generator_usage=gen_usage, gig_level=level, gig_mode=mode, page=page)
        model = model_for_file(fname, "extract")
        base["model"] = model
        doc, usage, meta = X.extract_entity(page, "PROVIDER", model, fname)
    except X.ContentRejected as e:
        record = {**base, "status": "rejected", "reason": f"content check, after retries: {e}"}
        return record, None, f"{fname} -> REJECTED ({record['reason']})"
    except Exception as e:
        record = {**base, "status": "error", "reason": f"api_error: {e}"}
        return record, None, f"{fname} -> ERROR ({e})"

    elapsed = round(time.perf_counter() - start, 2)
    base.update(usage=usage, elapsed=elapsed, **meta)
    if doc is None:
        record = {**base, "status": "rejected", "reason": "extraction returned {} for the generated page"}
        return record, None, f"{fname} ({generator}) -> REJECTED ({record['reason']})"
    ok, reason = X.quality_check("PROVIDER", doc)
    if not ok:
        return {**base, "status": "rejected", "reason": reason}, None, f"{fname} ({generator}) -> REJECTED ({reason})"

    doc["extracted_by_model"] = f"synthetic:{generator}/{model}"
    try:
        rec = X.finalize_record("PROVIDER", doc, meta.get("tags"))
    except Exception as e:
        record = {**base, "status": "error", "reason": f"api_error: {e}"}
        return record, None, f"{fname} -> ERROR ({e})"
    row = {**X.flat_columns("PROVIDER", rec), "source_file": fname, "classify_label": "PROVIDER",
           "extracted_at": timestamp, "time_taken_by_model": elapsed,
           **{k: gig_row.get(k) for k in X.INDUSTRY_FIELDS},
           **taxonomy.csv_columns(meta.get("tags")),
           **{f"roll_{k}": v for k, v in (meta.get("rolls") or {}).items()}}
    record = {**base, "status": "written", "title": rec.get("title"), "headline": rec.get("about_headline")}
    return record, (row, rec), f"{fname} ({generator}) -> WRITTEN ({rec.get('title')}) for: {gig['gig_title']}"


def load_progress() -> dict:
    """file -> latest manifest record."""
    latest = {}
    if MANIFEST_PATH.exists():
        with MANIFEST_PATH.open(encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    rec = json.loads(line)
                    latest[rec["file"]] = rec
    return latest


def write_list(n_zero: int, n_targets: int) -> None:
    """Rebuilds data/output/manufactured_providers.txt from the manifest."""
    written = sorted((r for r in load_progress().values() if r.get("status") == "written"),
                     key=lambda r: (r["target_hirer_ref"], r["variant"]))
    per_gig = {}
    for r in written:
        per_gig[r["target_gig"]] = per_gig.get(r["target_gig"], 0) + 1
    lines = [
        "# Manufactured provider profiles: synthetic, not extracted from a real page",
        "# Made by classifier_extractor/manufacture_providers.py. Targets: gigs with no provider graded 2 or 3",
        "# in the ranker's judging pools on the 29 Sep dataset (rubric_0_3.v2), written against each gig's",
        "# current wording. Two per gig: 'direct' aimed at grade 3, 'adjacent' at grade 2 (rubric_01.v5),",
        "# both at the gig_level / gig_mode the generator read from the gig (blank: made by prompt v1). Not yet graded.",
        "# Each is in data/output/providers.jsonl / providers.csv under its source_file; the generated",
        "# profile page it was extracted from is in data/manifests/manufacture.jsonl.",
        f"# {len(written)} providers for {len(per_gig)} gigs ({n_targets} of {n_zero} zero-count gigs have a "
        f"current gig; {sum(1 for n in per_gig.values() if n < 2)} of them have only one provider so far)",
        "#",
        "\t".join(["source_file", "variant", "aimed_grade", "target_hirer_ref", "target_gig_source_file",
                   "target_gig_title", "prompt_version", "gig_level", "gig_mode", "generator_model", "extractor_model",
                   "provider_title", "provider_headline"]),
    ]
    for r in written:
        lines.append("\t".join(str(v or "").replace("\t", " ").replace("\n", " ") for v in (
            r["file"], r["variant"], r["aimed_grade"], r["target_hirer_ref"], r["target_gig"],
            r["target_title"], r.get("prompt_version", "manufacture_provider.v1"), r.get("gig_level"),
            r.get("gig_mode"), r.get("generator"), r.get("model"), r.get("title"), r.get("headline"))))
    LIST_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"{LIST_PATH.name}: {len(written)} providers for {len(per_gig)} gigs", flush=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--counts", type=Path, required=True,
                        help="per-gig count file; gigs with v2_grade_2_or_3 == 0 are the targets")
    parser.add_argument("--limit", type=int, default=None, help="make at most this many providers this run")
    parser.add_argument("--workers", type=int, default=4, help="providers to make at once (default: 4)")
    parser.add_argument("--rps", type=float, default=1.0,
                        help="cap on requests/second across workers (SOCLAAS sustains ~1/s; default 1, 0 = no cap)")
    args = parser.parse_args()
    X._PACER = X.Pacer(args.rps) if args.rps else None
    X.check_csv_headers()

    targets, n_zero = load_targets(args.counts)
    done = {f for f, r in load_progress().items() if r.get("status") == "written"}
    jobs = [(g, row, v) for g, row in targets for v in VARIANTS if provider_file(g, v) not in done]
    if args.limit is not None:
        jobs = jobs[:args.limit]
    print(f"{n_zero} gigs with no provider graded 2 or 3; {len(targets)} have a current gig; "
          f"{len(done)} providers already written; {len(jobs)} to make now", flush=True)

    X.LOGS_DIR.mkdir(exist_ok=True)
    PID_PATH.write_text(str(os.getpid()), encoding="utf-8")
    consecutive_errors = 0
    try:
        with MANIFEST_PATH.open("a", encoding="utf-8") as manifest, \
                ThreadPoolExecutor(max_workers=max(1, args.workers)) as ex:
            futures = [ex.submit(make_provider, g, row, v) for g, row, v in jobs]
            for i, fut in enumerate(as_completed(futures), 1):
                record, out, line = fut.result()
                if out is not None:  # CSV and .jsonl before the manifest, so the manifest never claims an unwritten row
                    row, rec = out
                    X.append_csv_row(X.PROVIDERS_CSV, X.csv_fields("PROVIDER"), row)
                    X.append_jsonl(X.PROVIDERS_JSONL, rec)
                manifest.write(json.dumps(record, ensure_ascii=False) + "\n")
                manifest.flush()
                print(f"[{i}/{len(jobs)}] {line}", flush=True)
                consecutive_errors = consecutive_errors + 1 if record["status"] == "error" else 0
                if consecutive_errors >= X.MAX_CONSECUTIVE_ERRORS:
                    print(f"\n[ABORT] {consecutive_errors} errors in a row -- stopping. Fix the underlying "
                          f"issue and rerun; written providers are kept and skipped next time.", flush=True)
                    for f in futures:
                        f.cancel()
                    break
    finally:
        if PID_PATH.exists() and PID_PATH.read_text(encoding="utf-8").strip() == str(os.getpid()):
            PID_PATH.unlink()  # leave another instance's PID file alone
    write_list(n_zero, len(targets))
    X.export_json()


if __name__ == "__main__":
    main()
