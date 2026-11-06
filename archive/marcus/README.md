# Marcus pipeline (original)

The first version of the pipeline. It turned scraped web pages into two kinds of output: **gigs** (job-style requests) and **provider profiles** (anonymised bios).

All scripts call an OpenAI-compatible LLM endpoint set in `.env` (`SOCLAAS_BASE_URL`, `SOCLAAS_API_KEY`, `SOCLAAS_MODEL`). They write results to `.jsonl` manifests and skip files that are already done when rerun.

## Flow

```
raw HTML pages
     │
     ▼
triage.py ──► individual_profile/ ──► showcase.py ──► provider profiles
     │
     └──────► gig/ ──► gig.py ──► combine ──► review ──► repair ──► gigs
                                     ▲                     │
                                     └──── collect_retries ┘
```

## Scripts

| Step | Script | What it does |
|---|---|---|
| 1 | `triage.py` | The LLM labels each HTML page `INDIVIDUAL_PROFILE`, `GIG`, `IGNORE` or `UNCERTAIN`, then the page is copied into a folder named after its label. |
| 2a | `gig.py` | Turns each case-study page into one made-up gig `{title, description}`, written as if the original client were posting the job. It returns `{}` if the page has no real project. A random roll sets the length (Minimal, Standard or Detailed). |
| 2b | `showcase.py` | Turns each person's page into an anonymised profile `{about, achievements}`. spaCy masks names and gendered pronouns are made neutral. Pass 1 pulls out the facts; pass 2 rewrites them in a randomly chosen style. |
| 3 | `collect_gig_retries.py` | Copies source files whose gig output is broken into a retry folder so they can go through `gig.py` again. |
| 4 | `combine_gig_manifests.py` | Merges all the gig manifests. When a file shows up more than once, the newest record wins. |
| 5 | `review_gig_content.py` | A second LLM call checks each gig against its source and returns `keep` or `retry`. It only flags clear problems, such as made-up requirements or unrelated skills bundled together. |
| 6 | `gig_repair.py` | Rewrites the flagged gigs using the source, the old gig and the reviewer's reason. |

## Where it lives now

| Marcus script | Current pipeline |
|---|---|
| `triage.py` | `classifier_extractor/classify.py` + `prompts/classify_triage.md` |
| `gig.py` | `extract.py` hirer pass (`prompts/extract_hirer.md`) |
| `showcase.py` | `extract.py` provider passes (`prompts/extract_provider_facts.md`, `extract_provider_style.md`) |
| `review_gig_content.py` + `gig_repair.py` | `extract.py` hirer review + repair (`prompts/review_hirer.md`, `repair_hirer.md`) |
| `collect_gig_retries.py`, `combine_gig_manifests.py` | Not needed: records are schema-checked and retried before writing, and there's one manifest |

## Shared tricks

- **Thinking-mode probe:** before starting, the scripts try several ways to turn off Qwen-style "thinking" and keep the first one that works.
- **Resumable:** each result is added to the manifest as it finishes. Records with status `error` or `parse_error` are retried on the next run.
- **Grounding rules:** the prompts forbid made-up budgets, durations, certifications and similar details. The real company name is never used as the hirer.
