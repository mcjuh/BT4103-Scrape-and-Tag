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
- Each document is routed to exactly ONE model, never ensembled across all
  three -- per-doc voting would triple API cost/latency for a labeling/
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
  (docs/manifest.jsonl and docs/providers.csv/hirers.csv) instead of one
  diversification decision reused twice.

MODEL_POOL (from SOCLAAS's available models -- see `client.models.list()`;
excluded: bge-m3/whisper/advanced-vision/qwen3-vl are non-text-generation,
qwen3-coder-next/"coding" are code-specialized, "default"/"test" are
unversioned aliases not suitable for a reproducible record of which model
produced which output, and ornith1.0 is superseded by ornith1.5):
- "ornith1.5:35b" -- this pipeline's original model, NUS/SOCLAAS's own
  tuned model, kept for continuity and its already-proven judgment on this
  exact task. ~200 completion tokens on a trivial classification probe.
- "llama3.1:8b"   -- Meta family: a distinct training lineage from the
  other two, and the cheapest of everything tested (~35 completion tokens
  on the same probe).
- "qwen3.6:27b"    -- Alibaba Qwen family: distinct lineage again, and
  efficient (~150 completion tokens).
Deliberately not three sizes of the same family (e.g. three Qwen
variants), which would share correlated blind spots and defeat the point
of diversifying at all. Parameter count turned out to be a bad proxy for
actual cost here: a same-probe token-usage check across every non-vision
text candidate found qwen3.5:9b (2062 completion tokens) and gemma4:26b
(1212) both defaulting to a verbose internal "thinking" trace despite
being mid-sized, while qwen3.6:27b, qwen3.8:27b, and llama3.1:8b answered
directly in 35-160 tokens -- so qwen3.5:9b was dropped from the pool in
favor of qwen3.6:27b even though it's larger, since it's actually cheaper
per call in practice. Run this same probe again if SOCLAAS's model list
changes before assuming a small model is a cheap one.
"""

import hashlib

MODEL_POOL = ["ornith1.5:35b", "llama3.1:8b", "qwen3.6:27b"]


def model_for_file(filename: str, stage: str) -> str:
    """Deterministic model assignment for one (stage, filename) pair.
    `stage` should be a short constant per calling script (e.g. "classify"
    or "extract") so the two stages diversify independently instead of
    always pairing the same file with the same model twice."""
    digest = hashlib.sha256(f"{stage}:{filename}".encode("utf-8")).hexdigest()
    return MODEL_POOL[int(digest, 16) % len(MODEL_POOL)]
