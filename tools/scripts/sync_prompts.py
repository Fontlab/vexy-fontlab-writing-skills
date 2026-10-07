#!/usr/bin/env python3
# this_file: tools/scripts/sync_prompts.py
"""Write the long variant of every copyable prompt in prompts/ from its skill.

A prompt page is hand-written down to its long variant: the introduction, the
short variant and the front matter. The long variant is the skill itself,
assembled for pasting into a chat that cannot install skills: the requested
operation from the front matter, the skill's instructions, the shared house
rules and the skill's worked cases. It is generated between markers so it
cannot drift from the skill it copies.

Front matter keys:

  this_file    path of the page, as in every source file
  skill        the skill whose text forms the long variant
  operation    optional block (`operation: |`) placed first in the long variant
  checklists   instead of `skill`: space-separated skills whose checklists,
               with the house rules, form the long variant of a review prompt

Usage:
    python3 sync_prompts.py           # rewrite every long variant
    python3 sync_prompts.py --check   # exit 1 if any long variant is out of date
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PROMPTS = ROOT / "prompts"
START = "<!-- fontlab:long:start -->"
END = "<!-- fontlab:long:end -->"
SHARED_START = "<!-- fontlab:shared:start -->"
SHARED_END = "<!-- fontlab:shared:end -->"
REF_LINK = re.compile(r"\[([^\]]+)\]\((?:references/[^)]+|#[^)]+)\)")
REF_CODE = re.compile(r"`references/[a-z-]+\.md`")
FENCE = re.compile(r"^(`{3,}|~{3,})")


def front_matter(text: str) -> tuple[dict[str, str], str]:
    """Return the front matter as a dict of strings, and the remaining text.

    Only `key: value` lines and `key: |` block scalars occur in prompt pages,
    so a small parser keeps this script free of third-party imports.
    """
    if not text.startswith("---\n"):
        raise ValueError("no front matter")
    head, body = text[4:].split("\n---\n", 1)
    meta: dict[str, str] = {}
    key = None
    for line in head.splitlines():
        if key and (line.startswith("  ") or not line.strip()):
            meta[key] += line[2:] + "\n"
            continue
        key = None
        name, _, value = line.partition(":")
        value = value.strip()
        if value == "|":
            key = name.strip()
            meta[key] = ""
        else:
            meta[name.strip()] = value
    return {k: v.strip() for k, v in meta.items()}, body


def demote(text: str, levels: int = 2) -> str:
    """Push every Markdown heading down `levels` levels, leaving code untouched."""
    out, fence = [], None
    for line in text.splitlines():
        match = FENCE.match(line)
        if match:
            marker = match.group(1)
            if fence is None:
                fence = marker
            elif marker.startswith(fence[0]) and len(marker) >= len(fence):
                fence = None
        elif fence is None and re.match(r"#{1,4} ", line):
            line = "#" * levels + line
        out.append(line)
    return "\n".join(out)


def drop_section(text: str, heading: str) -> str:
    """Remove a level-2 section up to the next level-2 heading or shared block."""
    pattern = re.compile(rf"^## {re.escape(heading)}\s*$.*?(?=^## |^{re.escape(SHARED_START)}|\Z)",
                         re.M | re.S)
    return pattern.sub("", text)


def unlink(text: str) -> str:
    """Turn links into the skill's own files into plain words."""
    text = REF_LINK.sub(r"\1", text)
    return REF_CODE.sub("the worked cases", text)


def skill_text(name: str) -> str:
    """Return a skill's instructions and house rules, without packaging."""
    path = ROOT / name / "SKILL.md"
    _, body = front_matter(path.read_text(encoding="utf-8"))
    body = re.sub(r"^<!--.*?-->\n", "", body, flags=re.M)
    body = drop_section(body, "Related skills")
    body = body.replace(SHARED_START + "\n", "").replace(SHARED_END, "")
    return unlink(body).strip()


def worked_cases(name: str) -> str:
    path = ROOT / name / "references" / "moves.md"
    if not path.exists():
        return ""
    text = path.read_text(encoding="utf-8")
    if text.startswith("---\n"):
        _, text = front_matter(text)
    text = re.sub(r"^<!--.*?-->\n", "", text, flags=re.M)
    return unlink(text).strip()


def checklist(name: str) -> str:
    """Return one skill's checklist section, titled with the skill's H1."""
    text = skill_text(name)
    heading = re.search(r"^# (.+)$", text, re.M)
    if not heading:
        raise ValueError(f"{name} has no title")
    title = heading.group(1)
    match = re.search(r"^## Checklist\s*$(.*?)(?=^## |\Z)", text, re.M | re.S)
    if not match:
        raise ValueError(f"{name} has no checklist")
    return f"## Checklist: {title}\n{match.group(1).rstrip()}"


def house_rules() -> str:
    return (ROOT / "tools" / "house-rules.md").read_text(encoding="utf-8").strip()


def long_variant(meta: dict[str, str]) -> str:
    parts = []
    if meta.get("operation"):
        parts.append("# The requested operation\n\n" + meta["operation"])
    if meta.get("checklists"):
        parts += [checklist(name) for name in meta["checklists"].split()]
        parts.append(house_rules())
    else:
        parts.append(skill_text(meta["skill"]))
        cases = worked_cases(meta["skill"])
        if cases:
            parts.append(cases)
    body = demote("\n\n".join(parts))
    longest = max([len(m) for m in re.findall(r"^(`{3,})", body, re.M)] or [2])
    fence = "`" * max(3, longest + 1)
    return f"{fence}markdown\n{body}\n{fence}"


def render(text: str) -> str:
    meta, _ = front_matter(text)
    if START not in text or END not in text:
        raise ValueError("missing long-variant markers")
    head, rest = text.split(START, 1)
    _, tail = rest.split(END, 1)
    return f"{head}{START}\n{long_variant(meta)}\n{END}{tail}"


def pages() -> list[Path]:
    return sorted(p for p in PROMPTS.glob("*.md") if p.name != "index.md")


def main(argv: list[str]) -> int:
    check = "--check" in argv
    failures = []
    for path in pages():
        current = path.read_text(encoding="utf-8")
        try:
            updated = render(current)
        except (ValueError, KeyError, AttributeError) as error:
            failures.append(f"{path.relative_to(ROOT)}: {error}")
            continue
        if updated == current:
            print(f"ok       {path.relative_to(ROOT)}")
        elif check:
            failures.append(f"out of date: {path.relative_to(ROOT)}")
        else:
            path.write_text(updated, encoding="utf-8")
            print(f"synced   {path.relative_to(ROOT)}")
    for line in failures:
        print(f"FAIL     {line}", file=sys.stderr)
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
