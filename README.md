# BT4103 Scrape and Tag

Builds a seed dataset for **GreyGigz**, a gig marketplace for experienced professionals. The
pipeline crawls consulting and talent sites, uses LLMs to sort each page into a provider profile,
a hirer gig, or noise, extracts records shaped to the ML schemas, and scores how relevant each
provider is to each gig.

## Pipeline

```
scrapper/crawl.py                  ->  docs/unprocessed/*.md
classifier_extractor/classify.py   ->  docs/{provider,hirer,uncertain,ignore}/  +  docs/manifest.jsonl
classifier_extractor/industry.py   ->  docs/industry_manifest.jsonl             (industry of each page)
classifier_extractor/extract.py    ->  docs/providers.csv, docs/hirers.csv       (ML schema v1)
                                       (+ Singapore-set text, SkillsFuture category/specialisation/skills tags)
enricher/enrich.py                 ->  docs/providers_enriched.csv, docs/hirers_enriched.csv
                                       (+ rate/budget, seniority, availability, sector/track for the ranker)
labeller/label.py                  ->  docs/relevance_scores.csv
labeller/judge_pools.py            ->  the ranker fork's label files (0-3 grades for its judging pools)
monitor/dashboard.py                   read-only view of all of the above
```

Each stage talks to the next only through files in `docs/`, never through Python imports, so any
stage can be rerun or swapped out on its own. Every script is run-once: it processes what's
waiting, skips what's already done, and exits.

## Layout

| Path | What it is |
|---|---|
| `scrapper/` | `crawl.py` (crawl4ai best-first deep crawl, saved as pruned Markdown) and `seeds.md` (start URLs) |
| `classifier_extractor/` | `classify.py`, `industry.py`, `extract.py`, `llm_pool.py`, `taxonomy.py` (SkillsFuture tag vocabulary and checking), `localisation.py` (foreign-setting check), `prompts/`, and the `ML_*_schema_v1.json` JSON Schemas extraction is validated against |
| `enricher/` | `enrich.py`: tops up extracted records with synthetic rate/budget, seniority and availability, and a SkillsFuture sector/track, for the ranker; `taxonomy/` holds the sector and track lists; see `enricher/README.md` |
| `labeller/` | `label.py`: zero-shot relevance scoring of gig/provider pairs ([Zhuang et al., 2023](https://arxiv.org/abs/2310.14122)); `judge_pools.py`: grades the ranker's judging pools into training labels; see `labeller/README.md` |
| `monitor/` | `dashboard.py`: local dashboard at http://localhost:8765 |
| `docs/` | The data lake: crawled pages by bucket, manifests, extracted CSVs, the SkillsFuture framework tables (`docs/skillsfuture/`) |
| `context.md` | Full design notes and the reasoning behind them |

## Setup

Python 3.10+.

```
pip install crawl4ai openai python-dotenv jsonschema
crawl4ai-setup                     # installs the browser crawl4ai drives
cp .env.example .env               # then set SOCLAAS_API_KEY
```

Required by `extract.py`, which masks person names on provider pages before the model sees them:

```
pip install spacy
python -m spacy download en_core_web_sm
```

All LLM calls go to NUS SoC's SOCLAAS API. Each page is routed to one of 4 distinct chat models
SOCLAAS serves (see `MODEL_POOL` in `classifier_extractor/llm_pool.py`), and the model that
produced each record is stored with it, so models can be compared on the same corpus.

**Windows:** some crawled page names are long, so clone with long paths enabled:
`git clone -c core.longpaths=true <repo-url>`.

## Running

From the repo root:

```
python scrapper/crawl.py > crawl_run.log          # --start/--end pick a seed range, --concurrency N
python classifier_extractor/classify.py
python classifier_extractor/industry.py
python classifier_extractor/extract.py            # --limit 20 to try a batch first, --ping to check the models
python enricher/enrich.py                         # --no-llm regenerates the numbers from saved judgements
python labeller/label.py --max-pairs 50           # 7 LLM calls per pair
python labeller/judge_pools.py --model qwen3.6:35b --gigs 1-100   # needs the ranker fork's data_sat/ folder
python monitor/dashboard.py                       # then open http://localhost:8765
```

Redirecting `crawl.py`'s output to `crawl_run.log` is what feeds the dashboard's crawl panel.

To re-extract under new prompts without touching the existing CSVs, give both stages the same tag:

```
python classifier_extractor/extract.py --out-tag v2   # -> docs/hirers_v2.csv, providers_v2.csv, extract_manifest_v2.jsonl
python enricher/enrich.py --tag v2                    # -> docs/hirers_v2_enriched.csv, providers_v2_enriched.csv
```

## Outputs

- `docs/manifest.jsonl`: one classification per crawled page (label, reason, model).
- `docs/providers.csv`, `docs/hirers.csv`: one row per extracted record. Columns follow
  `classifier_extractor/ML_provider_schema_v1.json` / `ML_hirer_schema_v1.json`, plus `source_file`,
  `classify_label`, `extracted_at`, and `time_taken_by_model` (seconds to extract that row, including a
  hirer's review and repair). A page counts as extracted once its `source_file` has a row
  here.
  Each row also carries the industry columns from `industry.py` and the SkillsFuture tag columns
  (see [SkillsFuture tags](#skillsfuture-tags-and-singapore-setting)).
- `docs/extract_manifest.jsonl`: every extraction attempt, including rejections, style rolls,
  quality metrics, each hirer record's grounding review (reviewer model, keep/retry, reason,
  whether it was repaired), each provider's localisation result, and the tags with the model that
  chose them.
- `docs/industry_manifest.jsonl`: the industry tag for each classified page.
- `docs/providers_enriched.csv`, `docs/hirers_enriched.csv`: the extracted CSVs plus the enricher's
  columns, including SkillsFuture `sector` and `track`. The `*_v2*` files are the same outputs
  for a tagged run (`--out-tag v2` / `--tag v2`).
- `docs/relevance_labels.jsonl` / `docs/relevance_scores.csv`: per-call and per-pair relevance
  scores from the labeller.

## SkillsFuture tags and Singapore setting

Records are written for a Singapore marketplace, so `extract.py` does two things beyond filling
the schema:

- **Singapore setting.** The extraction prompts move each gig or profile to Singapore (Singapore
  regulators in place of foreign ones, S$ amounts, no real company names, Singapore English
  spelling). For providers, `localisation.py` then checks the finished text for leftover foreign
  phrases and, if it finds any, runs one repair pass; the repair is kept only if it leaves fewer
  phrases and blanks nothing. Leftovers that are right to keep (a membership, a foreign-market
  specialism) are logged as `localisation_residue` in the manifest. The hirer reviewer also
  retries a gig that still reads as foreign.
- **SkillsFuture tags.** Once a record is final, two more calls tag it from its own text:
  `category` (a SkillsFuture sector) and `specialisation` (a track), then `skills` (TSCs) chosen
  only from the chosen tracks' lists. At most 2 sectors, 3 tracks and 8 skills; a record that fits
  no track is tagged empty. The CSV gets `category`, `specialisation` and `skills` (` | `-joined),
  `tags_json` (the nested form) and `tag_taxonomy_version`. The framework tables are in
  `docs/skillsfuture/`.

The enricher separately judges one `sector` and `track` per record (`enricher/taxonomy/`, 39
sectors and 247 tracks) for the ranker; see `enricher/README.md`.

Prompts live in `classifier_extractor/prompts/` and `labeller/prompts/` as plain text, so a
wording change is a text edit, not a code change.
