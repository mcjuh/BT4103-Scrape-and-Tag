# Crafted gigs, second generation

100 more hand-written gigs (C101-C200) in schema v2 (`classifier_extractor/schemas/ML_hirer_schema_v2.json`), made the
same way as the first generation in `../crafted_gigs/` (C01-C100) and with no topic in common with it. They are
written the way a hirer fills in the platform's gig form: a title, a short description, optional notes and
user-picked SkillsFuture tags. The descriptions follow `classifier_extractor/prompts/extract_hirer.md` (PUBLIC POST
and short_description order): a one-line overview of the organisation or the need, the ask and the work, a
`Deliverable:` sentence, and last an `Engagement duration:` sentence. They are specific about the work and general
about the organisation: no backstory, insiders, counterparties, contract terms, money at stake or named estates.
Organisation size is left out unless it sizes the work.

No providers have been written for this set yet; the providers in `../crafted_gigs/` are for C01-C100 only.

## Files

- `hirers_crafted.json`: the 100 records, validated against the schema. `source_file` starts with `crafted-gig__`,
  `extracted_by_model` is `crafted`, `hirer_ref` and the duration weeks are filled with `extract.py`'s own
  `hirer_ref()` and `parse_duration_weeks()`, and the tags are built with `taxonomy.nest()`, so every category, track
  and skill is a real SkillsFuture name (each skill belongs to the track it sits under). `group` is null.
- `design.csv`: what each gig was written to cover (domain, the seniority the work implies, execution or advisory or
  mixed, generic or specific skills, word count, weeks, hirer notes). A coverage sheet for the people building
  features and labels; it is not in the records, so nothing downstream can read it as an answer.

## Coverage (`design.csv`)

- All 39 SkillsFuture sectors appear as a gig's main category, plus 2 gigs with no tag because none fits
  (C199 transcription, C200 price-list research). Sectors with many tracks go deeper: Infocomm Technology 13 gigs,
  Accountancy 11, Built Environment 7, Human Resource 6, Financial Services 5, Retail 5.
- Implied seniority 39 mid, 42 senior, 19 expert; mode of work 45 execution, 26 advisory, 29 mixed. All nine
  seniority x mode combinations are present (mid advisory 4, mid mixed 3, expert execution 4 are the thinnest).
- 76 specific, 16 mixed and 8 generic skill sets. The generic ones (IT runbooks, survey analysis, HRIS data clean-up,
  podcast editing, member survey, service standards, transcription, price research) are there for the rubric's rule
  that a generic ask is matched by a profile showing the skill, whatever its industry.
- Posts open in different ways (the organisation, the need, "I", "We", "Our", a plain noun phrase) so that a model
  cannot learn the first words.
- 55-74 words; 1 to 6 weeks; 25 gigs with hirer notes (a budget, a deadline, a start date, a qualification); 90 gigs
  with one tag category, 8 with two, 2 with none; 0-4 skills per gig, chosen by hand from the chosen tracks.

## Checks run

Schema validation; 55-120 words; "Deliverable:" second-last and "Engagement duration:" last; durations parsed;
unique `hirer_ref` and `source_file`; none of the prompt's stock phrases; no named company or place. Note that
many of the SF skills under a track are only loosely related to a gig (some tracks have no matching skill at all),
so a gig's skill list is sometimes short or empty on purpose.

## Next steps

To rank against these gigs they need providers: `manufacture_provider_v2.md` with two profiles aimed at each
`rubric_01.v5` grade, as was done for C01-C100. Grading uses the same command as for the first set, with `--gigs-csv`
pointing at this directory's `hirers_crafted.json`.
