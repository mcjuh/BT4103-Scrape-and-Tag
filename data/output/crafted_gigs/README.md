# Crafted gigs

30 hand-written gigs in schema v2 (`classifier_extractor/schemas/ML_hirer_schema_v2.json`), for the ranker to
learn from. They are written the way a hirer fills in the platform's gig form, not extracted from case
studies: they carry only a title, a short description that ends in `Deliverable:` and
`Engagement duration:` sentences, optional notes, and user-picked SkillsFuture tags. Organisation size and
revenue are left out unless the work depends on them.

- `hirers_crafted.json`: the 30 records, validated against the schema. `source_file` starts with
  `crafted-gig__`, `extracted_by_model` is `crafted`, `hirer_ref` and the duration weeks are filled with
  `extract.py`'s own `hirer_ref()` and `parse_duration_weeks()`, and the tags are built with
  `taxonomy.nest()`, so every category, track and skill is a real SkillsFuture name. `group` is null, as for
  extracted records.
- `design.csv`: what each gig was written to cover (domain, the seniority the work implies, execution or
  advisory or mixed, generic or specific skills, word count, weeks). It is a coverage sheet for the people
  building features and labels; it is not in the records, so nothing downstream can read it as an answer.

Coverage: 21 SkillsFuture sectors; implied seniority 11 mid, 13 senior, 6 expert; mode of work 12
execution, 11 advisory, 7 mixed, spread across every seniority level so that the two do not move together;
8 generic, 16 specific and 6 mixed skill sets; 43-119 words; 1 to 12 weeks; 8 gigs with hirer notes
(a budget, a start date or a required qualification).

Grade them with `python run.py grade --gigs-csv data/output/crafted_gigs/hirers_crafted.json ...`.
