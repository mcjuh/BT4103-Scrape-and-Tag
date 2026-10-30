# -*- coding: utf-8 -*-
"""
Model pool shared by classify.py, industry.py and extract.py.

The labels and records this pipeline produces are LLM output standing in
for hand-made data, so relying on one model would bake its quirks into the
whole corpus. Instead each file is routed to one model from MODEL_POOL.

- The model is a hash of (stage, filename), so a rerun gives the same file
  the same model and no shared counter is needed.
- Each stage uses its own salt, so the model that classified a page is not
  necessarily the one that extracts it.
- reviewer_for_file picks a different model to review a hirer record.

MODEL_POOL is the chat models the API serves. Left out on purpose:
- bge-m3 and whisper-large-v3 are not chat models.
- Aliases (default, coding, test, ...) would count a model twice.
- qwen3.5:9b and gemma4:26b cannot turn "thinking" off, so calls are too
  slow (qwen3.5:9b hits the gateway timeout).
- qwen3-coder-next is code-specialised.
- ornith1.5:35b and llama3.1:8b were dropped by the team. llama3.1 ignored
  the anonymisation rules and copied prompt examples. Older records still
  carry these names.
"""

import hashlib

MODEL_POOL = [
    "qwen3.8:27b",       # Alibaba Qwen (served before as the "qwen3.6:27b" alias)
    "qwen3.6:35b",       # Alibaba Qwen, 35B-A3B mixture-of-experts
    "qwen3-vl:32b",      # Alibaba Qwen, vision-language (text-only use here)
]


def model_for_file(filename: str, stage: str) -> str:
    """Deterministic model assignment for one (stage, filename) pair.
    `stage` should be a short constant per calling script (e.g. "classify"
    or "extract") so the two stages diversify independently instead of
    always pairing the same file with the same model twice."""
    digest = hashlib.sha256(f"{stage}:{filename}".encode("utf-8")).hexdigest()
    return MODEL_POOL[int(digest, 16) % len(MODEL_POOL)]


def reviewer_for_file(filename: str, author_model: str) -> str:
    """Deterministic reviewer for a record `author_model` produced: always a
    DIFFERENT pool model, so no model grades its own output (the
    self-preference bias Schaffelder & Gatt measure). Hashed like
    model_for_file, so a rerun picks the same reviewer."""
    others = [m for m in MODEL_POOL if m != author_model]
    digest = hashlib.sha256(f"review:{filename}".encode("utf-8")).hexdigest()
    return others[int(digest, 16) % len(others)]
