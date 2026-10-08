# -*- coding: utf-8 -*-
"""
Tops up extract.py's records with the structured fields the ranker's Stage-2
features need (see docs/ranker_input_spec.md): budget, rate, seniority and
availability, on both sides.

    python run.py enrich                     # judge new/changed records, then rebuild the outputs
    python run.py enrich --no-llm            # rebuild the outputs from saved judgements only

Two steps, kept apart so the numbers can be regenerated for free:

1. JUDGE (LLM, one call per record, resumable). A pool model reads the
   record's text and picks categories on one shared rubric: seniority
   (mid/senior/expert) and price tier (lean/standard/premium) for gigs and
   providers alike, plus urgency and days per week for gigs. Stored in
   data/manifests/enrich.jsonl, keyed by source_file and a hash of the text
   it read, so a re-extracted record is judged again and nothing else is.

2. GENERATE (code, no LLM). rate_card.json turns those categories into
   numbers. A provider's rate_per_hour and a gig's budget band are drawn from
   the SAME S$/hour band for the same (seniority, price tier), so budget_fit
   compares like with like. Availability fields the text can't support
   (provider start date and capacity) are drawn from rate_card.json's
   distributions. Every draw is seeded by (file, seed), so reruns are stable
   and bumping `seed` regenerates everything.

All of it is synthetic by design (the source pages are case studies and
bios, which never state rates or availability). duration_weeks is the one
field read from the text: the "Engagement duration:" line extract_hirer.md
asks for, itself an LLM estimate.

The judge also places each record in SkillsFuture's framework
(data/reference/skillsfuture/: 39 sectors, 247 tracks): the sector and track
of the WORK for a gig, of the SERVICE for a provider. Code checks the pair
against the files.

Outputs, rebuilt in full each run (original columns first, then the new ones):
  data/output/hirers_enriched.csv     + budget_lo, budget_hi, seniority_needed, start_by,
                                        commitment, duration_weeks, sector, track, used_in_ml
  data/output/providers_enriched.csv  + rate_per_hour, available_from, capacity,
                                        availability, sector, track, used_in_ml
Provider seniority is judged and drives the rate bands, but is not written out: the
ranker learns it from the text.
--tag v2 reads/writes the *_v2 files instead (see use_tag).
Unknown values stay blank (null), never a filler: a record whose judgement
failed gets blanks until the next run retries it.
"""

import argparse
import csv
import datetime as dt
import hashlib
import json
import os
import random
import re
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT_DIR = SCRIPT_DIR.parent
DATA_DIR = ROOT_DIR / "data"
OUTPUT_DIR = DATA_DIR / "output"
PROMPTS_DIR = SCRIPT_DIR / "prompts"

MANIFEST_PATH = DATA_DIR / "manifests" / "enrich.jsonl"
RATE_CARD_PATH = SCRIPT_DIR / "rate_card.json"
# SkillsFuture sectors and tracks: the same files extract.py's tagging reads
# (sector.csv and track.csv match the ranker's pipeline/data_taxo/ copies).
TAXONOMY_DIR = DATA_DIR / "reference" / "skillsfuture"
PID_PATH = ROOT_DIR / "logs" / "enrich.pid"

# Same pool as classifier_extractor/llm_pool.py. Duplicated rather than
# imported: roles only talk to each other through data/ (as labeller/ does).
MODEL_POOL = ["qwen3.8:27b", "qwen3.6:35b", "qwen3-vl:32b"]

LEVELS = ["mid", "senior", "expert"]
TIERS = ["lean", "standard", "premium"]
URGENCIES = ["asap", "soon", "flexible"]

ENTITIES = {
    "HIRER": {
        "csv": OUTPUT_DIR / "hirers.csv",
        "out": OUTPUT_DIR / "hirers_enriched.csv",
        "prompt": "judge_hirer.md",
        "text_fields": ["hire_title", "hire_description", "hire_description_additional_notes", "industry"],
        "new_fields": ["budget_lo", "budget_hi", "seniority_needed", "start_by", "commitment", "duration_weeks",
                       "sector", "track", "used_in_ml"],
    },
    "PROVIDER": {
        "csv": OUTPUT_DIR / "providers.csv",
        "out": OUTPUT_DIR / "providers_enriched.csv",
        "prompt": "judge_provider.md",
        "text_fields": ["about_title", "about_description", "services_offered_title",
                        "services_offered_description", "relevant_experience", "industry"],
        "new_fields": ["rate_per_hour", "available_from", "capacity", "availability",
                       "sector", "track", "used_in_ml"],
    },
}


def _norm_name(s) -> str:
    """Loose key for matching a model's sector/track spelling to the list."""
    return re.sub(r"\s+", " ", str(s or "").replace("&", "and")).strip().lower()


def load_taxonomy() -> dict:
    """{sector name: [track names]}, in the files' order. Track names repeat
    across sectors ("Operations", "Project Management", ...), so a track only
    means something together with its sector."""
    with (TAXONOMY_DIR / "sector.csv").open(newline="", encoding="utf-8") as f:
        sectors = {r["sector_id"]: r["name"].strip() for r in csv.DictReader(f)}
    tree = {name: [] for name in sectors.values()}
    with (TAXONOMY_DIR / "track.csv").open(newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            tree[sectors[r["sector_id"]]].append(r["name"].strip())
    return tree


TAXONOMY = load_taxonomy()
TAXONOMY_TEXT = "\n".join(f"- {sector}: {'; '.join(tracks)}" for sector, tracks in TAXONOMY.items())
SECTOR_KEYS = {_norm_name(s): s for s in TAXONOMY}

for _cfg in ENTITIES.values():
    _cfg["template"] = (PROMPTS_DIR / _cfg["prompt"]).read_text(encoding="utf-8").strip()
    # A prompt or taxonomy edit changes the version, so every record is judged again under it.
    _cfg["prompt_version"] = hashlib.sha256(
        (_cfg["template"] + TAXONOMY_TEXT).encode("utf-8")).hexdigest()[:10]


def use_tag(tag: str) -> None:
    """Enrich a tagged extraction (extract.py --out-tag), e.g. "v2": read
    data/output/hirers_v2.csv, write data/output/hirers_v2_enriched.csv, and keep
    judgements in data/manifests/enrich_v2.jsonl, so they never leak into the untagged
    outputs (build_outputs falls back to a judgement of older text)."""
    global MANIFEST_PATH
    MANIFEST_PATH = DATA_DIR / "manifests" / f"enrich_{tag}.jsonl"
    for stem, cfg in (("hirers", ENTITIES["HIRER"]), ("providers", ENTITIES["PROVIDER"])):
        cfg["csv"] = OUTPUT_DIR / f"{stem}_{tag}.csv"
        cfg["out"] = OUTPUT_DIR / f"{stem}_{tag}_enriched.csv"

MAX_RETRIES = 4
RETRY_BACKOFF_S = 2  # doubles each retry
MAX_CONSECUTIVE_ERRORS = 5
MAX_COMPLETION_TOKENS = 300  # a judgement is ~40-80 tokens
NO_THINKING = {"chat_template_kwargs": {"enable_thinking": False}}  # as extract.py

load_dotenv(ROOT_DIR / ".env")
_client = None


def client() -> OpenAI:
    """Created on first use, so --no-llm runs without an API key."""
    global _client
    if _client is None:
        _client = OpenAI(base_url=os.environ["SOCLAAS_BASE_URL"], api_key=os.environ["SOCLAAS_API_KEY"],
                         timeout=60, max_retries=0)
    return _client


class Pacer:
    """Spaces requests evenly across worker threads (--rps), as extract.py does."""

    def __init__(self, rps: float):
        self.gap, self.next_at, self.lock = 1.0 / rps, time.monotonic(), threading.Lock()

    def wait(self):
        with self.lock:
            now = time.monotonic()
            slot = max(now, self.next_at)
            self.next_at = slot + self.gap
        time.sleep(max(0.0, slot - now))


_PACER = None


def model_for_file(filename: str) -> str:
    """Hashed like llm_pool.model_for_file, with its own stage salt."""
    digest = hashlib.sha256(f"enrich:{filename}".encode("utf-8")).hexdigest()
    return MODEL_POOL[int(digest, 16) % len(MODEL_POOL)]


# ---------------------------------------------------------------------------
# Step 1: judge
# ---------------------------------------------------------------------------

def record_text(entity_type: str, row: dict) -> str:
    return "\n".join(f"{k}: {row[k].strip()}" for k in ENTITIES[entity_type]["text_fields"]
                     if (row.get(k) or "").strip())


def text_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


def _parse_json(raw: str) -> dict:
    raw = re.sub(r"<think>.*?</think>", "", raw, flags=re.DOTALL | re.IGNORECASE)
    start, end = raw.find("{"), raw.rfind("}")
    if start == -1 or end < start:
        raise ValueError(f"no JSON object in response: {raw[:120]!r}")
    return json.loads(raw[start:end + 1], strict=False)


def _pick(data: dict, key: str, allowed: list) -> str:
    value = str(data.get(key, "")).strip().lower()
    if value not in allowed:
        raise ValueError(f"{key} must be one of {allowed}, got {data.get(key)!r}")
    return value


def _pick_bool(data: dict, key: str) -> bool:
    value = data.get(key)
    if isinstance(value, str):
        value = {"true": True, "false": False}.get(value.strip().lower())
    if not isinstance(value, bool):
        raise ValueError(f"{key} must be true or false, got {data.get(key)!r}")
    return value


def _pick_sector_track(data: dict) -> dict:
    """The model's sector and track, spelled as in the taxonomy. The track must
    be listed under that sector; anything else raises, so it's retried."""
    sector = SECTOR_KEYS.get(_norm_name(data.get("sector")))
    if sector is None:
        raise ValueError(f"sector not in the taxonomy: {data.get('sector')!r}")
    track = next((t for t in TAXONOMY[sector] if _norm_name(t) == _norm_name(data.get("track"))), None)
    if track is None:
        raise ValueError(f"track {data.get('track')!r} is not listed under sector {sector!r}")
    return {"sector": sector, "track": track}


def validate(entity_type: str, data: dict) -> dict:
    """A parsed reply -> the judgement to store. Raises on anything off-scale,
    so the caller retries it like an API error."""
    if entity_type == "HIRER":
        days = data.get("days_per_week")
        try:
            days = int(round(float(days)))
        except (TypeError, ValueError):
            raise ValueError(f"days_per_week must be a number, got {days!r}")
        return {"seniority": _pick(data, "seniority_needed", LEVELS),
                "price_tier": _pick(data, "price_tier", TIERS),
                "urgency": _pick(data, "urgency", URGENCIES),
                "days_per_week": min(5, max(1, days)),
                "used_in_ml": _pick_bool(data, "used_in_ml"),
                **_pick_sector_track(data),
                "reason": str(data.get("reason") or "")[:300]}
    score = data.get("price_score")
    try:
        score = int(round(float(score)))
    except (TypeError, ValueError):
        raise ValueError(f"price_score must be a number, got {score!r}")
    return {"seniority": _pick(data, "seniority", LEVELS),
            "price_tier": _pick(data, "price_tier", TIERS),
            "price_score": min(10, max(1, score)),
            "used_in_ml": _pick_bool(data, "used_in_ml"),
            **_pick_sector_track(data),
            "reason": str(data.get("reason") or "")[:300]}


def judge(entity_type: str, fname: str, text: str) -> dict:
    """One manifest record for this file: status ok with a judgement, or error."""
    cfg = ENTITIES[entity_type]
    model = model_for_file(fname)
    base = {"file": fname, "entity_type": entity_type, "model": model,
            "prompt_version": cfg["prompt_version"], "text_hash": text_hash(text),
            "timestamp": dt.datetime.now().isoformat(timespec="seconds")}
    prompt = cfg["template"].format(record=text, taxonomy=TAXONOMY_TEXT)
    last = None
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            if _PACER is not None:
                _PACER.wait()
            resp = client().chat.completions.create(
                model=model, messages=[{"role": "user", "content": prompt}],
                max_completion_tokens=MAX_COMPLETION_TOKENS, extra_body=NO_THINKING,
                response_format={"type": "json_object"})
            judgement = validate(entity_type, _parse_json(resp.choices[0].message.content or ""))
            return {**base, "status": "ok", "judgement": judgement}
        except Exception as e:
            last = e
            if attempt < MAX_RETRIES:
                time.sleep(RETRY_BACKOFF_S * 2 ** (attempt - 1))
    return {**base, "status": "error", "reason": str(last)[:300]}


def load_manifest() -> dict:
    """(entity_type, file) -> latest ok record."""
    done = {}
    if MANIFEST_PATH.exists():
        with MANIFEST_PATH.open(encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    r = json.loads(line)
                    if r.get("status") == "ok":
                        done[(r["entity_type"], r["file"])] = r
    return done


def load_rows(path: Path) -> tuple:
    if not path.exists():
        return [], []
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader.fieldnames or []), list(reader)


def is_current(rec: dict, entity_type: str, text: str) -> bool:
    return (rec is not None and rec["prompt_version"] == ENTITIES[entity_type]["prompt_version"]
            and rec["text_hash"] == text_hash(text))


def run_judging(args) -> None:
    done = load_manifest()
    jobs = []
    for entity_type, cfg in ENTITIES.items():
        if args.entity and entity_type != args.entity.upper():
            continue
        for row in load_rows(cfg["csv"])[1]:
            text = record_text(entity_type, row)
            if not is_current(done.get((entity_type, row["source_file"])), entity_type, text):
                jobs.append((entity_type, row["source_file"], text))
    if args.limit is not None:
        jobs = jobs[: args.limit]
    print(f"{len(jobs)} record(s) to judge ({len(done)} already judged)", flush=True)
    if not jobs:
        return

    consecutive = 0
    with MANIFEST_PATH.open("a", encoding="utf-8") as manifest, \
            ThreadPoolExecutor(max_workers=args.workers) as ex:
        futures = [ex.submit(judge, *job) for job in jobs]
        try:
            for i, fut in enumerate(as_completed(futures), 1):
                rec = fut.result()
                manifest.write(json.dumps(rec) + "\n")
                manifest.flush()
                if rec["status"] == "ok":
                    j = rec["judgement"]
                    extra = f" {j['urgency']} {j['days_per_week']}d/wk" if rec["entity_type"] == "HIRER" else ""
                    print(f"[{i}/{len(jobs)}] {rec['entity_type'].lower()}/{rec['file']} ({rec['model']}) -> "
                          f"{j['seniority']} {j['price_tier']}{extra} | {j['sector']} / {j['track']}", flush=True)
                    consecutive = 0
                else:
                    print(f"[{i}/{len(jobs)}] {rec['entity_type'].lower()}/{rec['file']} ({rec['model']}) -> "
                          f"ERROR ({rec['reason']})", flush=True)
                    consecutive += 1
                    if consecutive >= MAX_CONSECUTIVE_ERRORS:
                        print(f"\n[ABORT] {consecutive} errors in a row -- stopping; rerun to resume.", flush=True)
                        for f_ in futures:
                            f_.cancel()
                        break
        finally:
            ex.shutdown(wait=True, cancel_futures=True)


# ---------------------------------------------------------------------------
# Step 2: generate
# ---------------------------------------------------------------------------

DURATION_RE = re.compile(
    r"Engagement duration:?\s*(?:about|around|approximately|up to|~)?\s*"
    r"(\d+(?:\.\d+)?)(?:\s*(?:-|–|to)\s*(\d+(?:\.\d+)?))?\s*(day|week|month)s?", re.IGNORECASE)
WEEKS_PER_UNIT = {"day": 1 / 5, "week": 1, "month": 4.33}  # days are working days


def duration_weeks(description: str):
    """Midpoint of the "Engagement duration:" line, in weeks, or None."""
    m = DURATION_RE.search(description or "")
    if not m:
        return None
    lo = float(m.group(1))
    hi = float(m.group(2) or lo)
    return round((lo + hi) / 2 * WEEKS_PER_UNIT[m.group(3).lower()], 1)


def _round(x: float, step: int) -> int:
    return int(step * round(x / step))


def _rate_point(card: dict, rng: random.Random, level: str, tier: str) -> float:
    lo, hi = card["rate_bands"][level]
    a, b = card["tier_slice"][tier]
    return lo + (hi - lo) * rng.uniform(a, b)


def _date_after(card: dict, days: int) -> str:
    return (dt.date.fromisoformat(card["reference_date"]) + dt.timedelta(days=days)).isoformat()


TIER_SCORE = {"lean": 2, "standard": 5.5, "premium": 9}  # for judgements made before price_score


def ranked_provider_tiers(judgements: dict, card: dict) -> dict:
    """{file: tier}, assigned by rank within each seniority level: the bottom
    third lean, the middle standard, the top premium. The model's own tier
    calls ~85% of big-firm bios premium, so on its own it barely separates
    providers; ranking by price_score keeps the model's ordering while making
    each level's rates span its whole band. Ties break by a seeded draw."""
    tiers = {}
    for level in LEVELS:
        files = [f for f, j in judgements.items() if j["seniority"] == level]
        files.sort(key=lambda f: (judgements[f].get("price_score", TIER_SCORE[judgements[f]["price_tier"]]),
                                  random.Random(f"{card['seed']}:rank:{f}").random()))
        for i, f in enumerate(files):
            tiers[f] = TIERS[min(2, i * 3 // len(files))]
    return tiers


def generate(entity_type: str, fname: str, row: dict, judgement: dict, card: dict, tier: str = None) -> dict:
    """`tier` overrides the judgement's own price tier (providers: see
    ranked_provider_tiers)."""
    rng = random.Random(f"{card['seed']}:{entity_type}:{fname}")
    step = card["round_to"]
    if entity_type == "HIRER":
        dur = duration_weeks(row.get("hire_description"))
        if judgement is None:
            return {"duration_weeks": dur}
        # What the hirer can afford: a charity pays less than a bank for the same level.
        multiplier = card["industry_budget_multiplier"].get(row.get("industry") or "", 1.0)
        centre = _rate_point(card, rng, judgement["seniority"], judgement["price_tier"]) * multiplier
        urgency = judgement["urgency"]
        start_by = ("asap" if urgency == "asap"
                    else _date_after(card, rng.randint(*card["start_by_days"][urgency])))
        return {
            "budget_lo": _round(centre * rng.uniform(*card["budget_lo_factor"]), step),
            "budget_hi": _round(centre * rng.uniform(*card["budget_hi_factor"]), step),
            "seniority_needed": judgement["seniority"],
            "start_by": start_by,
            "commitment": judgement["days_per_week"],
            "duration_weeks": dur,
            # .get: judgements made before sector/track existed leave them blank
            "sector": judgement.get("sector"),
            "track": judgement.get("track"),
            "used_in_ml": judgement.get("used_in_ml"),
        }
    if judgement is None:
        return {}
    level = judgement["seniority"]
    rate = _round(_rate_point(card, rng, level, tier or judgement["price_tier"]), step)
    weights = card["capacity_days_per_week"][level]
    capacity = int(rng.choices(list(weights), weights=list(weights.values()), k=1)[0])
    if rng.random() < card["available_now_share"]:
        available_from, when = "now", "now"
    else:
        available_from = _date_after(card, rng.randint(*card["available_later_days"]))
        when = f"from {dt.date.fromisoformat(available_from):%d %b %Y}"
    return {
        "rate_per_hour": rate,
        "available_from": available_from,
        "capacity": capacity,
        "availability": f"Available {when}, {capacity} day{'s' if capacity > 1 else ''} a week",
        "sector": judgement.get("sector"),
        "track": judgement.get("track"),
        "used_in_ml": judgement.get("used_in_ml"),
    }


def build_outputs() -> None:
    card = json.loads(RATE_CARD_PATH.read_text(encoding="utf-8"))
    done = load_manifest()
    for entity_type, cfg in ENTITIES.items():
        header, rows = load_rows(cfg["csv"])
        if not rows:
            print(f"{cfg['csv'].name}: no rows, skipped", flush=True)
            continue
        fields = header + [f for f in cfg["new_fields"] if f not in header]
        tiers = {}
        if entity_type == "PROVIDER":
            tiers = ranked_provider_tiers(
                {r["source_file"]: done[(entity_type, r["source_file"])]["judgement"]
                 for r in rows if (entity_type, r["source_file"]) in done}, card)
        judged = 0
        tmp = cfg["out"].with_name(cfg["out"].name + ".tmp")
        with tmp.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
            writer.writeheader()
            for row in rows:
                rec = done.get((entity_type, row["source_file"]))
                # A judgement of an older version of the record's text still
                # beats blanks; the next judging run replaces it.
                judgement = rec["judgement"] if rec else None
                judged += judgement is not None
                extra = generate(entity_type, row["source_file"], row, judgement, card,
                                 tiers.get(row["source_file"]))
                writer.writerow({**row, **{k: ("" if v is None else v) for k, v in extra.items()}})
        tmp.replace(cfg["out"])
        print(f"{cfg['out'].name}: {len(rows)} rows, {judged} with a judgement "
              f"({len(rows) - judged} left blank)", flush=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--no-llm", action="store_true",
                        help="skip judging; rebuild the enriched CSVs from saved judgements and rate_card.json")
    parser.add_argument("--entity", choices=["hirer", "provider"], default=None, help="judge only one type")
    parser.add_argument("--limit", type=int, default=None, help="judge at most this many records")
    parser.add_argument("--workers", type=int, default=4, help="records to judge at once (default: 4)")
    parser.add_argument("--rps", type=float, default=1.0,
                        help="cap on requests/second across workers (SOCLAAS sustains ~1/s; default 1, 0 = no cap)")
    parser.add_argument("--tag", default=None,
                        help="enrich a tagged extraction (extract.py --out-tag): read data/output/hirers_TAG.csv and "
                             "providers_TAG.csv, write *_TAG_enriched.csv, judgements in data/manifests/enrich_TAG.jsonl")
    args = parser.parse_args()
    global _PACER
    _PACER = Pacer(args.rps) if args.rps else None
    if args.tag:
        use_tag(args.tag)

    if not args.no_llm:
        PID_PATH.parent.mkdir(exist_ok=True)
        PID_PATH.write_text(str(os.getpid()), encoding="utf-8")
        try:
            run_judging(args)
        finally:
            if PID_PATH.exists() and PID_PATH.read_text(encoding="utf-8").strip() == str(os.getpid()):
                PID_PATH.unlink()
    build_outputs()


if __name__ == "__main__":
    main()
