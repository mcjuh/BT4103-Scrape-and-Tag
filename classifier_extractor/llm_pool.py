# -*- coding: utf-8 -*-
"""
Model pool shared by classify.py, industry.py and extract.py.

The labels and records this pipeline produces are LLM output standing in
for hand-made data. Each file is routed to one model from MODEL_POOL.

- The model is a hash of (stage, filename), so a rerun gives the same file
  the same model and no shared counter is needed.
- The stage name is included in the hash, so classification and extraction
  choose their models separately and may use different models.
- reviewer_for_file picks a different model to review a hirer record.

MODEL_POOL is the chat models the API serves. Left out:
- qwen3.5:9b and gemma4:26b cannot turn thinking off, so calls are too
  slow (qwen3.5:9b hits the gateway timeout).
- qwen3-coder-next (code-specialised).
- ornith1.5:35b and llama3.1:8b were dropped; llama3.1 ignored
  the anonymisation rules and copied prompt examples.
"""

import hashlib

MODEL_POOL = [
    "qwen3.8:27b",       # Alibaba Qwen, 27B-A3B mixture-of-experts
    "qwen3.6:35b",       # Alibaba Qwen, 35B-A3B mixture-of-experts
    "qwen3-vl:32b",      # Alibaba Qwen, vision-language (text-only use here)
]


def model_for_file(filename: str, stage: str) -> str:
    """Choose a model deterministically from the filename and stage.
    The same filename and stage always pick the same model. Different stages
    are chosen independently, but may still pick the same model.
    """
    digest = hashlib.sha256(f"{stage}:{filename}".encode("utf-8")).hexdigest()
    return MODEL_POOL[int(digest, 16) % len(MODEL_POOL)]


def reviewer_for_file(filename: str, author_model: str) -> str:
    """Deterministic reviewer for a record `author_model` produced: always a different pool
    model, so no model grades its own output. Hashed like model_for_file, so a rerun picks the
    same reviewer."""
    others = [m for m in MODEL_POOL if m != author_model]
    digest = hashlib.sha256(f"review:{filename}".encode("utf-8")).hexdigest()
    return others[int(digest, 16) % len(others)]
