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
    max_retries=0,  # our own retry loop below handles this — see extract.py notes
)
MODEL = os.environ["SOCLAAS_MODEL"]

_SCRIPT_START = time.perf_counter()

VALID_SOURCE_SUFFIXES = {".html", ".htm", ".md", ".markdown"}


def debug_log(msg: str) -> None:
    elapsed = time.perf_counter() - _SCRIPT_START
    print(f"[{elapsed:8.2f}s] {msg}", flush=True)


# Different serving harnesses disable Qwen3-style "thinking" mode via different,
# mutually incompatible parameter shapes, and some silently ignore params they don't
# recognize rather than erroring — so we can't just guess one and trust it worked.
# Tried in this order; the soft-switch text suffix is last since it's the one most
# likely to be silently ignored by a non-Qwen3 template, but it's also the one that
# can never cause an API-level rejection, so it's the safest final fallback.
THINKING_DISABLE_STRATEGIES = [
    {"name": "vLLM/SGLang chat_template_kwargs", "extra_body": {"chat_template_kwargs": {"enable_thinking": False}}, "suffix": ""},
    {"name": "DashScope top-level enable_thinking", "extra_body": {"enable_thinking": False}, "suffix": ""},
    {"name": "GLM-style thinking.disabled", "extra_body": {"thinking": {"type": "disabled"}}, "suffix": ""},
    {"name": "Qwen3 soft switch (/no_think in prompt text)", "extra_body": None, "suffix": "\n\n/no_think"},
]

_active_strategy = None  # set once by detect_thinking_strategy(), reused for every call after


def _response_shows_reasoning(response) -> tuple:
    content = response.choices[0].message.content or ""
    message_dict = response.choices[0].message.model_dump() if hasattr(response.choices[0].message, "model_dump") else {}
    reasoning_content = message_dict.get("reasoning_content")
    has_think_tag = "<think" in content.lower()
    return bool(has_think_tag or reasoning_content), has_think_tag, (len(reasoning_content) if reasoning_content else 0)


def detect_thinking_strategy() -> dict:
    """Probe each known thinking-disable parameter shape once, with a trivial prompt
    that would obviously show reasoning artifacts if thinking mode were still active.
    Locks in and reuses whichever one actually works, so this only costs a handful of
    small requests at startup, not one probe per file."""
    global _active_strategy
    probe_prompt = "What is 12 times 7? Reply with only the number, nothing else."

    for strategy in THINKING_DISABLE_STRATEGIES:
        debug_log(f"Probing thinking-disable strategy: {strategy['name']} ...")
        kwargs = {"model": MODEL, "messages": [{"role": "user", "content": probe_prompt + strategy["suffix"]}]}
        if strategy["extra_body"]:
            kwargs["extra_body"] = strategy["extra_body"]
        try:
            start = time.perf_counter()
            response = client.chat.completions.create(**kwargs)
            elapsed = time.perf_counter() - start
        except Exception as e:
            debug_log(f"  FAILED outright ({type(e).__name__}: {e}) — backend likely rejects "
                      f"this parameter shape, trying next")
            continue

        reasoning_detected, has_think_tag, reasoning_len = _response_shows_reasoning(response)
        completion_tokens = response.usage.completion_tokens if response.usage else "?"
        debug_log(f"  {elapsed:.2f}s, completion_tokens={completion_tokens}, "
                  f"<think> tag: {has_think_tag}, reasoning_content len: {reasoning_len}")

        if not reasoning_detected:
            debug_log(f"CONFIRMED working strategy: {strategy['name']}")
            _active_strategy = strategy
            return strategy

    debug_log("!! No strategy fully suppressed reasoning — falling back to the soft-switch "
              "text suffix as best-effort. Thinking mode may still add hidden latency/cost.")
    _active_strategy = THINKING_DISABLE_STRATEGIES[-1]
    return _active_strategy


try:
    import spacy
    nlp = spacy.load(
        "en_core_web_sm",
        exclude=["tagger", "parser", "lemmatizer", "attribute_ruler"]
    )
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

TITLE_STYLE_WEIGHTS = {
    "Descriptive": 0.6,
    "Authority": 0.3,
    "Value Prop": 0.1
}


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
        'Unintentionally switch grammatical tense mid-sentence '
        '(e.g., "led the team and develops new strategies")'
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


# ---------------------------------------------------------------------------
# PASS 1: SOURCE MATERIAL -> COMPACT FACTUAL JSON
# ---------------------------------------------------------------------------

PASS1_PROMPT = """
You are a programmatic data extraction engine.

Your task is to extract the professional experience of ONE individual from
the supplied source material and condense it into the required JSON structure.

The source material has already been cleaned and anonymized:
- The person's name has been replaced with "[CANDIDATE_NAME]".
- Gendered pronouns have been replaced with neutral ones.
- Do not try to guess, restore, or mention gender.

Your job in this pass is ONLY factual extraction and condensation.
Do not add marketing language, authority framing, stylistic hooks, or invented
credentials.

Prioritize information clearly describing the individual's own:
- professional role
- specialization
- experience
- responsibilities
- projects
- accomplishments
- expertise

### Output Format (Strict JSON Schema)

Return ONLY valid JSON:

{{
  "about": {{
    "title": "concise factual role/specialization, max 20 words",
    "description": "concise factual summary of the individual's experience, 70-100 words"
  }},
  "achievements": {{
    "items": [
      {{ "achievement": "specific, concise factual individual achievement or experience, max 30 words each" }}
    ]
  }},
  "meta": {{
    "imperfection_applied": false
  }}
}}

### Extraction Rules

- Do not invent or infer facts not supported by the source material.
- Condense redundant information.
- Keep the wording neutral and factual.
- "meta.imperfection_applied" must always be included and set to false in this pass.

### Achievement Rules

An achievement names a SPECIFIC outcome the individual personally produced.
It must have a concrete actor, a concrete object, and (ideally) a
measurable or verifiable result.
Include max 3 achievement items. If the material is too generic/broad and there is no
specific individual achievement, do not force one.

Contrastive examples:

GOOD: "Reduced loan underwriting time from 3 days to 4 hours by
       rebuilding the workflow in Salesforce Financial Services Cloud."
BAD:  "Supported underwriting transformation initiatives for banking clients."

GOOD: "Awarded two USPTO patents (9921894, 10203941) for an API-powered
       industry utility."
BAD:  "Authored content on API strategy and open banking."

GOOD: "Led a $5M engagement with a European insurance carrier to replace
       their legacy policy administration system."
BAD:  "Collaborated with global insurance clients on transformation projects."

GOOD: "Named to Computer Weekly's top 50 most influential women in IT
       three consecutive years."
BAD:  "Developed expertise in insurance technology and cyber security."

The following are NEVER achievements, even when they feel specific:
- Job titles, roles, responsibilities, or scope statements
- Collaborations, engagements, or client relationships without a named
  outcome or result
- Areas of expertise, skills, or specializations
- Education, degrees, fellowships, certifications
- Articles, blog posts, talks, or any content authorship
- Tenure statements ("20 years of experience")
- Restatements of the "about" description

If the source contains nothing that passes the GOOD bar, return:
  "achievements": {"items": []}

An empty array is the CORRECT output when the source is a bio, author
page, or role summary with no outcome-level content. Do not pad to
reach a count.
""".strip()


# ---------------------------------------------------------------------------
# PASS 2: COMPACT JSON -> FINAL STYLED JSON
# ---------------------------------------------------------------------------

PASS2_PROMPT = """
You are a programmatic data transformation engine.

The input below is a compact factual profile extracted from source material
describing ONE individual.

Transform it into the final skillset profile.

Do not invent, pad, or change factual claims.

### Output Format (Strict JSON Schema)

Return ONLY valid JSON:

{{
  "about": {{
    "title": "tagline, max 20 words",
    "description": "70-100 words"
  }},
  "achievements": {{
    "items": [
      {{ "achievement": "max 30 words each" }}
    ]
  }},
  "meta": {{
    "imperfection_applied": true | false
  }}
}}

### Experience/Role Rules

You are NOT formally employed currently.
(e.g. 'I am a retired CFO with 20 years of experience...', 'I was a project manager for...', 
'Former executive at...', 'I am a freelance web developer...', 'Retired software engineer...')
Your language should NOT indicate current employment.

### Transformation & Style Rules

1. Title Style — {title_style}: {title_instruction}

2. Achievement Grammar Style — {achievement_style}: {achievement_instruction}

3. Prose imperfection mode: {imperfection_instruction}

Do not change the underlying facts while transforming the wording.

If an imperfection mode is specified:
- Apply exactly ONE natural instance of that specified imperfection somewhere
  in the description or a single achievement item.
- Do not introduce any other grammatical, spelling, or punctuation errors.
- Set "meta.imperfection_applied" to true only if you actually applied the
  specified imperfection.

If the imperfection mode is "none":
- Set "meta.imperfection_applied" to false.
If the input has an empty achievements array, return an empty array. Do not populate it during style transformation.

### Achievement Verbs

Prefer past-tense, telic verbs that name a bounded outcome:
Led, Delivered, Launched, Built, Shipped, Won, Secured, Reduced, Grew,
Cut, Saved, Redesigned, Migrated, Negotiated.

Causal-role verbs (Facilitated, Enabled, Supported, Contributed to,
Collaborated with) are allowed ONLY when the sentence names a specific
object and a bounded scope or result:
  OK:  "Facilitated the migration of 40 services off mainframe,
        unblocking the Q3 release."
  BAD: "Facilitated digital transformation initiatives for clients."

Pure instrumentals (Leveraged, Utilized, Used, Employed, Applied) are
never achievement verbs. The real verb is downstream — promote it:
  BAD:  "Leveraged Salesforce to cut processing time."
  OK:   "Cut processing time by rebuilding the workflow in Salesforce."

Mentally test each achievement with: "and then what happened?"
If the sentence cannot answer that with a concrete outcome or result, it is not an
achievement — rewrite it or drop it
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

    return sorted(
        names,
        key=len,
        reverse=True
    )


def clean_html(html_content: str) -> str:
    t0 = time.perf_counter()

    soup = BeautifulSoup(html_content, "html.parser")

    for tag in soup([
        "script",
        "style",
        "nav",
        "footer",
        "header",
        "svg",
        "noscript",
        "iframe"
    ]):
        tag.decompose()

    t1 = time.perf_counter()

    # Strip ALL attributes on every remaining tag.
    attrs_stripped = 0

    for tag in soup.find_all(True):
        if tag.attrs:
            attrs_stripped += len(tag.attrs)
            tag.attrs = {}

    t1b = time.perf_counter()

    debug_log(
        f"    clean_html: stripped {attrs_stripped} attributes "
        f"in {t1b - t1:.2f}s"
    )

    plain_text = soup.get_text(separator=" ")
    html_str = str(soup)

    t2 = time.perf_counter()

    names = detect_person_names(plain_text)

    t3 = time.perf_counter()

    for name in names:
        html_str = html_str.replace(
            name,
            "[CANDIDATE_NAME]"
        )

    html_str = mask_pronouns(html_str)

    t4 = time.perf_counter()

    debug_log(
        f"    clean_html stages: parse/strip={t1 - t0:.2f}s, "
        f"attr-strip={t1b - t1:.2f}s, "
        f"get_text/str={t2 - t1b:.2f}s, "
        f"spaCy NER={t3 - t2:.2f}s ({len(names)} names), "
        f"mask+replace={t4 - t3:.2f}s, "
        f"TOTAL={t4 - t0:.2f}s"
    )

    debug_log(
        f"    clean_html: {len(html_content)} chars in -> "
        f"{len(html_str)} chars out "
        f"({100 * (1 - len(html_str) / max(len(html_content), 1)):.0f}% reduction)"
    )

    return html_str


def mask_source_text(plain_text: str) -> str:
    """Anonymize already-plain source (e.g. markdown): mask person names via
    spaCy NER, then neutralize gendered pronouns. Mirrors the masking step
    inside clean_html, minus the HTML parsing/attribute stripping — markdown
    is already plain text, so pushing it through BeautifulSoup would be
    pointless and could mangle legitimate markdown syntax."""
    t0 = time.perf_counter()

    names = detect_person_names(plain_text)

    t1 = time.perf_counter()

    masked = plain_text
    for name in names:
        masked = masked.replace(name, "[CANDIDATE_NAME]")
    masked = mask_pronouns(masked)

    t2 = time.perf_counter()

    debug_log(
        f"    mask_source_text: spaCy NER={t1 - t0:.2f}s ({len(names)} names), "
        f"mask+replace={t2 - t1:.2f}s, "
        f"TOTAL={t2 - t0:.2f}s"
    )

    return masked


def load_source_text(path: Path) -> str:
    """Dispatch on file suffix: HTML gets the full BS4 clean + anonymization;
    markdown (from the updated crawler) is already plain text and only needs
    the anonymization step."""
    suffix = path.suffix.lower()
    raw = path.read_text(encoding="utf-8")

    if suffix in {".html", ".htm"}:
        return clean_html(raw)
    elif suffix in {".md", ".markdown"}:
        debug_log(
            f"    load_source_text: markdown ({len(raw)} chars) — "
            f"skipping HTML parse, applying anonymization only"
        )
        return mask_source_text(raw)
    else:
        raise ValueError(
            f"Unsupported file type: {suffix} "
            f"(expected .html/.htm/.md/.markdown)"
        )


def build_prompt() -> tuple:
    title_style = random.choices(
        list(TITLE_STYLE_WEIGHTS),
        weights=list(TITLE_STYLE_WEIGHTS.values()),
        k=1
    )[0]

    achievement_style = random.choice(
        list(ACHIEVEMENT_STYLES)
    )

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
        IMPERFECTION_MODES[imperfection_mode]
        if imperfection_mode != "none"
        else "none; use flawless grammar and punctuation."
    )

    prompt = PASS2_PROMPT.format(
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
    """Sends a trivially small prompt, using whichever thinking-disable strategy
    is active (or detects one first if not yet set)."""

    global _active_strategy
    if _active_strategy is None:
        _active_strategy = detect_thinking_strategy()

    strategy = _active_strategy
    debug_log(
        f"Ping: sending a minimal request to {MODEL} "
        f"using '{strategy['name']}' ..."
    )

    start = time.perf_counter()

    try:
        kwargs = {
            "model": MODEL,
            "messages": [
                {
                    "role": "user",
                    "content": "Reply with exactly: OK" + strategy["suffix"]
                }
            ],
        }
        if strategy["extra_body"]:
            kwargs["extra_body"] = strategy["extra_body"]

        response = client.chat.completions.create(**kwargs)

        elapsed = time.perf_counter() - start

        content = response.choices[0].message.content
        debug_log(
            f"Ping SUCCEEDED in {elapsed:.2f}s — "
            f"contains <think> tag: {'<think' in (content or '').lower()}, "
            f"response: {content!r}"
        )

        debug_log(
            "Model/backend is alive and responsive to small requests."
        )

    except Exception as e:
        elapsed = time.perf_counter() - start

        debug_log(
            f"Ping FAILED after {elapsed:.2f}s — "
            f"{type(e).__name__}: {e}"
        )

        debug_log(
            "Backend/model itself is unhealthy"
        )


def _call_llm(messages, attempt_label: str, max_retries: int = 3):
    """
    Generic LLM call used by both passes. Uses the module-level
    _active_strategy to disable thinking mode; detects one lazily if needed.
    The strategy's text suffix is appended to the LAST user message's content.
    """

    global _active_strategy
    if _active_strategy is None:
        _active_strategy = detect_thinking_strategy()

    strategy = _active_strategy

    # Append the soft-switch suffix (if any) to the final user message.
    # Deep-copy the messages list so we don't mutate the caller's object across retries.
    suffixed_messages = [dict(m) for m in messages]
    if strategy["suffix"] and suffixed_messages:
        for m in reversed(suffixed_messages):
            if m.get("role") == "user":
                m["content"] = m["content"] + strategy["suffix"]
                break

    last_error = None

    for attempt in range(max_retries):
        debug_log(
            f"  {attempt_label}: attempt "
            f"{attempt + 1}/{max_retries} sending request to {MODEL} "
            f"(thinking-disable: {strategy['name']}) ..."
        )

        start = time.perf_counter()

        try:
            kwargs = {
                "model": MODEL,
                "messages": suffixed_messages,
            }
            if strategy["extra_body"]:
                kwargs["extra_body"] = strategy["extra_body"]

            response = client.chat.completions.create(**kwargs)

        except Exception as e:
            elapsed_fail = time.perf_counter() - start
            last_error = e

            debug_log(
                f"  {attempt_label}: attempt {attempt + 1} FAILED "
                f"after {elapsed_fail:.2f}s — "
                f"{type(e).__name__}: {e}"
            )

            wait = 2 ** attempt

            debug_log(
                f"  retrying in {wait}s..."
            )

            time.sleep(wait)
            continue

        elapsed = time.perf_counter() - start

        content = response.choices[0].message.content
        has_think_tag = "<think" in (content or "").lower()
        message_dict = (
            response.choices[0].message.model_dump()
            if hasattr(response.choices[0].message, "model_dump")
            else {}
        )
        reasoning_content = message_dict.get("reasoning_content")

        usage = {}
        if response.usage:
            usage = {
                "prompt_tokens": response.usage.prompt_tokens,
                "completion_tokens": response.usage.completion_tokens,
            }

        debug_log(
            f"  {attempt_label}: attempt {attempt + 1} "
            f"SUCCEEDED after {elapsed:.2f}s — "
            f"completion_tokens={usage.get('completion_tokens', '?')}, "
            f"content_len={len(content or '')} chars, "
            f"contains <think> tag: {has_think_tag}, "
            f"reasoning_content field present: "
            f"{reasoning_content is not None} "
            f"(len={len(reasoning_content) if reasoning_content else 0})"
        )

        if has_think_tag or reasoning_content:
            debug_log(
                f"  !! hidden reasoning detected even with "
                f"'{strategy['name']}' active — this explains inflated "
                f"completion_tokens relative to visible output length. "
                f"Consider re-running detect_thinking_strategy() or "
                f"accepting this as a cost/latency ceiling."
            )

        return (
            content,
            elapsed,
            usage,
        )

    raise last_error


def query_soc_llm(
    source_path: Path,
    prompt: str,
    max_retries: int = 3
):
    """
    Two-pass pipeline:

    Pass 1:
        cleaned source material -> compact factual JSON

    Pass 2:
        compact factual JSON -> final styled JSON
    """

    t0 = time.perf_counter()

    source_text = load_source_text(source_path)

    t1 = time.perf_counter()

    debug_log(
        f"  load_source_text: {t1 - t0:.2f}s -> "
        f"{len(source_text)} chars going to Pass 1 "
        f"(type: {source_path.suffix})"
    )

    # ---------------------------------------------------------------
    # PASS 1
    # ---------------------------------------------------------------

    debug_log(
        "  >>> PASS 1: extracting and condensing factual profile ..."
    )

    pass1_start = time.perf_counter()

    pass1_output, pass1_elapsed, pass1_usage = _call_llm(
        messages=[
            {
                "role": "user",
                "content": (
                    f"{PASS1_PROMPT}\n\n"
                    f"SOURCE MATERIAL:\n"
                    f"```\n"
                    f"{source_text}\n"
                    f"```"
                ),
            }
        ],
        attempt_label="PASS 1",
        max_retries=max_retries,
    )

    pass1_total = time.perf_counter() - pass1_start

    debug_log(
        f"  PASS 1 completed in {pass1_total:.2f}s"
    )

    debug_log(
        f"  PASS 1 raw output ({len(pass1_output)} chars): "
        f"{pass1_output[:1000]!r}"
    )

    try:
        condensed_profile = parse_output(pass1_output)
    except Exception as e:
        debug_log(
            f"  PASS 1 JSON PARSE FAILED: "
            f"{type(e).__name__}: {e}"
        )
        raise

    condensed_json = json.dumps(
        condensed_profile,
        ensure_ascii=False
    )

    debug_log(
        f"  PASS 1 parsed successfully: "
        f"{len(condensed_json)} chars of compact JSON"
    )

    # ---------------------------------------------------------------
    # PASS 2
    # ---------------------------------------------------------------

    debug_log(
        "  >>> PASS 2: applying styles and final transformation ..."
    )

    pass2_start = time.perf_counter()

    pass2_output, pass2_elapsed, pass2_usage = _call_llm(
        messages=[
            {
                "role": "user",
                "content": (
                    f"{prompt}\n\n"
                    f"CONDENSED PROFILE:\n"
                    f"```json\n"
                    f"{condensed_json}\n"
                    f"```"
                ),
            }
        ],
        attempt_label="PASS 2",
        max_retries=max_retries,
    )

    pass2_total = time.perf_counter() - pass2_start

    debug_log(
        f"  PASS 2 completed in {pass2_total:.2f}s"
    )

    debug_log(
        f"  PASS 2 raw output ({len(pass2_output)} chars): "
        f"{pass2_output[:1000]!r}"
    )

    total_elapsed = time.perf_counter() - t0

    usage = {
        "pass1": pass1_usage,
        "pass2": pass2_usage,
        "prompt_tokens": (
            pass1_usage.get("prompt_tokens", 0)
            + pass2_usage.get("prompt_tokens", 0)
        ),
        "completion_tokens": (
            pass1_usage.get("completion_tokens", 0)
            + pass2_usage.get("completion_tokens", 0)
        ),
    }

    debug_log(
        f"  TOTAL LLM pipeline time: {total_elapsed:.2f}s"
    )

    return pass2_output, total_elapsed, usage


def parse_output(raw_output: str) -> dict:
    text = raw_output.strip()

    if text.startswith("```"):
        text = text.strip("`")

        if text.lower().startswith("json"):
            text = text[4:]

        text = text.strip()

    return json.loads(text)


LEFTOVER_PRONOUN_RE = re.compile(
    r"\b(he|him|his|she|her|hers|himself|herself)\b",
    re.IGNORECASE
)


def validate_profile(profile: dict, roll_meta: dict) -> dict:
    """To assess batch quality per source file."""

    about = profile.get("about") or {}

    achievements = (
        (profile.get("achievements") or {}).get("items") or []
    )

    meta = profile.get("meta") or {}

    title = about.get("title")
    description = about.get("description")

    achievement_texts = [
        a.get("achievement")
        for a in achievements
        if isinstance(a, dict)
    ]

    all_text = " ".join(
        t
        for t in [title, description] + achievement_texts
        if t
    )

    return {
        "title_len": len(title) if title else 0,
        "title_overrun": bool(title) and len(title) > 60,
        "description_len": len(description) if description else 0,
        "description_overrun": bool(description) and len(description) > 255,
        "achievement_count": len(achievement_texts),
        "achievement_overrun_count": sum(
            1
            for a in achievement_texts
            if a and len(a) > 255
        ),
        "null_field_count": (
            sum(
                1
                for v in [title, description]
                if v is None
            )
            + sum(
                1
                for a in achievement_texts
                if not a
            )
        ),
        "leftover_pronoun_hits": len(
            LEFTOVER_PRONOUN_RE.findall(all_text)
        ),
        "imperfection_applied_self_report": meta.get(
            "imperfection_applied"
        ),
        "imperfection_roll": roll_meta["imperfection_roll"],
        "imperfection_intended": roll_meta["imperfection_intended"],
        "imperfection_consistent": (
            meta.get("imperfection_applied")
            == roll_meta["imperfection_intended"]
        ),
        "title_style": roll_meta["title_style"],
        "achievement_style": roll_meta["achievement_style"],
    }


def load_manifest(manifest_path: Path) -> dict:
    """Files already successfully processed. 'error'/'parse_error' records are
    intentionally excluded so a plain rerun retries them instead of skipping them."""

    done = {}

    if manifest_path.exists():
        with manifest_path.open(
            "r",
            encoding="utf-8"
        ) as f:

            for line in f:
                line = line.strip()

                if not line:
                    continue

                record = json.loads(line)

                if record.get("status") in (
                    "error",
                    "parse_error"
                ):
                    continue

                done[record["file"]] = record

    return done


def run_batch(input_dir: Path, output_dir: Path) -> None:
    global _active_strategy
    if _active_strategy is None:
        _active_strategy = detect_thinking_strategy()

    output_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    manifest_path = output_dir / "sc_master_manifest.jsonl"

    already_done = load_manifest(
        manifest_path
    )

    if input_dir.is_file():
        source_files = [input_dir]
    else:
        source_files = sorted(
            p for p in input_dir.iterdir()
            if p.suffix.lower() in VALID_SOURCE_SUFFIXES
        )

    if not source_files:
        print(
            f"No .html/.htm/.md/.markdown files found in {input_dir}"
        )
        return

    with manifest_path.open(
        "a",
        encoding="utf-8"
    ) as manifest:

        for source_path in source_files:

            if source_path.name in already_done:
                debug_log(
                    f"Skipping {source_path.name} "
                    f"(already in manifest)"
                )
                continue

            debug_log(
                f"=== Processing {source_path.name} ==="
            )

            prompt, roll_meta = build_prompt()

            debug_log(
                f"  Selected styles: "
                f"title={roll_meta['title_style']}, "
                f"achievement={roll_meta['achievement_style']}, "
                f"imperfection={roll_meta['imperfection_mode']} "
                f"(roll={roll_meta['imperfection_roll']})"
            )

            try:
                raw_output, elapsed, usage = query_soc_llm(
                    source_path,
                    prompt
                )

            except Exception as e:
                record = {
                    "file": source_path.name,
                    "status": "error",
                    "reason": f"api_error: {e}",
                    "timestamp": datetime.now().isoformat(
                        timespec="seconds"
                    ),
                }

                manifest.write(
                    json.dumps(record) + "\n"
                )

                manifest.flush()

                continue

            try:
                profile = parse_output(
                    raw_output
                )

                metrics = validate_profile(
                    profile,
                    roll_meta
                )

                record = {
                    "file": source_path.name,
                    "status": "ok",
                    "elapsed": round(
                        elapsed,
                        2
                    ),
                    "usage": usage,
                    "metrics": metrics,
                    "profile": profile,
                    "timestamp": datetime.now().isoformat(
                        timespec="seconds"
                    ),
                }

            except (
                json.JSONDecodeError,
                AttributeError,
                TypeError
            ) as e:

                record = {
                    "file": source_path.name,
                    "status": "parse_error",
                    "reason": str(e),
                    "raw_output": raw_output,
                    "roll_meta": roll_meta,
                    "timestamp": datetime.now().isoformat(
                        timespec="seconds"
                    ),
                }

            manifest.write(
                json.dumps(record) + "\n"
            )

            manifest.flush()

    print(
        f"\nDone. Manifest: {manifest_path}"
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=(
            "Extract structured, anonymized skillset profiles "
            "from HTML or markdown (folder or single file)"
        )
    )

    parser.add_argument(
        "input_dir",
        nargs="?",
        default=None,
        help=(
            "Folder containing .html/.htm/.md/.markdown files, "
            "or a single file of one of those types"
        )
    )

    parser.add_argument(
        "--output-dir",
        default=None,
        help=(
            "Where the manifest goes "
            "(default: the input path's parent directory, "
            "e.g. big_crawl/individual_profile -> big_crawl)"
        )
    )

    parser.add_argument(
        "--ping",
        action="store_true",
        help=(
            "Send one trivial request to test "
            "model/backend health, then exit"
        )
    )

    args = parser.parse_args()

    if args.ping:
        ping_model()
        raise SystemExit(0)

    if args.input_dir is None:
        parser.error(
            "input_dir is required unless using --ping"
        )

    input_path = Path(args.input_dir)
    output_dir = (
        Path(args.output_dir)
        if args.output_dir
        else input_path.parent
    )

    run_batch(input_path, output_dir)