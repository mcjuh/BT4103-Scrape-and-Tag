# Crafted gigs

30 hand-written gigs in schema v2 (`classifier_extractor/schemas/ML_hirer_schema_v2.json`), for the ranker to
learn from. They are written the way a hirer fills in the platform's gig form, not extracted from case
studies: they carry only a title, a short description, optional notes, and user-picked SkillsFuture tags.
The descriptions follow `classifier_extractor/prompts/extract_hirer.md` (its PUBLIC POST section and
short_description order): a one-line overview of the organisation or the need, the ask and the work, a
`Deliverable:` sentence, and last an `Engagement duration:` sentence. They are specific about the
work and general about the organisation: no backstory, insiders, counterparties, contract terms, money at
stake or named estates. Organisation size is left out unless it sizes the work.

- `hirers_crafted.json`: the 30 records, validated against the schema. `source_file` starts with
  `crafted-gig__`, `extracted_by_model` is `crafted`, `hirer_ref` and the duration weeks are filled with
  `extract.py`'s own `hirer_ref()` and `parse_duration_weeks()`, and the tags are built with
  `taxonomy.nest()`, so every category, track and skill is a real SkillsFuture name. `group` is null, as for
  extracted records.
- `design.csv`: what each gig was written to cover (domain, the seniority the work implies, execution or
  advisory or mixed, generic or specific skills, word count, weeks, hirer notes). It is a coverage sheet for the people
  building features and labels; it is not in the records, so nothing downstream can read it as an answer.

Coverage: 21 SkillsFuture sectors; implied seniority 11 mid, 13 senior, 6 expert; mode of work 12
execution, 11 advisory, 7 mixed, spread across every seniority level so that the two do not move together;
8 generic, 16 specific and 6 mixed skill sets; 56-101 words; 1 to 12 weeks; 8 gigs with hirer notes
(a budget, a start date or a required qualification).

The descriptions were rewritten on 2026-10-08 from a first version whose openings told the story behind
each need (see git history); domains, seniority, mode, specificity, durations and notes were kept, two
dates in the notes were made generic and two titles lost an "Our". Grades made from the first version are
stale.

Grade them with `python run.py grade --gigs-csv data/output/crafted_gigs/hirers_crafted.json ...`.

## Crafted providers

240 hand-written provider profiles in schema v2 (`classifier_extractor/schemas/ML_provider_schema_v2.json`),
eight per crafted gig: two aimed at each grade of `rubric_01.v5` (3, 2, 1, 0). They follow
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

- `providers_crafted.json`: the 240 records, each validated against the schema. `source_file` is
  `crafted-provider__<gig number>_<letter>.md`; the letters a-h are shuffled per gig, so the file name does not
  give away the target grade. `extracted_by_model` is `crafted`. The tags are built with `taxonomy.nest()` from
  hand-picked SkillsFuture tracks, with skills chosen by word overlap with the profile (some lists are empty).
- `providers_design.csv`: the answer sheet (target grade, route, seniority, years, mode, word count) per
  provider. It is not in the records.
- `crafted_pairs.json`: the 240 targeted gig x provider pairs, for `grade_pairs.py --pairs`.

The target grades are what each profile was written to be, not labels. The labels come from the grader:

    python run.py grade --gigs-csv data/output/crafted_gigs/hirers_crafted.json \
        --providers-csv data/output/crafted_gigs/providers_crafted.json \
        --pairs data/output/crafted_gigs/crafted_pairs.json

Leave out `--pairs` to grade all 30 x 240 pairs (each gig's own eight plus 232 off-target profiles, which
should mostly come back 0).

Checks run on every record: word counts per the schema (bio 70-100, each service 40-65, how_i_work 25-60,
headline up to 20, title 2-8), years inside the level's band, no "Senior", "Lead", "Principal", "Partner",
"Director" or "Head" in a mid-level title or headline, 3-5 achievements each with a figure, no six-word run
shared with the gig's text, no rate or availability, and none of the prompt's stock phrases. Profiles aimed at
grade 3 average about 15 words longer (213 against 196-198 for the other grades; the ranges overlap) and carry
a few more credentials (1.2 against 0.7-1.1 on average).
