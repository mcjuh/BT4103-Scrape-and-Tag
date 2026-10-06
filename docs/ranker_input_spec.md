# Ranker input spec: what hirers.json and providers.json need

The ranker (`ranker/pipeline/`) reads two files, `hirers.json` and `providers.json`.
`import_scrape_and_tag.py` currently builds them from this repo's `data/output/hirers.csv` and
`data/output/providers.csv` (`docs/` before the 2026-10-06 restructure; the counts below are from
the 29 Sep dataset, now in `data/archive/2026-10-06/`). Those files only carry text today. The Stage-2 ranker also needs
**structured** fields (budget, seniority and availability) for the signals text embeddings can't
see. This page defines those fields and explains why the current extraction can't supply them.

Fields marked **missing** are new.

## hirers.json (one record per gig)

| Field | Type | Status | Used for |
|---|---|---|---|
| `hire_id` | int | have | key |
| `hire_title` | string | have | BM25 (title-weighted), dense, cross-encoder |
| `hire_description` | string | have | BM25, dense, cross-encoder |
| `hire_description_additional_notes` | string or empty | have | same text signals |
| **`budget_lo`, `budget_hi`** | number, S$ per hour | **missing** | `budget_fit` |
| **`seniority_needed`** | `mid` / `senior` / `expert` | **missing** | `seniority_fit` |
| **`start_by`** | date or `"asap"` | **missing** | availability fit |
| **`commitment`** | days per week, or `full-time` / `part-time` | **missing** | availability fit |
| **`duration_weeks`** | number (range midpoint) | **missing, but already extracted** (see below) | availability fit |
| `industry`, `secondary_industry` | string | have | analysis only |

## providers.json (one record per provider)

| Field | Type | Status | Used for |
|---|---|---|---|
| `provider_id` | int | have | key |
| `about_title`, `about_description`, `services_offered_title`, `services_offered_description`, `relevant_experience` | string | have | BM25, dense, cross-encoder |
| **`rate_per_hour`** | number, S$, same unit as the hirer budget | **missing** | `budget_fit` |
| **`seniority`** | `mid` / `senior` / `expert` | **missing** | `seniority_fit` |
| **`available_from`** | date or `"now"` | **missing** | availability fit |
| **`capacity`** | same unit as the hirer's `commitment` | **missing** | availability fit |
| `availability` | free text | optional | display only |
| `industry`, `secondary_industry` | string | have | analysis only |

Use `null` for unknown values, not 0 or a default. The ranker's gradient-boosted model
(XGBoost LambdaMART) handles missing values natively; a filler value looks like real data.

## How the ranker uses them

These are the three structured features in `ranker/pipeline/features.py`:

- **`budget_fit`** is 1.0 when the provider's `rate_per_hour` is inside `[budget_lo, budget_hi]`
  and decays linearly outside it, normalised by the band width. Both sides must use the same
  currency and unit.
- **`seniority_fit`** is 1.0 for the same level, 0.5 for one level apart and 0.0 for two apart,
  on the scale `mid < senior < expert`.
- **`avail_immediacy`** is the current availability feature, and it only uses the provider side.
  It matches the provider's free-text `availability` against six hard-coded phrases from the
  synthetic data, so it scores how soon a provider can start regardless of what the gig needs. It
  should be replaced by a two-sided availability fit comparing `start_by` with `available_from`,
  and `commitment` (plus `duration_weeks`) with `capacity`.

In the synthetic data these fields came from generated values (`generate_synthetic_data.py`).
`features.py` reads them from `_hirers_with_taxonomy.json` / `_providers_with_taxonomy.json`, not
from `hirers.json` / `providers.json`. Moving them into the main files as specified here needs a
small change to `features.py`.

## Why the current extraction can't supply them

- **The schemas are text only.** `classifier_extractor/ML_hirer_schema_v1.json` and
  `ML_provider_schema_v1.json` have no budget, rate, seniority or availability fields.
- **Budget and seniority only appear in gig notes, and almost never.** `extract_hirer.md` puts
  budget, timeline and seniority in `hire_description_additional_notes` only when the source
  states them. In the current `docs/hirers.csv`, 25 of 1,074 gigs have notes. The 16 that
  mention money are cost savings ("saves S$138,000 annually"), not budgets. The source pages are
  mostly case studies, which don't publish rates or budgets.
- **The ranker import drops gigs with notes.** `import_scrape_and_tag.py` excludes any gig with
  additional notes, so even that small signal never reaches the ranker.
- **Provider pages don't state rates or availability.** They are consultant bios and service
  pages, not marketplace profiles.

**One field is already there: engagement duration.** `extract_hirer.md` asks for an
`Engagement duration:` estimate (usually 1–8 weeks, at most 6 months) at the end of every gig
description. `import_scrape_and_tag.py` strips it because it's identical boilerplate for text
matching. The import could instead parse it into `duration_weeks` before stripping it. It's an
LLM estimate, not a source fact, so treat it as approximate.

## Where the missing fields could come from

1. **The real platform.** Gig-posting and profile forms collect budget, rate, seniority and
   availability as structured inputs. This is the only source whose values match what the ranker
   will see in production.
2. **Generated values.** Assign plausible values per gig and provider, as the synthetic data did.
   This is quick, but the model then learns the generator's rules rather than real behaviour, and
   the features can become circular if the same rules also shape the labels.
3. **LLM inference from the text.** Seniority can reasonably be inferred from a provider's
   `relevant_experience` and headline (e.g. "Ex-CTO", "15 years"). Rates and availability cannot;
   the text doesn't contain them.

## The current labels don't reflect these fields

The 0–3 grades in `ranker/pipeline/data_sat/` (from `labeller/judge_pools.py`) use
`prompts/rubric_0_3.md`, which deliberately drops the budget and seniority clauses and judges
content fit only. A ranker trained on these labels has no reason to learn that a budget or
availability mismatch matters, even if the features are present. Two options:

- **Apply them outside the learned model**, as filters or score adjustments after ranking
  (e.g. demote providers whose rate is far above the budget, or who can't start in time).
- **Re-grade with a rubric that includes them.** This needs the fields filled in first, and the
  judging pools re-graded end to end so every label means the same thing.

## Decisions needed

1. Where the structured values will come from: platform data, generated values, or inferred.
2. Whether seniority stays as a feature. It's used by `features.py` today and needs a field on
   both sides.
3. Whether budget and availability are learned features (needs new labels) or post-ranking rules
   (works with the current labels).
4. Whether the import should parse `Engagement duration` into `duration_weeks`.
