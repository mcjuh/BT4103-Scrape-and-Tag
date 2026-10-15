# -*- coding: utf-8 -*-
"""Gig and provider generation with GLM (docs/GLM-TRIAL.md, steps 2-4): prompt, parse, validate, and
retry with the error message, up to 3 tries."""

import re
import sys
from pathlib import Path

import llm
import validate
from design import LEVEL_HINT, MODE_HINT

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "classifier_extractor"))
import extract as X  # noqa: E402
import taxonomy  # noqa: E402

GIG_PROMPT = (Path(__file__).parent / "prompts" / "gig.md").read_text(encoding="utf-8")
PROV_PROMPT = (Path(__file__).parent / "prompts" / "provider.md").read_text(encoding="utf-8")
TRIES = 3

SENIORITY_RULE = {
    "mid": "A practitioner or consultant with no team leadership beyond a small project. Never put \"Senior\", \"Lead\", \"Principal\", \"Partner\", \"Director\" or \"Head\" in the title or headline.",
    "senior": "Has led a team or a function and advises management.",
    "expert": "A partner, director, former regulator or court-accepted expert. Never junior to anyone.",
}
MODE_RULE = {
    "execution": "Hands-on production is what they do and offer.",
    "advisory": "Judgement and recommendations for management is what they do and offer.",
    "mixed": "They both produce the work and advise on it.",
}


def _fill(template: str, **kw) -> str:
    for k, v in kw.items():
        template = template.replace(f"<<{k}>>", str(v))
    return template


def _attempt(prompt: str, build, check):
    """Up to TRIES calls; a failed check is sent back to the model with its messages.
    Returns (record, tries, errors); record is None when no reply could be parsed."""
    errors, note, record = [], "", None
    for t in range(1, TRIES + 1):
        try:
            reply = llm.chat_json(prompt + note)
            record = build(reply)
            errors = check(record)
        except Exception as e:  # noqa: BLE001
            errors = [f"{type(e).__name__}: {e}"]
        if not errors:
            return record, t, []
        note = ("\n\nYour previous reply failed these checks:\n- " + "\n- ".join(errors) +
                "\nWrite it again from scratch and fix every one. Return only the JSON.")
    return record, TRIES, errors


def _slug(title: str) -> str:
    return "-".join(re.sub(r"[^a-z0-9]+", " ", title.lower()).split()[:3]) or "gig"


def _build_gig(rec: dict, row: dict) -> dict:
    title = str(rec.get("gig_title") or "").strip()
    source_file = f"glm-gig__{row['n']:02d}_{_slug(title)}.md"
    desc = str(rec.get("short_description") or "").strip()
    lo, hi = X.parse_duration_weeks(desc)
    notes = rec.get("additional_notes")
    pairs = [] if row["specificity"] == "generic" else [(row["sector"], row["track"])]
    return {
        "source_file": source_file, "extracted_by_model": llm.MODEL, "hirer_ref": X.hirer_ref(source_file),
        "source_company": None, "source_company_team": None, "gig_title": title, "short_description": desc,
        "duration_weeks_min": lo, "duration_weeks_max": hi,
        "additional_notes": notes.strip() if isinstance(notes, str) and notes.strip() else None,
        "tags": taxonomy.nest(pairs, []),
    }


def make_gig(row: dict):
    """(record, tries, errors) for one gig design row."""
    generic = row["specificity"] == "generic"
    prompt = _fill(
        GIG_PROMPT, sector=row["sector"], track=row["track"], level=row["level"], level_hint=LEVEL_HINT[row["level"]],
        mode=row["mode"], mode_hint=MODE_HINT[row["mode"]], opening=row["opening"], words=row["words"],
        weeks=row["weeks"],
        generic_line=(f"\n- The ask is a GENERIC skill, not a specialism: {row['generic_task']}. The organisation is in this "
                      "field, but the work itself would be the same in any industry." if generic else ""),
        notes_line=("add one short constraint in additional_notes (a budget range in S$, a start date or a required qualification)"
                    if row["notes"] else "none"),
        notes_rule=("one short sentence: a budget range in S$, a start date or a required qualification."
                    if row["notes"] else "null."))
    return _attempt(prompt, lambda r: _build_gig(r, row), lambda rec: validate.gig_errors(rec, row))


def _build_provider(rec: dict, prow: dict) -> dict:
    keep = ("title", "credentials", "years_experience", "about_headline", "about_bio", "services", "achievements",
            "technical_proficiency", "how_i_work")
    out = {"source_file": prow["provider"], "extracted_by_model": llm.MODEL, "name": None}
    out.update({k: rec[k] for k in keep if k in rec})
    out.update({"availability": None, "rate": None})
    return out


def make_provider(prow: dict, gig: dict):
    """(record, tries, errors) for one provider design row against its gig record."""
    notes = f"\nNotes: {gig['additional_notes']}" if gig["additional_notes"] else ""
    prompt = _fill(
        PROV_PROMPT, gig=f"{gig['gig_title']}\n{gig['short_description']}{notes}",
        seniority=prow["seniority"], years=prow["years_experience"], seniority_rule=SENIORITY_RULE[prow["seniority"]],
        mode=prow["mode_of_work"], mode_rule=MODE_RULE[prow["mode_of_work"]], route=prow["route"],
        route_meaning=prow["route_meaning"],
        title_rule=("No \"Senior\", \"Lead\", \"Principal\", \"Partner\", \"Director\" or \"Head\"." if prow["seniority"] == "mid" else ""))
    return _attempt(prompt, lambda r: _build_provider(r, prow), lambda rec: validate.provider_errors(rec, prow, gig))
