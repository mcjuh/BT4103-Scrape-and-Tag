# -*- coding: utf-8 -*-
"""GLM client for the trial (docs/GLM-TRIAL.md): SOCLAAS model x-test-1 through the OpenAI client.

Thinking cannot be switched off, so reasoning eats into max_tokens; an empty `content` means it ate
all of it, and the call is retried with more room."""

import json
import os
import re
import time
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI, RateLimitError

ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")

MODEL = "x-test-1"
# Thinking cannot be turned off, but the gateway passes `reasoning_effort` through. None sends nothing (the model's default).
REASONING_EFFORT = os.environ.get("GLM_REASONING_EFFORT") or None
client = OpenAI(base_url=os.environ["SOCLAAS_BASE_URL"], api_key=os.environ["SOCLAAS_API_KEY"],
                max_retries=0, timeout=900)


def chat(prompt: str, max_tokens: int = 10000, tries: int = 4, temperature: float = 1.0) -> str:
    """The reply's `content`. Retries on an empty reply (more tokens each time) and on API errors."""
    last, waits, attempt = None, 0, -1
    while attempt < tries - 1:
        attempt += 1
        try:
            r = client.chat.completions.create(
                model=MODEL, messages=[{"role": "user", "content": prompt}],
                max_tokens=max_tokens + 2000 * attempt, temperature=temperature,
                **({"reasoning_effort": REASONING_EFFORT} if REASONING_EFFORT else {}))
            content = (r.choices[0].message.content or "").strip()
            if content and r.choices[0].finish_reason != "length":
                return content
            last = "empty content" if not content else "reply cut off at max_tokens"
        except RateLimitError as e:
            # the gateway's per-key queue is full: wait it out, and do not count it as a failed try
            waits += 1
            if waits > 20:
                raise RuntimeError(f"GLM rate limited {waits} times: {e}")
            time.sleep(min(15 * waits, 120))
            continue
        except Exception as e:  # noqa: BLE001 - gateway errors vary
            last = f"{type(e).__name__}: {e}"
        time.sleep(2 + 3 * attempt)
    raise RuntimeError(f"GLM call failed after {tries} tries: {last}")


def chat_json(prompt: str, **kw) -> dict:
    """chat(), parsed as one JSON object (a ```json fence or surrounding prose is tolerated)."""
    text = chat(prompt, **kw)
    m = re.search(r"```(?:json)?\s*(.*?)```", text, re.S)
    if m:
        text = m.group(1)
    start, end = text.find("{"), text.rfind("}")
    if start < 0 or end < start:
        raise ValueError("no JSON object in reply")
    return json.loads(text[start:end + 1])
