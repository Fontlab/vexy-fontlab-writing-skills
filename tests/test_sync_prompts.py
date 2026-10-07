# this_file: tests/test_sync_prompts.py
"""The prompt generator copies each skill into its prompt's long variant."""
import importlib.util
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("sync_prompts", ROOT / "tools/scripts/sync_prompts.py")
assert spec and spec.loader
sync = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sync)


class FrontMatterTests(unittest.TestCase):
    def test_front_matter_when_block_scalar_then_keeps_paragraphs(self):
        meta, body = sync.front_matter("---\nskill: x\noperation: |\n  One.\n\n  Two.\n---\n# T\n")
        self.assertEqual(meta["skill"], "x", "Plain keys must be read")
        self.assertEqual(meta["operation"], "One.\n\nTwo.", "A block scalar must keep its blank line")
        self.assertEqual(body, "# T\n", "The body must start after the closing marker")

    def test_front_matter_when_missing_then_raises(self):
        with self.assertRaises(ValueError, msg="A page without front matter cannot name its skill"):
            sync.front_matter("# T\n")


class DemoteTests(unittest.TestCase):
    def test_demote_when_heading_inside_code_then_leaves_it(self):
        text = "# Title\n```python\n# comment\n```\n## Section"
        self.assertEqual(sync.demote(text), "### Title\n```python\n# comment\n```\n#### Section",
                         "Only Markdown headings outside fences may move")


class SkillTextTests(unittest.TestCase):
    def test_skill_text_when_packaged_then_drops_packaging(self):
        text = sync.skill_text("fontlab-neutral")
        self.assertNotIn("this_file", text, "Source-path comments are packaging, not instructions")
        self.assertNotIn("## Related skills", text, "Sibling pointers mean nothing in a pasted prompt")
        self.assertNotIn("fontlab:shared", text, "Sync markers must not leak into a prompt")
        self.assertNotIn("references/", text, "A pasted prompt has no reference files to open")
        self.assertIn("**H17.", text, "The house rules, including the check loop, must be included")
        self.assertIn("## Checklist", text, "The skill's checklist must be included")

    def test_checklist_when_skill_has_none_then_raises(self):
        with self.assertRaises(ValueError, msg="A review prompt cannot cite a missing checklist"):
            sync.checklist("fontlab-localization-de")


class PageTests(unittest.TestCase):
    def test_every_prompt_page_when_synced_then_up_to_date(self):
        for page in sync.pages():
            text = page.read_text(encoding="utf-8")
            self.assertEqual(sync.render(text), text, f"{page.name} is stale; run sync_prompts.py")

    def test_every_prompt_page_when_rendered_then_outer_fence_is_longest(self):
        for page in sync.pages():
            long = page.read_text(encoding="utf-8").split(sync.START, 1)[1].split(sync.END, 1)[0]
            outer = re.match(r"\n(`+)markdown\n", long)
            self.assertIsNotNone(outer, f"{page.name}: the long variant must open with a fence")
            inner = re.findall(r"^(`{3,})", long.strip().split("\n", 1)[1].rsplit("\n", 1)[0], re.M)
            self.assertTrue(all(len(f) < len(outer.group(1)) for f in inner),
                            f"{page.name}: an inner fence would close the outer one")

    def test_every_short_variant_when_read_then_asks_for_the_check_loop(self):
        for page in sync.pages():
            text = page.read_text(encoding="utf-8")
            short = text.split("## Short variant", 1)[1].split("## Long variant", 1)[0]
            self.assertRegex(short, r"(?i)checklist", f"{page.name}: the short variant needs its checklist")
            self.assertRegex(short, r"\n1\. ", f"{page.name}: the checklist must be numbered")

    def test_prompt_folder_when_scanned_then_holds_no_skill(self):
        self.assertFalse(list(sync.PROMPTS.rglob("SKILL.md")), "npx skills add would treat it as a skill")
        for page in sync.PROMPTS.glob("*.md"):
            meta, _ = sync.front_matter(page.read_text(encoding="utf-8"))
            self.assertNotIn("name", meta, f"{page.name}: skill-style front matter")


if __name__ == "__main__":
    unittest.main()
