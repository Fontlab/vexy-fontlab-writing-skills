---
name: fontlab-localization
description: >-
  Write FontLab and Vexy source English that survives translation, and run the term tables, tiers, and
  translation reviews that follow. Use when the user asks about localization, translation, "will this
  translate", "prepare this for translation", "write for a global audience", "add a language", "update
  the German terms", or when text is headed for machine translation or a translation vendor. Also use
  when reviewing UI strings, tooltips, button labels, or store copy that will ship in many languages.
license: MIT
metadata:
  version: "1.0.0"
  family: fontlab-writing
---

# FontLab localization

Most FontLab and Vexy readers are not native English speakers, and a growing share of them read a translation. Both facts change how the English gets written, long before anyone translates anything.

Most of the work is job one. `references/moves.md` carries worked pairs: a source sentence, the rewrite, and the mechanism that would have broken.

## Job one: English that survives translation

**Short sentences, one idea each.** A 40-word English sentence becomes an unreadable German one, because German holds the verb until the end and the reader has to carry everything until it arrives.

**No idioms and no culture-bound metaphors.** No sports figures, no cooking figures, no wordplay. The one metaphor a technical passage is allowed must be physical and universal: a drawer, a line, a queue.

**Repeat the noun instead of using a pronoun** when the referent is more than one clause away. Gendered languages resolve pronouns by grammatical gender, so an English "it" that points backwards across a clause boundary will attach to the wrong noun in translation, silently and confidently.

**Unstack the nouns.** "Font family name field label" has to be unstacked by every translator, and each one guesses a different structure. Write "the label of the Font family name field" and the structure is already decided.

**Say if and when precisely.** If is conditional; when is temporal. English blurs them and most languages use different words, so a translator who guesses wrong turns an optional step into a mandatory one.

**Never assemble a sentence from separate interface strings.** A sentence built from fragments cannot be reordered, and every language reorders. One string holds one whole sentence.

**Named placeholders, never positional.** `{glyph_count}` beats `%1`, because a translator can read what the slot holds and put it where the language wants it. A positional placeholder is a guess with no way to check it.

**Leave room.** German and Russian run 20 to 35 percent longer than English. A button label that barely fits in English will not fit at all. Design the control for the longest language, not the shortest.

**No contractions in interface strings.** They cost nothing in English and they break string matching and extraction.

**Write dates and numbers unambiguously.** `2026-08-30`, never `08/30/26`. Say the unit every time, including on the second mention.

## What never translates

Leave these exactly as they stand, in every language:

- Product names: FontLab, Fontlab Ltd., TransType 5, Fontographer, Vexy Lines, Vexy Linestra, Vexy Playlines, Vexy Vextra, Adobe Illustrator. Do not inflect them either: "in FontLab", not a case-marked form of the name.
- OpenType feature and axis tags: `kern`, `liga`, `calt`, `locl`, `frac`, `ss01`, `wght`.
- Table names: `GSUB`, `GPOS`, `cmap`, `OS/2`, `glyf`, `CVT`.
- File extensions and format identifiers: `.vfc`, `.vfj`, `.ufo`, `.otf`, `.ttf`, `.woff2`.
- Code, command lines, file paths, identifiers, API names, URLs, and domains.
- Interface strings that ship untranslated. If a menu command appears in English in the running application, the manual quotes it in English and glosses it in the target language once.

A term that stays in English inside a translated sentence is not a gap. A term invented to avoid leaving English there is a defect.

## The term table model

A term table maps a term id to one translation per language. Keep it wherever the project keeps its data; the shape is what matters.

```yaml
kerning-class:
  translation: Unterschneidungsklasse
  status: approved          # approved | proposed | do-not-translate
  note: "Kerning-Klasse is acceptable where the interface already says Kerning."
```

`approved` means a native reviewer signed it off and it ships. `proposed` means somebody drafted it and it is waiting: usable in a draft, never in shipped copy without a note. `do-not-translate` repeats the English term rather than leaving the field empty, so a vendor sees what to ship instead of an omission.

Three rules make forty languages survivable.

1. **Product names never translate.** They carry `do-not-translate` in every language, and the entry repeats the English form so nobody reads a blank field as a task.
2. **A term with no approved translation falls back to English** and counts against that language's coverage. A visible gap is honest. An invented word is neither honest nor visible, because it looks finished.
3. **A translation changes in the term table, once, and regenerates everywhere.** If a translator improves a term on a page, the improvement is lost and the page now disagrees with every other page. Change the table, not the page.

Where a language keeps the English word in practice, the note says so rather than inventing a calque. Where the language has a real term, the language wins. German splits `sidebearing` into two words, Vorbreite and Nachbreite, because there is no single one, and the note is where that fact lives.

## Tiers

The tier decides the workload for a language, not the importance of its market.

- **Tier A, full human review.** A native reviewer approves every term and reads the prose. Roughly ten languages: German, French, Spanish, Italian, Japanese, Chinese (Simplified), Polish, Russian, Portuguese (Brazil), Korean.
- **Tier B, machine translation with glossary enforcement and a native spot check.** The glossary is applied mechanically and a native speaker reads a sample, not the whole corpus.
- **Tier C, glossary only.** Terms may be proposed. No prose is translated yet, and the roster says so.

The tier decides what a language is allowed to claim. A tier C language with 12 approved terms is honest. The same language claiming a translated manual is not.

## Reviewing a translation

Three passes, in this order. Do not merge them: a register problem spotted first will pull attention away from a wrong number.

1. **Terms.** Every glossary term uses its approved translation, and every do-not-translate term is untouched, uninflected, and unspaced differently. This pass is mechanical and you can do it in a language you do not read.
2. **Facts.** Numbers, keyboard shortcuts, menu paths, file names, version numbers, units. These break silently: a decimal comma, a localized shortcut that does not exist, a menu path translated when the interface ships in English. Check each against the source.
3. **Register.** The translation reads as its own language, not as English wearing local words. A literal rendering that no native writer would produce is a defect even when every term is correct.

Pass three needs a native reader. Say what you verified in passes one and two, name what pass three still needs, and leave it there rather than guessing at style in a language you do not read.

## Output

For a source-text review, return a findings list: the line, the construction, the mechanism that breaks it, and the rewrite.

```
line 8   pronoun across clauses   "it" points back two clauses; gendered languages will attach
                                   it to the wrong noun   -> repeat "the master"
line 14  stacked nouns            "font family name field label", four nouns, no structure
                                   -> "the label of the Font family name field"
line 22  split string             sentence assembled from two strings; German puts the verb last
                                   -> one string, one sentence
line 29  positional placeholder   "%1" gives the translator nothing to read -> "{glyph_count}"
```

For a term-table task, return the entries to add or change as a YAML fragment, one line of rationale per term, and the coverage count before and after.

<!-- fontlab:shared:start -->
## House rules

This block is identical in every FontLab writing skill. It is calibrated against a measured corpus of 76,386 words that Adam Twardoch wrote himself: the FontLab 8 "what's new" essays and release notes, and the FontLab and TransType landing pages. Where a rule cites a number, the number came from counting that corpus, not from taste.

**H1. Agency.** You act. The app responds. Apps apply. Fonts and files have no agency. Write "FontLab stores the kerning in the font's `kern` feature", not "kerning is stored". Write "you adjust spacing with Alt and the arrow keys", not "spacing can be adjusted". A font can have a feature; it cannot do anything.

**H2. Never invent a fact.** Every number, name, date, menu label, keyboard shortcut, default, error string, version, and quotation comes from the source or from the user. Nothing else does. When a needed specific is missing, leave a visible placeholder: `[ADD VERIFIED METRIC]`, `[CONFIRM LABEL]`, `[CONFIRM DEFAULT]`. A plausible guess is the worst possible output, because it is the one nobody checks.

**H3. Never inflate certainty past the source.** "May reduce" does not become "eliminates". Keep every load-bearing caveat, especially about compatibility, licensing, data loss, and platform differences. **Never convert a limitation into a positioning.** "TransType does not export a new variable font" must not become "TransType focuses on static output".

**H4. Do not install a personality that is not there,** and do not remove the one that is. Manufactured stakes, performed candor, invented reader emotion ("you feel it by five o'clock"), and forced contrarianism are a new fingerprint. So is stripping the writer's own habits. You may reorder sentences, split paragraphs, and move a conclusion up. You may not add a fact, an attribution, a stake, or a stance the source did not have.

**H5. Cadence, with measured targets.** In neutral product prose the corpus runs a mean sentence length near 20 words with a standard deviation near 12, and 15 percent of sentences exceed 30 words. Do not cap sentences at 25 words: long enumerating sentences are part of the register. In marketing the mean drops to 11 to 15 words and a third of sentences run under 8. Match the register, and vary hard inside it.

**H6. One concrete specific per paragraph, minimum.** A name, a number, a mechanism, a tradeoff, a menu path, a version, an issue number. Issue numbers, build numbers, menu paths and version strings are load-bearing: never trim them for flow.

**H7. Dashes have a shape rule, not a ban.** The corpus prefers a colon over an em dash by about 47 to 1 in neutral prose. So prefer the colon. What is forbidden is the appositive gloss dash, the machine tell: `noun phrase, em dash, two adjectives of atmosphere`. What is permitted is the turn dash, where what follows the dash carries a finite verb or negates what preceded it, at roughly one per 3,000 words of neutral prose and one per 400 words of marketing. En dashes between words: no.

**H8. Banned vocabulary.** delve, leverage, seamless, robust, pivotal, crucial, comprehensive, transformative, game-changing, cutting-edge, meticulous, vibrant, intricate, nuanced, holistic, ever-evolving, tapestry, realm, elevate, unlock, unleash, harness, empower, foster, underscore, showcase, garner, bolster. Also the constructions "serves as", "stands as", "is a testament to", "boasts", and participle analysis tails such as ", highlighting its importance". A banned word inside a quotation or a product's own interface string stays.

**H9. Forbidden constructions, measured at zero in the corpus.** "It's not X, it's Y" (0 in 76,386 words). Comparison scaffolds: Before and After, The old way and The new way, Today versus With FontLab (0 instances; the corpus frame is "Previously, ... now ..."). Rhetorical questions in marketing body copy (0). A closing paragraph that adds no new fact (0 of 13 essays end with a summary or a call to action). A benefit clause standing alone as its own sentence: weld the benefit to the mechanism with "so you can", or drop it.

**H10a. The conditional frame is the house's default sentence.** `If you ...` opens 13.7 percent of sentences in the corpus, 463 instances, and zero percent of the pages an AI wrote for this company. It is the strongest single authorship marker measured. Write "If you don't want element references, first go to any glyph where the contours occur" rather than a comparison scaffold or a bare imperative. The parenthetical technical aside behaves the same way: 12 percent of house sentences carry one, against 2 percent on the AI pages. Do not flatten either into plainer syntax.

**H10. What to protect, because an editor will remove it.** Exclamation marks, at about one per 400 words in marketing and overview prose and one per 4,000 in reference prose. The rule of three, which is 7.6 percent of marketing sentences and the highest rate in the corpus. One travelling idiom per document. Self-undercutting asides ("it's up to you!", "this is just a suggestion"). Customer quotations with their repetition intact. The bare ampersand in headings. Bolded verbs rather than bolded nouns in marketing. Single-sentence paragraphs, which are 45 to 57 percent of neutral paragraphs: never merge them into developed paragraphs.

**H11. Names.** FontLab is the product; Fontlab Ltd. is the company. Lowercase `fontlab` is correct only in the Python module name and in domains. Product names never translate. FontLab and the Vexy products share nouns that mean different things: Layers, Masks, Groups, Fills, Brush, Knife, Transform, and at least Pencil, Eraser, Scissors. Name the app whenever a reader could be confused. A document may declare its own short form once, then must use it.

**H12. Do not touch** quotations, code, code blocks, command lines, file paths, identifiers, API names, URLs, licence text, interface strings, or data inside table cells.

**H13. Registers differ, and the rules bend with them.** Documentation and reference prose take sentence case, effectively no exclamation marks, and no title case. The marketing surface uses title case for pillar names and capitals for eyebrows, and it carries exclamation marks. Applying the documentation rules to a landing page produces prose the house did not write.

**H14. Two passes, always.** Pass one drafts. Pass two rereads the draft as a skeptic asking one question: what in this still reads as machine-written? Then sweep for the forbidden constructions in H9 and check that nothing in H10 was quietly removed.

**H15. Very short pieces.** Below roughly 40 words, H5 and H6 do not apply. H1, H2, H3, H4, H7, H8, H9 and H11 apply at every length, tooltips and button labels included.

**H16. The override.** Break any rule here sooner than write something worse. If a flagged word is the right word, keep it. Small roughness that carries rhythm, including the occasional comma splice, is not a defect to repair.
<!-- fontlab:shared:end -->
