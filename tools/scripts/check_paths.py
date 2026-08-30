#!/usr/bin/env python3
"""Fail if anything a fontlab-* skill references does not exist.

Two kinds of reference are checked:

  paths     markdown links, and backticked tokens containing a slash
  pointers  skill names listed under "Related VFWS skills"

The second kind is the point. A skill that points at a renamed or missing
sibling fails silently, which is how a style guide quietly stops being one.

Usage:
    python3 check_paths.py [skill-dir ...]
"""
import re
import sys
from pathlib import Path

SKILLS = ["fontlab-neutral", "fontlab-technical", "fontlab-marketing",
          "fontlab-terminology", "fontlab-localization", "fontlab-partners"]
LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
BACKTICK = re.compile(r"`([^`\n]+)`")
POINTER_SECTION = re.compile(
    r"^## Related skills\s*$(.*?)(?=^## |\Z)", re.M | re.S
)
SKIP_PREFIXES = ("http://", "https://", "#", "mailto:")
DOC_GLOBS = ("*.md", "*.py", "*.sh")


def path_refs(text):
    for match in LINK.finditer(text):
        ref = match.group(1).split("#")[0].strip()
        if ref and not ref.startswith(SKIP_PREFIXES):
            yield ref
    for match in BACKTICK.finditer(text):
        token = match.group(1).strip()
        # Only a token with a slash is a path. A bare filename in a table cell is prose.
        if "<" in token:
            continue  # a placeholder such as localization/<lang>.yaml
        if " " in token or "/" not in token:
            continue
        if not token.startswith(("references/", "tools/", "./")) and not (
                token.startswith("fontlab-") and "/" in token):
            continue
        if not token.startswith(SKIP_PREFIXES):
            yield token.rstrip(".,;:)")


def pointer_refs(text):
    for section in POINTER_SECTION.finditer(text):
        for match in BACKTICK.finditer(section.group(1)):
            token = match.group(1).strip()
            if "/" not in token and " " not in token and not token.endswith(")"):
                yield token


def check(skill_dir, root):
    """`root` is the skills directory; `root.parent` is the repository, which is
    where the glossary and localization data a skill reads actually lives."""
    problems = []
    docs = [d for glob in DOC_GLOBS for d in sorted(skill_dir.rglob(glob))]
    for doc in docs:
        text = doc.read_text(encoding="utf-8")
        rel = doc.relative_to(root)
        for ref in path_refs(text):
            bases = (doc.parent, skill_dir, root, root.parent)
            if any((base / ref).exists() for base in bases):
                continue
            if "*" in ref and any(list(base.glob(ref)) for base in bases):
                continue
            problems.append(f"{rel} -> path {ref}")
        for name in pointer_refs(text):
            if (root / name / "SKILL.md").exists():
                continue
            problems.append(f"{rel} -> skill {name}")
    return problems


def main():
    root = Path(__file__).resolve().parent.parent.parent   # the repository root
    names = sys.argv[1:] or SKILLS
    problems = []
    for name in names:
        skill_dir = root / name
        if not skill_dir.exists():
            problems.append(f"missing skill directory: {name}")
            continue
        found = check(skill_dir, root)
        print(f"{'FAIL' if found else 'ok  '}     {name}")
        problems.extend(found)
    for line in problems:
        print(f"  unresolved: {line}", file=sys.stderr)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
