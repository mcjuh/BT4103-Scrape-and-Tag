import argparse
import json
import os
import random
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
    max_retries=0,  # our own retry loop below handles this — see extract.py notes
)
MODEL = os.environ["SOCLAAS_MODEL"]

_SCRIPT_START = time.perf_counter()


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


# Real freelance gig posts skew short/medium far more often than "~200 words" (that
# figure is SEO advice for a *good* post, not a typical one). Weighting reflects that,
# and — same lesson as the imperfection dice roll — telling the model to "vary length
# based on the source" in prose alone tends to still converge on a safe medium; rolling
# the tier here forces the actual variety.
DETAIL_TIERS = {
    "Minimal": "Usually 40-80 words. Use a short paragraph or 2-3 bullets.",
    "Standard": "Usually 80-150 words. Use a short opening and concise bullets when they improve scannability.",
    "Detailed": "Usually 140-220 words. Use this only when the source supports several distinct scope items or deliverables.",
}
DETAIL_TIER_WEIGHTS = {
    "Minimal": 0.50,
    "Standard": 0.40,
    "Detailed": 0.10,
}

GIG_PROMPT_TEMPLATE = """
Create one realistic freelance or specialist consulting gig from the source material.

The source will usually be a completed case study, portfolio entry, or press release,
not an open job post. Treat a completed engagement as evidence of what the original
hirer could have requested before the work began.

A qualifying gig requires both:
1. A concrete problem, requirement, or project need in the source.
2. A matching technical or professional scope that was implemented.

If either is missing, return exactly: {{}}

Otherwise return ONLY valid JSON in exactly this format:
{{"title": "max 25 words", "description": "max 220 words"}}

TITLE
State the role and core task plainly. Do not use generic filler such as "Help Needed"
or "Project Opportunity."

DESCRIPTION
Write as the original hirer, before work begins. State the essential need, then include
only the source-backed scope, deliverables, tools, standards, and constraints.

Choose the most natural compact form:
- For simple work, use one short paragraph.
- When there are several distinct requirements, use one short opening followed by
  2-5 concise bullet points.
- Do not add headings merely to create structure.
- Mention each requirement once. Use bullets rather than restating the same task in
  different sentences.

Use this length guidance: {detail_instruction}

GROUNDING RULES
This is a realistic simulation, not a literal quotation. You may invent only the
hirer's voice, concise connecting language, and generic request framing needed to make
the source read naturally as a gig.

All matchable content must be source-backed: role, tasks, technologies, standards,
industry-specific requirements, deliverables, qualifications, project constraints, and
expected outcomes. When in doubt, omit a detail rather than infer it.

- Select one coherent specialist scope. If the source describes several unrelated
  services, choose the single clearest one; do not combine them into a catch-all role.
- Do not add employment type, staffing level, location or onsite requirements, duration,
  budget, proposal instructions, qualifications, or certifications unless the source
  explicitly states them.
- Do not add historic project dates, completed work, prior failures, remedial work, new
  incidents, urgency, or business problems unless explicitly established as the original
  need.
- Never identify the real company in the source as the hirer or client. Refer to it
  generically when necessary. Keep named tools, standards, and technologies only when
  they are genuine source-backed requirements.
- Keep the scope realistic for one specialist or a small focused engagement.
- Prefer concrete requirements over background, promotional language, or repeated
  explanations of why the work matters.

Your JSON object must contain exactly two keys: "title" and "description". Do not use
synonyms such as "role", "short_description", "required_skills", "status", or "error".
Return {{}} for non-qualifying material. Never return keys such as "status", "reason",
or "error".
""".strip()


def clean_html(html_content: str) -> str:
    soup = BeautifulSoup(html_content, "html.parser")
    for tag in soup(["script", "style", "nav", "footer", "header", "svg", "noscript", "iframe"]):
        tag.decompose()

    # Case-study pages tend to carry much heavier chrome than a bio page — related-
    # content carousels, testimonial sliders, newsletter blocks — none of which the
    # tag-name strip above catches, since those are usually plain <div>s. If the page
    # has a semantic <main> or <article>, prefer just that; otherwise fall back to the
    # whole (already-stripped) body so we never silently lose content on pages that
    # don't use these tags.
    main_content = soup.find("main") or soup.find("article")
    if main_content is not None:
        debug_log(f"  clean_html: found <{main_content.name}>, using it instead of the full page")
        soup = main_content

    # Strip all attributes too — class/style/id/data-* etc. are pure character bloat
    # for a text-extraction task (see the showcase pipeline for the full reasoning).
    for tag in soup.find_all(True):
        if tag.attrs:
            tag.attrs = {}
    return str(soup)


def load_source_text(path: Path) -> str:
    """HTML gets the full BS4 clean. Markdown (from the updated crawler) is already
    plain text — running it through an HTML parser would be pointless and could even
    mangle legitimate markdown syntax (e.g. '<' in a code block)."""
    suffix = path.suffix.lower()
    raw = path.read_text(encoding="utf-8")
    if suffix in {".html", ".htm"}:
        cleaned = clean_html(raw)
        debug_log(f"  load_source_text: {len(raw)} chars in -> {len(cleaned)} chars out "
                  f"({100 * (1 - len(cleaned) / max(len(raw), 1)):.0f}% reduction)")
        return cleaned
    elif suffix in {".md", ".markdown"}:
        return raw
    else:
        raise ValueError(f"Unsupported file type: {suffix} (expected .html/.htm/.md/.markdown)")


def build_prompt() -> tuple:
    tier = random.choices(
        list(DETAIL_TIER_WEIGHTS), weights=list(DETAIL_TIER_WEIGHTS.values()), k=1
    )[0]
    prompt = GIG_PROMPT_TEMPLATE.format(detail_instruction=DETAIL_TIERS[tier])
    return prompt, {"detail_tier": tier}


def ping_model() -> None:
    strategy = detect_thinking_strategy()
    debug_log(f"Ping: sending a minimal request to {MODEL} using '{strategy['name']}' ...")
    start = time.perf_counter()
    try:
        kwargs = {"model": MODEL, "messages": [{"role": "user", "content": "Reply with exactly: OK" + strategy["suffix"]}]}
        if strategy["extra_body"]:
            kwargs["extra_body"] = strategy["extra_body"]
        response = client.chat.completions.create(**kwargs)
        elapsed = time.perf_counter() - start
        content = response.choices[0].message.content
        usage = {"completion_tokens": response.usage.completion_tokens} if response.usage else {}
        debug_log(f"Ping SUCCEEDED in {elapsed:.2f}s — completion_tokens={usage.get('completion_tokens', '?')}, "
                  f"contains <think> tag: {'<think' in content.lower()}, response: {content!r}")
    except Exception as e:
        elapsed = time.perf_counter() - start
        debug_log(f"Ping FAILED after {elapsed:.2f}s — {type(e).__name__}: {e}")


def query_soc_llm(source_path: Path, prompt: str, max_retries: int = 3):
    global _active_strategy
    if _active_strategy is None:
        _active_strategy = detect_thinking_strategy()

    t0 = time.perf_counter()
    source_text = load_source_text(source_path)
    t1 = time.perf_counter()
    debug_log(f"  load_source_text: {t1 - t0:.2f}s -> {len(source_text)} chars going to the model "
              f"(type: {source_path.suffix})")

    full_prompt = f"{prompt}\n\nSOURCE MATERIAL:\n```\n{source_text}\n```" + _active_strategy["suffix"]

    last_error = None
    for attempt in range(max_retries):
        debug_log(f"  attempt {attempt + 1}/{max_retries}: sending request to {MODEL} "
                  f"(thinking-disable: {_active_strategy['name']}) ...")
        start = time.perf_counter()
        try:
            kwargs = {"model": MODEL, "messages": [{"role": "user", "content": full_prompt}]}
            if _active_strategy["extra_body"]:
                kwargs["extra_body"] = _active_strategy["extra_body"]
            response = client.chat.completions.create(**kwargs)
        except Exception as e:
            elapsed_fail = time.perf_counter() - start
            last_error = e
            debug_log(f"  attempt {attempt + 1} FAILED after {elapsed_fail:.2f}s — {type(e).__name__}: {e}")
            wait = 2 ** attempt
            debug_log(f"  retrying in {wait}s...")
            time.sleep(wait)
            continue

        elapsed = time.perf_counter() - start
        content = response.choices[0].message.content
        usage = {}
        if response.usage:
            usage = {
                "prompt_tokens": response.usage.prompt_tokens,
                "completion_tokens": response.usage.completion_tokens,
            }
        has_think_tag = "<think" in content.lower()
        message_dict = response.choices[0].message.model_dump() if hasattr(response.choices[0].message, "model_dump") else {}
        reasoning_content = message_dict.get("reasoning_content")
        debug_log(f"  attempt {attempt + 1} SUCCEEDED after {elapsed:.2f}s — "
                  f"completion_tokens={usage.get('completion_tokens', '?')}, content_len={len(content)} chars, "
                  f"contains <think> tag: {has_think_tag}, reasoning_content field present: "
                  f"{reasoning_content is not None} (len={len(reasoning_content) if reasoning_content else 0})")
        if has_think_tag or reasoning_content:
            debug_log(f"  !! hidden reasoning detected even with '{_active_strategy['name']}' active — "
                      f"this explains inflated completion_tokens relative to visible output length. "
                      f"Consider re-running detect_thinking_strategy() or accepting this as a cost/latency ceiling.")
        return content, elapsed, usage

    raise last_error


def parse_json_output(raw_output: str):
    text = raw_output.strip()
    if text.startswith("```"):
        text = text.strip("`")
        if text.lower().startswith("json"):
            text = text[4:]
        text = text.strip()
    return json.loads(text)  # let this raise — caller decides how to record the failure


def load_manifest(manifest_path: Path) -> dict:
    """Files already processed (status 'ok' or 'not_a_gig'). 'error'/'parse_error'
    are excluded so a plain rerun retries them instead of skipping them forever."""
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


def run_batch(input_path: Path, manifest_path: Path) -> None:
    global _active_strategy
    if _active_strategy is None:
        _active_strategy = detect_thinking_strategy()

    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    already_done = load_manifest(manifest_path)

    valid_suffixes = {".html", ".htm", ".md", ".markdown"}
    if input_path.is_file():
        source_files = [input_path]
    else:
        source_files = sorted(p for p in input_path.iterdir() if p.suffix.lower() in valid_suffixes)
    if not source_files:
        debug_log(f"No .html/.htm/.md/.markdown files found in {input_path}")
        return

    with manifest_path.open("a", encoding="utf-8") as manifest:
        for source_path in source_files:
            if source_path.name in already_done:
                debug_log(f"Skipping {source_path.name} (already in manifest)")
                continue

            debug_log(f"=== Processing {source_path.name} ===")
            prompt, roll_meta = build_prompt()

            try:
                raw_output, elapsed, usage = query_soc_llm(source_path, prompt)
            except Exception as e:
                record = {
                    "file": source_path.name,
                    "status": "error",
                    "reason": f"api_error: {e}",
                    "timestamp": datetime.now().isoformat(timespec="seconds"),
                }
                manifest.write(json.dumps(record) + "\n")
                manifest.flush()
                continue

            try:
                result = parse_json_output(raw_output)
                status = "not_a_gig" if result == {} else "ok"
                record = {
                    "file": source_path.name,
                    "status": status,
                    "elapsed": round(elapsed, 2),
                    "usage": usage,
                    "detail_tier": roll_meta["detail_tier"],
                    "result": result,
                    "timestamp": datetime.now().isoformat(timespec="seconds"),
                }
            except (json.JSONDecodeError, AttributeError, TypeError) as e:
                record = {
                    "file": source_path.name,
                    "status": "parse_error",
                    "reason": str(e),
                    "raw_output": raw_output,
                    "detail_tier": roll_meta["detail_tier"],
                    "timestamp": datetime.now().isoformat(timespec="seconds"),
                }

            manifest.write(json.dumps(record) + "\n")
            manifest.flush()

    print(f"\nDone. Manifest: {manifest_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Extract structured gig postings from case-study HTML or markdown (folder or single file)"
    )
    parser.add_argument("input_path", nargs="?", default=None,
                        help="Folder containing .html/.htm/.md/.markdown files, or a single file")
    parser.add_argument("--manifest", default=None,
                        help="Path to the manifest .jsonl file (default: gig_manifest.jsonl next to the input folder, "
                             "e.g. input big_crawl/gig -> big_crawl/gig_manifest.jsonl)")
    parser.add_argument("--ping", action="store_true", help="Send one trivial request to test model/backend health, then exit")
    args = parser.parse_args()

    if args.ping:
        ping_model()
        raise SystemExit(0)

    if args.input_path is None:
        parser.error("input_path is required unless using --ping")

    input_path = Path(args.input_path)
    manifest_path = Path(args.manifest) if args.manifest else input_path.parent / "gig_manifest.jsonl"
    debug_log(f"Manifest: {manifest_path}")

    run_batch(input_path, manifest_path)