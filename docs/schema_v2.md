# Proposed record shape (schema v2) for gigs and showcases

**Status: decisions settled; implemented in `extract.py` and smoke-tested on 15 real records
(7 providers, 7 gigs, plus a rerun). The full re-extraction has not been run.** The schemas are
`classifier_extractor/schemas/ML_hirer_schema_v2.json` and `ML_provider_schema_v2.json` (JSON Schema
draft-07). Each field carries `x-filled-by`, saying who writes it: `llm`, `code` (extract.py),
`tagger` (the tagging calls, assembled by code), `enricher`, `external` (populated afterwards,
outside the LLM) or `none` (left empty).

## What this changes

Today an extracted record is flat text: a provider has one headline, one bio, **one** service and
one paragraph of experience; a gig has a title and one description. The platform's forms take lists
and groups (several services, a list of achievements, grouped technical proficiency, and
category / specialisation with search tags). This proposal makes the extractor emit that shape
directly, so nothing has to be re-parsed from prose.

## Rules the shape follows

1. **Shallow where an LLM writes it.** The most nesting an LLM has to produce is a list of small
   objects: `services` (`{service_title, service_detail}`) and `technical_proficiency`
   (`{category, skills[]}`). Everything else is a string, a list of strings or a number. Small
   models make more JSON mistakes the deeper the nesting goes.
2. **The nested tags are built by code.** Category -> specialisation -> skills is three levels deep,
   but the model never writes that structure. It answers two flat questions (which sector and track
   pairs; which skills from those tracks), and code assembles and validates the nest, so every name
   is a real SkillsFuture sector, track or skill.
3. **A list that has nothing in it is `[]`, not `null`.** `null` is for optional single values.
4. **One home for each fact.** Tenure is `years_experience`, credentials are `credentials`, outcomes
   are `achievements`, so no field restates another.
5. **Facts, not styling, come from the source.** `how_i_work` is the one provider field that is
   not source-backed, and its description forbids new credentials, clients or figures.

## Provider showcase

| Platform form field | v2 field | Type | Filled by |
|---|---|---|---|
| Photo | (not generated; an upload) | | platform |
| Name | `name` | string or null | none: left empty (not generated, to save tokens) |
| Title | `title` | string, 2-8 words | LLM |
| Credentials | `credentials` | list of strings | LLM, from the source |
| (seniority signal) | `years_experience` | integer or null | LLM, from the source |
| About: Headline | `about_headline` | string, up to 20 words | LLM |
| About: Bio | `about_bio` | string, 70-100 words | LLM |
| Category / Specialisation / search tag | `tags` (nested, below) | object | tagger + code |
| Services I Offer | `services` | list of 1-3 `{service_title, service_detail}` | LLM |
| Relevant Achievements | `achievements` | list of strings, up to 5 | LLM |
| Technical Proficiency | `technical_proficiency` | list of up to 4 `{category, skills[]}` | LLM |
| How I Work | `how_i_work` | string or null | LLM (styled, not source-backed) |
| Availability | `availability` | string or null | enricher |
| Rate | `rate` | string or null | enricher |
| Links | (not generated; uploads) | | platform |

## Hirer gig

| Platform form field | v2 field | Type | Filled by |
|---|---|---|---|
| (hirer; one hirer, many gigs) | `hirer_ref` | string, `H-` plus 8 hex characters from the source file name | code (one hirer per record for now) |
| Gig Title | `gig_title` | string, 3-10 words | LLM |
| Short Gig Description | `short_description` | string, ends with a deliverable sentence (labelled `Deliverable:` or not) and an `Engagement duration:` sentence | LLM |
| (matching signal) | `duration_weeks_min`, `duration_weeks_max` | integer or null | code, parsed from the duration sentence |
| (matching signal) | `additional_notes` | string or null | LLM, only when the source states budget, timeline or seniority |
| Category / Specialisation / search tag | `tags` (nested, below) | object | tagger + code |
| (metadata) | `source_company`, `source_company_team` | string or null | LLM |

## The nested tags (same block on both records)

```
tags
  taxonomy_version
  categories[]                    at most 2          = SkillsFuture sectors
    name
    group                         Industry | Function | Subject | Others | null
    specialisations[]             1-3 per category   = SkillsFuture tracks
      name
      search_tag                  "<track> (<sector>)"
      skills[]                    up to 8            = SkillsFuture TSC titles
```

**What `group` is.** The platform's Category field is a multi-select grouped under four headings:
Industry, Function, Subject and Others. `group` says which heading a category sits under, so it is a
property of the category (a lookup from category name to heading), not of any one record.
SkillsFuture sectors carry no such grouping, so the extractor cannot know it and always writes
`null`. It is populated afterwards from the platform's own category list, never by the LLM. Since it
is a lookup, the platform could also join on the category name and leave the field off the records.

## Example provider record

```json
{
  "source_file": "example.com__people_example.md",
  "extracted_by_model": "qwen3.8:27b",
  "name": null,
  "title": "Restructuring and Insolvency Adviser",
  "credentials": [
    "Registered Liquidator (Singapore)",
    "Chartered Accountant (Australia and New Zealand)"
  ],
  "years_experience": 20,
  "about_headline": "Turnaround and insolvency adviser for distressed businesses in Singapore and Southeast Asia",
  "about_bio": "I spent over 20 years in insolvency and restructuring, acting as liquidator, receiver and judicial manager for boards, creditors and investors across Southeast Asia. My focus is restructuring plans, enforcement actions and contentious insolvency matters in sectors such as real estate, manufacturing, construction and maritime. I previously led the restructuring practice of a global advisory firm in Singapore. I work with distressed businesses that need a clear route through creditor negotiations.",
  "services": [
    {
      "service_title": "Restructuring and Insolvency Advisory",
      "service_detail": "Practical advisory for Singapore SMEs, family businesses and mid-sized companies facing financial distress. Services include formulating restructuring plans, advising boards on their duties, managing enforcement action against distressed companies, and navigating judicial management and schemes of arrangement. Familiar with the Insolvency, Restructuring and Dissolution Act (IRDA) and cross-border enforcement. Not focused on bookkeeping or tax filing."
    }
  ],
  "achievements": [
    "Led a scheme of arrangement implementation for a listed Singapore company.",
    "Advised on the restructuring of a Singapore-headquartered oil and gas company.",
    "Handled enforcement engagements over assets held in several jurisdictions."
  ],
  "technical_proficiency": [
    {
      "category": "Insolvency",
      "skills": ["Restructuring plans", "Judicial management", "Schemes of arrangement", "Cross-border enforcement"]
    }
  ],
  "how_i_work": "I start with a short review of cash, creditors and directors' duties, set out the realistic options in plain terms, and then work alongside management and creditors to carry the chosen route through. I report in writing after every milestone.",
  "availability": "Available from November 2026, 2 days a week.",
  "rate": "From S$3,000 per day.",
  "tags": {
    "taxonomy_version": "sf_v1",
    "categories": [
      {
        "name": "Accountancy",
        "group": null,
        "specialisations": [
          {
            "name": "Restructuring and Insolvency",
            "search_tag": "Restructuring and Insolvency (Accountancy)",
            "skills": ["Debt Restructuring", "Restructuring Insolvency Advisory", "Stakeholder Management"]
          }
        ]
      }
    ]
  }
}
```

## Example hirer gig

```json
{
  "source_file": "example.com__case-study_example.md",
  "extracted_by_model": "qwen3.6:35b",
  "hirer_ref": "H-5d48a79a",
  "source_company": "Example Firm",
  "source_company_team": null,
  "gig_title": "Draft Data Processing Agreements for Payments Start-up",
  "short_description": "We're a payments start-up in Singapore, regulated by MAS. Looking for someone to draft and review 20-30 data processing agreements against PDPA and MAS requirements, working from our existing privacy templates and aligning them with how we handle data today. At the end we'd like the completed agreements and a brief summary of the compliance checks. Engagement duration: 3-5 weeks.",
  "duration_weeks_min": 3,
  "duration_weeks_max": 5,
  "additional_notes": null,
  "tags": {
    "taxonomy_version": "sf_v1",
    "categories": [
      {
        "name": "Legal Services",
        "group": null,
        "specialisations": [
          {
            "name": "Advisory and Advocacy",
            "search_tag": "Advisory and Advocacy (Legal Services)",
            "skills": ["Contract Drafting", "Legal Writing", "Legal Research and Analysis"]
          }
        ]
      }
    ]
  }
}
```

## Compatibility with the stages that read the CSVs

The enricher, labeller and ranker import read the v1 text columns. The CSV keeps them, derived by
code from the v2 fields, so those stages don't change and relevance features see the same kind of
text:

| v1 column | Derived from |
|---|---|
| `about_title` | `about_headline` |
| `about_description` | `about_bio` |
| `services_offered_title` | `services[0].service_title` |
| `services_offered_description` | the one service's detail; with several services, every service as `title: detail`, so the ranker's text holds them all |
| `relevant_experience` | `years_experience` as a sentence ("20 years of experience."), then `achievements`, then "Credentials: ..." |
| `hire_title` | `gig_title` |
| `hire_description` | `short_description` |
| `hire_description_additional_notes` | `additional_notes` |

Four small structured columns ride along: `years_experience` (providers), `hirer_ref` and
`duration_weeks_min` / `duration_weeks_max` (gigs). The nested records are written to
`providers.json` / `hirers.json`; the CSV's `tags_json` column carries the nested tags.

## How it is implemented in `extract.py`

- `ENTITY_CONFIG` points at the v2 schemas. Each prompt's field list and skeleton are generated
  from them, now including the item keys of a list of objects, and only fields marked
  `x-filled-by: llm` are asked of the model.
- The provider facts pass returns the title, credentials, years, headline, bio, services,
  achievements and technical proficiency. The style pass returns only the headline, bio,
  achievements and `how_i_work`; everything else is carried over from the facts pass, so a restyle
  can't drift the facts and the pass costs fewer tokens.
- A model reply is tidied before validation (a list field given as null, one object or a bulleted
  string becomes a list; lists are cut to their maximum; "20 years" becomes 20). A service missing
  its detail is dropped. A provider with no service is rejected as non-qualifying.
- `name` and the tag `group` are written as null; `hirer_ref` and the duration weeks are filled by
  code; the enricher fills `availability` and `rate`.
- The localisation check and spelling pass read the new text fields (`services`, `achievements`,
  `technical_proficiency`, `how_i_work`) and skip `credentials`, which are personal facts and never
  localised.
- Every finished record is validated against the whole v2 schema before it is written.

## Decisions

Settled:

1. **Services per provider: 1-3 allowed.** Each is still one engagement a single client could hire
   for. Expect a longer extraction than today's single service.
2. **`name`: left empty (null)**, not generated, to save tokens. **`availability` and `rate`:** the
   enricher fills them.
3. **`group`: left null by the extractor** and populated afterwards, outside the LLM, from the
   platform's own category list.
4. **`hirer_ref`: filled by code, not the LLM, one per record for now.** One hirer can post several
   gigs, but every crawled page yields one gig, so each record is its own hirer. A shared
   `hirer_ref` for several gigs would need a grouping rule (for example one publisher or one source
   team) added to `hirer_ref()` in `extract.py`.

Nothing is left open.
