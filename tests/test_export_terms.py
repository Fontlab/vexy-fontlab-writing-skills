# this_file: tests/test_export_terms.py
"""The skill exporter consumes the canonical localization directory."""
import importlib.util
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("export_terms", ROOT / "tools/scripts/export_terms.py")
export = importlib.util.module_from_spec(spec)
spec.loader.exec_module(export)

class ExportTermsTests(unittest.TestCase):
    def test_export_when_core_is_in_localization_then_writes_portable_table(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            memory = root / "localization/de-core.tmx"
            memory.parent.mkdir()
            memory.write_text('<tmx><header><prop type="x-language-name">German</prop></header><body><tu><prop type="x-category">interface</prop><prop type="x-status">approved</prop><tuv xml:lang="en"><seg>panel</seg></tuv><tuv xml:lang="de"><seg>Panel</seg></tuv></tu></body></tmx>')
            with patch.object(export, "ROOT", root), patch("sys.argv", ["export_terms", "--styleguide", folder, "de"]):
                self.assertEqual(export.main(), 0, "Canonical core directory must be supported")
            output = (root / "fontlab-localization-de/references/terms.md").read_text()
            self.assertIn("| panel |", output)
            self.assertIn("localization/de-core.tmx", output)
            self.assertNotIn("localization/tm/", output)
