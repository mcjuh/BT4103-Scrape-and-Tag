# -*- coding: utf-8 -*-
"""Claude half of the comparison batch. Claude writes the gigs and providers by hand (there is no Claude model on
the gateway), this tool shows the design rows, checks what was written with the same validators the GLM run uses,
and builds the files.

    python glm/claude_batch.py show 1-10        # design rows for gigs 1-10 (gig spec, then its 4 providers)
    python glm/claude_batch.py add draft.json   # validate and store; prints what was rejected and why
    python glm/claude_batch.py addtxt draft.txt # the same, from the compact text format (see parse_txt)
    python glm/claude_batch.py status
    python glm/claude_batch.py build            # hirers.json, providers.json, pairs.json

draft.json: {"gigs": {"G01": {"gig_title", "short_description", "additional_notes"}},
             "providers": {"01_a": {title, credentials, years_experience, about_headline, about_bio, services,
                                    achievements, technical_proficiency, how_i_work}}}
Output: data/output/compare_batch/claude/, same record shapes as the GLM run, extracted_by_model "crafted"."""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import batch_design  # noqa: E402
import make  # noqa: E402
import validate  # noqa: E402

X = make.X
OUT = batch_design.OUT / "claude"
ROWS = {g["gig"]: g for g in batch_design.gig_rows()}


def load(name, default):
    p = OUT / name
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else default


def save(name, data):
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / name).write_text(json.dumps(data, indent=1, ensure_ascii=False), encoding="utf-8")


def provider_row(key: str) -> dict:
    """Design row for a draft key such as "01_a"."""
    gid = f"G{key.split('_')[0]}"
    for p in batch_design.provider_rows(ROWS[gid], "crafted"):
        if p["provider"] == f"crafted-provider__{key}.md":
            return p
    raise KeyError(key)


def build_gig(gid: str, rec: dict) -> dict:
    out = make._build_gig(rec, ROWS[gid])
    out["source_file"] = out["source_file"].replace("glm-gig__", "crafted-gig__", 1)
    out["hirer_ref"] = X.hirer_ref(out["source_file"])
    out["extracted_by_model"] = "crafted"
    return out


def build_provider(key: str, rec: dict) -> dict:
    out = make._build_provider(rec, provider_row(key))
    out["extracted_by_model"] = "crafted"
    return out


def cmd_show(spec: str):
    a, _, b = spec.partition("-")
    for n in range(int(a), int(b or a) + 1):
        g = ROWS[f"G{n:02d}"]
        print(f"\n== G{n:02d}  {g['sector']} > {g['track']}  | {g['level']} {g['mode']} | ~{g['words']} words | {g['weeks']} weeks"
              f" | {'GENERIC: ' + g['generic_task'] if g['specificity'] == 'generic' else 'specific'} | notes: {'yes' if g['notes'] else 'no'}"
              f" | industry: {g['industry']}\n   opening: {g['opening']}")
        for p in batch_design.provider_rows(g, "crafted"):
            print(f"   {p['provider'].split('__')[1][:-3]}  grade {p['target_grade']} route {p['route']}  {p['years_experience']}y  {p['route_meaning']}")


def cmd_add(path: str):
    draft = json.loads(Path(path).read_text(encoding="utf-8"))
    gigs, provs = load("gigs_by_id.json", {}), load("providers_by_file.json", {})
    bad = 0
    for gid, rec in draft.get("gigs", {}).items():
        built = build_gig(gid, rec)
        errs = validate.gig_errors(built, ROWS[gid])
        if errs:
            bad += 1
            print(f"REJECT {gid}: {errs}")
        else:
            gigs[gid] = built
    for key, rec in draft.get("providers", {}).items():
        gid = f"G{key.split('_')[0]}"
        if gid not in gigs:
            print(f"REJECT {key}: gig {gid} not stored")
            bad += 1
            continue
        prow = provider_row(key)
        built = build_provider(key, rec)
        errs = validate.provider_errors(built, prow, gigs[gid])
        if errs:
            bad += 1
            print(f"REJECT {key}: {errs}")
        else:
            provs[prow["provider"]] = built
    save("gigs_by_id.json", gigs)
    save("providers_by_file.json", provs)
    print(f"stored: {len(gigs)} gigs, {len(provs)} providers; rejected this draft: {bad}")


def parse_txt(text: str) -> dict:
    """Compact draft format. A line "@G01" starts a gig (title:, desc:, notes:), "@01_a" starts a provider (title:,
    cred: a | b, headline:, bio:, svc: title || detail, ach: a || b || c, tech: Cat: s, s; Cat: s, s, how:).
    years_experience is filled in from the design row."""
    draft, cur, kind = {"gigs": {}, "providers": {}}, None, None
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("@"):
            key = line[1:]
            kind = "gigs" if key.startswith("G") else "providers"
            cur = draft[kind].setdefault(key, {})
            continue
        field, _, val = line.partition(":")
        val = val.strip()
        if kind == "gigs":
            cur[{"title": "gig_title", "desc": "short_description", "notes": "additional_notes"}[field]] = (
                None if field == "notes" and val.lower() in ("", "none", "null") else val)
        else:
            if field == "title":
                cur["title"] = val
            elif field == "cred":
                cur["credentials"] = [c.strip() for c in val.split("|") if c.strip()]
            elif field == "headline":
                cur["about_headline"] = val
            elif field == "bio":
                cur["about_bio"] = val
            elif field == "svc":
                t, _, d = val.partition("||")
                cur["services"] = [{"service_title": t.strip(), "service_detail": d.strip()}]
            elif field == "ach":
                cur["achievements"] = [a.strip() for a in val.split("||") if a.strip()]
            elif field == "tech":
                groups = []
                for g in val.split(";"):
                    c, _, sk = g.partition(":")
                    groups.append({"category": c.strip(), "skills": [x.strip() for x in sk.split(",") if x.strip()]})
                cur["technical_proficiency"] = groups
            elif field == "how":
                cur["how_i_work"] = val
            else:
                raise ValueError(f"unknown field {field!r} in {line[:40]}")
    for key, rec in draft["providers"].items():
        rec.setdefault("credentials", [])
        rec["years_experience"] = provider_row(key)["years_experience"]
    return draft


def cmd_addtxt(path: str):
    draft = parse_txt(Path(path).read_text(encoding="utf-8"))
    tmp = Path(path).with_suffix(".json")
    tmp.write_text(json.dumps(draft, ensure_ascii=False, indent=1), encoding="utf-8")
    cmd_add(str(tmp))
    tmp.unlink()


def cmd_status():
    gigs, provs = load("gigs_by_id.json", {}), load("providers_by_file.json", {})
    missing = [g for g in ROWS if g not in gigs]
    print(f"{len(gigs)}/100 gigs, {len(provs)}/400 providers; next missing gig: {missing[:1]}")


def cmd_build():
    gigs, provs = load("gigs_by_id.json", {}), load("providers_by_file.json", {})
    hirers, providers, pairs = [], [], {}
    for gid, g in ROWS.items():
        if gid not in gigs:
            continue
        hirers.append(gigs[gid])
        for p in batch_design.provider_rows(g, "crafted"):
            if p["provider"] in provs:
                providers.append(provs[p["provider"]])
                pairs.setdefault(gigs[gid]["source_file"], []).append(p["provider"])
    save("hirers.json", hirers)
    save("providers.json", providers)
    save("pairs.json", pairs)
    print(f"wrote {len(hirers)} gigs, {len(providers)} providers, {sum(map(len, pairs.values()))} pairs to {OUT}")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "status"
    {"show": lambda: cmd_show(sys.argv[2]), "add": lambda: cmd_add(sys.argv[2]), "addtxt": lambda: cmd_addtxt(sys.argv[2]), "status": cmd_status,
     "build": cmd_build}[cmd]()
