# -*- coding: utf-8 -*-
"""Probe which request argument switches thinking off for a SOCLAAS model (default x-test-1, GLM).

Run on the NUS network with SOCLAAS_* in .env:  python glm/probe_thinking.py [--model x-test-1]

First it prints what the gateway says about its serving software (/v1/models fields and response
headers). Then it sends one tiny prompt per variant and prints latency, completion tokens, reasoning
size and the reply. A variant works when reasoning is 0 and the reply is non-empty and fast."""

import argparse
import json
import os
import time
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

PROMPT = "Reply with only the number: what is 12 times 7?"

VARIANTS = [
    ("baseline (nothing)", {}, ""),
    ("chat_template_kwargs.enable_thinking=false  [GLM model card, vLLM/SGLang]",
     {"extra_body": {"chat_template_kwargs": {"enable_thinking": False}}}, ""),
    ("top-level enable_thinking=false", {"extra_body": {"enable_thinking": False}}, ""),
    ("thinking={type: disabled}  [Z.ai API]", {"extra_body": {"thinking": {"type": "disabled"}}}, ""),
    ("both chat_template_kwargs and thinking",
     {"extra_body": {"chat_template_kwargs": {"enable_thinking": False}, "thinking": {"type": "disabled"}}}, ""),
    ("reasoning_effort=none", {"extra_body": {"reasoning_effort": "none"}}, ""),
    ("reasoning_effort=minimal", {"extra_body": {"reasoning_effort": "minimal"}}, ""),
    ("reasoning_effort=low", {"extra_body": {"reasoning_effort": "low"}}, ""),
    ("think=false  [Ollama native]", {"extra_body": {"think": False}}, ""),
    ("/no_think suffix", {}, "\n\n/no_think"),
]


def reasoning_size(msg) -> int:
    d = msg.model_dump() if hasattr(msg, "model_dump") else {}
    r = d.get("reasoning_content") or d.get("reasoning") or ""
    return len(r)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="x-test-1")
    ap.add_argument("--max-tokens", type=int, default=800)
    args = ap.parse_args()
    client = OpenAI(base_url=os.environ["SOCLAAS_BASE_URL"], api_key=os.environ["SOCLAAS_API_KEY"],
                    max_retries=0, timeout=300)

    print("== /v1/models entry (owned_by 'vllm' + max_model_len means vLLM; 'library' means Ollama)")
    try:
        for m in client.models.list().data:
            if m.id == args.model:
                print(json.dumps(m.model_dump(), indent=1, default=str))
    except Exception as e:  # noqa: BLE001
        print("models.list failed:", type(e).__name__, e)

    for name, kw, suffix in VARIANTS:
        t0 = time.perf_counter()
        try:
            raw = client.chat.completions.with_raw_response.create(
                model=args.model, messages=[{"role": "user", "content": PROMPT + suffix}],
                max_tokens=args.max_tokens, temperature=0, **kw)
            r = raw.parse()
            dt = time.perf_counter() - t0
            msg = r.choices[0].message
            content = (msg.content or "").strip().replace("\n", " ")
            details = getattr(r.usage, "completion_tokens_details", None)
            rtok = getattr(details, "reasoning_tokens", None)
            print(f"\n[{name}]\n  {dt:5.1f}s  completion_tokens={r.usage.completion_tokens}  reasoning_tokens={rtok}"
                  f"  reasoning_chars={reasoning_size(msg)}  think_tag_in_content={'<think' in content.lower()}"
                  f"  finish={r.choices[0].finish_reason}\n  reply: {content[:120]!r}")
            if name.startswith("baseline"):
                hdrs = {k: v for k, v in raw.headers.items()
                        if k.lower().startswith(("server", "x-", "via", "openai", "litellm"))}
                print("  response headers:", hdrs)
        except Exception as e:  # noqa: BLE001
            print(f"\n[{name}]\n  {time.perf_counter() - t0:5.1f}s  ERROR {type(e).__name__}: {str(e)[:200]}")


if __name__ == "__main__":
    main()
