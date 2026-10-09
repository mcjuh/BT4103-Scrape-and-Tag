# Labeller

Third role in the pipeline, after scraper and classifier/extractor: **zero-shot LLM relevance
labels between hirer gigs and provider profiles**, scored with the method from Zhuang et al.,
["Beyond Yes and No: Improving Zero-Shot LLM Rankers via Scoring Fine-Grained Relevance
Labels"](https://arxiv.org/abs/2310.14122) (arXiv:2310.14122).

```
python run.py label [--max-pairs 50]
```
Step-by-step usage for `label.py` and `evaluate.py` is in [USAGE.md](USAGE.md).

Reads `data/output/hirers.csv` and `data/output/providers.csv` (from `classifier_extractor/extract.py`).
Writes `data/manifests/relevance_labels.jsonl` (one line per LLM call) and rebuilds
`data/output/relevance_scores.csv` (one row per pair, all five scores side by side) at the end of
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

- **Approaches 1-4** use one model per gig, picked by a hash of the gig (the same routing idea
  as `classifier_extractor/llm_pool.py`). Every provider for a gig, under all four prompts, sees
  the same model, so a gig's ranking and the differences between prompts aren't driven by which
  model a pair happened to land on, while the corpus still spreads across models gig by gig.
  (Routing per pair was tried first: `llama3.1:8b`, since dropped from the pool, scored clearly irrelevant pairs ~0.2-0.9 where
  the Qwen models give ~0, so a gig's ranking mostly reflected the model assignment.)
- **Approach 5** (not in the paper) scores the paper's best prompt, RG-3L (tied with RG-S(0,4)),
  on every model in the pool and averages. It reuses the routed model's `rg_3l` call, so a pair
  costs **6 LLM calls**, not 7. It's only reported when all three models succeeded.

## Adaptations from the paper
- Prompt text is the paper's verbatim (labels listed most relevant first, as in the paper), plus
  one line ("Output only the label." / "Output only the number."), since chat-tuned models
  otherwise open with "I would rate..." instead of the label.
- Thinking is disabled (`chat_template_kwargs.enable_thinking = False`). With it on, a model that
  reasons first gets its reasoning scored instead of the answer. Probed on every pool model: with
  it off, each emits the label as its first token with probabilities for the alternatives.
- Each label is scored by its first token among the top-20 logprobs at the answer position
  (the labels are chosen so their first tokens differ). Surface variants of the same label
  ("Not", " not", "N") are summed. A label outside the top 20 gets a floor just below the lowest
  logprob seen.
- Provider records carry no name (the provider schema has none, and extract.py anonymises
  provider pages), so a name can't sway the score.

## Grading the platform sample format (`grade_pairs.py`)

`grade_pairs.py` is the grader for the new standard format (`data/output/platform_sample/`). It is
self-contained and independent of `label.py` and `judge_pools.py`, which grade the older
`hirers.csv` / `providers.csv` format (`judge_pools.py` reads the ranker's `data_sat/` pools). One model
grades each run: `qwen3.8:27b` by default, the grader of the ranker's labels (`ranker/pipeline/label.md`).

```
python run.py grade --dry-run                                   # show a prompt, call nothing
python run.py grade --max-pairs 20                              # smoke test
python run.py grade --pairs data/output/platform_sample/pilot_pairs.json   # the 30-pair pilot
python run.py grade                                             # every gig x every provider
python run.py grade --export                                    # log -> data/output/gig_grades.csv
```
Needs `SOCLAAS_BASE_URL` and `SOCLAAS_API_KEY` in a gitignored `.env` at the repo root (copy
`.env.example`). Offline tests (no API): `python -m unittest labeller/test_grade_pairs.py`.

**The prompt** (`prompts/rubric_01_v5.md`, prompt version `rubric_01.v5`). The model answers `"<grade> <score>"`
(e.g. `2 0.62`): a grade 0-3 and a score inside that grade's range (0: 0-0.16, 1: 0.17-0.49, 2: 0.50-0.83,
3: 0.84-0.99). It judges content fit first, then the practical terms, which can only lower the result:
- **Seniority is the main term.** The same level has no effect; one level apart, in either direction, caps
  the grade at 2; mid against expert caps it at 1. The provider's level comes from `years_experience` when
  the record has it, then the years in the text, then the title.
- **Mode of work.** Execution (drafting, building, preparing) against advisory (reviewing, recommending,
  steering), read from the gig's deliverable and from what the provider says they did. Either side can be
  mixed, and a mixed side never mismatches; a clear mismatch caps the grade at 2.
- **Availability** (start date and days a week) counts less than seniority and mode of work. A minor
  mismatch (up to 3 weeks late, one day a week fewer, or only shorter or longer engagements) lowers the
  score a little and never the grade; a serious one (more than 6 weeks late, or two or more days fewer)
  caps the grade at 2.
- **Budget counts least.** It never lowers the grade: only a rate more than about 40% over the level's
  day-rate band lowers the score, by about 0.05 inside its grade. A hirer's own budget may be a guess, and
  the gig usually states none.

The data carries only some of this. The provider's `availability` and `rate` are text and are shown to the
model; the gig has no budget, seniority or start date, only the extractor's "Engagement duration" estimate
(shown as "Estimated duration"), and neither side states its level directly. So the model works out the
gig's terms and the provider's level from the text, the way `enricher/` does with an LLM judge (`judge_*.md`:
mid / senior / expert by stated years and title). The budget bands are `enricher/rate_card.json`'s hourly
bands x 8 (mid S$480-960, senior S$720-1,600, expert S$1,200-2,800 a day). Name, links and tags are never
shown: tags are user input on the platform and taken as they are, and `--with-tags` adds the SkillsFuture
category / specialisation as an ablation. `rubric_01_v4.md` is kept as it was, for the `rubric_01.v4.1` run
in the log.

**Inputs.** The platform sample CSVs by default. `--gigs-csv` / `--providers-csv` also take the schema v2
`hirers.json` / `providers.json` (see `docs/schema_v2.md`), mapped like this (a v2 record has no gig or provider
id, so its `source_file` is the id and `--gigs 1-10` counts by position):

| Prompt line | Sample column | Schema v2 field |
|---|---|---|
| Scope | `short_gig_description` | `short_description` |
| Notes from the hirer | `additional_notes` (optional) | `additional_notes` |
| Estimated duration | the "Engagement duration:" sentence | `duration_weeks_min` / `duration_weeks_max` |
| Years of experience | `years_experience` (optional) | `years_experience` |
| Services | `services_i_offer` | `services[]` as `title: detail` |
| Achievements | `relevant_achievements` | `achievements[]` as bullets |
| Technical proficiency | `technical_proficiency` | `technical_proficiency[]` as `category: skills` |
| Credentials | `credentials` | `credentials[]` joined with `;` |

`data/output/crafted_gigs/` holds 30 hand-written v2 gigs for the ranker (see its README).

**The score.** The grade is the most probable band from the answer-position logprobs, and the score is
the band-weighted expectation clipped into that band, so the two always agree (`round(score * 3) ==
grade`). Thinking is off, as in `label.py`. The band edges are not fitted to data: they are the points
where `round(score * 3)` changes, the rule `judge_pools.py` and the ranker's `grade_from_score()` use to
turn a score back into a grade. Treat the score's second decimal as noise; the band is the part to trust.

**Outputs.** `data/manifests/gig_grades.jsonl` is the log (one line per call, per model and prompt version; reruns
skip what is already graded, so a stopped run resumes). `--export` writes `data/output/gig_grades.csv`, one row
per pair, model and prompt version. The committed log is the full run: all 900 gigs x providers of the
sample on `qwen3.8:27b` with the earlier prompt `rubric_01.v4.1` (789 pairs at grade 0, 105 at grade 1, 6 at grade 2,
none at 3; no errors). Using several models was tried on the 30-pair pilot and removed: `gemma4:26b` cannot
switch thinking off (about 30 s and 1,900 tokens a call against 0.5 s), and the three Qwens ranked pairs
almost identically (Spearman 0.93-0.95), with no label set yet to show that pooling beats one model.

`data/output/platform_sample/pilot_pairs.json` is the pilot: 10 seeded gigs, each with its best TF-IDF text
match, a mid-ranked provider and a random lower-half one. The similarity only picked the pairs; the
models never see it.

## Replaces the earlier plans
- **Binary model vs. hand-tuned weighted-sum score.** The binary model becomes the `rg_2l`
  baseline, and the fine-grained labels take the place of the weighted sum.
- **`speciality_ids` overlap / embedding similarity matching.** Dropped: there's no prefilter, and
  every requested pair goes to the LLM judge.

## Cost
Every gig x every provider is `hirers x providers x 6` calls, so the whole cross-product gets
large fast. `--max-pairs` (default 50) caps a run, taking pairs gig by gig, so a small run gives a
complete ranking for the first gig(s). Reruns skip calls already recorded.

## Evaluating predictions
```
py -3 labeller/evaluate.py data/output/relevance_scores.csv rg_2l rg_3l rg_3l_multi [--per-gig out.csv]
```
Scores any predictions CSV against the graded gold labels in `experiments/gold.json`: the client's 30 test gigs, each with one intended showcase graded 0-3 from the client's four bands (OBVIOUS 3, SUBTLE 2, PARTIAL 1, NEAR-MISS 0).
The client wrote the workbook with an LLM, so these are an ordinal development check, not measured ground
truth, and the other 29 showcases per gig are scored as grade 0. Metrics: NDCG@10 with a bootstrap interval, NDCG@5, Kendall tau-b, AUC, how many
of each gig's relevant providers were scored at all, and pooled Spearman (whether scores are
comparable across gigs). With several methods it adds a paired test against the first. Input: a
gig column (`hirer_file`/`gig`), a provider column (`provider_file`/`provider`), and either one
score column per method (`relevance_scores.csv`'s shape) or `method` + `score` columns. Only gigs
in the gold file count, and predictions must use its ids (`client_gig_01`..., `client_showcase_01`...: the
`source_file` column of `experiments/client_testset/`). `label.py` reads `data/output/hirers.csv` and
`providers.csv`, so none of the scripts here scores that set yet.

## Prompt experiments
[`experiments/`](experiments/README.md) compares the prompts (the five above plus a Yes/No baseline and
three ablations) on every pool model, reporting NDCG@10 and whether combining models beats one. Its
saved grid was run against an earlier 18-gig set of Claude-written labels that is no longer in the repo,
and `run_grid.py` / `analyze.py` do not currently run against the 30-gig `gold.json`; see its README.
