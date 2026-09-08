import argparse
import json
import os
import shutil
import time
from datetime import datetime
from pathlib import Path
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url=os.environ["SOCLAAS_BASE_URL"],
    api_key=os.environ["SOCLAAS_API_KEY"],
    timeout=50,
)
MODEL = os.environ["SOCLAAS_MODEL"]

TRIAGE_PROMPT = """
You are classifying a single raw HTML page into exactly one category.

Return ONLY valid JSON in this exact format:
{"label": "INDIVIDUAL_PROFILE" | "GIG" | "IGNORE" | "UNCERTAIN", "reason": "one short phrase, max 15 words"}

### INDIVIDUAL_PROFILE
The page's primary subject is ONE specific, named person, and the content is substantially
about that person's own career, experience, skills, or work history; written as their
personal bio, profile, or portfolio. Required, not just present:
- A specific individual's full name is the primary subject of the page (not a company, a
  team, or a list of multiple names).
- The page is describing THAT person's own roles, background, expertise, or achievements —
  not what a company, team, or client project achieved.
- Reads as "about me" / an individual bio / a personal portfolio — not "about us" / a case
  study / a deal summary.

KEY RULE: a page about what a COMPANY or TEAM did — a deal, a case study, a client
engagement, a project outcome — is IGNORE even if it names or quotes an individual, unless
that person's own career and background (not the deal or project) is the actual subject of
the page.
Example: a case study titled "Firm X advises on a $9B restructuring" is IGNORE. The subject
is the deal and the firm's role in it, not any one person's career, even if a partner is
named or quoted in it.

### GIG
The page is a request for work — a job posting, task listing, or brief with a defined scope,
deliverable, budget, and/or deadline for someone to fulfill.
Signals: budget/rate, deadline/timeline, "looking for", skills required for a task (not a
person's own skills), proposal/application language.

### IGNORE
Anything that is not one person's own bio page and not a specific work request. This
includes, but is not limited to:
- Company/team "About Us," leadership, or "meet the team" pages listing multiple people.
- Marketing, service-description, landing, or category/marketplace pages.
- Press releases, case studies, or deal/project summaries (see KEY RULE above).
- Recruiting, "join us," careers, or generic hiring-marketing pages.
- Legal, contact, privacy, or other boilerplate pages.
- 404/error pages, empty pages, cookie banners, login walls.
If the page is generic, company-level, deal-level, or not centered on one named individual's
own career, it is IGNORE — do not default to UNCERTAIN just because the page is low-value.

### UNCERTAIN
Use only when the page genuinely contains a substantial INDIVIDUAL_PROFILE (per the rule
above) that ALSO carries explicit GIG signals on the same page (e.g. a personal portfolio
that also states a rate, budget, or "hire me"), or you truly cannot decide after applying
the rules above. Do not use UNCERTAIN as a catch-all for pages that are simply generic or
low-value; those are IGNORE.

Do not extract, summarize, or comment on anything beyond the label and reason.
""".strip()


def clean_html(html_content: str) -> str:
    soup = BeautifulSoup(html_content, "html.parser")
    for tag in soup(["script", "style", "nav", "footer", "header", "svg", "noscript", "iframe"]):
        tag.decompose()
    return str(soup)


def parse_label(raw_output: str) -> dict:
    """Pull {label, reason} out of the model's response. Never raises — anything
    that doesn't parse cleanly gets routed to UNCERTAIN for manual review."""
    text = raw_output.strip()
    if text.startswith("```"):
        text = text.strip("`")
        if text.lower().startswith("json"):
            text = text[4:]
        text = text.strip()

    try:
        data = json.loads(text)
        label = str(data.get("label", "UNCERTAIN")).upper()
        reason = data.get("reason", "")
        if label not in {"INDIVIDUAL_PROFILE", "GIG", "IGNORE", "UNCERTAIN"}:
            label, reason = "UNCERTAIN", f"unrecognized label: {label}"
        return {"label": label, "reason": reason}
    except (json.JSONDecodeError, AttributeError) as e:
        return {"label": "UNCERTAIN", "reason": f"parse_error: {e}"}


def query_soc_llm(html_path: Path, prompt: str):
    html_content = clean_html(html_path.read_text(encoding="utf-8"))

    start = time.perf_counter()
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": f"{prompt}\n\nHTML:\n```html\n{html_content}\n```"}],
    )
    elapsed = time.perf_counter() - start

    usage = {}
    if response.usage:
        usage = {
            "prompt_tokens": response.usage.prompt_tokens,
            "completion_tokens": response.usage.completion_tokens,
        }
    return response.choices[0].message.content, elapsed, usage


def load_manifest(manifest_path: Path) -> dict:
    """Load already-processed files so re-runs skip them instead of re-billing the API."""
    done = {}
    if manifest_path.exists():
        with manifest_path.open("r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                record = json.loads(line)
                done[record["file"]] = record
    return done


def run_triage(input_dir: Path, output_dir: Path, prompt: str) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = output_dir / "manifest.jsonl"
    already_done = load_manifest(manifest_path)

    bucket_dirs = {
        "INDIVIDUAL_PROFILE": output_dir / "individual_profile",
        "GIG": output_dir / "gig",
        "IGNORE": output_dir / "ignore",
        "UNCERTAIN": output_dir / "uncertain",
    }
    for d in bucket_dirs.values():
        d.mkdir(parents=True, exist_ok=True)

    if input_dir.is_file():
        html_files = [input_dir]
    else:
        html_files = sorted(input_dir.glob("*.html"))
    if not html_files:
        print(f"No .html files found in {input_dir}")
        return

    with manifest_path.open("a", encoding="utf-8") as manifest:
        for html_path in html_files:
            if html_path.name in already_done:
                print(f"Skipping {html_path.name} (already in manifest)")
                continue

            print(f"Classifying {html_path.name}...")
            try:
                raw_output, elapsed, usage = query_soc_llm(html_path, prompt)
                parsed = parse_label(raw_output)
            except Exception as e:
                raw_output, elapsed, usage = f"ERROR: {e}", 0, {}
                parsed = {"label": "UNCERTAIN", "reason": f"api_error: {e}"}

            record = {
                "file": html_path.name,
                "label": parsed["label"],
                "reason": parsed["reason"],
                "elapsed": round(elapsed, 2),
                "usage": usage,
                "timestamp": datetime.now().isoformat(timespec="seconds"),
            }
            if parsed["reason"].startswith(("parse_error", "api_error", "unrecognized label")):
                record["raw_output"] = raw_output  # only keep this when the parse actually failed
            manifest.write(json.dumps(record) + "\n")
            manifest.flush()  # crash mid-batch shouldn't lose earlier results

            try:
                dest = bucket_dirs[parsed["label"]] / html_path.name
                shutil.copy2(html_path, dest)  # copy, not move — original dump stays untouched
            except OSError as e:
                print(f"WARNING: could not copy {html_path.name}: {e}")

    counts = {k: len(list(v.glob("*.html"))) for k, v in bucket_dirs.items()}
    print(f"\nDone. Manifest: {manifest_path}")
    print(f"Counts: {counts}")
    print(f"Check {bucket_dirs['UNCERTAIN']} + the manifest's 'reason' field for manual review.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Classify a folder of HTML files as INDIVIDUAL_PROFILE / GIG / IGNORE / UNCERTAIN")
    parser.add_argument("input_dir", help="Folder containing .html files (e.g. html_dump), or a single .html file")
    parser.add_argument("--output-dir", default="triage_output", help="Where the manifest + sorted folders go")
    args = parser.parse_args()

    run_triage(Path(args.input_dir), Path(args.output_dir), TRIAGE_PROMPT)