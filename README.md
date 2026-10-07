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
| `fontlab-simplify` | Plain-language, controlled-English (ASD-STE100 writing rules) or easy-to-read rewrites that keep every fact, condition, hedge and label. |
| `fontlab-terminology` | Product names, term checking, the nouns that mean different things in different apps. |
| `fontlab-localization` | Writing English that survives translation, Qt catalog mechanics, translation memories, machine drafts, and the error typology a review measures against. |
| `fontlab-localization-de` | German: register, headline-style compression, compounds and loanwords, plural and number facts, mnemonics, key names, false friends, and the German term table. |
| `fontlab-localization-es` | Latin American Spanish (`es_MX`): register, dialect discipline, terminology, plural and number facts, mnemonics, key names, and the Spanish term table. |
| `fontlab-localization-fr` | French: register, the Haralambous-based terminology, typographic spacing, plural and number facts, mnemonics, key names, and the French term table. |
| `fontlab-localization-pl` | Polish: register, case and gender with placeholders, the matryca and firet decisions, four plural categories against Qt's three forms, diacritics, and the Polish term table. |
| `fontlab-localization-zh` | Simplified Chinese (`zh_CN`): register without pronouns, verb-object labels, the single plural form with classifiers, mainland punctuation and vocabulary, appended mnemonics, false friends, and the Simplified Chinese term table. Machine-drafted guidance and proposed term table; no native review yet. |
| `fontlab-localization-zh-hant` | Traditional Chinese (`zh_TW`): register, Taiwan's punctuation and character forms, the single plural form with classifiers, appended mnemonics, false friends, and the Traditional Chinese term table. Machine-drafted guidance and proposed term table; no native review yet. |
| `fontlab-localization-ru` | Russian (`ru_RU`): the вы register, sentence case, three plural forms, mnemonics on Cyrillic letters, alphabet mixing, false friends, and the Russian term table. Machine-drafted guidance and proposed term table; no native review yet. |
| `fontlab-localization-pt` | Brazilian Portuguese (`pt_BR`): the você register, the 1990 orthography, two plural forms under the `pt_BR` rule, mnemonics on unaccented letters, false friends, and the Portuguese term table. Machine-drafted guidance and proposed term table; no native review yet. |
| `fontlab-localization-ar` | Arabic (`ar`): Modern Standard Arabic, verbal-noun commands, six plural forms, mnemonics on Arabic letters, bidirectional rules, false friends, and the Arabic term table. Machine-drafted guidance and proposed term table; no native review yet. |
| `fontlab-localization-hi` | Hindi (`hi_IN`): the आप register, two plural forms, appended mnemonics, Devanagari encoding and spelling, false friends, and the Hindi term table. Machine-drafted guidance and proposed term table; no native review yet. |
| `fontlab-localization-ja` | Japanese (`ja_JP`): the です・ます register, counters and the single plural form, Japanese–Latin spacing, appended mnemonics, katakana loans, false friends, and the Japanese term table. Machine-drafted guidance and proposed term table; no native review yet. |
| `fontlab-localization-it` | Italian (`it_IT`): the tu register, two plural forms and their agreement, mnemonics on unaccented letters, names and loans, false friends, and the Italian term table. Machine-drafted guidance and proposed term table; no native review yet. |
| `fontlab-localization-id` | Indonesian (`id_ID`): the Anda register, the single plural form without reduplication, mnemonics, names and loans, false friends, and the Indonesian term table. Machine-drafted guidance and proposed term table; no native review yet. |
| `fontlab-localization-ko` | Korean (`ko_KR`): the 하세요 register, counters and the single plural form, appended mnemonics, Hangul-only spelling, false friends, and the Korean term table. Machine-drafted guidance and proposed term table; no native review yet. |
| `fontlab-localization-tr` | Turkish (`tr_TR`): the siz register, the single plural form with singular nouns after numbers, the dotted and dotless i, mnemonics, false friends, and the Turkish term table. Machine-drafted guidance and proposed term table; no native review yet. |
| `fontlab-localization-vi` | Vietnamese (`vi_VN`): the bạn register, the single plural form, mnemonics on unmarked letters, tone-mark placement, false friends, and the Vietnamese term table. Machine-drafted guidance and proposed term table; no native review yet. |
| `fontlab-localization-th` | Thai (`th_TH`): register without pronouns or particles, classifiers and the single plural form, appended mnemonics, line breaking and character order, false friends, and the Thai term table. Machine-drafted guidance and proposed term table; no native review yet. |
| `fontlab-localization-uk` | Ukrainian (`uk_UA`): the ви register, the 2019 orthography, three plural forms, mnemonics on Cyrillic letters, the apostrophe letter, false friends, and the Ukrainian term table. Machine-drafted guidance and proposed term table; no native review yet. |
| `fontlab-localization-cs` | Czech (`cs_CZ`): vykání, sentence case, three plural forms, mnemonics on a letter of the translation, false friends, and the Czech term table. Machine-drafted guidance and proposed term table; no native review yet. |
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
python3 tools/scripts/new_language_skills.py  # rewrite the fifteen machine-drafted language skills from the guide
python3 tools/scripts/export_terms.py         # regenerate the per-language term tables from ../vexy-fontlab-writing-styleguide
python3 tools/scripts/sync_shared.py          # write the block into every skill
python3 tools/scripts/sync_shared.py --check  # fail if any skill is out of date
python3 tools/scripts/check_paths.py          # fail on an unresolvable path or sibling name
bash tools/scripts/check_all.sh               # all of the above
```

The German, Spanish, French and Polish skills are hand-written and reviewed.
The other fifteen language skills are generated. `new_language_skills.py`
reads each language's localization guide in `../vexy-fontlab-writing-styleguide`
and writes the skill: a statement of the draft status, the guide's sections
before "Current terminology", and a pointer to the term table. It turns
relative links into plain text, keeps the house-rules block already in the
file, and refuses `de`, `es`, `fr` and `pl`. To change a generated skill, edit
the guide and run the script again. Pass language codes to limit a run, as
with `export_terms.py`. Once a native reviewer takes a language over, move its
code to the script's refused list and maintain the skill by hand.

The combined check also runs the script tests. Punctuation choices
need editorial review; a dash alone does not fail the structural checks.

## Website

`./build.py` (a self-contained `uv` script) renders this README and every skill
with ProperDocs, MaterialX and the fltheme26 theme into `docs/fl1992mk/`, published at
<https://fontlab.dev/vexy-fontlab-writing-skills/fl1992mk/>. The `Site` GitHub
workflow rebuilds it on every push and commits the result. `./build.py --serve`
previews it locally.

## Licence

MIT. See `LICENSE`.
