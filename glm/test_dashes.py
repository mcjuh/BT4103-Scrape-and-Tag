# -*- coding: utf-8 -*-
"""Offline tests for dashes.py and the dash / verb-mix checks in validate.py: python -m unittest glm/test_dashes.py"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import dashes  # noqa: E402
import validate  # noqa: E402

EM, EN = "—", "–"


class Strip(unittest.TestCase):
    def test_ranges_and_compounds_get_a_hyphen(self):
        self.assertEqual(dashes.strip_dashes(f"Budget S$5,000{EN}S$7,000 for 1{EN}2 weeks."), "Budget S$5,000-S$7,000 for 1-2 weeks.")
        self.assertEqual(dashes.strip_dashes(f"English{EN}Chinese translator"), "English-Chinese translator")

    def test_list_after_the_dash_becomes_a_colon(self):
        self.assertEqual(dashes.strip_dashes(f"For Singapore SMEs {EM} clinics, schools and offices."),
                         "For Singapore SMEs: clinics, schools and offices.")

    def test_plain_break_becomes_a_comma(self):
        self.assertEqual(dashes.strip_dashes(f"I stay hands-on {EM} drafting plans myself."), "I stay hands-on, drafting plans myself.")

    def test_joining_word_gets_a_comma(self):
        self.assertEqual(dashes.strip_dashes(f"Insurers {EM} whose board needs more."), "Insurers, whose board needs more.")

    def test_new_clause_gets_a_full_stop_and_capital(self):
        self.assertEqual(dashes.strip_dashes(f"Operators {EM} we need a review."), "Operators. We need a review.")

    def test_aside_with_a_list_gets_brackets_and_without_commas(self):
        self.assertEqual(dashes.strip_dashes(f"our setup {EM} Xero, a CCTV system {EM} and the rest."), "our setup (Xero, a CCTV system) and the rest.")
        self.assertEqual(dashes.strip_dashes(f"watching trading {EM} peak and quiet {EM} then talk."), "watching trading, peak and quiet, then talk.")

    def test_deliverable_stays_one_sentence_with_one_colon(self):
        out = dashes.strip_dashes(f"Deliverable: a report {EM} we need it signed, dated and filed.")
        self.assertEqual(out, "Deliverable: a report, we need it signed, dated and filed.")

    def test_clean_text_is_untouched_and_idempotent(self):
        t = "A plain sentence, with a well-known hyphen."
        self.assertIs(dashes.strip_dashes(t), t)
        once = dashes.strip_dashes(f"A {EM} b, c.")
        self.assertEqual(dashes.strip_dashes(once), once)

    def test_record_walk_skips_identifiers(self):
        rec = {"source_file": f"x{EN}y.md", "short_description": f"a {EM} b, c", "achievements": [f"1{EN}2 days"]}
        out = dashes.apply_to_record(rec)
        self.assertEqual(out["source_file"], f"x{EN}y.md")
        self.assertFalse(dashes.has_dash(out["short_description"]) or dashes.has_dash(out["achievements"]))


class VerbMix(unittest.TestCase):
    def test_single_class(self):
        self.assertEqual(validate.single_verb_class(["Advised a", "Reviewed b"]), "advisory")
        self.assertEqual(validate.single_verb_class(["Built a", "Wrote b"]), "production")

    def test_any_other_or_second_class_breaks_it(self):
        self.assertEqual(validate.single_verb_class(["Advised a", "Cut b"]), "")
        self.assertEqual(validate.single_verb_class(["Advised a", "Built b"]), "")
        self.assertEqual(validate.single_verb_class(["Cut a", "Reduced b"]), "")


if __name__ == "__main__":
    unittest.main()
