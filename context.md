# Scrapper Agent -- Project Context

## What this is
A scraping pipeline that builds a seed dataset for **GreyGigz**, a gig marketplace for
experienced/senior professionals spanning ~36 industries and ~39 functional specialties (see
`client_files/*.sql` -- `categories`, `services`, `specialities`, `speciality_tags`, `tags`,
`hirers`, `providers` -- for the platform's real taxonomy and record schema).

## Architecture: an agentic workflow, one folder per role
Each role owns its own script(s) and talks to the others only through the shared `docs/` data
lake on disk (JSONL manifests, bucket folders, CSVs) -- never through Python imports across
role folders. That's deliberate: a role should keep working even if another role's internals
change or gets swapped out entirely (this replaced an earlier design where one script imported
directly from another, which broke the moment the imported-from script was removed).

```
scrapper-agent/
  scrapper/               crawl.py, seeds.md
  classifier_extractor/   classify.py, extract.py, llm_pool.py, prompts/
  labeller/                label.py, prompts/
  monitor/                 dashboard.py
  docs/                    shared data lake (see below)
  providers.sql, hirers.sql, .env, context.md
  crawl_run.log            (crawl.py's output, if redirected there; read by the dashboard)
```

### 1. `scrapper/crawl.py`
Deep-crawls each seed in `scrapper/seeds.md` (`BestFirstCrawlingStrategy`, keyword-weighted,
same-domain only) up to `MAX_DEPTH=5` / `MAX_PAGES_PER_DOMAIN=1000`, `SEED_TIMEOUT_S=1800`.
Saves each page as pruned Markdown (`PruningContentFilter` + `DefaultMarkdownGenerator`, plus a
`strip_link_farms()` backstop for boilerplate the filter misses) into `docs/unprocessed/`.
Detects and discards bot-block/consent-wall pages (`block_reason()`). Dedup is per-seed-URL,
keyed on `(label, url)`, and a "successful" crawl that actually saved 0 pages (crawl4ai's memory
dispatcher throttling under RAM pressure, without raising) does NOT count as done -- it's
retried rather than silently skipped forever. `--concurrency N` runs multiple seeds in parallel
via a bounded `asyncio.Semaphore`.

### Multi-LLM routing (`classifier_extractor/llm_pool.py`)
Both `classify.py` and `extract.py` route each file to one of three SOCLAAS models rather than
a single fixed model -- `model_for_file(filename, stage)` picks deterministically via a hash of
`(stage, filename)`, so a given file always lands on the same model on a rerun, but `classify`
and `extract` diversify independently (the model that labeled a page isn't necessarily the one
that later extracted it). Every file still costs exactly one LLM call, not three -- this is
about diversifying which model generates the pipeline's labels/extractions across the corpus,
not per-document ensembling/voting.

**Why**: `docs/manifest.jsonl` and `docs/providers.csv`/`hirers.csv` are synthetic/derived data
(LLM output standing in for ground truth), not raw fact -- the same risk that applies to
training on synthetic data applies to generating it. Shumailov et al., ["AI models collapse when
trained on recursively generated
data"](https://www.nature.com/articles/s41586-024-07566-y) (*Nature* 631, 755-759, 2024)
demonstrate that a narrow/single generative source compounds its own idiosyncrasies and loses
distributional coverage over repeated generation. Schaffelder & Gatt, ["Synthetic Eggs in Many
Baskets: The Impact of Synthetic Data Diversity on LLM
Fine-Tuning"](https://arxiv.org/abs/2511.01490) (Findings of ACL 2026, arXiv:2511.01490) show
the direct mitigation implemented here: synthetic data drawn from **multiple source models**
measurably mitigates distribution collapse and reduces self-preference bias versus single-source
synthetic data.

**`MODEL_POOL`** (from SOCLAAS's `client.models.list()`; non-text-generation and
code/vision-specialized models excluded): `ornith1.5:35b` (this pipeline's original model, kept
for continuity), `llama3.1:8b` (Meta family), `qwen3.6:27b` (Alibaba Qwen family). Three
distinct architectural lineages, not three sizes of one family -- picking e.g. three Qwen
variants would share correlated blind spots and defeat the point. Parameter count was a bad
proxy for cost here: a same-probe token-usage check found `qwen3.5:9b` and `gemma4:26b` both
defaulting to a verbose internal "thinking" trace (2062 and 1212 completion tokens on a trivial
probe) despite being mid-sized, while `qwen3.6:27b`/`llama3.1:8b` answered directly in
35-160 tokens -- `qwen3.5:9b` was dropped from the pool in favor of the larger-but-cheaper
`qwen3.6:27b` as a result. Re-run that probe if SOCLAAS's model list changes.

Which model produced a given record is recorded (`"model"` in `manifest.jsonl`/
`extract_manifest.jsonl`, `extracted_by_model` in the CSVs) and surfaced in
`monitor/dashboard.py`'s per-model breakdown chips, so the routing is auditable, not just
assumed to be working.

### Prompts (`classifier_extractor/prompts/`)
Prompt text lives in its own plain-text files, not inline in the `.py` files, so a wording
change or a taxonomy experiment is a plain-text diff/swap instead of a Python code change, and
the prompt's own edit history is a normal file history instead of buried inside a much larger
script's:
- `classify_triage.md` -- classify.py's full labeling prompt, read verbatim (`TRIAGE_PROMPT =
  (PROMPTS_DIR / "classify_triage.md").read_text(...).strip()`).
- `extract_hirer.md` -- extract.py's hirer prompt (one pass).
- `extract_provider_facts.md` + `extract_provider_style.md` -- extract.py's two provider passes:
  neutral facts first, then a first-person restyle of those facts.
- `extract_variations.json` -- the per-file style rolls those prompts draw on (hirer detail
  tier; provider title style, achievement grammar, rare prose imperfection), with weights.
  Each roll fills `{<roll>}` / `{<roll>_instruction}`.
  `{field_block}` / `{skeleton}` are generated from the ML schema files, not written by hand,
  so the schemas stay the one place that defines the fields.

Editing any of these files and rerunning `classify.py`/`extract.py` picks up the change immediately
(loaded at module import, no separate reload step). There's no versioned/numbered filename
scheme (`_v1`, `_v2`, ...) yet -- if trying several prompt variants side by side becomes a
regular need, that's the natural next step, but wasn't built speculatively here.

### 2. `classifier_extractor/classify.py`
Runs the SOC LLM (NUS-hosted; credentials in `.env`) over `docs/unprocessed/*.md`, sorting each
into `docs/provider/`, `docs/hirer/`, `docs/ignore/`, or `docs/uncertain/`. Labels are named to
match `providers.sql`/`hirers.sql` and the `ProviderDocument`/`HireDocument` ML schemas
(`classifier_extractor/ML_provider_schema_v1.md`, `classifier_extractor/ML_hirer_schema_v1.md`) directly, rather than an
in-between name like the earlier `individual_profile`/`gig`:
- **provider**: the page's primary subject is one named person's own
  career/background/expertise -- a bio, profile, or portfolio.
- **hirer**: a request for work with a defined scope/deliverable/budget/deadline, OR a concrete
  case study/completed engagement with a specific scope and outcome.
- **ignore**: company/team pages, marketing, generic case-study blurbs, boilerplate -- anything
  that isn't one person's own bio or one concrete work request/engagement.
- **uncertain**: a genuine provider profile that also carries explicit hirer signals, or a
  response that didn't parse cleanly. Not a dumping ground for merely low-value pages.

Moves (not copies) each file out of `docs/unprocessed/` into its bucket once classified.
Retries transient failures with backoff; aborts after 5 consecutive errors rather than
mislabeling everything. A failed file is left in `unprocessed/` so it's retried next run, not
lost. `_drain_stuck_moves()` also relocates any file that was already classified (recorded "ok"
in the manifest) but somehow never got moved -- e.g. from a prior run that was killed mid-move --
so nothing is left permanently stranded in `unprocessed/`. Progress is tracked in
`docs/manifest.jsonl`. `--watch` keeps it running alongside a still-active `crawl.py`.

### 3. `classifier_extractor/extract.py`
Reads `docs/manifest.jsonl` directly (not `classify.py`'s code) to find pages worth extracting
-- `PROVIDER`, `HIRER`, `UNCERTAIN` -- and turns each into one record shaped exactly like
`classifier_extractor/ML_provider_schema_v1.md` / `ML_hirer_schema_v1.md` (plain JSON Schema),
written to `docs/providers.csv` / `docs/hirers.csv` with columns in schema order. The schemas are
the source of truth: prompt field lists are generated from them and every LLM response is
validated against them (`jsonschema`); a mismatch is retried, never written. `source_file` and
`extracted_by_model` are filled in by code. Providers and hirers share one code path; the
difference is the prompts and `ENTITY_CONFIG`:
- **Hirer** (one pass, from a teammate's `gig.py`): reframes a case study as the gig its original
  hirer could have posted, grounded in the source, never naming the real company in the gig text.
- **Provider** (two passes, from a teammate's `showcase.py`): neutral fact extraction, then a
  first-person restyle, so styling can't add facts. The page is anonymised first (spaCy name
  masking if installed, plus gendered-pronoun neutralisation).
Either prompt returns `{}` for a non-qualifying page (recorded as rejected). Per-file style rolls
come from `prompts/extract_variations.json`, seeded by file name. Thinking mode is disabled per
model by probing four known parameter shapes once per run. Code-side checks still apply after
the schema check (a real gig title/description; >=2 substantive provider fields; no leaked name
placeholder). The earlier `speciality_ids` matching and name-based provider dedup were dropped:
the schemas have no field for them. Progress tracked in `docs/extract_manifest.jsonl` (with the
style rolls and quality metrics per record); `--ping` checks every pool model responds.

### 4. `labeller/label.py`
Zero-shot LLM relevance labels between each gig in `hirers.csv` (the "query") and each provider
in `providers.csv` (the "document"), following Zhuang et al., ["Beyond Yes and No: Improving
Zero-Shot LLM Rankers via Scoring Fine-Grained Relevance Labels"](https://arxiv.org/abs/2310.14122)
(arXiv:2310.14122). Five approaches per pair: the paper's four fine-grained prompts (`rg_2l`,
`rg_3l`, `rg_4l`, `rg_s04`) on the pair's one hash-routed model, plus `rg_3l_multi` -- RG-3L on
all three pool models, averaged. Scores are expected relevance from label logprobs, normalised
to 0-1. Calls must disable thinking (`chat_template_kwargs.enable_thinking=False`), or
ornith1.5/qwen3.6 score their reasoning instead of the answer. Output: `docs/relevance_labels.jsonl`
(per call) and `docs/relevance_scores.csv` (per pair). Replaces the earlier plan of matching by
`speciality_ids` overlap / embeddings. Run-once with `--max-pairs` (6 calls per pair). See
`labeller/README.md`.

### `monitor/dashboard.py` -- centralised monitoring
A read-only local dashboard (stdlib `http.server`, no external deps) at
`http://localhost:8765`, covering every role from one place: crawl progress (`crawl_run.log` +
`docs/_crawl_state.json`), classify progress and token usage (`docs/manifest.jsonl`), extract
progress and CSV row counts (`docs/extract_manifest.jsonl`, `providers.csv`, `hirers.csv`), and
labeller progress (`docs/relevance_labels.jsonl`, `docs/relevance_scores.csv`). Safe to start/stop/restart independently of every
other script -- it only ever reads their output files, never writes to them.

## Current state (as of the last full run)
- 86 seeds processed, 10,590 pages saved (see `docs/_crawl_report.md` for the per-seed
  breakdown). McKinsey returns 0 pages on every attempt (bot-blocked); kept in `scrapper/seeds.md` in
  case that changes.
- Classified: **1,856 provider, 1,011 hirer, 9,372 ignore, 27 uncertain** (all of
  `unprocessed/` has been drained).
- Extraction into `providers.csv`/`hirers.csv` just started against this backlog.

## Key gotchas for future readers
- Every role's paths resolve relative to its own folder plus one `.parent` hop to the project
  root (`ROOT_DIR = SCRIPT_DIR.parent`) to reach the shared `docs/`, `.env`, etc. `seeds.md` is
  the one exception -- it's `scrapper`'s own input config, not shared, so `crawl.py` reads it
  via `SCRIPT_DIR` directly instead of `ROOT_DIR`. Moving a role's script to yet another nesting
  depth means updating whichever of these hops it uses.
- `domain_of()` in `crawl.py` normalizes `www`/`www2`/`www3` prefixes -- `www2.deloitte.com` and
  `www.deloitte.com` are treated as the same domain for dedup and file-naming.
- `classify.py`'s `MAX_CHARS=24000` (also used by `extract.py`) truncates from the **front** of
  the page text -- a page with a long boilerplate preamble can still hide real content from the
  LLM even after `strip_link_farms()`, if the remaining preamble is still large.
- `extract.py`'s `_norm()` must tolerate a field coming back as a list instead of a string (the
  model itemizing something like `relevant_experience` as bullet points) -- an earlier version
  crashed on this; it now joins list items into one string instead of raising.
- Seeding from a firm's `/industries` or `/services` hub reaches case-study/service content
  well, but usually does **not** reach that firm's separate people/leadership bio section --
  these are often disconnected content trees. `scrapper/seeds.md` has a dedicated "People / Leadership
  Hubs" section with verified second seeds for EY, Bain, and PwC; BCG/KPMG/Deloitte/Accenture
  hub URLs are still unresolved -- documented as a known gap in `scrapper/seeds.md` rather than guessed
  at again.
- System memory pressure is the dominant operational failure mode for `crawl.py`: crawl4ai's
  `MemoryAdaptiveDispatcher` throttles or crashes fetches under RAM pressure, which can look like
  a code bug but isn't one -- check free RAM before assuming the crawler itself is broken.

## Next steps
1. Let `extract.py` work through the full `provider`/`hirer`/`uncertain` backlog.
2. Find real people/leadership hub URLs for BCG, KPMG, Deloitte, Accenture, if pursuing that
   gap further.
3. Run `labeller/label.py` over more pairs once `hirers.csv` has rows (6 LLM calls per pair --
   see `labeller/README.md` for cost).
