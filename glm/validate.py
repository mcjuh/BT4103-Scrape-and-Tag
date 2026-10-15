# -*- coding: utf-8 -*-
"""The checks of docs/GLM-TRIAL.md for GLM's gigs and providers. Each returns a list of error
messages (empty = pass); the messages go back to GLM on a retry."""

import json
import re
import sys
from pathlib import Path

from jsonschema import Draft7Validator

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "classifier_extractor"))
from extract import parse_duration_weeks  # noqa: E402

SCHEMAS = ROOT / "classifier_extractor" / "schemas"
_GIG_SCHEMA = Draft7Validator(json.loads((SCHEMAS / "ML_hirer_schema_v2.json").read_text(encoding="utf-8")))
_PROV_SCHEMA = Draft7Validator(json.loads((SCHEMAS / "ML_provider_schema_v2.json").read_text(encoding="utf-8")))

STOCK = ["comprehensive", "robust", "cutting-edge", "cutting edge", "end-to-end", "seamless", "leverage",
         "drive transformation", "seasoned", "we are seeking", "help us", "proven track record"]
COMPANY = re.compile(r"\b(Pte\.?\s*Ltd|Ltd\.?|Inc\.?|LLP|LLC|Corp\.?|Holdings|GmbH)\b", re.I)
BIG_NAMES = re.compile(r"\b(DBS|OCBC|UOB|Singtel|Grab|CapitaLand|Temasek|GIC|Keppel|SMRT|NTUC|Deloitte|PwC|KPMG|"
                       r"McKinsey|Accenture|Shopee|Lazada)\b")
PERSON = re.compile(r"\b(Mr|Ms|Mrs|Mdm|Dr|Prof)\.?\s+[A-Z][a-z]+")
NUMBER_WORDS = re.compile(r"(one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|twenty|thirty|forty|fifty|"
                          r"hundred|thousand|million|half|double|triple|dozen)", re.I)
MID_BANNED = ("senior", "lead", "principal", "partner", "director", "head")


def words(s) -> int:
    return len(str(s or "").split())


def _schema_errors(validator, record) -> list:
    return [f"schema: {'/'.join(map(str, e.absolute_path)) or 'record'}: {e.message}" for e in validator.iter_errors(record)]


def _names(text: str) -> list:
    errs = []
    m = COMPANY.search(text) or BIG_NAMES.search(text)
    if m:
        errs.append(f'names a company or firm ("{m.group(0)}"); describe the kind of organisation instead')
    if PERSON.search(text):
        errs.append("names a person; never name anyone")
    low = text.lower()
    errs += [f'uses the stock phrase "{p}"' for p in STOCK if p in low]
    return errs


def _runs(a: str, b: str, n: int = 6) -> bool:
    """True when the two texts share a run of n words."""
    def tok(s):
        return re.findall(r"[a-z0-9$%']+", s.lower())
    ta, tb = tok(a), tok(b)
    grams = {tuple(tb[i:i + n]) for i in range(len(tb) - n + 1)}
    return any(tuple(ta[i:i + n]) in grams for i in range(len(ta) - n + 1))


def gig_errors(rec: dict, row: dict) -> list:
    errs = _schema_errors(_GIG_SCHEMA, rec)
    desc = rec.get("short_description") or ""
    n = words(desc)
    if not 55 <= n <= 120 or abs(n - row["words"]) > 15:
        errs.append(f"short_description is {n} words; it must be within 15 of {row['words']} (and 55-120)")
    d, e = desc.find("Deliverable:"), desc.rfind("Engagement duration:")
    if d < 0 or e < d:
        errs.append('the "Deliverable:" sentence must come second-last and "Engagement duration:" last')
    elif re.search(r"[.!?]\s+\S", desc[e:].strip()):
        errs.append('nothing may follow the "Engagement duration:" sentence')
    elif re.search(r"[.!?]\s+\S", desc[d:e].strip()):
        errs.append('"Deliverable:" must be a single sentence directly before "Engagement duration:"')
    lo, hi = parse_duration_weeks(desc)
    if lo is None:
        errs.append('"Engagement duration:" must read like "Engagement duration: 3-4 weeks."')
    else:
        a, _, b = row["weeks"].partition("-")
        if (lo, hi) != (int(a), int(b or a)):
            errs.append(f'the engagement duration must be {row["weeks"]} weeks')
    title = rec.get("gig_title") or ""
    if not 3 <= words(title) <= 10:
        errs.append(f"gig_title is {words(title)} words; it must be 3-10")
    errs += _names(f"{title} {desc}")
    if re.search(r"\b(mid|senior|expert)[- ]level\b|\b\d+\+? years\b", desc, re.I):
        errs.append("do not state the seniority level or years of experience")
    return errs


def provider_errors(rec: dict, row: dict, gig: dict) -> list:
    errs = _schema_errors(_PROV_SCHEMA, rec)
    if rec.get("name") is not None:
        errs.append("name must be null")
    t = rec.get("title") or ""
    if not 2 <= words(t) <= 8:
        errs.append(f"title is {words(t)} words; it must be 2-8")
    if words(rec.get("about_headline")) > 20:
        errs.append("about_headline is over 20 words")
    if not 70 <= words(rec.get("about_bio")) <= 100:
        errs.append(f"about_bio is {words(rec.get('about_bio'))} words; it must be 70-100")
    for s in rec.get("services") or []:
        if not isinstance(s, dict):
            continue
        if not 40 <= words(s.get("service_detail")) <= 65:
            errs.append(f"service_detail \"{s.get('service_title')}\" is {words(s.get('service_detail'))} words; it must be 40-65")
        if not 3 <= words(s.get("service_title")) <= 10:
            errs.append(f"service_title \"{s.get('service_title')}\" must be 3-10 words")
    if len(rec.get("services") or []) != 1:
        errs.append("give exactly one service")
    if len(rec.get("credentials") or []) > 2:
        errs.append("give at most 2 credentials")
    errs += [f'achievement is {words(a)} words; keep each under 20' for a in rec.get("achievements") or [] if words(a) > 20]
    if not 25 <= words(rec.get("how_i_work")) <= 60:
        errs.append(f"how_i_work is {words(rec.get('how_i_work'))} words; it must be 25-60")
    if rec.get("years_experience") != row["years_experience"]:
        errs.append(f"years_experience must be exactly {row['years_experience']}")
    if row["seniority"] == "mid":
        for field in (t, rec.get("about_headline") or ""):
            hit = [w for w in MID_BANNED if re.search(rf"\b{w}\b", field, re.I)]
            if hit:
                errs.append(f"a mid-level title or headline must not contain {hit[0]!r}")
    ach = rec.get("achievements") or []
    if not 3 <= len(ach) <= 5:
        errs.append(f"achievements has {len(ach)} items; it must have 3-5")
    errs += [f'achievement without a figure: "{str(a)[:60]}"' for a in ach if not (re.search(r"\d", str(a)) or NUMBER_WORDS.search(str(a)))]
    if rec.get("rate") is not None or rec.get("availability") is not None:
        errs.append("rate and availability must be null")
    body = json.dumps({k: v for k, v in rec.items() if k not in ("source_file", "extracted_by_model", "tags")})
    errs += _names(body)
    gig_text = f"{gig.get('gig_title', '')} {gig.get('short_description', '')}"
    if _runs(body, gig_text):
        errs.append("shares a run of six words with the gig; reword")
    return errs
