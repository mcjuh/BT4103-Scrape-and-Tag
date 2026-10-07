# Backlog

Tracked work items. Newest section at the top of each list. This is the running list; the old
`PROGRESS_NOTES_TMP.md` snapshot was folded in here and deleted on 20 Sep (recoverable from git
if anything in it is missed).

> **Paths below predate the 2026-10-06 restructure** (`docs/` -> `data/`, `scrapper/` -> `scraper/`,
> `context.md` -> `docs/design.md`, one log per stage). The path map is at the top of
> `docs/design.md`; the README's Layout section is current.

---

## Done

### K. Industry replaces subject as stage 3 — 21 Sep 2026
At your direction, the academic-subject stage is gone and `classifier_extractor/industry.py`
tags every page with the **industry the work is done for** instead.
- **Taxonomy `industry_v1`** (`prompts/industry_taxonomy.json`): the client's 30-gig `industry`
  column collapsed into 12 groups, plus Energy & Resources, Public Sector and Education for the
  consulting-heavy corpus, plus `Cross-industry` and `OTHER`. Each entry records its origin.
- **Why:** on the client's own 30 gigs the subject taxonomy put 21 into Mathematics, Accountancy
  or Law. The industry tagger agrees with the client's label on **26 of 30**. The misses are
  one defensible (#21), two borderline (#12, #26) and one clear miss (#4, which should have been
  Cross-industry). See `context.md` §3b.
- **Prompt fix found along the way:** the models tagged the *type* of work (reputation
  management, expert witness) as Professional Services. A general rule ("the type of work never
  decides the industry") fixed both cases. It uses invented examples, so the prompt isn't tuned
  to the client's test set.
- **Code:** the CSVs carry `industry`, `secondary_industry` and `taxonomy_version` (code-filled),
  `--balance` cells are `(entity_type, industry)`, `--backfill-subjects` is now
  `--backfill-industries`, `relevance_scores.csv` has `hirer_industry` / `provider_industry` /
  `same_industry`, and the dashboard's stage 3 is Industry.
- **Removed from the pipeline:** `subject.py`, `subject_taxonomy.json`, `classify_subject.md`
  and `subject_manifest.jsonl`, all moved to `docs/archive/2026-09-21/subject_v1/`.
- ⚠️ `industry_manifest.jsonl` is empty. Tagging the 2,894 pages (~1 hour) is item L below, and
  it has to happen before a `--balance` extraction means anything.

### G. Thinking-off change validated: no quality drop found — 21 Sep 2026
I ran a 200-file `extract.py --balance` under the new defaults and compared it with the ON era
(records before 20 Sep 19:00), using the latest outcome per file.

| hirer, 1st review keep | ON | OFF |
|---|---|---|
| **qwen3.8:27b** (the only model whose behaviour changed) | 88.6% (31/35), median 69.3s / 4,520 tok | **95.7% (22/23)**, 7.8s / 184 tok |
| whole pool | 82.5% (104/126) | 85.3% (87/102) |
| still flagged after repair, pool | 3.2% | 4.9% |

- Providers from `qwen3.8:27b` were written 100% of the time in both eras (138 ON, 24 OFF), and
  its median time fell from 195s to 11s.
- Specificity didn't move: 35% of hirer descriptions contained a digit ON, 33% OFF.
- ⚠️ The whole-pool provider write rate fell from 93% to 87%. The drop sits entirely on
  `qwen3.6:35b` (75% → 58%, n=26). That model's thinking was never on, so the change can't be
  the cause; it points to the balanced run selecting a different file mix. The same confound
  applies to every row above, and the OFF samples are small (23–27 per model). Enough to rule
  out a large regression, not a small one.
- The 1,500-token cap fired twice in ~450 calls. Both retries succeeded.
- This run added **85 provider + 97 hirer rows** (CSVs now 622 + 219), with 3 retryable
  errors, all from existing content guards.

### C. Tag columns carried into the CSVs and the labeller — 21 Sep 2026
`providers.csv` / `hirers.csv` carry stage 3's tag after `classify_label`: now `industry`,
`secondary_industry` and `taxonomy_version` (see K). They're code-filled from the tag manifest,
never asked of the LLM, and `extract.py --backfill-industries` refreshes them with no LLM calls.
`relevance_scores.csv` has `hirer_industry`, `provider_industry` and `same_industry`.

⚠️ The question behind this (is `rg_3l` scoring relevance or just a tag match?) can't be
answered yet. It needs tagged, extracted rows and a real `label.py` run first.

### F. Every pipeline script writes a PID file — 21 Sep 2026
`classify.py`, `industry.py`, `extract.py` and `label.py` write `docs/_<stage>.pid`, as `crawl.py`
already did. Each removes its file on exit, and only if the file still holds its own PID. The
dashboard's RUNNING is now exact for all five stages; the 90s manifest-mtime guess is gone.
Verified live: `extract running` during a run, `idle` after, no stale files left behind.

### H. Token caps and new `extract.py` defaults — 21 Sep 2026
- `max_completion_tokens` is 1,500 per extract call and 300 per tagging call. The largest
  thinking-off outputs seen were 655 (both provider passes combined) and 75. A reply cut off
  by the cap raises an explicit error instead of failing as bad JSON. `--ping` confirmed all
  four pool models accept the parameter.
- `extract.py` now defaults to `--workers 4 --rps 1` (was 1 worker, no cap). `--rps 0` removes
  the cap.

### 1. Style rolls are now part of the extracted output — 20 Sep 2026
`extract_variations.json`'s per-file rolls were only in `docs/extract_manifest.jsonl`, so anyone
reading `providers.csv` / `hirers.csv` on their own couldn't tell which wording variant produced
a row — or check whether a variant correlates with weaker records.

- `csv_fields()` now appends one `roll_<name>` column per roll defined for that entity type, so
  the columns follow `extract_variations.json` the way the others follow the JSON schemas.
  Hirer gets `roll_detail`, `roll_voice`; provider gets `roll_title_style`,
  `roll_achievement_style`, `roll_imperfection`.
- Existing rows were backfilled from `extract_manifest.jsonl` (lossless, no re-extraction):
  **531 provider + 122 hirer rows, rolls found for all of them.** Backups at
  `docs/*.csv.pre_rolls.bak`.
- ⚠️ 24 of the oldest hirer rows predate the `voice` roll, so their `roll_voice` is blank. That's
  accurate, not missing data — don't backfill it with a guess.

### 4. Dashboard rebuilt as a pipeline view — 20 Sep 2026
`monitor/dashboard.py` now renders Crawl -> Classify -> Industry -> Extract -> Label left to
right, every stage reporting the same three things (running state, processed, queued) with the
handoff count between each pair. Detail (model chips, tokens, seed table, manifest table) moved
behind a collapsed section. Two accuracy fixes came out of it: the seed total now comes from
`seeds.md` rather than a log line, and the crawl log is whichever `crawl*.log` is newest rather
than a hardcoded `crawl_run.log`. Stage 3 is on it for the first time. See the
`monitor/dashboard.py` section of `context.md`.

### 5. `extract.py --balance` — tag-balanced extraction — 20 Sep 2026
Extraction spends its calls evenly across `(entity_type, <stage-3 tag>)` cells rather than in
manifest (= crawl) order; since K the tag is industry. Measured under the earlier tags, first 200
files: manifest order drew from **3 domains**, `--balance` from **12**. `--per-cell N` caps
per-cell spend; over-cap files stay pending. See the `extract.py` section of `context.md`.

### 6. Thinking switched off in extract.py and the tagging stage — 20 Sep 2026
Applied at your direction. `qwen3.8:27b` went from a median **171.2s / 11,832 completion tokens**
per extraction to **6.0s / 406** — one call in the old regime was observed running 611.7s for a
single record. A 4-file balanced run (2 of them routed to qwen3.8:27b, one with a retry) now
finishes in **41s**; the equivalent 2-file run before the change ran past 600s. The other three
models are unaffected either way.

The quality effect was measured later as item G, and no drop was found.

⚠️ `classify.py` still has thinking on — out of scope here, and its 12,269 pages are done.

The `max_completion_tokens` cap and the `--workers` default were done later, as item H.

### 3. Seed expansion beyond professional services — 20 Sep 2026
35 new seeds in `scrapper/seeds.md` under "Coverage Expansion": science, health, environment,
architecture, design, language, heritage and social-research firms that the
professional-services seed list can't reach. All returned 200 to a plain GET.

---

## Open

### A2. The crawler is starved of RAM — 98 of 121 seeds save nothing  [DIAGNOSED 20 Sep]
The expansion crawl finished having saved **63 pages from 3 domains** (axiomlaw, unitedlex,
elevateservices). All 35 new seeds and 60 of the 63 retried old ones returned zero. The cause is
not the sites and not the seed choices:

- **The machine was at 98% memory — 0.3 GB free of 15.9 GB — for the whole run.**
- 3 seeds died with crawl4ai's explicit `Memory usage exceeded threshold for 600.0 seconds`.
- The other 95 returned `OK (0 pages crawled, 0 saved)` **with no error note at all** — the
  silent `MemoryAdaptiveDispatcher` throttle-to-zero that `context.md` flags as the dominant
  operational failure mode. It is indistinguishable from a genuinely empty site except that it
  produces nothing.

Top consumers at the time: Memory Compression 3.7 GB (itself a symptom), `vmmemWSL` 3.2 GB, and
a game (`Marvel-Win64-Shipping`) 2.3 GB. Freeing WSL and the game recovers ~5.5 GB.

**This retracts the earlier conclusion that 63 seeds were "structurally barren".** They have
almost certainly never run under adequate memory. The seed list may have been fine all along —
and the 35 coverage-expansion seeds are *untested*, not disproven.

Next, in order:
1. Free RAM (`wsl --shutdown`, close the game), confirm >8 GB free.
2. Re-run `crawl.py` at `--concurrency 1`, not 3 — concurrency multiplies browser memory, and 3
   was a bad call on a machine this loaded.
3. Only after a run under healthy memory should any seed be judged barren. Then check
   `docs/_crawl_report.md` — a seed that lands on 0 *twice* with RAM free needs a real diagnosis
   (JS-only SPA, robots.txt, browser-level bot block).
4. Consider lowering `MAX_PAGES_PER_DOMAIN` from 1000 for the long tail, so one greedy domain
   can't consume the whole memory budget.

### L. Tag the corpus with industry, then extract
`docs/industry_manifest.jsonl` is empty and the CSVs were reset. In order:
1. `industry.py` over the 2,894 PROVIDER/HIRER/UNCERTAIN pages (~1 hour at 4 workers / 1 rps),
   or press Start on the dashboard's Industry card.
2. `industry.py --report`: check how big OTHER and Cross-industry are. A large OTHER list is the
   taxonomy gap signal. The corpus's consulting pages will likely lean on Financial Services,
   Energy & Resources and Public Sector, and the client's SME sectors (F&B, marine, social
   services) will be thin. That thinness is the seeding target, not a tagging fault.
3. `extract.py --balance`.

### D. Seed for the client's industries
The client's gigs are Singapore SMEs: F&B, construction, marine, healthcare (TCM, dental), social
services and NGOs, retail. The corpus is global consulting firms. Once L's report shows which
industries are thin, seed for them (see item I on why source selection matters more than prompt
tuning).

### E. People/leadership hubs for BCG, KPMG, Deloitte, Accenture
Unchanged from `seeds.md` — still unresolved. Next attempt is seeding from one confirmed
individual profile URL per firm rather than guessing a hub.

### I. The client Excel is a TARGET SPEC, not ground truth
`client_documents/20260917 Senseigigs_NUS_Test_Dataset_Team31.xlsx` — 30 gigs, 30 showcases, a
1:1 matching key with 0–100 `expected_score_range` and OBVIOUS/SUBTLE/PARTIAL/NEAR-MISS bands.

⚠️ **It is LLM-generated.** The client wrote it with Claude and is not technical. Do NOT use its
scores as an evaluation target: grading our LLM labels against another LLM's labels is circular
and invites exactly the self-preference bias `llm_pool.py` is built to avoid. It is also not a
held-out test set in any meaningful sense.

**What it IS good for: the shape of the output we are trying to produce, grounded in real pages.**
Measured gap between the spec and our current CSVs:

| field | client spec | ours | gap |
|---|---|---|---|
| gig_description contains a digit | 100% | 35% | specificity |
| relevant_experience states "N years" | 100% | 2% | tenure |
| relevant_experience contains a digit | 100% | 40% | specificity |
| gig mentions money/% | 20% | 4% | |
| gig_description length | 400–605 (med 506) | 241–1213 (med 558) | ragged, not tight |
| services_offered_description length | 311–493 (med 380) | 98–488 (med 271) | thin and ragged |

Lengths are roughly right; **specificity is the real gap**, along with the world it describes —
the spec is Singapore SME (hawker stalls, NEA/SFA, MAS, SGX Catalist, BizSAFE, A*STAR, TCM,
NGOs) and our corpus is global big-4 consulting. **4 of 2,894 pages even mention Singapore.**

⚠️ Honest tension: the spec is fully synthetic, so it can be 100% specific and perfectly paired.
Grounded extraction cannot hit 100% "N years" without inventing tenure the source never stated.
The target is "as specific as the source supports, and reject sources too thin to support it" —
which makes **source selection matter more than prompt tuning**.

Also missing: the spec is **paired** (gig n ↔ provider n). Our pipeline produces gigs and
showcases from unrelated pages and has no pairing at all. See item J.

### J. Produce paired gig/showcase records from one source page
To match the spec's shape we need pairs, grounded. A case study page describes both the need and
the expertise applied to it — so one page can yield a gig AND its matched showcase, naturally
paired and both grounded in the same real text. `extract.py` currently forces a page to be
either HIRER or PROVIDER, never both; this would be a real change to `ENTITY_CONFIG` and the
manifest's one-record-per-file assumption.

Difficulty bands could then be constructed rather than guessed: OBVIOUS = the page's own pair;
NEAR-MISS = a showcase paired with a gig from a *different* page carrying the same industry tag
(surface-similar, actually different) — which is a second payoff for the industry tag.
