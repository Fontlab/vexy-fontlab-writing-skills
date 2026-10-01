# this_file: tests/test_new_language_skills.py
"""The skill generator turns a localization guide into a self-contained draft skill."""
import contextlib
import importlib.util
import io
from pathlib import Path
import re
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("new_language_skills", ROOT / "tools/scripts/new_language_skills.py")
skills = importlib.util.module_from_spec(spec)
spec.loader.exec_module(skills)

GUIDE = """---
this_file: src_docs/md/localization/it.md
---

# Italian localization guide

Use these rules with the [localization principles](principles.md),
[Qt interface rules](ui-strings.md) and [Italian language guide](../languages/it.md).
Examples tagged FB are quoted from Font Book.

## Locale and register

Address the reader as *tu*. See [plural rules](ui-strings.md#plurals), the
[term table](it-terms.md) and [Qt's documentation](https://doc.qt.io/).

## Review

1. Terms match the term table.

## Current terminology

The [Italian term table](it-terms.md) is the terminology authority.

| English | Italian |
|---|---|
| glyph | glifo |
"""


def run(folder, *codes):
    """Run the generator against a temporary repository; return its status and stderr."""
    errors = io.StringIO()
    with patch.object(skills, "ROOT", Path(folder)), \
            patch("sys.argv", ["new_language_skills", "--styleguide", folder, *codes]), \
            contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(errors):
        return skills.main(), errors.getvalue()


def write_guide(folder, code):
    guide = Path(folder) / f"src_docs/md/localization/{code}.md"
    guide.parent.mkdir(parents=True, exist_ok=True)
    guide.write_text(GUIDE, encoding="utf-8")


class NewLanguageSkillsTests(unittest.TestCase):
    def test_main_when_guide_has_terminology_section_then_skill_drops_it(self):
        with tempfile.TemporaryDirectory() as folder:
            write_guide(folder, "it")
            status, errors = run(folder, "it")
            self.assertEqual(status, 0, f"A known language with a guide must be written: {errors}")
            output = (Path(folder) / "fontlab-localization-it/SKILL.md").read_text(encoding="utf-8")
        self.assertIn("name: fontlab-localization-it\n", output, "Front matter must name the skill")
        self.assertIn("# FontLab localization: Italian\n", output, "The H1 must name the language")
        self.assertIn("## Locale and register", output, "Guide sections must be carried over")
        self.assertIn("Examples tagged FB", output, "The guide's legend of example tags must be kept")
        self.assertNotIn("## Current terminology", output, "The terminology section must be dropped")
        self.assertNotIn("| glyph | glifo |", output, "The key-term table belongs in references/terms.md")
        self.assertIn("no native reviewer has approved", output, "The draft status must be stated")

    def test_main_when_guide_has_relative_links_then_none_survives(self):
        with tempfile.TemporaryDirectory() as folder:
            write_guide(folder, "it")
            run(folder, "it")
            output = (Path(folder) / "fontlab-localization-it/SKILL.md").read_text(encoding="utf-8")
        relative = re.findall(r"\]\((?!https?://)[^)]*\)", output)
        self.assertEqual(relative, [], "A relative link points outside the skill directory")
        self.assertIn("localization principles (in `fontlab-localization`)", output,
                      "A shared page must be named as the fontlab-localization skill")
        self.assertIn("plural rules (in `fontlab-localization`)", output,
                      "A link with a fragment must be rewritten too")
        self.assertIn("term table (`references/terms.md`)", output,
                      "The term page must become the skill's own term table")
        self.assertIn("Italian language guide (in the FontLab writing guide)", output,
                      "A page outside the localization chapter must be named as the writing guide")
        self.assertIn("[Qt's documentation](https://doc.qt.io/)", output, "An external link must be kept")

    def test_main_when_code_is_a_reviewed_skill_then_refuses_it(self):
        for code in ("de", "es", "fr", "pl"):
            with tempfile.TemporaryDirectory() as folder:
                write_guide(folder, code)
                status, errors = run(folder, code)
                written = (Path(folder) / f"fontlab-localization-{code}/SKILL.md").exists()
            self.assertEqual(status, 1, f"{code} is hand-written and must be refused")
            self.assertIn("hand-written", errors, f"The refusal of {code} must say why")
            self.assertFalse(written, f"No SKILL.md may be written for {code}")

    def test_main_when_code_is_unknown_or_guide_is_missing_then_fails(self):
        with tempfile.TemporaryDirectory() as folder:
            self.assertEqual(run(folder, "xx")[0], 1, "A code without language data must fail")
            self.assertEqual(run(folder, "it")[0], 1, "A missing guide must fail")
            self.assertFalse((Path(folder) / "fontlab-localization-it").exists(),
                             "A failed language must leave no directory behind")

    def test_main_when_run_twice_then_keeps_the_synced_house_rules(self):
        with tempfile.TemporaryDirectory() as folder:
            write_guide(folder, "it")
            run(folder, "it")
            path = Path(folder) / "fontlab-localization-it/SKILL.md"
            first = path.read_text(encoding="utf-8")
            self.assertIn(f"{skills.START}\n{skills.END}\n", first, "A new skill must carry empty sync markers")
            synced = first.replace(f"{skills.START}\n", f"{skills.START}\n## House rules\n")
            path.write_text(synced, encoding="utf-8")
            run(folder, "it")
            self.assertEqual(path.read_text(encoding="utf-8"), synced, "A rerun must not change a synced skill")

    def test_guide_parts_when_guide_has_no_section_then_raises(self):
        with self.assertRaises(ValueError, msg="A guide without a section has no body to carry"):
            skills.guide_parts("# Title\n\nOnly an introduction.\n")

    def test_front_matter_when_rendered_then_description_fits_the_skill_limit(self):
        for code, (name, phrases) in skills.LANGUAGES.items():
            block = skills.front_matter(code, name, phrases)
            description = " ".join(line.strip() for line in block.splitlines()[3:-6])
            self.assertLessEqual(len(description), 1024, f"{code}: description exceeds the 1024-character limit")
            for phrase in phrases:
                self.assertIn(f'"{phrase}"', description, f"{code}: a trigger phrase was broken across lines")
