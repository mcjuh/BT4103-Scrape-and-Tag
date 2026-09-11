# Labeller

Third role in the pipeline, after scrapper and classifier/extractor: **zero-shot LLM relevance
labels between hirer gigs and provider profiles**, scored with the method from Zhuang et al.,
["Beyond Yes and No: Improving Zero-Shot LLM Rankers via Scoring Fine-Grained Relevance
Labels"](https://arxiv.org/abs/2310.14122) (arXiv:2310.14122).

```
py -3 labeller/label.py [--max-pairs 50]
```

Reads `../docs/hirers.csv` and `../docs/providers.csv` (from `classifier_extractor/extract.py`).
Writes `../docs/relevance_labels.jsonl` (one line per LLM call) and rebuilds
`../docs/relevance_scores.csv` (one row per pair, all five scores side by side) at the end of
every run. Run-once: it scores what's asked for and exits.

## Method
Pointwise ranking: each (gig, provider) pair is one prompt, with the gig as the paper's
**query** and the provider profile as its **document**. Rather than Yes/No, the model picks from
fine-grained relevance labels, and the score is the paper's **expected relevance**: a softmax
over the log-likelihood the model gives each label, weighted by label value. The paper shows this
beats parsing the single generated label, which causes ties; parsing is kept only as a fallback
when a response carries no usable logprobs (recorded as `"scoring": "parsed"`).

| Approach | Prompt | Labels (value) |
|---|---|---|
| `rg_2l` | RG-2L | Not Relevant (0), Relevant (1) |
| `rg_3l` | RG-3L | Not Relevant (0), Somewhat Relevant (1), Highly Relevant (2) |
| `rg_4l` | RG-4L | ... + Perfectly Relevant (3) |
| `rg_s04` | RG-S(0,4) | "From a scale of 0 to 4" (0-4) |
| `rg_3l_multi` | RG-3L on all 3 models | mean of the three models' `rg_3l` scores |

All scores are normalised to 0-1 (expected relevance / top label value) so they're comparable.

- **Approaches 1-4** use one model per pair, picked by a hash of the pair (the same routing idea
  as `classifier_extractor/llm_pool.py`). All four prompts for a pair see the same model, so
  differences between them are down to the prompt, while the corpus still spreads across models.
- **Approach 5** (not in the paper) scores the paper's best prompt, RG-3L (tied with RG-S(0,4)),
  on every model in the pool and averages. It reuses the routed model's `rg_3l` call, so a pair
  costs **6 LLM calls**, not 7. It's only reported when all three models succeeded.

## Adaptations from the paper
- Prompt text is the paper's verbatim, plus one line ("Output only the label." / "Output only the
  number."), since chat-tuned models otherwise open with "I would rate..." instead of the label.
- Thinking is disabled (`chat_template_kwargs.enable_thinking = False`). With it on, ornith1.5 and
  qwen3.6 reason first and the scored token comes from the reasoning, not the answer.
- Each label is scored by its first token among the top-20 logprobs at the answer position
  (the labels are chosen so their first tokens differ). A label outside the top 20 gets a floor
  just below the lowest logprob seen.
- Provider records carry no name (the provider schema has none, and extract.py anonymises
  provider pages), so a name can't sway the score.

## Replaces the earlier plan
This role was previously only a plan to match by `speciality_ids` overlap or embedding
similarity. That's dropped: there's no prefilter, and every requested pair goes to the LLM judge.

## Cost
Every gig x every provider is `hirers x providers x 6` calls, so the whole cross-product gets
large fast. `--max-pairs` (default 50) caps a run, taking pairs gig by gig, so a small run gives a
complete ranking for the first gig(s). Reruns skip calls already recorded.
