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

## The skills

| Skill | Use it for |
|---|---|
| `fontlab-neutral` | Release notes, what's new, announcements, introductions, About pages. The primary voice skill. |
| `fontlab-marketing` | Landing pages, product pages, store copy, campaigns, taglines. |
| `fontlab-technical` | Manuals, procedures, reference pages, help articles, tooltips, API docs. |
| `fontlab-balanced-writing` | New text that connects emotional appeal to precise technical explanation. |
| `fontlab-balanced-editing` | Existing mixed text: recognize each passage's job, edit in the matching style, and smooth the transitions. |
| `fontlab-tldr` | Literary condensation to about 20%, preserving source voice, structure, named identities, and distinctive phrases through three private rounds. |
| `fontlab-terminology` | Product names, term checking, the nouns that mean different things in different apps. |
| `fontlab-localization` | Writing English that survives translation, and maintaining term tables. |
| `fontlab-partners` | Content for partners.fontlab.com, where the traps are structural rather than stylistic. |

Each skill is self-contained. It installs on its own, carries every rule it enforces, and reads no file outside its own directory.

Balanced is a deliberate mixture, not a new name for neutral. Use neutral for the established factual house voice. Use balanced writing when a new piece needs both reader appeal and technical detail; use balanced editing when a draft already mixes those jobs. There is no fixed percentage, and limitations, prices, and procedures stay factual. The balanced skills reuse the measured registers; no separate balanced corpus or score is claimed.

Use `/fontlab-tldr` to condense a source while keeping its own narrative voice. It combines neutral-writing discipline with three rounds at the same 20% target, then returns only the final text. When no distinctive English style is identifiable, it uses ASD-STE100 as the fallback.

## Why these are not generic writing skills

They are calibrated against a measured corpus: 67,000 words of FontLab 8 "what's new" essays, 48,000 words of release notes, and the FontLab and TransType landing pages, all written by the same person. Where a rule cites a number, the number came from counting that corpus.

That measurement changed several rules that a generic anti-AI writing skill would state as absolutes:

- **Dashes.** The house prefers a colon over an em dash by roughly 47 to 1 in neutral prose, so prefer the colon. But it does use a dash where what follows carries a finite verb or turns the sentence. What is forbidden is the appositive gloss dash, `noun phrase, dash, two adjectives of atmosphere`, which is the actual machine tell.
- **Exclamation marks.** About one per 4,000 words in reference prose, and one per 400 in marketing and announcements. "Have fun!" is a real house heading. A blanket ban is wrong by a factor of ten in the second case.
- **The rule of three.** 7.6 percent of house marketing sentences, the highest rate in the corpus. It is a signature, not a tell.
- **Long sentences.** Fifteen percent of house neutral sentences run over 30 words. A readability pass that caps sentences at 25 destroys the register.
- **Single-sentence paragraphs.** Between 45 and 57 percent of house paragraphs. Merging them into developed paragraphs is a rewrite, not an edit.
- **Questions.** A question answered in the same line is a house device, not a tell. What the house never does is ask one and leave it hanging.

There are four registers, not three. The overview and announcement register, a release-notes front page or a what's-new index, sits between neutral and marketing: shorter sentences than the essays, more second person than anything else measured, and about ten times the exclamation rate of reference prose. `measure_voice.py --register announcement` carries its bands.

The full set of what a skill must protect, and what it must forbid, is in the shared house rules at the end of every `SKILL.md`.

## Maintaining them

The shared block lives once, in `tools/house-rules.md`, and is copied into each skill between markers. Never edit it inside a skill.

```bash
python3 tools/scripts/sync_shared.py          # write the block into every skill
python3 tools/scripts/sync_shared.py --check  # fail if any skill is out of date
python3 tools/scripts/check_paths.py          # fail on an unresolvable path or sibling name
bash tools/scripts/check_all.sh               # all of the above
```

## Licence

MIT. See `LICENSE`.
