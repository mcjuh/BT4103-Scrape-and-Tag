# BT4103 Scrape and Tag

Builds a seed dataset for **GreyGigz**, a gig marketplace for experienced professionals. The
pipeline crawls consulting and talent sites, uses LLMs to sort each page into a provider profile,
a hirer gig, or noise, extracts records shaped to the ML schemas, and scores how relevant each
provider is to each gig.

## Pipeline

```
scraper/crawl.py                   ->  data/pages/unprocessed/*.md
classifier_extractor/classify.py   ->  data/pages/{provider,hirer,uncertain,ignore}/  +  data/manifests/classify.jsonl
classifier_extractor/industry.py   ->  data/manifests/industry.jsonl                  (industry of each page)
classifier_extractor/extract.py    ->  data/output/providers.json, hirers.json         (ML schema v2, nested)
                                       data/output/providers.csv, hirers.csv           (flat text columns for the later stages)
                                       (+ Singapore-set text, SkillsFuture category/specialisation/skills tags)
enricher/enrich.py                 ->  data/output/providers_enriched.csv, hirers_enriched.csv
                                       (+ rate/budget, seniority, availability, sector/track for the ranker)
labeller/label.py                  ->  data/output/relevance_scores.csv
labeller/judge_pools.py            ->  the ranker fork's label files (0-3 grades for its judging pools)
monitor/dashboard.py                   read-only view of all of the above
```

Each stage talks to the next only through files in `data/`, never through Python imports, so any
stage can be rerun or swapped out on its own. Every script is run-once: it processes what's
waiting, skips what's already done, and exits.

## Layout

| Path | What it is |
|---|---|
| `run.py` | Runs a stage and appends its output to `logs/<stage>.log` (see [Running](#running)) |
| `scraper/` | `crawl.py` (crawl4ai best-first deep crawl, saved as pruned Markdown), `fetch_urls.py` (fetch an explicit URL list), `seeds.md` (start URLs), `url_lists/` (the lists given to `fetch_urls.py`) |
| `classifier_extractor/` | `classify.py`, `industry.py`, `extract.py`, `manufacture_providers.py` (synthetic providers for gigs with no good match, see [Outputs](#outputs)), `llm_pool.py`, `taxonomy.py` (SkillsFuture tag vocabulary and checking), `localisation.py` (foreign-setting check), `prompts/`, and `schemas/` (the `ML_*_schema_v2.json` JSON Schemas extraction is validated against) |
| `enricher/` | `enrich.py`: tops up extracted records with synthetic rate/budget, seniority and availability, and a SkillsFuture sector/track, for the ranker; see `enricher/README.md` |
| `labeller/` | `label.py`: zero-shot relevance scoring of gig/provider pairs ([Zhuang et al., 2023](https://arxiv.org/abs/2310.14122)); `judge_pools.py`: grades the ranker's judging pools into training labels; `evaluate.py`; `experiments/`; see `labeller/README.md` |
| `monitor/` | `dashboard.py`: local dashboard at http://localhost:8765 |
| `marcus/` | The original pipeline, kept for reference; `marcus/README.md` maps each script to its replacement |
| `data/pages/` | Crawled pages: `unprocessed/` until classified, then one folder per label |
| `data/manifests/` | One progress record per page or call, per stage: `classify.jsonl`, `industry.jsonl`, `extract.jsonl`, `enrich.jsonl`, `relevance_labels.jsonl`, plus the crawl's `crawl_state.json` and `crawl_report.md` |
| `data/output/` | The datasets: `providers.*`, `hirers.*`, `*_enriched.csv`, `relevance_scores.csv`, `platform_sample/` |
| `data/reference/` | Inputs from outside the pipeline: the SkillsFuture framework tables (`skillsfuture/`) and the client's test workbook (`client_documents/`) |
| `data/archive/` | Superseded runs, by date (not in git) |
| `docs/` | `design.md` (full design notes and the reasoning behind them), `backlog.md`, `schema_v2.md` (the record shape and who fills each field), `ranker_input_spec.md` |
| `logs/` | One log and one PID file per stage, plus `archive_*.zip` of older logs (not in git) |

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

All LLM calls go to NUS SoC's SOCLAAS API. Each page is routed to one of the chat models
SOCLAAS serves (see `MODEL_POOL` in `classifier_extractor/llm_pool.py`), and the model that
produced each record is stored with it, so models can be compared on the same corpus.

**Windows:** some crawled page names are long, so clone with long paths enabled:
`git clone -c core.longpaths=true <repo-url>`.

## Running

From the repo root, run each stage through `run.py`. Everything after the stage name goes to the
stage's script:

```
python run.py crawl                          # --start/--end pick a seed range, --concurrency N
python run.py classify
python run.py industry
python run.py extract                        # --limit 20 to try a batch first, --ping to check the models
python run.py enrich                         # --no-llm regenerates the numbers from saved judgements
python run.py label --max-pairs 50           # 6 LLM calls per pair
python run.py judge --model qwen3.6:35b --gigs 1-100   # needs the ranker fork's data_sat/ folder
python run.py fetch scraper/url_lists/<list>.tsv       # fetch exact URLs, no link-following
python run.py manufacture --counts <per-gig counts.csv> # synthetic providers for unmatched gigs
python monitor/dashboard.py                  # then open http://localhost:8765
```

`python run.py` with no stage lists the stages. The scripts still run directly
(`python classifier_extractor/extract.py ...`), but then nothing is logged.

**Logs.** Each stage has one log, `logs/<stage>.log`. Every run is appended to it, starting with a
`----- run <time>: <command>` line and ending with `----- exit <code>`. The dashboard's Start
buttons append to the same files, and its crawl panel reads the latest run in `logs/crawl.log`.
Older logs are in `logs/archive_2026-10-06.zip`. Each running script also writes
`logs/<stage>.pid`, which is how the dashboard knows it's running.

To re-extract under new prompts without touching the current dataset, give both stages the same tag:

```
python run.py extract --out-tag v4   # -> data/output/hirers_v4.csv, providers_v4.csv, data/manifests/extract_v4.jsonl
python run.py enrich --tag v4        # -> data/output/hirers_v4_enriched.csv, providers_v4_enriched.csv
```

## Outputs

The current dataset is the 3 Oct 2026 extraction under schema v2 with Singapore localisation
(formerly the `_v3` files). Earlier runs are in `data/archive/2026-10-06/`. It hasn't been
enriched yet, so the `*_enriched.csv` files appear after the next `run.py enrich`.

- `data/manifests/classify.jsonl`: one classification per crawled page (label, reason, model).
- `data/output/providers.json`, `hirers.json`: the nested records, one per extracted page, in the
  shape of `classifier_extractor/schemas/ML_provider_schema_v2.json` / `ML_hirer_schema_v2.json` (a
  provider's services, achievements and technical proficiency are lists; the tags nest category ->
  specialisation -> skills). They are built from `providers.jsonl` / `hirers.jsonl`, which the
  extractor appends to as each record completes; `extract.py --export-json` rebuilds them. The
  shape and who fills each field are in `docs/schema_v2.md`.
- `data/output/providers.csv`, `hirers.csv`: one row per extracted record. The text columns are the
  old flat ones (`about_title`, `about_description`, `services_offered_*`, `relevant_experience`,
  `hire_title`, `hire_description`, ...), derived from the nested record so the enricher, labeller
  and ranker import read what they always did, plus `years_experience`, `hirer_ref` and
  `duration_weeks_min` / `duration_weeks_max`, `source_file`, `classify_label`, `extracted_at`, and
  `time_taken_by_model` (seconds to extract that row, including a hirer's review and repair). A page
  counts as extracted once its `source_file` has a row here.
  Each row also carries the industry columns from `industry.py` and the SkillsFuture tag columns
  (see [SkillsFuture tags](#skillsfuture-tags-and-singapore-setting)).
- `data/manifests/extract.jsonl`: every extraction attempt, including rejections, style rolls,
  quality metrics, each hirer record's grounding review (reviewer model, keep/retry, reason,
  whether it was repaired), each provider's localisation result, and the tags with the model that
  chose them.
- `data/manifests/industry.jsonl`: the industry tag for each classified page.
- `data/output/providers_enriched.csv`, `hirers_enriched.csv`: the extracted CSVs plus the
  enricher's columns, including SkillsFuture `sector` and `track`. Its judgements are kept in
  `data/manifests/enrich.jsonl`.
- `data/manifests/relevance_labels.jsonl` / `data/output/relevance_scores.csv`: per-call and
  per-pair relevance scores from the labeller.
- `data/output/platform_sample/`: a small sample of records in the platform's shape.
- **Synthetic providers.** `providers.jsonl` / `providers.csv` also hold providers that were not
  extracted from a real page: `run.py manufacture` wrote two for each gig that had no provider
  graded 2 or 3 in the ranker's judging pools (one aimed at grade 3, one at grade 2), by having a
  pool model write a fictional profile page and running it through the normal provider
  extraction. Their `source_file` starts with `synthetic-provider__` and their
  `extracted_by_model` with `synthetic:`; filter on either to leave them out.
  `data/output/manufactured_providers.txt` lists them with the gig each targets, and
  `data/manifests/manufacture.jsonl` keeps the generated pages.

## SkillsFuture tags and Singapore setting

Records are written for a Singapore marketplace, so `extract.py` does two things beyond filling
the schema:

- **Singapore setting.** The extraction prompts move each gig or profile to Singapore (Singapore
  regulators in place of foreign ones, S$ amounts, no real company names, Singapore English
  spelling). For providers, `localisation.py` then checks the finished text for leftover foreign
  phrases, or for no mention of Singapore at all, and runs up to two repair passes; a repair is kept
  only if it leaves fewer problems and blanks nothing. Credentials are never localised. Leftovers
  that are right to keep (a foreign-market specialism) are logged as `localisation_residue` in the
  manifest. The hirer reviewer also retries a gig that still reads as foreign.
- **SkillsFuture tags.** Once a record is final, two more calls tag it from its own text:
  `category` (a SkillsFuture sector) and `specialisation` (a track), then `skills` (TSCs) chosen
  only from the chosen tracks' lists. At most 2 sectors, 3 tracks and 8 skills; a record that fits
  no track is tagged empty. The CSV gets `category`, `specialisation` and `skills` (` | `-joined),
  `tags_json` (the nested form) and `tag_taxonomy_version`. The framework tables are in
  `data/reference/skillsfuture/`.

The enricher separately judges one `sector` and `track` per record (from the same
`data/reference/skillsfuture/` tables: 39 sectors and 247 tracks) for the ranker; see
`enricher/README.md`.

Prompts live in `classifier_extractor/prompts/`, `enricher/prompts/` and `labeller/prompts/` as
plain text, so a wording change is a text edit, not a code change.
