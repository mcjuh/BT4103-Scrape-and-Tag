# -*- coding: utf-8 -*-
"""Offline tests for grade_pairs.py (no API calls): python -m unittest labeller/test_grade_pairs.py"""

import math
import sys
import unittest
from pathlib import Path
from types import SimpleNamespace as NS

sys.path.insert(0, str(Path(__file__).resolve().parent))
import grade_pairs as gp  # noqa: E402


def ranker_grade(score: float) -> int:
    """judge_pools.grade_of: the rule the ranker's grade_from_score() applies to round(score * 100)."""
    return int(round(round(score * 100) * 3 / 100))


def first_token(**probs):
    """An answer-position token whose top-k holds the given grade probabilities, e.g. g2=0.7."""
    cands = [NS(token=k[1:], logprob=math.log(p)) for k, p in probs.items()]
    return [NS(token=max(probs, key=probs.get)[1:], top_logprobs=cands)]


class Bands(unittest.TestCase):
    def test_every_score_in_a_band_maps_back_to_its_grade(self):
        for grade, (lo, hi) in gp.BANDS.items():
            for pct in range(round(lo * 100), round(hi * 100) + 1):
                self.assertEqual(ranker_grade(pct / 100), grade, f"{pct / 100} should be grade {grade}")

    def test_bands_are_contiguous(self):
        edges = [gp.BANDS[g] for g in range(4)]
        for (_, hi), (lo, _) in zip(edges, edges[1:]):
            self.assertAlmostEqual(lo - hi, 0.01)

    def test_prompt_grades_the_terms(self):
        text = gp.PROMPT_PATH.read_text(encoding="utf-8")
        for term in ("Seniority (the main term).", "Mode of work.", "Availability.", "Budget (counts least)."):
            self.assertIn(term, text)

    def test_budget_never_lowers_the_grade(self):
        text = gp.PROMPT_PATH.read_text(encoding="utf-8")
        self.assertIn("budget never lowers the grade", text)
        self.assertLess(text.index("Seniority (the main term)"), text.index("Budget (counts least)"))

    def test_default_model_is_the_rankers_grader(self):
        self.assertEqual(gp.DEFAULT_MODEL, "qwen3.8:27b")
        self.assertIn(gp.DEFAULT_MODEL, gp.MODEL_POOL)

    def test_prompt_states_the_same_ranges(self):
        text = gp.PROMPT_PATH.read_text(encoding="utf-8")
        for grade, (lo, hi) in gp.BANDS.items():
            self.assertIn(f"score {lo:.2f}-{hi:.2f}", text, f"grade {grade} range missing from prompt")


class Parsing(unittest.TestCase):
    def test_accepts_grade_then_score(self):
        r = gp.score_reply("2 0.62", [])
        self.assertEqual((r["grade"], r["score"], r["scoring"]), (2, 0.62, "parsed"))

    def test_rejects_the_old_bare_score_format(self):
        for bad in ("0.62", "", "The match is good", ".62"):
            with self.assertRaises(ValueError, msg=bad):
                gp.score_reply(bad, [])

    def test_out_of_band_score_is_clipped_and_flagged(self):
        r = gp.score_reply("3 0.40", [])
        self.assertEqual((r["grade"], r["score"], r["flags"]), (3, 0.84, ["score_out_of_band"]))

    def test_missing_score_uses_midpoint_and_is_flagged(self):
        r = gp.score_reply("1", [])
        self.assertEqual((r["grade"], r["score"], r["flags"]), (1, gp.MIDPOINT[1], ["score_missing"]))

    def test_score_of_one_is_capped_at_the_top_band(self):
        self.assertEqual(gp.score_reply("3 1.00", [])["score"], 0.99)

    def test_tolerates_quotes_and_separators(self):
        self.assertEqual(gp.score_reply('"1, 0.30"', [])["grade"], 1)


class LogprobScoring(unittest.TestCase):
    def test_confident_answer_keeps_the_stated_score(self):
        r = gp.score_reply("2 0.62", first_token(g2=0.999, g1=0.001))
        self.assertEqual(r["grade"], 2)
        self.assertAlmostEqual(r["score"], 0.62, places=2)
        self.assertEqual(r["scoring"], "logprobs")

    def test_grade_is_the_most_probable_band_not_a_rounded_average(self):
        # 55% on grade 3, 45% on grade 2: the average lands near 0.8 (grade 2 by rounding),
        # but the model's likeliest band is 3, and the score is clipped into that band.
        r = gp.score_reply("3 0.90", first_token(g3=0.55, g2=0.45))
        self.assertEqual(r["grade"], 3)
        self.assertEqual(ranker_grade(r["score"]), 3)
        self.assertLess(r["score_raw"], 0.84)

    def test_tie_goes_to_the_lower_grade(self):
        r = gp.score_reply("3 0.90", first_token(g3=0.5, g2=0.5))
        self.assertEqual(r["grade"], 2)

    def test_uncertainty_lowers_the_score_within_a_band(self):
        sure = gp.score_reply("2 0.70", first_token(g2=0.99, g1=0.01))["score"]
        unsure = gp.score_reply("2 0.70", first_token(g2=0.6, g1=0.4))["score"]
        self.assertLess(unsure, sure)

    def test_grade_and_score_always_agree(self):
        for said in range(4):
            for mix in ({0: .1, 1: .2, 2: .3, 3: .4}, {0: .7, 1: .1, 2: .1, 3: .1}, {0: .25, 1: .25, 2: .25, 3: .25}):
                tok = first_token(**{f"g{g}": p for g, p in mix.items()})
                r = gp.score_reply(f"{said} {gp.MIDPOINT[said]:.2f}", tok)
                self.assertEqual(ranker_grade(r["score"]), r["grade"], (said, mix, r))

    def test_surface_variants_of_a_grade_digit_are_summed(self):
        tok = [NS(token="2", top_logprobs=[NS(token="2", logprob=math.log(0.3)), NS(token=" 2", logprob=math.log(0.3)),
                                           NS(token="1", logprob=math.log(0.4))])]
        self.assertAlmostEqual(gp.grade_probs(tok)[2], 0.6)

    def test_no_grade_digit_in_top_k_falls_back_to_parsed(self):
        tok = [NS(token="x", top_logprobs=[NS(token="x", logprob=-0.1)])]
        self.assertEqual(gp.score_reply("1 0.30", tok)["scoring"], "parsed")


class SampleFormat(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.gigs = gp.load_rows(gp.GIGS_CSV, "gig_id")
        cls.providers = gp.load_rows(gp.PROVIDERS_CSV, "provider_id")
        cls.template = gp.PROMPT_PATH.read_text(encoding="utf-8").strip()

    def test_sample_loads(self):
        self.assertEqual((len(self.gigs), len(self.providers)), (30, 30))

    def test_every_prompt_has_gig_and_provider_text(self):
        for g, gig in self.gigs.items():
            self.assertIn("Scope: ", gp.describe(gig, gp.GIG_FIELDS), g)
        for p, prov in self.providers.items():
            self.assertIn("About: ", gp.describe(prov, gp.PROVIDER_FIELDS), p)

    def test_duration_moves_out_of_the_scope_onto_its_own_line(self):
        for g, gig in self.gigs.items():
            shown = gp.describe(gig, gp.GIG_FIELDS)
            self.assertNotIn("Engagement duration", shown, g)
            self.assertTrue(shown.rstrip().endswith((".", ")", "?")), f"{g} ends oddly: {shown[-60:]!r}")
            self.assertRegex(gp.gig_duration(gig), r"^\d+(-\d+)? weeks$", g)
            self.assertIn(f"Estimated duration: {gp.gig_duration(gig)}", gp.render(self.template, gig, self.providers["P001"]))

    def test_provider_availability_and_rate_are_shown_and_identity_is_not(self):
        p4 = self.providers["P004"]
        shown = gp.render(self.template, self.gigs["G001"], p4)
        self.assertIn(f"Availability: {p4['availability']}", shown)
        self.assertIn(f"Rate: {p4['rate']}", shown)
        for secret in (p4["name"], p4["category"], p4["search_tags"]):
            self.assertNotIn(secret, shown)

    def test_terms_follow_the_content_fields(self):
        shown = gp.describe(self.providers["P004"], gp.PROVIDER_FIELDS + gp.TERMS_FIELDS)
        self.assertLess(shown.index("How they work"), shown.index("Availability:"))
        self.assertTrue(shown.rstrip().split("\n")[-1].startswith("Rate:"))

    def test_every_provider_states_availability_and_a_rate(self):
        for pid, prov in self.providers.items():
            self.assertTrue(prov["availability"].strip() and prov["rate"].strip(), pid)

    def test_with_tags_adds_category_and_specialisation_only(self):
        p4 = self.providers["P004"]
        shown = gp.render(self.template, self.gigs["G001"], p4, with_tags=True)
        self.assertIn("Category: Sea Transport", shown)
        self.assertNotIn(p4["search_tags"], shown)

    def test_multiline_fields_keep_their_lines(self):
        shown = gp.describe(self.providers["P004"], gp.PROVIDER_FIELDS)
        self.assertIn("Technical proficiency:\nRegulations: SOLAS, MARPOL, MLC 2006\nAudits: ISM, ISPS, DOC", shown)

    def test_prompt_renders_with_no_leftover_placeholders(self):
        shown = gp.render(self.template, self.gigs["G002"], self.providers["P001"])
        self.assertNotIn("{query}", shown)
        self.assertNotIn("{document}", shown)

    def test_default_pairs_are_every_gig_by_every_provider(self):
        pairs = gp.build_pairs(self.gigs, self.providers)
        self.assertEqual(sum(len(v) for v in pairs.values()), 900)

    def test_parse_gigs(self):
        ids = list(self.gigs)
        self.assertEqual(gp.parse_gigs("1-3,7", ids), ["G001", "G002", "G003", "G007"])


V2_GIG = {"source_file": "crafted-gig__x.md", "hirer_ref": "H-0000abcd", "gig_title": "Review a Lease",
          "short_description": "We need our lease reviewed. Deliverable: memo. Engagement duration: 2-3 weeks.",
          "additional_notes": "Budget about S$4,000.", "duration_weeks_min": 2, "duration_weeks_max": 3}
V2_PROVIDER = {"source_file": "p.md", "title": "Tax Adviser", "years_experience": 18, "credentials": ["CA (Singapore)", "ACCA"],
               "about_headline": "h", "about_bio": "b",
               "services": [{"service_title": "Tax Advisory", "service_detail": "Corporate tax for SMEs."}],
               "achievements": ["Won a penalty waiver.", "Cut a tax bill."],
               "technical_proficiency": [{"category": "Tax", "skills": ["GST", "CIT"]}], "how_i_work": "I start with the filings."}


class V2Mapping(unittest.TestCase):
    def test_gig_adapter_renames_and_keeps_the_new_fields(self):
        row = gp.adapt_v2_gig(V2_GIG)
        self.assertEqual((row["gig_id"], row["hirer_id"]), ("crafted-gig__x.md", "H-0000abcd"))
        shown = gp.describe(row, gp.GIG_FIELDS)
        self.assertIn("Notes from the hirer: Budget about S$4,000.", shown)
        self.assertNotIn("Engagement duration", shown)

    def test_duration_comes_from_the_parsed_weeks_for_v2(self):
        self.assertEqual(gp.gig_duration(gp.adapt_v2_gig(V2_GIG)), "2-3 weeks")
        self.assertEqual(gp.gig_duration({"duration_weeks_min": 4, "duration_weeks_max": 4}), "4 weeks")
        self.assertEqual(gp.gig_duration({"short_gig_description": "x Engagement duration: 5-6 weeks."}), "5-6 weeks")

    def test_provider_adapter_shows_years_and_flattens_the_lists(self):
        shown = gp.describe(gp.adapt_v2_provider(V2_PROVIDER), gp.PROVIDER_FIELDS)
        self.assertIn("Years of experience: 18", shown)
        self.assertIn("Tax Advisory: Corporate tax for SMEs.", shown)
        self.assertIn("Tax: GST, CIT", shown)
        self.assertIn("Credentials: CA (Singapore); ACCA", shown)
        self.assertIn("- Won a penalty waiver.", shown)

    def test_sample_rows_without_the_new_fields_render_as_before(self):
        shown = gp.describe({"title": "T", "about_bio": "B"}, gp.PROVIDER_FIELDS)
        self.assertNotIn("Years of experience", shown)

    def test_parse_gigs_counts_by_position_for_file_name_ids(self):
        self.assertEqual(gp.parse_gigs("2-3", ["a.md", "b.md", "c.md", "d.md"]), ["b.md", "c.md"])


class EndToEnd(unittest.TestCase):
    def test_grade_pair_with_a_stubbed_model(self):
        reply = NS(choices=[NS(message=NS(content="3 0.91"),
                               logprobs=NS(content=first_token(g3=0.9, g2=0.1)))],
                   usage=NS(prompt_tokens=500, completion_tokens=6))
        original, gp.complete = gp.complete, lambda prompt, model: reply
        try:
            r = gp.grade_pair("prompt", "qwen3.6:35b")
        finally:
            gp.complete = original
        self.assertEqual((r["grade"], r["generated"], r["usage"]["completion_tokens"]), (3, "3 0.91", 6))


if __name__ == "__main__":
    unittest.main()
