#!/usr/bin/env python3
# this_file: tools/scripts/export_terms.py
"""Write the portable term table of each per-language localization skill.

Reads the core translation memories of the writing guide
(`localization/<code>-core.tmx` in the vexy-fontlab-writing-styleguide
repository) and writes `fontlab-localization-<code>/references/terms.md`: one
table per category with the English term, the translation, its status and the
translator note. The English definition is included so the skill can work
without the guide installed.

Usage:
    python3 tools/scripts/export_terms.py [--styleguide PATH] [de es fr pl]
"""
import argparse
import sys
import xml.etree.ElementTree as ET
from collections import defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
DEFAULT_STYLEGUIDE = ROOT.parent / "vexy-fontlab-writing-styleguide"
XML_LANG = "{http://www.w3.org/XML/1998/namespace}lang"
TITLES = {"brand": "Names", "type-design": "Type design", "font-engineering": "Font engineering",
          "opentype": "OpenType", "file-format": "File formats", "interface": "Interface",
          "vector": "Vector drawing"}
ORDER = list(TITLES)


def read_core(path):
    root = ET.parse(path).getroot()
    name = ""
    for prop in root.find("header").findall("prop"):
        if prop.get("type") == "x-language-name":
            name = prop.text or ""
    units = []
    for tu in root.iter("tu"):
        props = {p.get("type"): (p.text or "") for p in tu.findall("prop")}
        definition = (tu.findtext("note") or "").strip()
        source = target = note = ""
        for tuv in tu.findall("tuv"):
            seg = tuv.findtext("seg") or ""
            if tuv.get(XML_LANG) == "en":
                source = seg
            else:
                target = seg
                note = (tuv.findtext("note") or "").strip()
        units.append((props, source, target, note, definition))  # x-fallback lives in props
    return name, units


def cell(text):
    return " ".join(text.split()).replace("|", "\\|")


def render(code, name, units):
    by_category = defaultdict(list)
    for unit in units:
        by_category[unit[0].get("x-category", "interface")].append(unit)
    covered = sum(1 for u in units if u[0].get("x-status") in ("approved", "do-not-translate"))
    lines = [f"<!-- this_file: fontlab-localization-{code}/references/terms.md -->", "",
             f"# {name} terms", "",
             f"Portable term table, snapshot of {date.today():%d %B %Y}, generated from the core "
             f"translation memory `localization/{code}-core.tmx` of the FontLab writing guide "
             f"by `tools/scripts/export_terms.py`. {covered} of {len(units)} terms are approved or "
             "protected; a proposed translation is a candidate for a native reviewer, and the "
             "English term is the fallback until it is approved. Use newer supplied project data "
             "when it disagrees with this snapshot.", "",
             "A status of do-not-translate protects the English spelling; it does not approve a "
             "draft English name. The definition says what the term means in FontLab; the note "
             "says why the translation was chosen or how to inflect it. The fallback original "
             "term is a plain English phrase to translate instead of the term when the term "
             "itself will not travel (stem: main stroke; overshoot: optical surplus).", ""]
    for category in ORDER:
        entries = sorted(by_category.get(category, []), key=lambda u: u[1].lower().lstrip("."))
        if not entries:
            continue
        lines += [f"## {TITLES[category]}", "",
                  f"| English | Fallback | {name} | Status | Note | Definition |",
                  "|---|---|---|---|---|---|"]
        for props, source, target, note, definition in entries:
            lines.append(f"| {cell(source)} | {cell(props.get('x-fallback', ''))} | {cell(target)} "
                         f"| {props.get('x-status', '')} | {cell(note)} | {cell(definition)} |")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--styleguide", type=Path, default=DEFAULT_STYLEGUIDE)
    parser.add_argument("codes", nargs="*", default=["de", "es", "fr", "pl"])
    args = parser.parse_args()
    tm = args.styleguide / "localization"
    status = 0
    for code in args.codes:
        source = tm / f"{code}-core.tmx"
        if not source.exists():
            print(f"FAIL     {source} not found", file=sys.stderr)
            status = 1
            continue
        name, units = read_core(source)
        out = ROOT / f"fontlab-localization-{code}" / "references" / "terms.md"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(render(code, name, units), encoding="utf-8")
        print(f"ok       {out.relative_to(ROOT)}: {len(units)} terms")
    return status


if __name__ == "__main__":
    sys.exit(main())
