# -*- coding: utf-8 -*-
"""
Grades the ranker's judging pools 0-3, producing the training labels for its
Stage-2 reranker (cross-encoder + LambdaMART).

Input is the ranker fork's pipeline/data_sat/ folder, built there by
import_scrape_and_tag.py (gigs + providers from this repo's docs/ CSVs) and
build_judging_pools_sat.py (per gig: RRF/BM25/dense top candidates + randoms).

The prompt (prompts/rubric_0_3.md) carries the ranker's own 0-3 rubric
(llm_judgments.py), minus the budget/seniority clauses our data has no fields
for, so these grades mean what its synthetic grades mean. Scoring is label.py's:
the log-likelihood of each grade token at the answer position, so every call
keeps the full grade distribution; the grade is its argmax.

One model grades every pair. The 100x100 run showed the pool's models disagree
far more than prompts do (llama3.1:8b rated 82% of pairs relevant, the Qwens
<=6%; llama has since been dropped from the pool), and training labels have to
mean the same thing across gigs.

    py -3 labeller/judge_pools.py --model qwen3.6:35b --sample 20        # pilot
    py -3 labeller/judge_pools.py --model qwen3.6:35b                    # every gig
    py -3 labeller/judge_pools.py --model qwen3.6:35b --export           # -> ranker label files

--prompt v2 (prompts/rubric_0_3_v2.md) also grades the practical terms -- budget vs
rate, seniority, start date and days per week -- from the structured fields of the
enriched import (hirers_enriched.csv / providers_enriched.csv). Those fields are
appended to the gig and profile text shown to the model.

For a deadline: --order random grades gigs in a seeded random order, so a run
stopped early leaves a random sample of fully graded gigs rather than the first N
by id, and --export-every N re-exports the label files every N calls.

--prompt v3 (prompts/rubric_01_v3.md) grades the same content and terms as v2 but
asks for a continuous 0-1 score (two decimals) instead of a 0-3 grade. Its anchor
bands sit on the 0-3 grades' rounding cutoffs, so the exported grade is
round(score * 3). The score is smoothed like label.py's expected relevance: the
generated number with its leading digit and tenths digit replaced by their
expectations under the answer-position logprobs (Qwen tokenises digits one at a
time), falling back to the parsed number when the output has another shape.
ground_truth_llm.json then carries round(score * 100) rather than 0/33/67/100,
which the ranker's grade_from_score() maps back to the same grade.

Reruns skip pairs already graded by that model and prompt, so a stopped run resumes.
"""

import argparse
import json
import math
import random
import re
import time
from collections import Counter
from datetime import datetime
from pathlib import Path

from label import GIG_FIELDS, MODEL_POOL, PROFILE_FIELDS, _bare, _describe, complete, judge_prompt

SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_DATA = SCRIPT_DIR.parent.parent / "ranker" / "pipeline" / "data_sat"
# --prompt -> (template file, prompt_version recorded with every judgment)
PROMPTS = {"v1": ("rubric_0_3.md", "rubric_0_3.v1"), "v2": ("rubric_0_3_v2.md", "rubric_0_3.v2"),
           "v3": ("rubric_01_v3.md", "rubric_01.v3")}
CONTINUOUS = {"v3"}  # prompts answered with a 0-1 score, not a 0-3 grade
WITH_TERMS = {"v2", "v3"}  # prompts shown the budget/seniority/availability fields
GRADES = ["0", "1", "2", "3"]
SCORE_RE = re.compile(r"(?<![\d.])(1(?:\.0+)?|0?\.\d+|0)(?![\d.])")
MAX_CONSECUTIVE_ERRORS = 5


def load(data_dir: Path, name: str):
    return json.loads((data_dir / name).read_text(encoding="utf-8"))


def load_ok(path: Path, model: str, version: str) -> dict:
    """(hire_id, provider_id) -> record, for this model's successful calls."""
    out = {}
    if path.exists():
        with path.open(encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    r = json.loads(line)
                    if r.get("status") == "ok" and r["model"] == model and r["prompt_version"] == version:
                        out[(r["hire_id"], r["provider_id"])] = r
    return out


def _date(v) -> str:
    try:
        return datetime.strptime(v, "%Y-%m-%d").strftime("%d %b %Y").lstrip("0")
    except (TypeError, ValueError):
        return v


def gig_terms(h: dict) -> str:
    lines = []
    if h.get("budget_lo") is not None and h.get("budget_hi") is not None:
        lines.append(f"Budget: S${h['budget_lo']:g}-{h['budget_hi']:g} per hour")
    if h.get("seniority_needed"):
        lines.append(f"Seniority needed: {h['seniority_needed']}")
    if h.get("start_by"):
        lines.append("Start: as soon as possible" if h["start_by"] == "asap"
                     else f"Start by: {_date(h['start_by'])}")
    if h.get("commitment") is not None:
        dur = f" for about {h['duration_weeks']:g} weeks" if h.get("duration_weeks") is not None else ""
        lines.append(f"Time needed: {h['commitment']} days a week{dur}")
    return "\n".join(lines)


def provider_terms(p: dict) -> str:
    lines = []
    if p.get("rate_per_hour") is not None:
        lines.append(f"Rate: S${p['rate_per_hour']:g} per hour")
    if p.get("seniority"):
        lines.append(f"Seniority: {p['seniority']}")
    if p.get("available_from"):
        start = "now" if p["available_from"] == "now" else f"from {_date(p['available_from'])}"
        days = f", {p['capacity']} days a week" if p.get("capacity") is not None else ""
        lines.append(f"Availability: {start}{days}")
    return "\n".join(lines)


def render(template: str, prompt: str, h: dict, p: dict) -> str:
    query, document = _describe(h, GIG_FIELDS), _describe(p, PROFILE_FIELDS)
    if prompt in WITH_TERMS:
        query = "\n".join(x for x in [query, gig_terms(h)] if x)
        document = "\n".join(x for x in [document, provider_terms(p)] if x)
    return template.format(query=query, document=document)


def _digit_probs(tok, digits: str):
    """Probability of each of `digits` at one output token, renormalised over
    the top-k candidates that are one of them; None if none of them appear."""
    mass = [sum(math.exp(c.logprob) for c in tok.top_logprobs if _bare(c.token) == d) for d in digits]
    total = sum(mass)
    return [m / total for m in mass] if total > 0 else None


def score_prompt(prompt: str, model: str) -> dict:
    """Score one rendered prompt whose answer is a 0-1 number."""
    response = complete(prompt, model)
    choice = response.choices[0]
    text = choice.message.content or ""
    m = SCORE_RE.search(text)
    if not m:
        raise ValueError(f"no 0-1 score in output {text!r}")
    parsed = float(m.group(1))

    # Expected score when the answer is "0" "." d h, one digit per token:
    # P(1) * 1.0 + P(0) * (E[tenths] / 10 + h / 100). The hundredths digit stays
    # the generated one -- its distribution is only known on the greedy path.
    toks = [t for t in (choice.logprobs.content if choice.logprobs and choice.logprobs.content else [])
            if _bare(t.token) or t.token.strip() == "."]
    lead = tenths = None
    if len(toks) >= 4 and [t.token.strip() for t in toks[:2]] == ["0", "."] \
            and _bare(toks[2].token).isdigit() and len(_bare(toks[2].token)) == 1 \
            and _bare(toks[3].token).isdigit() and len(_bare(toks[3].token)) == 1:
        lead = _digit_probs(toks[0], "01")
        tenths = _digit_probs(toks[2], "0123456789")
    if lead and tenths:
        hundredths = int(_bare(toks[3].token)) / 100
        score = lead[1] + lead[0] * (sum(p * d / 10 for d, p in enumerate(tenths)) + hundredths)
        scoring = "logprobs"
    else:
        score, scoring = parsed, "parsed"

    usage = {}
    if response.usage:
        usage = {"prompt_tokens": response.usage.prompt_tokens, "completion_tokens": response.usage.completion_tokens}
    return {
        "generated": text.strip(),
        "parsed_score": parsed,
        "score": round(score, 4),
        "lead_probs": [round(p, 4) for p in lead] if lead else None,
        "tenths_probs": [round(p, 4) for p in tenths] if tenths else None,
        "scoring": scoring,
        "usage": usage,
    }


def grade_of(score: float) -> int:
    """0-1 score -> 0-3 grade, the same rounding the ranker's grade_from_score()
    applies to ground_truth_llm.json's 0-100 values."""
    return int(round(round(score * 100) * 3 / 100))


def pilot_gigs(pools: dict, n: int, seed: int) -> list:
    return sorted(random.Random(seed).sample(sorted(pools, key=int), n), key=int)


def parse_gigs(spec: str, pools: dict) -> list:
    """"1-100" or "3,7,10-12" -> those hire_ids that have a pool, in id order."""
    ids = set()
    for part in spec.split(","):
        lo, _, hi = part.strip().partition("-")
        ids.update(range(int(lo), int(hi or lo) + 1))
    return [h for h in sorted(pools, key=int) if int(h) in ids]


def export(data_dir: Path, done: dict, pools: dict):
    """Writes the two label files the ranker's features.py / evaluate.py read:
    llm_judgments_merged.json  {hire_id: {provider_id: grade}}  incl. zeros (training)
    ground_truth_llm.json      {hire_id: {provider_id: 0/33/67/100}}  grade > 0 only (evaluation)
                               (a 0-1 score instead exports as round(score * 100))
    Only gigs whose whole pool is graded are exported -- a half-graded pool
    would make its ungraded candidates look like confirmed negatives."""
    merged, gt = {}, {}
    for hid, pids in pools.items():
        if all((hid, str(p)) in done for p in pids):
            recs = {str(p): done[(hid, str(p))] for p in pids}
            merged[hid] = {p: r["grade"] for p, r in recs.items()}
            gt[hid] = {p: round(r["score"] * 100) if "score" in r else round(r["grade"] * 100 / 3)
                       for p, r in recs.items() if r["grade"] > 0}
    (data_dir / "llm_judgments_merged.json").write_text(json.dumps(merged, indent=1), encoding="utf-8")
    (data_dir / "ground_truth_llm.json").write_text(json.dumps(gt, indent=1), encoding="utf-8")
    dist = Counter(g for row in merged.values() for g in row.values())
    print(f"exported {len(merged)}/{len(pools)} fully graded gigs, {sum(dist.values())} pairs; "
          f"grades {dict(sorted(dist.items()))}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True, choices=MODEL_POOL)
    ap.add_argument("--data-dir", type=Path, default=DEFAULT_DATA,
                    help="the ranker fork's pipeline/data_sat/ (default: sibling checkout)")
    ap.add_argument("--sample", type=int, default=0, help="grade only N seeded-random gigs (pilot)")
    ap.add_argument("--gigs", default=None, help='grade only these hire_ids, e.g. "1-100" or "3,7,10-12"')
    ap.add_argument("--seed", type=int, default=4103)
    ap.add_argument("--export", action="store_true", help="write the ranker's label files and exit")
    # SOCLAAS sustains ~1 rps; unpaced, the pilot drew a 429 every ~90 calls
    ap.add_argument("--rps", type=float, default=1.0, help="max calls per second (default: 1)")
    ap.add_argument("--prompt", choices=sorted(PROMPTS), default="v1",
                    help="v1 = content fit only; v2 = content + budget/seniority/availability; "
                         "v3 = v2's criteria as a continuous 0-1 score")
    ap.add_argument("--order", choices=["id", "random"], default="id",
                    help="gig order; random (seeded by --seed) makes a partial run a random sample")
    ap.add_argument("--export-every", type=int, default=0,
                    help="re-export the label files every N calls (0 = only with --export)")
    args = ap.parse_args()
    template_file, version = PROMPTS[args.prompt]
    template = (SCRIPT_DIR / "prompts" / template_file).read_text(encoding="utf-8").strip()

    hirers = {str(h["hire_id"]): h for h in load(args.data_dir, "hirers.json")}
    providers = {str(p["provider_id"]): p for p in load(args.data_dir, "providers.json")}
    pools = load(args.data_dir, "judging_pools.json")
    out_path = args.data_dir / "judgments.jsonl"
    done = load_ok(out_path, args.model, version)

    if args.export:
        export(args.data_dir, done, pools)
        return

    if args.gigs:
        gigs = parse_gigs(args.gigs, pools)
    else:
        gigs = pilot_gigs(pools, args.sample, args.seed) if args.sample else sorted(pools, key=int)
    if args.order == "random":
        random.Random(args.seed).shuffle(gigs)
    jobs = [(hid, str(pid)) for hid in gigs for pid in pools[hid] if (hid, str(pid)) not in done]
    print(f"{len(gigs)} gigs, {sum(len(pools[h]) for h in gigs)} pairs; {len(jobs)} call(s) to make "
          f"on {args.model}, prompt {version}", flush=True)

    consecutive_errors = 0
    next_call = 0.0
    with out_path.open("a", encoding="utf-8") as out:
        for i, (hid, pid) in enumerate(jobs, 1):
            record = {"hire_id": hid, "provider_id": pid, "model": args.model,
                      "prompt_version": version,
                      "timestamp": datetime.now().isoformat(timespec="seconds")}
            prompt = render(template, args.prompt, hirers[hid], providers[pid])
            time.sleep(max(0.0, next_call - time.time()))
            t0 = time.time()
            next_call = t0 + 1.0 / args.rps
            try:
                if args.prompt in CONTINUOUS:
                    r = score_prompt(prompt, args.model)
                    grade = grade_of(r["score"])
                    record.update(status="ok", grade=grade, score=r["score"], parsed_score=r["parsed_score"],
                                  lead_probs=r["lead_probs"], tenths_probs=r["tenths_probs"],
                                  generated=r["generated"], scoring=r["scoring"],
                                  usage=r["usage"], elapsed=round(time.time() - t0, 2))
                    shown = f"score {r['score']:.3f} (said {r['parsed_score']:.2f})"
                else:
                    r = judge_prompt(prompt, GRADES, args.model)
                    grade = max(range(len(GRADES)), key=lambda g: r["probs"][g])
                    record.update(status="ok", grade=grade, expected_grade=r["expected_relevance"],
                                  probs=r["probs"], generated=r["generated"], scoring=r["scoring"],
                                  usage=r["usage"], elapsed=round(time.time() - t0, 2))
                    shown = f"(E={r['expected_relevance']:.2f})"
                consecutive_errors = 0
                done[(hid, pid)] = record
                print(f"[{i}/{len(jobs)}] gig {hid:>4} <- {pid:>4}  grade {grade}  {shown}", flush=True)
            except Exception as e:
                consecutive_errors += 1
                record.update(status="error", reason=str(e)[:300])
                print(f"[{i}/{len(jobs)}] gig {hid:>4} <- {pid:>4}  ERROR ({e})", flush=True)
            out.write(json.dumps(record) + "\n")
            out.flush()
            if args.export_every and i % args.export_every == 0:
                export(args.data_dir, done, pools)
            if consecutive_errors >= MAX_CONSECUTIVE_ERRORS:
                print(f"\n[ABORT] {consecutive_errors} errors in a row -- fix and rerun; "
                      f"graded pairs are kept and skipped.", flush=True)
                break

    done = load_ok(out_path, args.model, version)
    if args.export_every:
        export(args.data_dir, done, pools)
    dist = Counter(r["grade"] for (h, _), r in done.items() if h in set(gigs))
    print(f"\nDone. grades over these gigs: {dict(sorted(dist.items()))}")


if __name__ == "__main__":
    main()
