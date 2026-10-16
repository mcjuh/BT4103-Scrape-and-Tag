# 16 Oct TODO

Notes from the review of the GLM trial (200 gigs, 1,348 of 1,600 providers committed at the time) against the
Claude base set (100 gigs, 800 providers), and of how `labeller/grade_pairs.py` turns logprobs into grades.
Numbers are from `data/output/glm_trial/` and `data/manifests/gig_grades.jsonl` on `new-grader-oct03`.

> **Caveat (as of writing).** The Qwen grading of the GLM pairs has not been done: the committed grade log holds
> only the pilot's 41 GLM pairs. Everything below about GLM is about the text, not its grades. Once the 1,600 pairs
> are graded we will see the grade distribution (how close Qwen lands to each provider's target grade, and how
> many pairs are low-confidence), and the grading decisions in section 5 and the order of work should be
> revisited then. Sections 3 and 4 change the GLM text, so grades made before the mend (section 6) are stale for
> any record it touches.

## 1. Linguistic rigidity: what we found

**Both sets are repetitive in their wording, and that is mostly fine.** The client's own 30 gigs mostly open
"We run..." or "We are a...", so plain, literal, repetitive posts are realistic.

| Pattern | Base set (Claude) | GLM |
|---|---|---|
| Gig opener | "We are a" 19%, "Looking for a" 15% | "I run a" 29, "Looking for a" 26, "We run a" 24 (of 200) |
| Gig shape | 4 or 5 sentences (89 of 100) | 5 sentences in 107 of 200, 4 to 6 overall |
| Deliverable starts | varied ("review report", "gap assessment", ...) | "a written..." in 60 of 200 |
| Gig length | 70 words (sd 10) | 90 words (sd 13), same for mid, senior and expert |
| Provider bio opener | "I have N years" in 800 of 800 | "I have spent..." in 853 of 1,348 (63%) |
| Provider shape | 1 service, exactly 4 achievements | 1 service, 4 or 5 achievements, length sd 8 against 13 |
| Em dash | 0 | 34% of gigs (68 of 200), 2.5% of providers |
| Achievement verb tied to mode | tendency (see below) | near rule (see below) |

**Achievement verbs against mode of work** (share of achievements that start with an advisory verb / an execution verb):

| Provider mode | Base set | GLM |
|---|---|---|
| Advisory | 38% / 22% | 99% / 0% |
| Execution | 9% / 44% | 1% / 55% |
| Mixed | 13% / 36% | 33% / 36% |

Nothing else we measured moves with the target grade in GLM providers (words 177.8, 177.1, 177.7, 178.8 for targets
3, 2, 1, 0; achievements and credentials are flat too).

## 2. The rule

**Stylistic or word-level rigidity matters only if it can affect the label or the ranker's features.** Repetitive
openers, a fixed sentence count, one service, a narrow length spread and similar sameness are harmless on their own:
the ranker reads content, not first words, and real posts are repetitive too. A pattern is a problem when:

1. **It predicts the label (or a rubric term) deterministically,** so a model could learn the generator instead of
   the world. This is the achievement verb to mode pattern above. The years band to seniority link is the same kind
   of pattern, but the rubric reads years, so it is intended and stays.
2. **It tells apart authors that get mixed in one training set** (the em dash). Only matters when GLM and Claude data
   are merged; the plan already splits train and test by gig.

Test it directly: train on the base set and test on GLM, then the reverse. A large drop points at generator artefacts.

## 3. Suggested GLM prompt changes (from the rule)

Change only what touches the label. Edit `glm/prompts/provider.md` and `glm/prompts/gig.md`, and `glm/validate.py` if noted.

- [ ] **Decouple achievement verbs from mode (provider prompt).** Say that mode shows in what the person offers
      (services, `how_i_work`), not in the verb class of every achievement. Ask for a mix of verbs: advisory
      profiles should include some production verbs (Wrote, Built, Prepared), execution profiles some leading or
      advising verbs. Aim at the base set's tendency, not a rule: advisory about 38% advisory / 22% execution,
      execution about 9% / 44%, mixed about 13% / 36%.
- [ ] **Soft validator check.** Reject a provider only when all achievements fall in one verb class (that is the
      near-rule pattern). Do not enforce the base-set percentages.
- [ ] **Gig side: leave the mode verbs.** Advisory gigs lean on "review" and "recommend" and execution gigs on
      "draft" and "build". The rubric defines mode from the deliverable and its verbs, so this is by design. Check
      that mixed gigs name both a thing to produce and a thing to advise on.
- [ ] **Leave alone (no label effect):** "I have spent" bio opener, the 5-sentence gig shape, "a written..."
      deliverables, "Independent..." titles, one service, 4 or 5 achievements, 90-word gigs, years inside the
      level band. Optional, only if GLM data will be merged with Claude data: bring the gig word target down
      toward 70 and vary the deliverable opening.
- [ ] Do not edit prompts or `design.py` while the 200-gig run is still going. Change them for the next batch, or
      after the run is committed.

## 4. Pending action: remove em dashes, keep the text readable

Affects 68 of 200 gigs and about 34 of 1,348 providers (2.5%); the base set has none.

- [ ] **Prompt rule (first line of defence):** "Never use em dashes or en dashes. Use a comma, a colon, brackets or
      start a new sentence."
- [ ] **Post-process in `glm/make.py`, before `validate.py`,** for what slips through. Do not swap the dash for a
      hyphen. Handle it by case:
      - a clause break ("X, Y"): replace with a comma;
      - an aside between two dashes: replace the pair with commas or brackets;
      - a dash that introduces an explanation or a list: replace with a colon;
      - a dash before a full second clause: end the sentence with a full stop and capitalise the next word;
      - a number range with an en dash ("1-2 weeks"): hyphen, as the base set writes ranges.
- [ ] **Validator:** fail if any of the dash characters remains, and re-check that word counts and the "Deliverable:" /
      "Engagement duration:" ordering still pass after the replacement.
- [ ] **Readability check:** list every changed sentence for a 20 to 30 sample read-through (before and after side
      by side) and confirm the cut does not leave a fragment, a run-on or a double comma.
- [ ] **Existing data:** the 200 gigs and the committed providers already contain dashes. Decide between
      regenerating the affected records and fixing them in place with the same rules plus the sample check.
      Coordinate with the run in progress so the same files are not edited from two places.

## 5. Grading: tradeoffs of each method

`grade_pairs.py` today: the model answers "grade score"; the probabilities are a softmax over the four digit
tokens at the answer position (top-20 logprobs, renormalised); the grade is the argmax; the score is the
band-weighted expectation, where the chosen band uses the score the model wrote and every other band its midpoint,
clipped into the grade's range. Figures are from the 841 v5 pairs in the log.

| | **Ordinal (grade 0 to 3)** | **Continuous (score 0 to 1)** |
|---|---|---|
| **Argmax / softmax (take the top band; for the score, only the chosen band's written number)** | **Pro:** a real mode of the model's distribution; never invents a grade it did not favour; stable and easy to explain; ties go to the lower grade. **Con:** throws away confidence: 199 pairs (24%) have a top-band probability under 0.6, and mean top probability is 0.80 with 30% of pairs above 0.99. Labels at 0.5/0.5 look the same as labels at 0.99. | **Pro:** simple and uses the rubric's own ranges. **Con:** the written number is an anchor, not a measurement: 0.05 (228 times), 0.95 (96), 0.35 (90), 0.98 (90), 0.68 (89). The second decimal is noise, confidence is ignored, and many pairs tie. |
| **Expectation (probability-weighted mean of the four bands)** | **Pro:** uses the whole distribution and is smooth, which suits ranking and ordinal regression. **Con:** `round(E[grade])` disagrees with argmax on 81 pairs (10%): 48 argmax 0 become 1, 29 argmax 2 become 1, 4 argmax 3 become 2. It creates a middle grade for split pairs although the model gave that grade almost no weight, and grade 1 is already the thinnest class. | **Pro:** reflects confidence, and the ranking is almost the same as today's score (Spearman 0.9955). **Con:** saturates: with 30% of pairs above 0.99 the value sits exactly on 0, 1/3, 2/3 or 1, so 573 pairs share a value (rounded to 0.001) against 341 with today's hybrid score. The written score is the only thing that separates saturated pairs inside a band, and today's clipping piles values at band edges (0.98: 75, 0.00: 74, 0.16: 72). |

**Leaning, to confirm with the calibration check below:**

- Grade: keep the argmax and store the top-band probability (or entropy) next to it. Use it as a sample weight, or
  drop the lowest-confidence pairs from hard-label training.
- Score: use the expectation as the main value and the written score only as a small tie-breaker inside the band.
  Do not drop the written score entirely; that adds ties.
- Keep trusting the band over the second decimal, as the README says.

### Open item: a grader variant for the other scoring type

The latest grader (`grade_pairs.py`, rubric v5) produces one fixed pairing: an ordinal grade by argmax and a
continuous score by the band-weighted expectation with the model's written number mixed in. The other cells of the
table are not built: an ordinal grade from the expectation, a continuous score from the pure expectation of the
band probabilities, and a continuous score from the written number alone.

- [ ] Build the missing variants as options of `grade_pairs.py` (a `--scoring` flag recorded in the log next to
      `prompt_version`, so runs stay separable), changing only how `grade_probs` is turned into the output.
- [ ] Grade-test them on the client's 30 gold gigs (`gold.json`) and on the GLM pairs once those are graded: ranking
      quality (NDCG, Spearman within gig), pooled Spearman across gigs, tie counts, and agreement with each
      provider's target grade.
- [ ] Choose after seeing the GLM grade distribution; the leaning above is not a decision.

### Pending analysis (not run yet)

- [ ] **Calibration against `labeller/experiments/gold.json`** (the client's 30 gigs, ordinal 0 to 3): reliability
      table of predicted band probability against gold band; per-band accuracy; whether a temperature or Platt
      rescale on the logprobs improves it. The repo currently has no distribution or calibration analysis, and the
      band edges are not fitted to data.
- [ ] **Anchor check on the digit token:** the grade digit is itself a "pick a number" choice. Compare the digit
      distribution on graded pairs with the true band mix in the gold set to see whether one band (0 in `v4.1`,
      789 of 900) is over-chosen.
- [ ] Re-grade the GLM pairs with the chosen rule once the run is committed, and report the target-against-Qwen table
      under both rules.

## 6. Temporary mending script for the existing GLM samples

The 200 gigs and the 1,600 providers took days to generate and should not be thrown away. Once the prompt changes in
section 3 and the dash rules in section 4 are implemented, a throwaway script brings the existing records in line
with them without regenerating from scratch.

- [ ] **`glm/mend_tmp.py` (temporary; delete it once every record has been mended and verified).** Reads
      `gigs_by_id.json` and `providers_by_file.json`, applies the fixes, and writes the mended files next to a
      backup of the originals (`glm_trial/_pre_mend/`). Never edits a file in place without that backup.
- [ ] **Fixes it applies:**
      - em dashes and en dashes: the rule-based replacement from section 4;
      - achievement verbs: for providers whose achievements all sit in one verb class, ask GLM to rewrite only the
        opening verb phrase of the achievements that need it (same facts, same figures, same length band),
        through the same try, validate and retry loop as `make._attempt`;
      - anything else the updated `gig.md` and `provider.md` now require.
- [ ] **Keep the design parameters.** The mended record must still match its row in `design.csv` /
      `providers_design.csv`: sector and track (and so the tags), level and the implied seniority, mode, specificity,
      the weeks in the "Engagement duration:" sentence, the word target (within the 15-word tolerance), the opening
      style, and for providers the years inside the level's band, the route and the target grade, the schema's
      field counts, and `availability` and `rate` null. Fixes touch wording only, never the work, the level, the
      mode of the gig or the figures.
- [ ] **Built-in validator for the fixes.** After each record is mended the script checks, and rolls back that
      record to the original if a check fails:
      - everything `glm/validate.py` already checks (schema, word counts, ordering, no company or person names,
        no shared six-word run with the gig, no stock phrases);
      - no em dash or en dash remains;
      - the design parameters above are unchanged, compared field by field against the original record and its
        design row;
      - the verb mix is no longer a single class, and the changed text is otherwise close to the original (a
        word-level diff under a set threshold), so the fix cannot rewrite the profile;
      - an end report: records checked, mended, rolled back, and the list of rolled-back keys for a manual look.
- [ ] **Review sample.** Print before and after for 20 to 30 mended records and read them (coherence at every cut,
      no fragments).
- [ ] **Re-grade.** Mended providers (and gigs) get graded after the mend, not before. Grades on the old text are
      stale for those records.
- [ ] **Delete `glm/mend_tmp.py`** and the `_pre_mend/` backup once the mended files are committed and the report
      is clean. The generator keeps the updated prompts and validator, so new batches need no mending.
