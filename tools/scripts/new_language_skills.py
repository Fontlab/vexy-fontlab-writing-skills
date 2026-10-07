#!/usr/bin/env python3
# this_file: tools/scripts/new_language_skills.py
"""Write the SKILL.md of each machine-drafted per-language localization skill.

Reads the language's localization guide in the writing guide
(`src_docs/md/localization/<code>.md` in the vexy-fontlab-writing-styleguide
repository) and writes `fontlab-localization-<code>/SKILL.md`: front matter, an
opening that states the draft status, the guide from its first section up to
"Current terminology", and a pointer to `references/terms.md`. Relative links
become plain text, so the skill reads no file outside its own directory.

The German, Spanish, French and Polish skills are hand-written and reviewed;
this script refuses them. The house-rules block is left to `sync_shared.py`,
and a block already in the file is kept, so a second run changes nothing.

Usage:
    python3 tools/scripts/new_language_skills.py [--styleguide PATH] [zh ru ja ...]
"""
import argparse
import re
import sys
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
DEFAULT_STYLEGUIDE = ROOT.parent / "vexy-fontlab-writing-styleguide"
REVIEWED = ("de", "es", "fr", "pl")
START = "<!-- fontlab:shared:start -->"
END = "<!-- fontlab:shared:end -->"
TERMINOLOGY = "## Current terminology"
LINK = re.compile(r"!?\[([^\]]*)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
EXTERNAL = ("http://", "https://", "mailto:")
# English name, then what a user may say in the language itself: its name and "translate".
LANGUAGES = {
    "zh": ("Simplified Chinese", ("简体中文", "翻译成中文")),
    "zh-hant": ("Traditional Chinese", ("繁體中文", "翻譯成繁體中文")),
    "ru": ("Russian", ("по-русски", "переведи")),
    "pt": ("Brazilian Portuguese", ("em português", "traduza")),
    "ar": ("Arabic", ("بالعربية", "ترجم")),
    "hi": ("Hindi", ("हिन्दी में", "अनुवाद")),
    "ja": ("Japanese", ("日本語", "日本語に翻訳")),
    "it": ("Italian", ("in italiano", "traduci")),
    "id": ("Indonesian", ("bahasa Indonesia", "terjemahkan")),
    "ko": ("Korean", ("한국어", "한국어로 번역")),
    "tr": ("Turkish", ("Türkçe", "çevir")),
    "vi": ("Vietnamese", ("tiếng Việt", "dịch sang tiếng Việt")),
    "th": ("Thai", ("ภาษาไทย", "แปลเป็นภาษาไทย")),
    "uk": ("Ukrainian", ("українською", "переклади")),
    "cs": ("Czech", ("česky", "přelož")),
}


def delink(text, code):
    """Replace each relative Markdown link with its label and the place its target lives."""
    def plain(match):
        label, target = match.group(1), match.group(2)
        if target.startswith(EXTERNAL):
            return match.group(0)
        page = target.split("#")[0]
        if not page:
            return label
        if page == f"{code}-terms.md":
            return f"{label} (`references/terms.md`)"
        if page.endswith(".md") and "/" not in page:
            return f"{label} (in `fontlab-localization`)"
        return f"{label} (in the FontLab writing guide)"
    return LINK.sub(plain, text)


def guide_parts(text):
    """Return the guide's introduction and its sections before "Current terminology"."""
    lines = text.splitlines()
    heads = [i for i, line in enumerate(lines) if line.startswith("## ")]
    if not heads:
        raise ValueError("no section heading")
    title = next(i for i, line in enumerate(lines) if line.startswith("# "))
    end = next((i for i in heads if lines[i].strip() == TERMINOLOGY), len(lines))
    intro = "\n".join(lines[title + 1:heads[0]]).strip()
    body = "\n".join(lines[heads[0]:end]).strip()
    return intro, body


def front_matter(code, name, phrases):
    said = ", ".join(f'"{phrase}"' for phrase in phrases)
    description = (
        f"Translate and review {name} for FontLab and Vexy: the application UI (Qt .ts catalogs), "
        f"the Help Panel, manuals, release notes and store copy. Use when the user asks for a "
        f'translation into {name}, says {said}, "review the {name}", "{name} term for", or hands '
        f"over {name} catalogs, ledgers or translation memories. A machine-researched first "
        f"draft that no native reviewer has approved: carries draft guidance on register, the grammar of "
        f"interface strings, plurals, punctuation, mnemonics, key names and false friends, and a "
        f"portable copy of the {name} term table with each term’s approval status. "
        f"Use with fontlab-localization for the rules shared by every language.")
    folded = textwrap.fill(description, width=100, initial_indent="  ", subsequent_indent="  ",
                           break_on_hyphens=False, break_long_words=False)
    return (f"---\nname: fontlab-localization-{code}\ndescription: >-\n{folded}\nlicense: MIT\n"
            f'metadata:\n  version: "0.1.0"\n  family: fontlab-writing\n  language: {code}\n---')


def opening(name):
    return textwrap.dedent(f"""\
        A first draft for {name}. A model researched the guidance below and the
        term table in `references/terms.md`; no native reviewer has approved the
        language as a whole. Individual terms carry their own approval status; a
        proposed term remains proposed, and a protected name keeps its glossary spelling. The {name} interface catalogs
        are unfinished machine drafts: a string found in one settles neither a term
        nor a rule.

        Use `references/terms.md`, and a newer core memory when one is supplied, for
        terminology, definitions and review status. Keep a proposed term consistent
        across the interface and help, and report it as proposed. Where a native
        reviewer's decision or newer project data disagrees with this skill, follow
        it and record the change. Report only checks performed: text written with
        this skill is not reviewed by a native speaker and not tested in the running
        application until someone does that.""")


def closing(code, name):
    return textwrap.dedent(f"""\
        ## Run the review as a loop

        The Review list above is this skill's checklist. Run it on each portion
        as H17 describes: one item at a time against source, target and the term
        table; name the string behind each answer; repair what fails and recheck
        it. Stop after three rounds and report what still fails.

        ## References

        - `references/terms.md`: the full {name} term table, generated from the core
          memory `{code}-core.tmx` of the writing guide, with the status, translator
          note and definition of every term.
        - The {name} localization guide of the writing guide is the source of the
          sections above.

        ## Related skills

        `fontlab-localization` for the shared rules; `fontlab-terminology` for
        product names and shared nouns; `fontlab-technical` for {name} help text.""")


def shared_block(path):
    """The house-rules block already in the skill, so a rerun does not empty it."""
    if not path.exists():
        return ""
    text = path.read_text(encoding="utf-8")
    if START not in text or END not in text:
        return ""
    return text.split(START, 1)[1].split(END, 1)[0]


def render(code, guide, shared=""):
    name, phrases = LANGUAGES[code]
    intro, body = guide_parts(guide)
    parts = [front_matter(code, name, phrases),
             f"<!-- this_file: fontlab-localization-{code}/SKILL.md -->\n"
             f"<!-- Generated by tools/scripts/new_language_skills.py from the writing guide's "
             f"src_docs/md/localization/{code}.md. Edit the guide, then regenerate. -->",
             f"# FontLab localization: {name}",
             opening(name)]
    if intro:
        parts.append(delink(intro, code))
    parts += [delink(body, code), closing(code, name), f"{START}{shared or chr(10)}{END}"]
    return "\n\n".join(parts) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--styleguide", type=Path, default=DEFAULT_STYLEGUIDE)
    parser.add_argument("codes", nargs="*", default=list(LANGUAGES))
    args = parser.parse_args()
    guides = args.styleguide / "src_docs" / "md" / "localization"
    status = 0
    for code in args.codes:
        skill = f"fontlab-localization-{code}"
        source = guides / f"{code}.md"
        problem = ""
        if code in REVIEWED:
            problem = f"{skill} is hand-written and reviewed; this script does not write it"
        elif code not in LANGUAGES:
            problem = f"no language data for {code}"
        elif not source.exists():
            problem = f"{source} not found"
        else:
            out = ROOT / skill / "SKILL.md"
            try:
                text = render(code, source.read_text(encoding="utf-8"), shared_block(out))
            except ValueError as error:
                problem = f"{source}: {error}"
        if problem:
            print(f"FAIL     {problem}", file=sys.stderr)
            status = 1
            continue
        out.parent.mkdir(parents=True, exist_ok=True)
        if out.exists() and out.read_text(encoding="utf-8") == text:
            print(f"ok       {skill}")
            continue
        out.write_text(text, encoding="utf-8")
        print(f"wrote    {skill}")
    return status


if __name__ == "__main__":
    sys.exit(main())
