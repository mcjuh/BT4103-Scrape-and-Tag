# Gold-label spot check

This sheet checks the earlier 18-gig label set that the saved grid in `../results/` was scored against.
That set was labelled by Claude, not a person, and is no longer in the repo: the current `../gold.json` is
the client's 30-gig set, so `spotcheck_key.csv` no longer joins to it. The sheet itself is unfilled (0 of
60 graded). A teammate grades
`spotcheck_sheet.csv` blind (60 pairs: every grade-3 pair plus random grade-2/1/0 pairs),
using the rubric at the end of this file, **without opening `spotcheck_key.csv`**. Then compare
`your_grade_0to3` with `gold_grade` in the key (e.g. quadratic-weighted Cohen's kappa, and how
often grade >=2 vs <=1 agrees). Rubric: 3 shortlist (core skill AND domain), 2 relevant
(core skill, other domain), 1 marginal (adjacent), 0 not relevant.
