# Crafted gigs

100 hand-written gigs (C01-C100) in schema v2 (`classifier_extractor/schemas/ML_hirer_schema_v2.json`) and 800
hand-written provider profiles for them (eight per gig), for the ranker to learn from. The gigs are written the way
a hirer fills in the platform's gig form, not extracted from case studies: they carry only a title, a short
description, optional notes, and user-picked SkillsFuture tags. The descriptions follow
`classifier_extractor/prompts/extract_hirer.md` (its PUBLIC POST section and short_description order): a one-line
overview of the organisation or the need, the ask and the work, a `Deliverable:` sentence, and last an
`Engagement duration:` sentence. They are specific about the work and general about the organisation: no backstory,
insiders, counterparties, contract terms, money at stake or named estates. Organisation size is left out unless it
sizes the work.

## Gigs

- `hirers_crafted.json`: the 100 records, validated against the schema. `source_file` starts with
  `crafted-gig__`, `extracted_by_model` is `crafted`, `hirer_ref` and the duration weeks are filled with
  `extract.py`'s own `hirer_ref()` and `parse_duration_weeks()`, and the tags are built with
  `taxonomy.nest()`, so every category, track and skill is a real SkillsFuture name. `group` is null, as for
  extracted records.
- `design.csv`: what each gig was written to cover (domain, the seniority the work implies, execution or
  advisory or mixed, generic or specific skills, word count, weeks, hirer notes). It is a coverage sheet for the people
  building features and labels; it is not in the records, so nothing downstream can read it as an answer.

Coverage (`design.csv`):

- All 39 SkillsFuture sectors appear as a gig's main category, plus 2 gigs with no tag at all because none fits.
  The sectors with many tracks go deeper (Infocomm Technology 13 gigs, Accountancy 11, Built Environment 7, Human
  Resource 6, Financial Services 5, Retail 5), each gig on a different track, so that two gigs in one sector often
  need different people.
- Implied seniority 39 mid, 42 senior, 19 expert; mode of work 38 execution, 35 advisory, 27 mixed. The two are
  crossed on purpose: all nine seniority x mode combinations are present (mid advisory and expert execution exist, not
  only the common mid execution and expert advisory).
- 65 specific, 19 generic and 16 mixed skill sets. The generic-skill gigs (proofreading, translation, Excel clean-up,
  slide design, inbox admin, job descriptions, mystery shopping) are there for the rubric's rule that a generic ask is
  matched by a profile showing the skill, whatever its industry.
- Posts open in different ways (the organisation, the need, "I", "Our", a third-person description) so that a model
  cannot learn the first words; a few use bullets. Details that size the work (volumes, tools, regulators) are in.
- 56-101 words; 1 to 16 weeks (two gigs run past 8, as the prompt allows up to 6 months); 25 gigs with hirer notes
  (a budget, a start date or a required qualification); 89 gigs with one tag category, 9 with two, 2 with none.

The descriptions of C01-C30 were rewritten on 2026-10-08 from a first version whose openings told the story behind
each need (see git history). Grades made before that date are stale.

## Providers

800 provider profiles in schema v2 (`classifier_extractor/schemas/ML_provider_schema_v2.json`), eight per gig: two
aimed at each grade of `rubric_01.v5` (3, 2, 1, 0). They follow
`classifier_extractor/prompts/manufacture_provider_v2.md`: each person matches the gig's seniority (years inside
the level's band: mid 6-9, senior 12-18, expert 22-30, with a title and roles of that level) and its mode of
work (execution, advisory or mixed, from design.csv), so the content fit is the only thing that varies. They
state years as a number, name credentials in full, keep one body of work, never name a person or a real
company, never mention the gig or reuse its wording, and state no rate or availability (`availability` and
`rate` are null, as for extracted records before the enricher).

The two profiles per grade take different routes, taken from the rubric's own examples:

| grade | route a | route b |
|---|---|---|
| 3 | the same work on the same kind of problem, in a similar setting | the same work, built up in a different industry |
| 2 | same discipline, a neighbouring sub-focus | the right skills, mostly applied to a different kind of problem |
| 1 | an adjacent area or a transferable skill | a generic skill with no sign of the gig's domain |
| 0 | shares only the gig's industry or setting | shares only a tool, regulator or keyword (e.g. "mezzanine" financing for a mezzanine floor) |

- `providers_crafted.json`: the 800 records, each validated against the schema. `source_file` is
  `crafted-provider__<gig number>_<letter>.md`; the letters a-h are shuffled per gig, so the file name does not
  give away the target grade. `extracted_by_model` is `crafted`. The tags are built with `taxonomy.nest()` from
  hand-picked SkillsFuture tracks, with skills chosen by word overlap with the profile (some lists are empty).
- `providers_design.csv`: the answer sheet (target grade, route, seniority, years, mode, word count) per
  provider. It is not in the records.
- `crafted_pairs.json`: the 800 targeted gig x provider pairs, for `grade_pairs.py --pairs`.

The target grades are what each profile was written to be, not labels. The labels come from the grader:

    python run.py grade --gigs-csv data/output/crafted_gigs/hirers_crafted.json \
        --providers-csv data/output/crafted_gigs/providers_crafted.json \
        --pairs data/output/crafted_gigs/crafted_pairs.json

Leave out `--pairs` to grade all 100 x 800 pairs: each gig's own eight plus 792 off-target profiles, which should
mostly come back 0, with a few same-sector 1s and 2s (for example the tax, cyber security or data profiles against
the accountancy, security and analytics gigs).

Checks run on every record: word counts per the schema (bio 70-100, each service 40-65, how_i_work 25-60,
headline up to 20, title 2-8), years inside the level's band, no "Senior", "Lead", "Principal", "Partner",
"Director" or "Head" in a mid-level title or headline, 3-5 achievements each with a figure, no six-word run
shared with the gig's text, no rate or availability, and none of the prompt's stock phrases. Profiles aimed at
grade 3 average about 13 words longer (203 against 189-190 for the other grades, counting bio, service,
achievements and how_i_work; the ranges overlap) and carry a few more credentials (1.2 against 0.5-1.0 on average).
