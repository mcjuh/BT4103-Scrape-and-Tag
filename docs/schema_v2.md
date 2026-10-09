# Record schema v2

JSON Schema (draft-07): `classifier_extractor/schemas/ML_provider_schema_v2.json` and
`ML_hirer_schema_v2.json`. Records are written to `data/output/providers.json` / `hirers.json`.

## Provider

| Field | Type | Filled by |
|---|---|---|
| `name` | null (left empty) | none |
| `title` | string, 2-8 words | LLM |
| `credentials` | list of strings | LLM |
| `years_experience` | integer or null | LLM |
| `about_headline` | string, up to 20 words | LLM |
| `about_bio` | string, 70-100 words | LLM |
| `services` | 1-3 of `{service_title, service_detail}` | LLM |
| `achievements` | list of strings, up to 5 | LLM |
| `technical_proficiency` | up to 4 of `{category, skills[]}` | LLM |
| `how_i_work` | string or null | LLM |
| `availability`, `rate` | string or null | enricher |
| `tags` | object (below) | tagger + code |
| `source_file`, `extracted_by_model` | string | code |

## Gig

| Field | Type | Filled by |
|---|---|---|
| `hirer_ref` | `H-` + 8 hex chars | code |
| `gig_title` | string, 3-10 words | LLM |
| `short_description` | string, ends with `Deliverable:` and `Engagement duration:` sentences | LLM |
| `duration_weeks_min`, `duration_weeks_max` | integer or null | code |
| `additional_notes` | string or null | LLM |
| `source_company`, `source_company_team` | string or null | LLM |
| `tags` | object (below) | tagger + code |
| `source_file`, `extracted_by_model` | string | code |

## Tags (both records)

```
tags
  taxonomy_version
  categories[]                 max 2        = SkillsFuture sectors
    name
    group                      always null
    specialisations[]          1-3          = SkillsFuture tracks
      name
      search_tag               "<track> (<sector>)"
      skills[]                 max 8        = SkillsFuture skills
```

## Rules

- Empty list is `[]`, not `null`.
- Each fact has one home (tenure in `years_experience`, outcomes in `achievements`).
- `how_i_work` is the only provider field not backed by the source.
