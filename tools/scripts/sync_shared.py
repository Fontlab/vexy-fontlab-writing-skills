#!/usr/bin/env python3
"""Copy house-rules.md into every fontlab-* SKILL.md between sync markers.

Usage:
    python3 sync_shared.py           # write the block into every target
    python3 sync_shared.py --check   # exit 1 if any target is out of date
"""
import re
import sys
from pathlib import Path

START = "<!-- fontlab:shared:start -->"
END = "<!-- fontlab:shared:end -->"
def targets(root):
    """Every fontlab-* skill in the repository, so a new one is never silently unsynced."""
    return sorted(
        path for path in root.glob("fontlab-*/SKILL.md") if True
    )


def splice(text, block):
    if START not in text or END not in text:
        raise ValueError("missing sync markers")
    head, rest = text.split(START, 1)
    _, tail = rest.split(END, 1)
    return f"{head}{START}\n{block}\n{END}{tail}"


def main():
    check = "--check" in sys.argv
    here = Path(__file__).resolve().parent
    block = (here.parent / "house-rules.md").read_text(encoding="utf-8").strip()
    rules = len(re.findall(r"^\*\*H\d+\.", block, re.M))
    stated = re.search(r"These (twelve|thirteen|fourteen|fifteen|\d+) rules", block)
    if stated:
        print(f"FAIL     house-rules.md states a rule count in prose; it will go stale ({rules} rules found)", file=sys.stderr)
        return 1
    print(f"block: {rules} rules")
    root = here.parent.parent   # the repository root
    failures = []
    found = targets(root)
    if not found:
        failures.append("no fontlab-*/SKILL.md targets found")
    for path in found:
        current = path.read_text(encoding="utf-8")
        try:
            updated = splice(current, block)
        except ValueError:
            failures.append(f"no sync markers: {path}")
            continue
        if updated == current:
            print(f"ok       {path.parent.name}")
        elif check:
            failures.append(f"out of date: {path}")
        else:
            path.write_text(updated, encoding="utf-8")
            print(f"synced   {path.parent.name}")
    for line in failures:
        print(f"FAIL     {line}", file=sys.stderr)
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
