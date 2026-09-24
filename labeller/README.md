# Labeller

Third role in the pipeline, after scrapper and classifier/extractor: **zero-shot LLM relevance
labels between hirer gigs and provider profiles**, scored with the method from Zhuang et al.,
["Beyond Yes and No: Improving Zero-Shot LLM Rankers via Scoring Fine-Grained Relevance
Labels"](https://arxiv.org/abs/2310.14122) (arXiv:2310.14122).

```
py -3 labeller/label.py [--max-pairs 50]
```
Step-by-step usage for `label.py` and `evaluate.py` is in [USAGE.md](USAGE.md).

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
| `rg_3l_multi` | RG-3L on all 4 models | mean of the four models' `rg_3l` scores |

All scores are normalised to 0-1 (expected relevance / top label value) so they're comparable.

- **Approaches 1-4** use one model per gig, picked by a hash of the gig (the same routing idea
  as `classifier_extractor/llm_pool.py`). Every provider for a gig, under all four prompts, sees
  the same model, so a gig's ranking and the differences between prompts aren't driven by which
  model a pair happened to land on, while the corpus still spreads across models gig by gig.
  (Routing per pair was tried first: `llama3.1:8b` scores clearly irrelevant pairs ~0.2-0.9 where
  the Qwen models give ~0, so a gig's ranking mostly reflected the model assignment.)
- **Approach 5** (not in the paper) scores the paper's best prompt, RG-3L (tied with RG-S(0,4)),
  on every model in the pool and averages. It reuses the routed model's `rg_3l` call, so a pair
  costs **7 LLM calls**, not 8. It's only reported when all four models succeeded.

## Adaptations from the paper
- Prompt text is the paper's verbatim (labels listed most relevant first, as in the paper), plus
  one line ("Output only the label." / "Output only the number."), since chat-tuned models
  otherwise open with "I would rate..." instead of the label.
- Thinking is disabled (`chat_template_kwargs.enable_thinking = False`). With it on, a model that
  reasons first gets its reasoning scored instead of the answer. Probed on all four pool models: with
  it off, each emits the label as its first token with probabilities for the alternatives.
- Each label is scored by its first token among the top-20 logprobs at the answer position
  (the labels are chosen so their first tokens differ). Surface variants of the same label
  ("Not", " not", "N") are summed. A label outside the top 20 gets a floor just below the lowest
  logprob seen.
- Provider records carry no name (the provider schema has none, and extract.py anonymises
  provider pages), so a name can't sway the score.

## Replaces the earlier plans
- **Binary model vs. hand-tuned weighted-sum score.** The binary model becomes the `rg_2l`
  baseline, and the fine-grained labels take the place of the weighted sum.
- **`speciality_ids` overlap / embedding similarity matching.** Dropped: there's no prefilter, and
  every requested pair goes to the LLM judge.

## Cost
Every gig x every provider is `hirers x providers x 7` calls, so the whole cross-product gets
large fast. `--max-pairs` (default 50) caps a run, taking pairs gig by gig, so a small run gives a
complete ranking for the first gig(s). Reruns skip calls already recorded.

## Evaluating predictions
```
py -3 labeller/evaluate.py docs/relevance_scores.csv rg_2l rg_3l rg_3l_multi [--per-gig out.csv]
```
Scores any predictions CSV against the graded gold labels in `experiments/gold.json` (18 gigs,
every provider graded 0-3): NDCG@10 with a bootstrap interval, NDCG@5, Kendall tau-b, AUC, how many
of each gig's relevant providers were scored at all, and pooled Spearman (whether scores are
comparable across gigs). With several methods it adds a paired test against the first. Input: a
gig column (`hirer_file`/`gig`), a provider column (`provider_file`/`provider`), and either one
score column per method (`relevance_scores.csv`'s shape) or `method` + `score` columns. Only gigs
in the gold file count, so label.py output is only informative once it has scored those gigs.

## Prompt experiments
[`experiments/`](experiments/README.md) compares the prompts (the five above plus a Yes/No baseline and
three ablations) on all four models against graded gold labels for 18 gigs, reporting NDCG@10 and
whether combining models beats one. Results land in `experiments/results/report.md`.
