# Labeller prompt experiments

> **Status.** `results/` (the grid, `candidates.json`) was run against an earlier set of 18 gigs from
> `docs/hirers.csv`, graded 0-3 by Claude, which is no longer in the repo: the `gold.json` here was
> regenerated from the client's workbook (30 gigs, one intended showcase each) before the first commit,
> so it no longer matches. `run_grid.py` stops on it (its gig ids are not in `hirers.csv`) and
> `analyze.py` has nothing to join the saved grid to. Running this again means pointing `run_grid.py` at
> the client set (`client_testset/`) or restoring an 18-gig gold. The Design section below describes
> the saved grid, not the current `gold.json`.

Which relevance prompt ranks providers best for a gig? This folder runs every prompt variant on
every pool model over a fixed candidate set and scores the rankings against graded gold labels.

```
py -3 labeller/experiments/run_grid.py [--rps 1.0] [--workers 8]   # the LLM calls (resumable)
py -3 labeller/experiments/analyze.py                                # tables -> results/report.md
```

## Design
- **Gold labels of the saved grid (no longer in the repo):** 18 gigs from `docs/hirers.csv`, chosen to span the providers'
  domains (finance/ERP, insurance, banking, AI, cyber, tax, M&A, supply chain, sports, public
  sector, sales). Every one of the 154 providers was graded against each gig on a 0-3 rubric
  (in the file), so the labels are complete rather than pooled from the systems being compared.
  135 graded pairs: 13 at grade 3, 37 at 2, 85 at 1; the rest 0.
  **They were silver labels:** written by Claude (claude-opus-5), a model outside the pool, from the
  full gig and profile text before any experiment score was seen, and never spot-checked by hand
  (`spotcheck/` is that sheet, unfilled).
- **Current `gold.json`:** the client's 30 test gigs, each with one intended showcase graded 0-3 from the client's four bands (OBVIOUS 3, SUBTLE 2, PARTIAL 1, NEAR-MISS 0), built by `build_gold.py` from the client workbook. The
  workbook was written by the client with an LLM, so it is an ordinal development check, not ground truth.
  Its other 29 showcases per gig are unlabelled and score as grade 0, and the 4 NEAR-MISS gigs have no
  relevant showcase.
- **Candidates** (`results/candidates.json`): per gig, every graded provider plus seeded random
  grade-0 providers, 40 in total. This is the paper's re-ranking setting (it re-ranks BM25's top 100).
- **Conditions** (8 prompts x 3 models = 24 calls per pair, 17,280 in total; the first run also had llama3.1:8b, since dropped):

  | id | prompt |
  |---|---|
  | `yn` | Yes/No baseline (the paper's RG-YN) |
  | `rg_2l`, `rg_3l`, `rg_4l`, `rg_s04` | the four prompts `label.py` uses (paper wording) |
  | `rg_s02` | ablation: a 0-2 scale |
  | `rg_3l_asc` | ablation: RG-3L with labels listed least relevant first |
  | `rg_3l_gig` | ablation: RG-3L worded for the domain ("gig" / "provider profile") |

- **Scoring** from the same calls: expected relevance (the paper's and `label.py`'s score), peak
  relevance, and the single generated label.
- **Multi-model**: per prompt, the pool models' scores combined by mean score (`label.py`'s
  `rg_3l_multi`), mean rank, and mean per-model z-score, against label.py's routed single model.
- **Metrics**: NDCG@10 (the paper's metric) as the expectation over random tie-breaking, plus
  NDCG@5, Kendall tau-b vs gold, AUC, and calibration of raw scores across gigs. 95% bootstrap
  intervals and paired permutation tests are both taken over gigs, so with the saved grid's 18 gigs only large
  differences reach significance.

## Rate limit
SOCLAAS returns bare 429s (no headers) past a burst of ~60 and sustains ~1 request/s, shared
across models. `run_grid.py` paces all workers to `--rps` and disables the OpenAI client's hidden
retries; the full grid takes ~5 hours at 1 rps. It can be stopped at any time and rerun; recorded
calls are skipped. `analyze.py` scores only gigs whose grid is complete, so it can run mid-way.
The run holds the team's shared API budget while it's going.

## Files
- `gold.json` (the client set), `build_gold.py`, `client_testset/`, `prompts/` -- inputs
- `results/grid.jsonl` -- one line per call (label probabilities, log-likelihoods, latency)
- `results/candidates.json`, `results/report.md`, `results/per_gig.csv`, `results/run_grid.log`
