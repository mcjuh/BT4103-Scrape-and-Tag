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
Both `classify.py` and `extract.py` route each file to one of the SOCLAAS models in `MODEL_POOL` rather than
a single fixed model -- `model_for_file(filename, stage)` picks deterministically via a hash of
`(stage, filename)`, so a given file always lands on the same model on a rerun, but `classify`
and `extract` diversify independently (the model that labeled a page isn't necessarily the one
that later extracted it). Every file still costs exactly one LLM call, not one per model -- this is
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

**`MODEL_POOL`** is every usable distinct chat model SOCLAAS serves (`client.models.list()`),
widened from the original three so each model's performance can be compared on the same corpus:
`llama3.1:8b`, `qwen3.8:27b`, `qwen3.6:35b`, `qwen3-vl:32b`.
Left out: `ornith1.5:35b` (the original model, dropped at the team's request), `bge-m3` (embeddings), `whisper-large-v3` (audio), `qwen3-coder-next`
(code-specialised), `gemma4:26b` (can't switch thinking off; ~30-45s per extraction), aliases that would
count a model twice (`default`, `coding`, `advanced-vision`, `test`, `ornith1.0:35b`, and
`qwen3.6:27b` -- now an alias of `qwen3.8:27b`, so older records labelled `qwen3.6:27b` came
from that model), and `qwen3.5:9b`, which can't have "thinking" switched off and so takes ~75s
per extraction -- right at SOCLAAS's gateway cutoff, so its calls 502 whatever the client
timeout. The earlier three-model pool deliberately picked three distinct families; the wider
pool spans only two families (Meta and Qwen; 3 of 4 are Qwen), trading much of that diversity away.
**`extract.py` and `industry.py` now switch thinking OFF** (`chat_template_kwargs.enable_thinking=False`),
as `labeller/label.py` always has; `classify.py` still leaves it on. The 180s timeout is unchanged.
The labeller keeps its own copy of the same four models (see below).

Thinking was left on deliberately at first, but the cost turned out to sit almost entirely on one
model. `qwen3.8:27b` reasoned on **100%** of its extract calls, emitting a median **11,832**
completion tokens against ~350 for the other three, at a median **171.2s** per record versus
4.0-10.8s (p90 378s, max 734s -- one observed call ran **611.7s** for a single record). Routed a
quarter of all files, it was ~85-90% of total extraction wall clock. With thinking off it runs a
median **6.0s / 406 tokens** -- and the other three models are unaffected either way
(`qwen3.6:35b`: 1.4s on, 2.4s off).

The quality check has now been run on 21 Sep, comparing the ON era (records before 20 Sep 19:00)
with a 200-file OFF-era `--balance` run. No quality drop was found. On `qwen3.8:27b`, the only model
whose behaviour changed, hirer first-review keep went from 88.6% (n=35) to 95.7% (n=23), and
providers were written 100% of the time in both eras. The whole-pool hirer keep rate went from
82.5% to 85.3%. The samples are small, and the OFF files were chosen by `--balance`, so they
differ in mix from the ON era (crawl order); see BACKLOG item G for the full table.

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
  tier and voice/opening; provider title style, achievement grammar, rare prose imperfection), with weights.
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
(`classifier_extractor/ML_provider_schema_v1.json`, `classifier_extractor/ML_hirer_schema_v1.json`) directly, rather than an
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
`classifier_extractor/ML_provider_schema_v1.json` / `ML_hirer_schema_v1.json` (plain JSON Schema),
written to `docs/providers.csv` / `docs/hirers.csv` with columns in schema order. The schemas are
the source of truth: prompt field lists are generated from them and every LLM response is
validated against them (`jsonschema`); a mismatch is retried, never written. `source_file` and
`extracted_by_model` are filled in by code. Providers and hirers share one code path; the
difference is the prompts and `ENTITY_CONFIG`:
- **Hirer** (one pass, from a teammate's `gig.py`): reframes a case study as the gig its original
  hirer could have posted, grounded in the source, never naming the real company in the gig text.
  The shape follows the client's own 30 test gigs (`labeller/experiments/gold.json` /
  `client_testset/gigs.csv`):
  - It describes the **work**, not the person. The title names a task ("Design Target Operating
    Model for Finance Function"), never a job title. The old "Role first" voice was replaced by
    "Problem first".
  - It stays **small**: one self-contained piece a single specialist could finish in under a
    year, carved out of a big programme if necessary.
  - The description runs situation -> work -> `Deliverable:` -> `Engagement duration:` in at
    most 120 words (the client's are 60-92). The duration is the one detail the model may
    estimate without the source. The reviewer (`review_hirer.md`) accepts it if it's plausible
    and under 12 months, and flags a gig that is too big.
  - On a 10-page dry run: every gig had both lines, durations from 4 weeks to 8 months, 59-110
    words, and all were kept by review.
- **Provider** (two passes, from a teammate's `showcase.py`): neutral fact extraction, then a
  first-person restyle, so styling can't add facts. The page is anonymised first (spaCy name
  masking, required, plus gendered-pronoun neutralisation).
- **Anonymisation** (both types): the prompts replace company, client, division and team names with
  generic descriptions; provider pages also have the publisher's name swapped for "the firm" before
  the model reads them; and a record whose shown text names the page's publisher (its domain or a
  known alias, `PUBLISHER_ALIASES`) is rejected and retried. `source_company`/`source_company_team`
  are metadata and may name it.
- **Hirer review + repair** (from the teammate's `review_gig_content.py` + `gig_repair.py`): before
  a hirer row is written, a *different* pool model (`llm_pool.reviewer_for_file`, never the
  extractor, to avoid self-preference) checks it against the source and answers keep/retry,
  flagging only clear defects (unsupported scope, catch-all roles, invented requirements). On
  retry the extractor redoes its pass once with the reviewer's reason and its previous record
  (`prompts/review_hirer.md`, `prompts/repair_hirer.md`); the same reviewer checks the rewrite
  once more, and one that's still flagged is rejected. The verdict is
  stored in `extract_manifest.jsonl`. The teammate's `collect_gig_retries.py` and
  `combine_gig_manifests.py` aren't ported: schema validation + retries already keep malformed
  records out, and there's a single append-only manifest.
Either prompt returns `{}` for a non-qualifying page (recorded as rejected). Per-file style rolls
come from `prompts/extract_variations.json`, seeded by file name and now also written to the CSVs
as `roll_*` columns. Thinking mode is switched off for every model (see the pool section above for
the measurements); whether a record's model reasoned first is still logged as `hidden_reasoning`,
which is what makes the before/after rows comparable. Code-side checks still apply after
the schema check (a real gig title/description; >=2 substantive provider fields; no leaked name
placeholder). The earlier `speciality_ids` matching and name-based provider dedup were dropped:
the schemas have no field for them. Progress tracked in `docs/extract_manifest.jsonl` (with the
style rolls and quality metrics per record); `--ping` checks every pool model responds.

**Industry columns.** `industry`, `secondary_industry` and `taxonomy_version` sit after
`classify_label` in both CSVs. Like `source_file` they're filled in by code, copied from
`docs/industry_manifest.jsonl` when the row is written, never asked of the LLM. A file that
`industry.py` hadn't tagged yet gets blanks. `--backfill-industries` rewrites both CSVs with the
current tags, joined on `source_file`, with no LLM calls. Run it after re-tagging, and to migrate
a CSV written before these columns existed. The first rewrite keeps `docs/*.csv.pre_industry.bak`.
It refuses a CSV with columns the code doesn't know, since that means a schema change rather than
a missing column.

**Defaults and guards.** `--workers 4 --rps 1` is now the default (was 1 worker, no cap), the
settings the tagging stage ran 2,894 pages on cleanly. Every call is capped at
`max_completion_tokens=1500` (`industry.py`: 300) as a guard against runaway output. With thinking
off, the largest record seen was 655 tokens across both provider passes, and a tagging answer is
under 100. A reply cut off by the cap fails as an explicit error rather than as unparseable JSON.

**`--balance`** spends extraction calls evenly across `(entity_type, industry)` cells instead of
working through the manifest in order. Manifest order is crawl order, and crawl order is
dominated by whichever domains produced most pages -- so extracting in it reproduces the corpus's
skew in the CSVs no matter how many rows get written. (Measured under the earlier tagging stage,
the first 200 files came from 3 domains in manifest order versus 12 with `--balance`.)

Cells round-robin one file each in turn; a cell that empties drops out of the rotation, so a rare
industry with 3 files still contributes all 3. `--per-cell N` additionally caps what any one cell
contributes this run -- over-cap files stay pending rather than being spent, so raising the cap
later resumes exactly where it left off. Note the cell is `(entity_type, industry)`, so an
industry present as both provider and hirer can contribute up to `2N`. Files `industry.py` hasn't
tagged yet form one `(untagged)` cell rather than being dropped, so extraction never stalls
waiting on tagging, but can't be dominated by it either. It reads `docs/industry_manifest.jsonl`
directly, not `industry.py`'s code, like every other cross-role read here.

### 3b. `classifier_extractor/industry.py`
Tags each already-classified page with the **industry the work is done for**: the sector of the
client (for an engagement or request) or of the person's experience (for a profile) -- never the
publisher's. The taxonomy, `industry_v1`, comes from the client: the `industry` column of their
test workbook (`client_documents/20260917 Senseigigs_NUS_Test_Dataset_Team31.xlsx`, 30 gigs),
collapsed into 12 groups -- Food & Beverage, Construction & Real Estate, Financial Services,
Manufacturing, Logistics & Distribution, Healthcare, Marine & Offshore, Technology & Software,
Retail & Consumer, Professional Services, Engineering Services, Social Services & Non-profit.
Three more were added because the consulting-heavy corpus has a lot of work in them: Energy &
Resources, Public Sector, Education. Every entry records its `origin` (client or corpus) and the
client labels it absorbs. Plus `Cross-industry` (the page never says what the client does, or the
expertise is explicitly general) and `OTHER`, which asks the model to name the sector it wanted,
so taxonomy gaps get measured instead of guessed at.

The taxonomy lives in `prompts/industry_taxonomy.json` (versioned, `taxonomy_version` on every
record) and the prompt's industry list is generated from it, the same way `extract.py`'s
`{field_block}` is generated from the ML schemas. Each record carries `industry`, an optional
`secondary_industry`, `other_industry` (only for OTHER) and a short `reason`.

The prompt (`prompts/classify_industry.md`) has two rules that matter:
1. Label the client's industry, not the publisher's. Most pages come from consultancies, so
   Professional Services is only for work whose client is itself a professional firm.
2. The *type* of work never decides the industry. Finance, legal, HR, marketing and IT work
   happen in every sector; if the page never says what the client does, the answer is
   Cross-industry. Without this rule the models tagged reputation work for a pet-grooming chain,
   and expert-witness work for an IT firm, as Professional Services.

**Why industry and not an academic subject.** It replaced an earlier academic-subject stage
(taxonomy from `SenseigigsDoc1.pdf`). Run on the client's own 30 gigs, that taxonomy put 21 of
them into Mathematics, Accountancy or Law, so it couldn't separate the work the client cares
about. Run on the same 30 gigs, `industry_v1` agreed with the client's own industry label on 26.
Of the 4 misses, #21 (an online homeware store the client labelled Technology/Software because
the work is a chatbot) is arguably right on rule 2, and #12 (food-packaging materials) and #26
(a distributor's JV restructure) are borderline. #4 is a clear miss: finance work for a listed SME
whose sector the text never states was tagged Financial Services, not Cross-industry. Don't tune
the prompt further against those 30 gigs -- they're the client's test set (see BACKLOG item I).
The old stage's code and manifest are archived in `docs/archive/2026-09-21/subject_v1/`.

The point is **dataset balance**: the corpus is 23 domains and the top 3 (kroll, bcg,
alvarezandmarsal) are ~47% of everything extractable, so an industry label gives `extract.py` a
key to spend its calls evenly on, and gives `scrapper/seeds.md` a concrete list of starved
industries to seed for.

It's its own stage, not a field on either neighbour, for two reasons. Folding it into
`extract.py`'s schemas would be free but useless for balancing -- by the time that call returns
it's already paid for, and balance means knowing the industry *before* deciding whether to spend
an extraction. Folding it into `classify_triage.md` is impossible without a re-run of everything:
`classify.py` only globs `docs/unprocessed/`, so the 12k labelled pages would all have to be
moved back -- and editing that prompt would perturb a PROVIDER/HIRER/IGNORE boundary that already
has 12k rows behind it.

Reads `docs/manifest.jsonl` (not `classify.py`'s code) for `PROVIDER`/`HIRER`/`UNCERTAIN`,
reads each page out of its bucket folder and **never moves it** -- industry is a second,
orthogonal axis on the existing buckets. `--include-ignore` also tags the ~9.4k IGNORE pages,
off by default since they never reach `extract.py`. Hash-routed across `MODEL_POOL` with its own
`"industry"` stage salt, for the reason `llm_pool.py` documents. Progress in
`docs/industry_manifest.jsonl`; `--watch`, `--limit`, `--workers` (default 4), `--rps` (default
1), retry-with-backoff and the same 5-consecutive-error circuit breaker as the other two.
`--report` prints the distribution (industry, industry x classify label, secondary, OTHER gaps,
per model, per domain) straight from the manifest with no LLM calls, so it's safe to run mid-run.

### 4. `labeller/label.py`
Zero-shot LLM relevance labels between each gig in `hirers.csv` (the "query") and each provider
in `providers.csv` (the "document"), following Zhuang et al., ["Beyond Yes and No: Improving
Zero-Shot LLM Rankers via Scoring Fine-Grained Relevance Labels"](https://arxiv.org/abs/2310.14122)
(arXiv:2310.14122). Five approaches per pair: the paper's four fine-grained prompts (`rg_2l`,
`rg_3l`, `rg_4l`, `rg_s04`) on the gig's one hash-routed model (per gig, not per pair, so a
gig's ranking isn't driven by model calibration differences), plus `rg_3l_multi` -- RG-3L on
all four pool models, averaged. Scores are expected relevance from label logprobs, normalised
to 0-1. Calls must disable thinking (`chat_template_kwargs.enable_thinking=False`), or
models that reason first score their reasoning instead of the answer. Output: `docs/relevance_labels.jsonl`
(per call) and `docs/relevance_scores.csv` (per pair, with `hirer_industry`, `provider_industry`
and `same_industry` taken from the CSVs' industry column, so it can be checked whether a score
tracks relevance or just industry match). Replaces the earlier plan of comparing a
binary model with a hand-tuned weighted-sum score (the binary model is now the `rg_2l` baseline;
the fine-grained labels replace the weighted sum), and the older one of matching by
`speciality_ids` overlap / embeddings. Run-once with `--max-pairs` (7 calls per pair). See
`labeller/README.md`.

### `monitor/dashboard.py` -- centralised monitoring
A local dashboard (stdlib `http.server`, no external deps) at
`http://localhost:8765`, laid out as **the pipeline itself**: Crawl -> Classify -> Industry ->
Extract -> Label, left to right, with the handoff count between each pair of stages.

Every stage answers the same three questions in the same shape -- is it RUNNING, how many
documents has it PROCESSED, how many are QUEUED for it -- because that's what you actually want
at a glance. Per-model chips, token counts, the seed table and the classify manifest are
secondary and live behind a collapsed "Detail" section, which is also only rendered while it's
open.

How each stage's two numbers are derived, since they're not all the same kind of thing:
- **Crawl** counts *seeds*, and a seed counts as processed only if it actually saved a page --
  matching `crawl.py`'s own rule that a `saved_count == 0` seed gets retried rather than being
  treated as done. The old dashboard showed a green 86/86 while 63 of those seeds had never
  produced a single page.
- **Classify**'s queue is just `docs/unprocessed/*.md`: `classify.py` moves each file out as it
  goes, so the directory listing *is* the queue.
- **Industry** and **Extract** share one queue set -- the `PROVIDER`/`HIRER`/`UNCERTAIN` files in
  `docs/manifest.jsonl` -- so the two stages' totals match and can be read against each other.
  Extract counts *rejected* pages as processed: a page the model judged non-qualifying is
  finished work, not backlog.
- **Label** counts (gig, provider) pairs, so its queue is the full cross product implied by the
  two CSVs and jumps every time `extract.py` writes a row.

Two things it deliberately gets from source rather than from a log: the seed total comes from
`scrapper/seeds.md` (so adding seeds moves the number immediately), and the crawl log is the
newest `crawl*.log` in the root rather than a fixed `crawl_run.log` (a run redirected elsewhere
used to leave the dashboard quoting a stale run's numbers as current).

RUNNING is exact for every stage: each script (`crawl.py`, `classify.py`, `industry.py`,
`extract.py`, `label.py`) writes `docs/_<stage>.pid` at startup and removes it on exit, and the
dashboard checks whether that PID is still alive. This replaced an earlier guess from manifest
mtimes (last 90s), which read high after a run ended and low for a script stuck on one slow call.
A hard kill leaves a stale PID file, which the liveness check handles. `industry.py --report` and
`extract.py --ping`/`--backfill-industries` don't write one, since they aren't runs.

**Start/Stop buttons.** Each card can launch its stage in the background:
- **Crawl:** `crawl.py --concurrency 1`. It refuses to start with less than 8 GB of RAM free
  (BACKLOG A2).
- **Classify:** `classify.py`.
- **Industry:** `industry.py`, with an optional `--limit`.
- **Extract:** `extract.py --balance`, with optional `--limit` and `--per-cell`.
- **Label:** `label.py`, with an optional `--max-pairs`.

Each run logs to `logs/<stage>_<timestamp>.log`, and the card shows the last few lines. Stop
terminates the stage's process and removes its PID file. Every script tolerates this: finished
files are already in its manifest, and in-flight ones are redone on the next run.

Safety:
- The page sends only a stage key and integer options, never a command line, and nothing goes
  through a shell.
- Launch and stop need a per-session token that is embedded in the page.
- Requests addressed to a Host other than localhost/127.0.0.1 get a 403.
- Stop only kills a Python process, so a stale PID file can't hit an unrelated program.

Launched runs are their own processes, so closing the dashboard doesn't stop them. The dashboard
still never writes to any role's data files.

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
3. Run `labeller/label.py` over more pairs once `hirers.csv` has rows (7 LLM calls per pair --
   see `labeller/README.md` for cost).
