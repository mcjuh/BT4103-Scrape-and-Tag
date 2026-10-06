# Using the labeller and the evaluator

Run every command from the project root (`BT4103-Scrape-and-Tag/`).

## Setup (once)
1. `.env` in the project root has `SOCLAAS_BASE_URL` and `SOCLAAS_API_KEY` (copy `.env.example`).
2. Python packages: `py -3 -m pip install openai python-dotenv`.
3. `data/output/hirers.csv` and `data/output/providers.csv` exist. They come from `classifier_extractor/extract.py`.

## 1. Label gig-provider pairs: `label.py`
```
python run.py label --max-pairs 50
```
- Each (gig, provider) pair is scored for relevance by the LLM with five methods: `rg_2l`, `rg_3l`,
  `rg_4l`, `rg_s04`, and `rg_3l_multi` (the average of RG-3L over all three models). Every score is 0-1,
  and higher means more relevant.
- `--max-pairs N` sets how many pairs to score (default 50). Pairs go gig by gig: all providers for the
  first gig, then the next gig. There are 154 providers, so `--max-pairs 154` gives one complete ranking
  for the first gig.
- Each pair costs 6 LLM calls. SOCLAAS allows about 1 call per second, so 50 pairs take about
  5 minutes. Don't run two LLM scripts at the same time: they share the same rate limit.
- It's safe to stop and rerun. Calls already made are skipped, so raising `--max-pairs` only pays for
  the new pairs.

**Outputs**
| File | What's in it |
|---|---|
| `data/output/relevance_scores.csv` | One row per pair: `hirer_file`, `provider_file`, the titles, `routed_model`, `hirer_industry`/`provider_industry`/`same_industry` (from the CSVs' industry column; `same_industry` is blank if either side is untagged), and one score column per method. Rebuilt at the end of every run. |
| `data/manifests/relevance_labels.jsonl` | One line per LLM call, with the label probabilities, for debugging. |

A blank `rg_3l_multi` means one of the three models failed on that pair. Rerun to fill it in.

## 2. Score predictions against the gold labels: `evaluate.py`
```
py -3 labeller/evaluate.py data/output/relevance_scores.csv rg_3l
py -3 labeller/evaluate.py data/output/relevance_scores.csv rg_2l rg_3l rg_3l_multi --per-gig per_gig.csv
```
- The first argument is a predictions CSV. After that, list one or more method names to score.
- The gold labels are in `labeller/experiments/gold.json`: 18 gigs, with every provider graded
  from 0 (not relevant) to 3 (would shortlist). Use `--gold` to point at a different file.
- `--per-gig out.csv` also writes the results for each gig.

**Predictions CSV format**. There is one row per (gig, provider) pair, in either layout:

*Wide*: one column per method. This is the format `label.py` writes.
```
hirer_file,provider_file,rg_2l,rg_3l
pwc.com__...shipping-case-study-html.md,ey.com__en_gl_people_cedric-foray.md,0.85,0.59
```
*Long*: a `method` column and a `score` column. This layout is handy for scores from other tools.
```
gig,provider,method,score
pwc.com__...shipping-case-study-html.md,ey.com__en_gl_people_cedric-foray.md,my_method,0.42
```
Gig and provider values are the `source_file` names from `hirers.csv` and `providers.csv`. A higher
score means more relevant. Blank scores are skipped.

**Reading the output**
```
method             gigs  pairs  NDCG@10 [95% CI]      NDCG@5  tau-b  AUC    relevant scored  pooled Spearman  p vs rg_2l@...
rg_2l@qwen3.8:27b  1     40     0.844 [0.844, 0.844]  0.923   0.504  1.000  1.000            0.568            -
rg_3l@qwen3.6:35b  1     40     0.481 [0.481, 0.481]  0.593   0.342  0.829  1.000            0.424            1.000 (1 gigs)
```
| Column | Meaning |
|---|---|
| NDCG@10 | The main metric: how well the top 10 of each gig's ranking matches the gold grades. 1.0 is perfect. The mean over gigs is shown with a 95% interval. |
| NDCG@5 | The same, for the top 5. |
| tau-b, AUC | Agreement with the gold grades over the whole ranking. AUC is the chance that a relevant provider (grade 2 or 3) is scored above an irrelevant one. |
| relevant scored | The share of each gig's relevant providers that the predictions scored at all. If this is low, the ranking left the right people out, even when NDCG looks good. |
| pooled Spearman | Whether scores mean the same thing across gigs. This matters if you threshold scores, for example "show matches above 0.5". |
| p vs ... | Given only when you pass several methods. It's a paired test against the first method. Below 0.05 means the difference is unlikely to be chance. |

**Things to know**
- Only the 18 gold gigs are scored, so predictions for other gigs are ignored. Run `label.py` over
  those gigs before evaluating its output.
- If none of the providers scored for a gig is relevant, that gig can't be ranked. The script says so
  and leaves the gig out.
- With fewer than about 5 gigs, the interval and p-value mean little.
- The gold labels were written by Claude, not a person. `experiments/spotcheck/` has a sheet for
  checking a sample by hand.

## 3. The prompt experiment (optional)
To compare every prompt on every model, see [experiments/README.md](experiments/README.md):
```
py -3 labeller/experiments/run_grid.py      # about 17k LLM calls, about 5 hours, resumable
py -3 labeller/experiments/analyze.py       # tables -> labeller/experiments/results/report.md
```
