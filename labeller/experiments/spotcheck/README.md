# Gold-label spot check

`gold.json` was labelled by Claude, not a person. To check it, a teammate grades
`spotcheck_sheet.csv` blind (60 pairs: every grade-3 pair plus random grade-2/1/0 pairs),
using the rubric in `../gold.json`, **without opening `spotcheck_key.csv`**. Then compare
`your_grade_0to3` with `gold_grade` in the key (e.g. quadratic-weighted Cohen's kappa, and how
often grade >=2 vs <=1 agrees). Rubric: 3 shortlist (core skill AND domain), 2 relevant
(core skill, other domain), 1 marginal (adjacent), 0 not relevant.
