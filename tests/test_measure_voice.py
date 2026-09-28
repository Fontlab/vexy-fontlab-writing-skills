# this_file: tests/test_measure_voice.py
"""Check the measurement CLI's review-only output contract."""

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "tools/scripts/measure_voice.py"


class MeasureVoiceTests(unittest.TestCase):
    def run_report(self, text: str) -> str:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "draft.md"
            path.write_text(text, encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(SCRIPT), str(path)],
                capture_output=True, text=True, check=False,
            )
        self.assertEqual(result.returncode, 0, result.stderr)
        return result.stdout

    def test_short_copy_keeps_counts_without_band_judgments(self):
        output = self.run_report("Save the file.")
        self.assertIn("comparison bands omitted", output)
        self.assertNotIn("outside", output)
        self.assertNotIn("last paragraph", output)

    def test_accurate_word_match_is_a_review_candidate_not_a_ban(self):
        output = self.run_report("Unlock the layer before editing its paths.")
        self.assertIn("REVIEW", output)
        self.assertNotIn("FORBIDDEN", output)
        self.assertNotIn("banned", output)
        self.assertIn("not errors or authorship evidence", output)

    def test_long_copy_describes_comparison_without_requiring_a_target(self):
        output = self.run_report("The report lists the selected files. " * 10)
        self.assertIn("comparison range", output)
        self.assertIn("review signal(s)", output)
        self.assertNotIn("last paragraph", output)

    def test_empty_file_reports_no_prose_without_false_warning(self):
        output = self.run_report("")
        self.assertIn("No prose to measure", output)
        self.assertIn("0 review signal(s)", output)


if __name__ == "__main__":
    unittest.main()
