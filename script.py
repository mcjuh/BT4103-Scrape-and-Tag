import argparse
import json
import os
import random
import re
import time
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse
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

_SCRIPT_START = time.perf_counter()


def debug_log(msg: str) -> None:
    elapsed = time.perf_counter() - _SCRIPT_START
    print(f"[{elapsed:8.2f}s] {msg}", flush=True)  # flush so lines show up even if it hangs later

try:
    import spacy
    nlp = spacy.load("en_core_web_sm", exclude=["tagger","parser","lemmatizer","attribute_ruler"])
except Exception:
    nlp = None
    print(
        "WARNING: spaCy / en_core_web_sm not available; person names will not be masked"
    )

TITLE_STYLES = {
    "Authority": 'Rewrite their core role as an official corporate/industry-leader title (e.g., "Former Head of [Field] & Industry Leader").',
    "Value Prop": 'Rewrite their core role as a client-focused, benefit-driven hook (e.g., "Smart Financing as you Deserve").',
    "Descriptive": 'State their core role and specialization plainly and factually — no authority framing, no sales hook (e.g., "Senior Management Consultant specializing in supply chain transformation for retail clients").',
}

TITLE_STYLE_WEIGHTS = {"Descriptive": 0.6, "Authority": 0.3, "Value Prop": 0.1}

ACHIEVEMENT_STYLES = {
    "Direct First-Person": 'Use explicit "I" pronouns with active verbs (e.g., "I managed...", "I led..."). Cap at 3 items.',
    "Implied First-Person": 'Drop pronouns completely. Start directly with punchy action verbs (e.g., "Managed...", "Led..."). Cap at 3 items.',
}

IMPERFECTION_MODES = {
    "missing_preposition": (
        'Missing preposition (e.g., "managed transition [to] new system")'
    ),
    "double_connecting_word": (
        'Accidental double connecting word (e.g., "for the the project")'
    ),
    "mid_sentence_tense_switch": (
        'Unintentionally switch grammatical tense mid-sentence (e.g., "led the team and develops new strategies")'
    ),
    "omitted_trailing_period": (
        'Leave the final sentence without its period'
    ),
}

PRONOUN_MAP = [
    (r"\bhimself\b", "themself"), (r"\bHimself\b", "Themself"),
    (r"\bherself\b", "themself"), (r"\bHerself\b", "Themself"),
    (r"\bhe\b", "they"), (r"\bHe\b", "They"),
    (r"\bshe\b", "they"), (r"\bShe\b", "They"),
    (r"\bhim\b", "them"), (r"\bHim\b", "Them"),
    (r"\bhis\b", "their"), (r"\bHis\b", "Their"),
    (r"\bhers\b", "theirs"), (r"\bHers\b", "Theirs"),
    (r"\bher\b", "them"), (r"\bHer\b", "Them"),
]

PROMPT_TEMPLATE = """
You are a programmatic data extraction and transformation engine. Your task is to parse a raw HTML page describing ONE individual and rewrite their experience into a structured skillset profile.

Any direct name or gendered pronoun has been masked/neutralized as a bias-reduction step:
- The person's name has been replaced with the placeholder "[CANDIDATE_NAME]".
- Gendered pronouns have been replaced with neutral ones (they/them/their). Do not try to guess, restore, or mention gender..

### Output Format (Strict JSON Schema)
Return ONLY valid JSON. Use null for fields where the HTML provides no foundational context.
{{
  "about": {{
    "title": "tagline, max 60 char",
    "description": "max 255 char"
  }},
  "achievements": {{
    "items": [
      {{ "achievement": "max 255 char" }}
    ]
  }},
  "meta": {{
    "imperfection_applied": true | false
  }}
}}

### Transformation & Style Rules
Do not invent/pad fake credentials or fictional facts. Condense and transform the factual raw text using these exact parameters:

1. Title Style — {title_style}: {title_instruction}
2. Achievement Grammar Style — {achievement_style}: {achievement_instruction}
3. Prose imperfection mode: {imperfection_instruction}
   - Set "meta.imperfection_applied" to true only if you applied an imperfection; otherwise set it to false.
""".strip()


def mask_pronouns(text: str) -> str:
    for pattern, repl in PRONOUN_MAP:
        text = re.sub(pattern, repl, text)
    return text


def detect_person_names(plain_text: str) -> list:
    if nlp is None:
        return []
    doc = nlp(plain_text)
    names = {ent.text for ent in doc.ents if ent.label_ == "PERSON"}
    return sorted(names, key=len, reverse=True)  # longest first: full name before bare first name


def clean_html(html_content: str) -> str:
    t0 = time.perf_counter()
    soup = BeautifulSoup(html_content, "html.parser")
    for tag in soup(["script", "style", "nav", "footer", "header", "svg", "noscript", "iframe"]):
        tag.decompose()
    t1 = time.perf_counter()

    # Strip ALL attributes on every remaining tag. class/style/id/data-*/aria-* etc.
    # carry zero semantic value for text extraction but are usually the dominant
    # source of character bloat on framework-heavy sites (Tailwind utility classes
    # especially can be several times the size of the actual visible text).
    attrs_stripped = 0
    for tag in soup.find_all(True):
        if tag.attrs:
            attrs_stripped += len(tag.attrs)
            tag.attrs = {}
    t1b = time.perf_counter()
    debug_log(f"    clean_html: stripped {attrs_stripped} attributes in {t1b - t1:.2f}s")

    # NER runs on the plain-text rendering (tags confuse the tagger); the detected
    # name strings are then literal-replaced in the tag-containing HTML, which avoids
    # having to reconcile character offsets between two differently-shaped strings.
    plain_text = soup.get_text(separator=" ")
    html_str = str(soup)
    t2 = time.perf_counter()

    names = detect_person_names(plain_text)
    t3 = time.perf_counter()

    for name in names:
        html_str = html_str.replace(name, "[CANDIDATE_NAME]")
    html_str = mask_pronouns(html_str)
    t4 = time.perf_counter()

    debug_log(
        f"    clean_html stages: parse/strip={t1 - t0:.2f}s, attr-strip={t1b - t1:.2f}s, "
        f"get_text/str={t2 - t1b:.2f}s, spaCy NER={t3 - t2:.2f}s ({len(names)} names), "
        f"mask+replace={t4 - t3:.2f}s, TOTAL={t4 - t0:.2f}s"
    )
    debug_log(f"    clean_html: {len(html_content)} chars in -> {len(html_str)} chars out "
               f"({100 * (1 - len(html_str) / max(len(html_content), 1)):.0f}% reduction)")
    return html_str


def build_prompt() -> tuple:
    title_style = random.choices(
        list(TITLE_STYLE_WEIGHTS), weights=list(TITLE_STYLE_WEIGHTS.values()), k=1
    )[0]
    achievement_style = random.choice(list(ACHIEVEMENT_STYLES))
    imperfection_roll = random.randint(1, 100)
    imperfection_intended = imperfection_roll <= 5

    imperfection_mode = (
        random.choices(
            list(IMPERFECTION_MODES),
            weights=[0.25, 0.15, 0.05, 0.55],
            k=1,
        )[0]
        if imperfection_intended
        else "none"
    )

    imperfection_instruction = (
        IMPERFECTION_MODES[imperfection_mode] + 
            """\nApply exactly ONE natural instance of the specified imperfection 
            somewhere in the description or a single achievement item. Do not introduce any 
            other grammatical, spelling, or punctuation errors."""
        if imperfection_mode != "none"
        else "none; use flawless grammar and punctuation."
    )

    prompt = PROMPT_TEMPLATE.format(
        title_style=title_style,
        title_instruction=TITLE_STYLES[title_style],
        achievement_style=achievement_style,
        achievement_instruction=ACHIEVEMENT_STYLES[achievement_style],
        imperfection_instruction=imperfection_instruction,
    )

    roll_meta = {
        "title_style": title_style,
        "achievement_style": achievement_style,
        "imperfection_roll": imperfection_roll,
        "imperfection_intended": imperfection_intended,
        "imperfection_mode": imperfection_mode,
    }
    return prompt, roll_meta


def ping_model() -> None:
    """Sends a trivially small prompt. If this comes back fast, the timeouts are 
    almost certainly about prompt size."""
    debug_log(f"Ping: sending a minimal request to {MODEL} ...")
    start = time.perf_counter()
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": "Reply with exactly: OK"}],
        )
        elapsed = time.perf_counter() - start
        debug_log(f"Ping SUCCEEDED in {elapsed:.2f}s — response: {response.choices[0].message.content!r}")
        debug_log("Model/backend is alive and responsive to small requests. Prompt likely too long")
    except Exception as e:
        elapsed = time.perf_counter() - start
        debug_log(f"Ping FAILED after {elapsed:.2f}s — {type(e).__name__}: {e}")
        debug_log("Backend/model itself is unhealthy")


def query_soc_llm(html_path: Path, prompt: str, max_retries: int = 3):
    t0 = time.perf_counter()
    raw_html = html_path.read_text(encoding="utf-8")
    t1 = time.perf_counter()
    debug_log(f"  read file: {t1 - t0:.2f}s ({len(raw_html)} chars)")

    html_content = clean_html(raw_html)
    t2 = time.perf_counter()
    debug_log(f"  clean_html total: {t2 - t1:.2f}s -> {len(html_content)} chars going to the model")

    last_error = None
    for attempt in range(max_retries):
        debug_log(f"  attempt {attempt + 1}/{max_retries}: sending request to {MODEL} ...")
        start = time.perf_counter()
        try:
            response = client.chat.completions.create(
                model=MODEL,
                messages=[{"role": "user", "content": f"{prompt}\n\nHTML:\n```html\n{html_content}\n```"}],
            )
        except Exception as e:
            elapsed_fail = time.perf_counter() - start
            last_error = e
            debug_log(f"  attempt {attempt + 1} FAILED after {elapsed_fail:.2f}s — {type(e).__name__}: {e}")
            wait = 2 ** attempt
            debug_log(f"  retrying in {wait}s...")
            time.sleep(wait)
            continue

        elapsed = time.perf_counter() - start
        debug_log(f"  attempt {attempt + 1} SUCCEEDED after {elapsed:.2f}s")
        usage = {}
        if response.usage:
            usage = {
                "prompt_tokens": response.usage.prompt_tokens,
                "completion_tokens": response.usage.completion_tokens,
            }
        return response.choices[0].message.content, elapsed, usage

    raise last_error


def parse_output(raw_output: str) -> dict:
    text = raw_output.strip()
    if text.startswith("```"):
        text = text.strip("`")
        if text.lower().startswith("json"):
            text = text[4:]
        text = text.strip()
    return json.loads(text)


LEFTOVER_PRONOUN_RE = re.compile(r"\b(he|him|his|she|her|hers|himself|herself)\b", re.IGNORECASE)


def validate_profile(profile: dict, roll_meta: dict) -> dict:
    """To assess batch quality per html file."""
    about = profile.get("about") or {}
    achievements = (profile.get("achievements") or {}).get("items") or []
    meta = profile.get("meta") or {}

    title = about.get("title")
    description = about.get("description")
    achievement_texts = [a.get("achievement") for a in achievements if isinstance(a, dict)]

    all_text = " ".join(t for t in [title, description] + achievement_texts if t)

    return {
        "title_len": len(title) if title else 0,
        "title_overrun": bool(title) and len(title) > 60,
        "description_len": len(description) if description else 0,
        "description_overrun": bool(description) and len(description) > 255,
        "achievement_count": len(achievement_texts),
        "achievement_overrun_count": sum(1 for a in achievement_texts if a and len(a) > 255),
        "null_field_count": sum(1 for v in [title, description] if v is None)
        + sum(1 for a in achievement_texts if not a),
        "leftover_pronoun_hits": len(LEFTOVER_PRONOUN_RE.findall(all_text)),
        "imperfection_applied_self_report": meta.get("imperfection_applied"),
        "imperfection_roll": roll_meta["imperfection_roll"],
        "imperfection_intended": roll_meta["imperfection_intended"],
        "imperfection_consistent": meta.get("imperfection_applied") == roll_meta["imperfection_intended"],
        "title_style": roll_meta["title_style"],
        "achievement_style": roll_meta["achievement_style"],
    }


def load_manifest(manifest_path: Path) -> dict:
    """Files already successfully processed. 'error'/'parse_error' records are
    intentionally excluded so a plain rerun retries them instead of skipping them."""
    done = {}
    if manifest_path.exists():
        with manifest_path.open("r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                record = json.loads(line)
                if record.get("status") in ("error", "parse_error"):
                    continue
                done[record["file"]] = record
    return done


def run_batch(input_dir: Path, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = output_dir / "manifest.jsonl"
    already_done = load_manifest(manifest_path)

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
                debug_log(f"Skipping {html_path.name} (already in manifest)")
                continue

            debug_log(f"=== Processing {html_path.name} ===")
            prompt, roll_meta = build_prompt()

            try:
                raw_output, elapsed, usage = query_soc_llm(html_path, prompt)
            except Exception as e:
                record = {
                    "file": html_path.name,
                    "status": "error",
                    "reason": f"api_error: {e}",
                    "timestamp": datetime.now().isoformat(timespec="seconds"),
                }
                manifest.write(json.dumps(record) + "\n")
                manifest.flush()
                continue

            try:
                profile = parse_output(raw_output)
                metrics = validate_profile(profile, roll_meta)
                record = {
                    "file": html_path.name,
                    "status": "ok",
                    "elapsed": round(elapsed, 2),
                    "usage": usage,
                    "metrics": metrics,
                    "profile": profile,
                    "timestamp": datetime.now().isoformat(timespec="seconds"),
                }
            except (json.JSONDecodeError, AttributeError, TypeError) as e:
                record = {
                    "file": html_path.name,
                    "status": "parse_error",
                    "reason": str(e),
                    "raw_output": raw_output,
                    "roll_meta": roll_meta,
                    "timestamp": datetime.now().isoformat(timespec="seconds"),
                }

            manifest.write(json.dumps(record) + "\n")
            manifest.flush()

    print(f"\nDone. Manifest: {manifest_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Extract structured, anonymized skillset profiles from HTML (folder or single file)"
    )
    parser.add_argument("input_dir", nargs="?", default=None, help="Folder containing .html files, or a single .html file")
    parser.add_argument("--output-dir", default="extract_output", help="Where the manifest goes")
    parser.add_argument("--ping", action="store_true", help="Send one trivial request to test model/backend health, then exit")
    args = parser.parse_args()

    if args.ping:
        ping_model()
        raise SystemExit(0)

    if args.input_dir is None:
        parser.error("input_dir is required unless using --ping")

    run_batch(Path(args.input_dir), Path(args.output_dir))