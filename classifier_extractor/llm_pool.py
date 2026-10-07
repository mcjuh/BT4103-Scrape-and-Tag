# -*- coding: utf-8 -*-
"""
Shared multi-model pool for classifier_extractor's two LLM-calling scripts
(classify.py and extract.py). Every page classify.py labels and every
record extract.py extracts is synthetic/derived data (LLM output standing
in for a hand-labeled or hand-entered ground truth), not raw scraped fact
-- so the same risk that applies to training on synthetic data applies
here: a single generative source compounds its own idiosyncrasies.
Shumailov et al., "AI models collapse when trained on recursively
generated data" (Nature 631, 755-759, 2024) demonstrate the mechanism --
a narrow/single generative distribution loses tail coverage and diversity
over repeated generation, i.e. model collapse. Schaffelder & Gatt,
"Synthetic Eggs in Many Baskets: The Impact of Synthetic Data Diversity on
LLM Fine-Tuning" (Findings of ACL 2026, arXiv:2511.01490) show the direct
mitigation this module implements: synthetic data drawn from MULTIPLE
source models, rather than one, measurably mitigates distribution
collapse and reduces self-preference bias relative to single-source
synthetic data.

Design choices that follow from those two papers:
- Each document is routed to exactly ONE model, never ensembled across the
  whole pool -- per-doc voting would multiply API cost/latency for a labeling/
  extraction task that doesn't need it, and the papers' mitigation is
  about diversifying the CORPUS's source distribution, not about
  per-example consensus.
- Assignment is a deterministic hash of (stage, filename), not a shared
  round-robin counter -- the same file always gets the same model on a
  rerun (reproducible, and safe to parallelize later without a race on
  "whose turn is next"), while still landing roughly evenly across the
  pool over a large corpus.
- classify.py and extract.py hash with different `stage` salts, so the
  model that labeled a given page is not necessarily the same one that
  later extracts its fields -- two independently-diversified corpora
  (data/manifests/classify.jsonl and data/output/providers.csv/hirers.csv) instead of one
  diversification decision reused twice.

MODEL_POOL is every usable distinct chat model SOCLAAS serves (from
`client.models.list()`), so each one's output can be compared on the same
corpus. Left out:
- bge-m3 (embeddings) and whisper-large-v3 (audio transcription): not chat
  models.
- Aliases, which would just count a pool member twice: "default" ->
  qwen3.6:35b; "coding" and "qwen3.6:27b" -> qwen3.8:27b; "advanced-vision"
  and "test" -> qwen3-vl:32b; "ornith1.0:35b" -> ornith1.5:35b. Records
  produced before the pool was widened carry "qwen3.6:27b" -- that's
  qwen3.8:27b.
- qwen3.5:9b: it can't switch "thinking" off, so an extraction takes ~75s,
  right at SOCLAAS's own gateway cutoff -- its calls 502 whatever the
  client timeout, so the files routed to it would error on every run.
- qwen3-coder-next: code-specialised, not a fit for prose extraction.
- ornith1.5:35b: the pipeline's original model, dropped at the team's
  request. Records extracted before then still carry it.
- gemma4:26b: it can't switch "thinking" off either; an extraction took
  ~30-45s and ~1.5-2k completion tokens, versus 1-10s for the rest.
- llama3.1:8b: dropped 2026-09-28 at the team's request. It ignored the
  anonymisation rules (named a person's former regulator employer), copied
  prompt examples verbatim, and returned off-schema keys. Records and
  classify/industry labels produced before then still carry it.
Rerun that listing if SOCLAAS's model list changes. classify.py leaves
"thinking" on for every model; extract.py and industry.py switch it off.
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
