# enricher

Adds the structured fields the ranker's Stage-2 features need (see `docs/ranker_input_spec.md`) to
`extract.py`'s records. It runs after extraction:

```
python run.py enrich              # judge new or changed records, then rebuild the outputs
python run.py enrich --no-llm     # rebuild the outputs from saved judgements (no API calls)
```

| Output | New columns |
|---|---|
| `data/output/hirers_enriched.csv` | `budget_lo`, `budget_hi` (S$/hour), `seniority_needed`, `start_by` (date or `asap`), `commitment` (days/week), `duration_weeks`, `sector`, `track` |
| `data/output/providers_enriched.csv` | `rate_per_hour` (S$), `seniority`, `available_from` (date or `now`), `capacity` (days/week), `availability` (display text), `sector`, `track` |

`sector` and `track` come from SkillsFuture's skills framework (`data/reference/skillsfuture/sector.csv`,
`track.csv`: 39 sectors, 247 tracks, the same files as the ranker's `pipeline/data_taxo/`). They place the
*work* (gigs) or the *service* (providers), not the client's industry. Track names repeat across sectors,
so read a track together with its sector.

`--tag v4` enriches a tagged extraction (`extract.py --out-tag v4`): it reads `data/output/hirers_v4.csv` /
`providers_v4.csv`, writes `*_v4_enriched.csv`, and keeps its judgements in `data/manifests/enrich_v4.jsonl`.

Both files keep every column of `hirers.csv` / `providers.csv`, so the ranker import can read them
in their place.

## How the values are made

**All synthetic, apart from `duration_weeks`.** The source pages are case studies and bios, which
never state rates or availability.

1. **Judge (LLM).** One Qwen call per record picks categories on one shared rubric: seniority
   (mid / senior / expert), price tier (lean / standard / premium) and SkillsFuture sector and
   track on both sides, plus urgency and days per week for gigs. Code checks that the sector exists
   and the track is listed under it, and retries the call if not. These are saved in `data/manifests/enrich.jsonl`, keyed by the file
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
