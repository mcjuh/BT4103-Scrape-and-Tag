# BT4103 Scrape and Tag

Builds a seed dataset for **GreyGigz**, a gig marketplace for experienced professionals. The
pipeline crawls consulting and talent sites, uses LLMs to sort each page into a provider profile,
a hirer gig, or noise, extracts records shaped to the ML schemas, and scores how relevant each
provider is to each gig.

## Pipeline

```
scrapper/crawl.py                  ->  docs/unprocessed/*.md
classifier_extractor/classify.py   ->  docs/{provider,hirer,uncertain,ignore}/  +  docs/manifest.jsonl
classifier_extractor/extract.py    ->  docs/providers.csv, docs/hirers.csv       (ML schema v1)
labeller/label.py                  ->  docs/relevance_scores.csv
monitor/dashboard.py                   read-only view of all of the above
```

Each stage talks to the next only through files in `docs/`, never through Python imports, so any
stage can be rerun or swapped out on its own. Every script is run-once: it processes what's
waiting, skips what's already done, and exits.

## Layout

| Path | What it is |
|---|---|
| `scrapper/` | `crawl.py` (crawl4ai best-first deep crawl, saved as pruned Markdown) and `seeds.md` (start URLs) |
| `classifier_extractor/` | `classify.py`, `extract.py`, `llm_pool.py`, `prompts/`, and the `ML_*_schema_v1.md` JSON Schemas extraction is validated against |
| `labeller/` | `label.py`: zero-shot relevance scoring of gig/provider pairs ([Zhuang et al., 2023](https://arxiv.org/abs/2310.14122)); see `labeller/README.md` |
| `monitor/` | `dashboard.py`: local dashboard at http://localhost:8765 |
| `docs/` | The data lake: crawled pages by bucket, manifests, extracted CSVs |
| `context.md` | Full design notes and the reasoning behind them |

## Setup

Python 3.10+.

```
pip install crawl4ai openai python-dotenv jsonschema
crawl4ai-setup                     # installs the browser crawl4ai drives
cp .env.example .env               # then set SOCLAAS_API_KEY
```

Optional, for masking person names on provider pages before extraction (pronouns are neutralised
either way):

```
pip install spacy
python -m spacy download en_core_web_sm
```

All LLM calls go to NUS SoC's SOCLAAS API. Each page is routed to one of three models from
different families (`ornith1.5:35b`, `llama3.1:8b`, `qwen3.6:27b`; see `classifier_extractor/llm_pool.py`),
and the model that produced each record is stored with it.

**Windows:** some crawled page names are long, so clone with long paths enabled:
`git clone -c core.longpaths=true <repo-url>`.

## Running

From the repo root:

```
python scrapper/crawl.py > crawl_run.log          # --start/--end pick a seed range, --concurrency N
python classifier_extractor/classify.py
python classifier_extractor/extract.py            # --limit 20 to try a batch first, --ping to check the models
python labeller/label.py --max-pairs 50           # 6 LLM calls per pair
python monitor/dashboard.py                       # then open http://localhost:8765
```

Redirecting `crawl.py`'s output to `crawl_run.log` is what feeds the dashboard's crawl panel.

## Outputs

- `docs/manifest.jsonl`: one classification per crawled page (label, reason, model).
- `docs/providers.csv`, `docs/hirers.csv`: one row per extracted record. Columns follow
  `classifier_extractor/ML_provider_schema_v1.md` / `ML_hirer_schema_v1.md`, plus `source_file`,
  `classify_label`, and `extracted_at`. A page counts as extracted once its `source_file` has a row
  here.
- `docs/extract_manifest.jsonl`: every extraction attempt, including rejections, style rolls, and
  quality metrics.
- `docs/relevance_labels.jsonl` / `docs/relevance_scores.csv`: per-call and per-pair relevance
  scores from the labeller.

Prompts live in `classifier_extractor/prompts/` and `labeller/prompts/` as plain text, so a
wording change is a text edit, not a code change.
