# enricher

Adds the structured fields the ranker's Stage-2 features need (see `ranker_input_spec.md`) to
`extract.py`'s records. It runs after extraction:

```
py -3 enricher/enrich.py              # judge new or changed records, then rebuild the outputs
py -3 enricher/enrich.py --no-llm     # rebuild the outputs from saved judgements (no API calls)
```

| Output | New columns |
|---|---|
| `docs/hirers_enriched.csv` | `budget_lo`, `budget_hi` (S$/hour), `seniority_needed`, `start_by` (date or `asap`), `commitment` (days/week), `duration_weeks` |
| `docs/providers_enriched.csv` | `rate_per_hour` (S$), `seniority`, `available_from` (date or `now`), `capacity` (days/week), `availability` (display text) |

Both files keep every column of `hirers.csv` / `providers.csv`, so the ranker import can read them
in their place.

## How the values are made

**All synthetic, apart from `duration_weeks`.** The source pages are case studies and bios, which
never state rates or availability.

1. **Judge (LLM).** One Qwen call per record picks categories on one shared rubric: seniority
   (mid / senior / expert) and price tier (lean / standard / premium) on both sides, plus urgency
   and days per week for gigs. These are saved in `docs/enrich_manifest.jsonl`, keyed by the file
   and a hash of the text read. A re-extracted record, or an edit to `prompts/`, gets judged again;
   nothing else does.
2. **Generate (code).** `rate_card.json` turns categories into numbers. A provider's rate and a
   gig's budget band come from the **same** S$/hour band for the same (seniority, tier), so
   `budget_fit` compares like with like. Provider start dates and capacity are drawn from the
   card's distributions. `duration_weeks` is parsed from the gig's "Engagement duration:" line.

Every draw is seeded by (file, `seed`), so reruns give the same numbers. To regenerate, edit the
bands or bump `seed` in `rate_card.json`, then run `--no-llm`.

Unknown values stay blank (null), never a filler: the ranker's model handles missing values, while
a filler would look like real data.
