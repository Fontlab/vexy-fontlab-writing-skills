---
this_file: README.md
---

# FontLab writing skills

Agent skills that write in the FontLab house voice. Install them into Claude Code, Cursor, Codex, or any tool that reads `SKILL.md` files:

```bash
npx skills add Fontlab/vexy-fontlab-writing-skills
```

Add one at a time with `-s`, or take the set:

```bash
npx skills add Fontlab/vexy-fontlab-writing-skills -s fontlab-neutral
npx skills add Fontlab/vexy-fontlab-writing-skills --all
```

Current localization guidance follows the core memories. Language pages state
the current decisions; dated review ledgers and Git history retain earlier
wording. Term tables are regenerated from the core memories, including their
notes and approval status.

## The skills

| Skill | Use it for |
|---|---|
| `fontlab-neutral` | Release notes, what's new, announcements, introductions, About pages. The primary voice skill. |
| `fontlab-marketing` | Landing pages, product pages, store copy, campaigns, taglines. |
| `fontlab-technical` | Manuals, procedures, reference pages, help articles, tooltips, API docs. |
| `fontlab-write` | New text that connects emotional appeal to precise technical explanation. |
| `fontlab-rewrite` | Existing mixed text: recognize each passage's job, edit in the matching style, and smooth the transitions. |
| `fontlab-tldr` | Literary condensation to about 20%, preserving source voice, structure, named identities, and distinctive phrases through three private rounds. |
| `fontlab-terminology` | Product names, term checking, the nouns that mean different things in different apps. |
| `fontlab-localization` | Writing English that survives translation, Qt catalog mechanics, translation memories, machine drafts, and the error typology a review measures against. |
| `fontlab-localization-de` | German: register, headline-style compression, compounds and loanwords, plural and number facts, mnemonics, key names, false friends, and the German term table. |
| `fontlab-localization-es` | Latin American Spanish (`es_MX`): register, dialect discipline, terminology, plural and number facts, mnemonics, key names, and the Spanish term table. |
| `fontlab-localization-fr` | French: register, the Haralambous-based terminology, typographic spacing, plural and number facts, mnemonics, key names, and the French term table. |
| `fontlab-localization-pl` | Polish: register, case and gender with placeholders, the matryca and firet decisions, four plural categories against Qt's three forms, diacritics, and the Polish term table. |
| `fontlab-partners` | Content for partners.fontlab.com, where the traps are structural rather than stylistic. |

Each skill is self-contained. It installs on its own, carries every rule it enforces, and reads no file outside its own directory.

Balanced is a deliberate mixture, not a new name for neutral. Use neutral for the established factual house voice. Use balanced writing when a new piece needs both reader appeal and technical detail; use balanced editing when a draft already mixes those jobs. There is no fixed percentage, and limitations, prices, and procedures stay factual. The balanced skills reuse the measured registers; no separate balanced corpus or score is claimed.

Use `/fontlab-tldr` to condense a source while keeping its own narrative voice. It combines neutral-writing discipline with three rounds at the same 20% target, then returns only the final text. When no distinctive English style is identifiable, it uses ASD-STE100 as the fallback.

## How the skills use the house voice

Neutral states facts and changes warmly. Marketing connects an offer with the
reader's work. Technical writing explains a mechanism or gives usable
instructions. Choose the register per passage; do not force a whole document
into one register because it contains a procedure or an offer.

The shared craft rules teach concrete attention, connected paragraphs and
varied pace. A developed sentence can explain a relationship; a short one can
settle it. Recurring details should acquire meaning as the explanation proceeds.
The neutral skill demonstrates this method through paired short and patient
examples. The remaining skill cores are being revised individually.

The skills preserve useful conditionals, qualifications, rhythm, and exact
source material. They do not add pronouns, named tools, metaphors, or punctuation
to meet a quota. A corpus measurement can identify a passage worth inspecting;
it cannot establish correctness, usability, or authorship.

Worked cases state their evidence before the revision. Fictional examples are
labelled and do not establish real product behavior or current offer terms.
Every skill carries the shared factual, editorial, and output safeguards.

The measurement tool remains an optional diagnostic aid. Its stored register
bands are legacy comparison data, not writing requirements. Below 40 words it
omits range comparisons; this display threshold does not make longer samples
reliable. Word matches are review candidates, including accurate technical
uses. Its lightweight Markdown cleanup is approximate: select coherent prose
and inspect quotations, labels and examples separately. It cannot verify facts
or identify an author.

## Maintaining them

The shared block lives once, in `tools/house-rules.md`, and is copied into each skill between markers. Never edit it inside a skill.

```bash
python3 tools/scripts/export_terms.py         # regenerate the per-language term tables from ../vexy-fontlab-writing-styleguide
python3 tools/scripts/sync_shared.py          # write the block into every skill
python3 tools/scripts/sync_shared.py --check  # fail if any skill is out of date
python3 tools/scripts/check_paths.py          # fail on an unresolvable path or sibling name
bash tools/scripts/check_all.sh               # all of the above
```

The combined check also runs the measurement CLI tests. Punctuation choices
need editorial review; a dash alone does not fail the structural checks.

## Licence

MIT. See `LICENSE`.
