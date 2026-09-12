# Progress notes (temporary) — 11 Sep 2026

Working notes from today's session. Delete once the open items are settled.

## State right now

- No pipeline script is running. The last `extract.py` run finished around 23:36.
- Data (uncommitted): `docs/hirers.csv` 29 rows, `docs/providers.csv` 7 rows.
  **All 36 were written before today's anonymisation and robustness fixes.**
- Classification is complete: 12,269 pages → 1,011 hirer, 1,856 provider, 27 uncertain,
  9,375 ignore (2,894 usable, 23.6%). All were classified by a single model, before
  multi-model routing existed.
- Restart `extract.py` before the next batch. A running process keeps the code and prompts it
  loaded at start-up.

## What changed today

| Area | Change |
|---|---|
| Model pool | `llama3.1:8b`, `qwen3.8:27b`, `qwen3.6:35b`, `qwen3-vl:32b`. Dropped: `ornith1.5:35b` (team request), `gemma4:26b` and `qwen3.5:9b` (too slow / SOCLAAS 502s), `qwen3-coder-next` (code-specialised). The labeller uses the same four models, which costs 7 calls per pair. |
| Thinking mode | The disable strategies were removed from `extract.py`, so thinking is on. The timeout is now 180s in `classify.py` and `extract.py`. The labeller still turns thinking off, because its scoring needs that. |
| Hirer review | Marcus's review and repair step is ported: a different model reviews each gig and it is rewritten once if flagged. **New:** the rewrite is reviewed again, and it's rejected if still flagged. |
| Hirer prompt | Asks for a natural, informal marketplace voice, with a per-file "voice" option (task / context / role / individual / organisation) to stop the "We need…" openings. |
| Anonymisation | Prompts (provider facts and style, hirer, review) require generic names for firms, clients, divisions and teams. Provider pages have the publisher's name replaced with "the firm" before the model reads them. A code check rejects and retries any record that names the publisher (`PUBLISHER_ALIASES`). spaCy is installed and now required, for masking person names. |
| Robustness | The API's JSON-only mode is on for all extraction calls. List- and dict-shaped fields are joined into strings. Records that copy the prompt's example achievements are rejected and retried. |
| Output | New CSV column `time_taken_by_model` (seconds per row). The 14 older hirer rows were backfilled from the manifest. |
| Schemas | `ML_*_schema_v1.md` → `.json` (already committed). |

## Verified

- The offline tests pass (mocked model calls: review, repair, re-review, provider passes).
- **Live test, 4 provider bios (EY, PwC):** anonymised ("a major professional services firm") with no errors.
- **Live test, the Hillsborough County gig run 4 times:** 3 clean. In 1 run the reviewer kept a rewrite that still
  mentioned Hillsborough or Florida somewhere in the record (see open item 2).

## Open items (decisions needed)

1. **Re-extract the existing 36 rows?** All 7 providers and about 4 hirers name a firm, client, team or award
   (U.S. Bank, the Federal Aviation Agency, EY Americas, the Financial Conduct Authority, …). To redo them: back up,
   remove the rows and their manifest lines, then rerun.
2. **Client names can still slip through.** The code check only knows the publisher. Client names depend on the
   reviewer, which missed one in 4 test runs.
3. **llama3.1:8b invents provider achievements** (for example the mobile apps and $100K savings attributed to a financial regulator). Nothing checks
   provider records against the source. Options: review providers too, or take llama off provider pages.
4. **Titles repeat** the "<Role> Specialist for <X>" pattern. Could add a per-file title option.
5. **`source_company` / `source_company_team`** (hirer metadata) still name the firm. Keep or blank them?
6. **The reviewer can be over-strict.** It once removed tools the source supported (Power Platform, Power BI).
7. **`qwen3.8:27b` is slow:** 50–440s per record.

## Files and links

- Week 5 update (Word): `Week5_Update_Data_Engineering_v2.docx` (current). The original `.docx` is superseded.
- Diagram of the extract loops: https://claude.ai/code/artifact/72f48225-9183-4f91-b55b-fb3051c500e4
- Week 6 update page: https://claude.ai/code/artifact/10ec4f2a-e7f8-4cc8-8c22-733aa1eac9a4 (out of date: lists
  5 models, including `ornith1.5:35b`).
- Backups of `providers.csv` and `extract_manifest.jsonl`, from before the fabricated Woolard row was removed, are in
  the session scratchpad.
