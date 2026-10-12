# GLM trial: synthetic gigs and providers

**Status: planned, nothing built yet.**

## Goal

Grow the ranker's training data without Claude writing it. A second model (GLM, `x-test-1` on SOCLAAS) writes
gigs and providers, and the existing Qwen grader labels the pairs. The base set (100 gigs and 800 providers,
`data/output/crafted_gigs/`, written by Claude and graded by Qwen) stays and is merged in later.

## Target (update as we go)

**Now: pilot.** 5 gigs x 8 providers = 40 providers, 40 targeted pairs.

Later: a bigger batch, then the full batch (e.g. 100 gigs x 8), with the base set merged in.

## How it works

1. **Design rows (code).** Code decides what each gig is before any model is called: sector and track (real
   SkillsFuture names), seniority (mid, senior, expert), mode (execution, advisory, mixed), generic or specific
   skills, word target, weeks, an opening style, notes or not. This is the main source of variety, so no example
   is needed to make gigs differ. Rules: every sector can appear, all nine level x mode combinations, a few
   generic gigs. The pilot's 5 rows should cover all three levels, all three modes and at least one generic gig.
2. **GLM writes the gig** from its row, following `classifier_extractor/prompts/extract_hirer.md`
   (PUBLIC POST and short_description order, no source material).
3. **GLM writes 8 providers per gig,** two aimed at each grade 3, 2, 1, 0, one per route (table in
   `data/output/crafted_gigs/README.md`). Level, mode and the years band come from the design row, not from
   GLM's reading of the gig, so only content fit varies. Prompt: `manufacture_provider_v2.md` adapted to return
   the schema v2 record directly (`ML_provider_schema_v2.json`), as the base set's providers are.
4. **Validate, retry.** Each output is checked in code; a failure is sent back to GLM with the error message,
   up to 3 tries.
5. **Grade with Qwen** (`qwen3.8:27b`, rubric_01.v5) on the targeted pairs only. Where the Qwen grade is 2 or
   more away from the target, regenerate that provider once and grade again. Do not filter any harder: the
   grade is the label, the target is only an aim.
6. **Compare** with the base set (see "Pilot passes if").

Examples: none at first (zero-shot). If a check fails, add 1-2 examples drawn at random from the base set,
from other sectors than the target, the same kind whatever the target grade, with "form only, never copy
details". Never one fixed example, and never one per grade, or style would become tied to the grade.

## Scripts (to build, in `glm/`)

| File | Does |
|---|---|
| `glm/llm.py` | GLM client: reads `SOCLAAS_*` from `.env`, model `x-test-1`, `max_tokens` of 4000 or more, returns `content`, retries on empty |
| `glm/design.py` | samples the design rows (gigs) and the route per provider |
| `glm/make_gigs.py` | design row to gig record (schema v2) |
| `glm/make_providers.py` | gig plus route to provider record (schema v2) |
| `glm/validate.py` | the checks below, for gigs and providers |
| `glm/run_trial.py` | design, make, validate, retry, write; then calls the grader and the comparison |
| `glm/prompts/` | `gig.md`, `provider.md` |

Outputs go to `data/output/glm_trial/`, with the same shapes as `crafted_gigs/`: `hirers.json`,
`providers.json`, `design.csv`, `providers_design.csv`, `pairs.json`. File names: `glm-gig__<n>_<slug>.md` and
`glm-provider__<n>_<letter>.md`; `extracted_by_model` is `x-test-1`. Fill `hirer_ref` and the duration weeks
with `extract.py`'s `hirer_ref()` and `parse_duration_weeks()`. Shuffle the provider letters per gig so the
name does not give away the target grade. Tags are optional for the pilot (the grader ignores them unless
`--with-tags`); add them later with `taxonomy.nest()`.

Grade:

    python run.py grade --gigs-csv data/output/glm_trial/hirers.json \
        --providers-csv data/output/glm_trial/providers.json \
        --pairs data/output/glm_trial/pairs.json

## GLM notes (probed 2026-10-12)

- Thinking cannot be switched off (`thinking: disabled` and `enable_thinking: False` both do nothing, and the
  second leaks reasoning into `content`). The reasoning comes back in a separate `reasoning_content` field.
- Too small a `max_tokens` leaves `content` empty (reasoning ate it). Use 4000 or more and retry on empty.
- 1M-token context; list price about $0.15 in and $0.50 out per million tokens (a third and a fifth of
  `qwen3.8:27b`), though reasoning tokens are billed as output.
- Logprobs work but are not needed: Qwen grades.
- Not yet tried on these prompts.

## Validation checks

Gig: schema v2; 55-120 words; "Deliverable:" second-to-last sentence and "Engagement duration:" last; duration
parses; no named company; none of `extract_hirer.md`'s stock phrases ("comprehensive", "robust", "seamless", ...).

Provider: schema v2; word counts per the schema (bio 70-100, each service 40-65, how_i_work 25-60, headline up
to 20, title 2-8); years inside the level's band (mid 6-9, senior 12-18, expert 22-30); no "Senior", "Lead",
"Principal", "Partner", "Director" or "Head" in a mid-level title or headline; 3-5 achievements, each with a
figure; no six-word run shared with the gig; no rate or availability (both null); no named person or company.

## Pilot passes if

- At least 90% of outputs pass validation within 3 tries.
- Qwen's grade equals the target for most providers, with nothing 2 or more away after one regeneration.
  Show the target-vs-Qwen table next to the base set's (from `providers_design.csv` and `gig_grades.jsonl`);
  similar shape means GLM follows the routes as well as Claude did.
- Word counts, years and titles look like the base set's (no tell-tale length or phrasing by grade).
- Optional author check: run step 3 on 2 base-set gigs and compare GLM's 8 with Claude's 8 for the same gig.

## Merging later

- Keep one author per gig (all 8 providers from the same model) so style never separates a gig's providers.
- Always split train and test by gig. Train on the base set and test on GLM's as a check that the ranker is not
  reading the author.
- The base set's earlier shelved batch (`data/output/KIV/crafted_gigs_2/`) is not part of this.
