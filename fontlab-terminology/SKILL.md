---
name: fontlab-terminology
description: >-
  Check and fix product names, terminology, and capitalization in any FontLab or Vexy text. Use when
  the user asks whether a name is written correctly, says "check the terminology", "is it FontLab or
  Fontlab", "which name do we use", "fix the product names", "audit this for terms", or when any draft
  mentions FontLab, Fontlab Ltd., TransType, Fontographer, Vexy Lines, Vexy Linestra, Vexy Playlines,
  or Vexy Vextra. Also use when two products use the same word for different things, or when a draft
  needs a new term defined. The term list in references/terms.md is the source of truth.
license: MIT
metadata:
  version: "1.0.0"
  family: fontlab-writing
---

# FontLab terminology

One word, one meaning, one spelling, in every document and every language.

`references/terms.md` ships with this skill and holds the data: the settled names, the domains, the ten collision nouns, the four names with no house form, and a table of the domain vocabulary. Read it before you rule on a word. Do not answer a naming question from memory: the whole point of the file is that the FontLab and Fontlab spellings look like typos and are not.

## The three verdicts

Every finding lands in one of three buckets, and mixing them up is the failure mode this skill exists to prevent.

**Fix.** The house form is settled and the draft got it wrong. `Fontlab 8` becomes `FontLab 8`. `Vexy-Lines` becomes `Vexy Lines`. Section 1 of the term list decides these.

**Name the app.** The word is a collision noun and the sentence could be read two ways. You do not change the word; you add the product. Section 3 of the term list has all ten and the meanings each carries.

**Flag and ask.** No house form exists, or the correction has a cost the author has to weigh. Section 4 of the term list has these: three draft names, one retired name, and one version mismatch. You report them and stop. An invented house rule is worse than an open question, because nobody rechecks it.

## The checking procedure

Run these in order over a draft.

1. **Product and company names.** Spelling, capitalization, spacing, version form. FontLab is the product; Fontlab Ltd. is the company; both spellings can sit in one sentence and neither gets normalized into the other. Lowercase `fontlab` is correct only in the Python module name and in domains.
2. **Domains.** Lowercase, no `www`, code font. Any domain not in section 2 of the term list is a flag, not a fix.
3. **Collision nouns.** For each occurrence: does the sentence name the application, or does the document cover exactly one product? If neither, the finding is "name the app".
4. **Declared short forms.** A short form is declared once before first use and then used consistently. Silent alternation between the long and short name is a defect.
5. **One name per concept.** The same panel, format, or feature is called the same thing throughout. Elegant variation is a defect here, not a virtue.
6. **Interface vocabulary.** Panel, property bar, dialog, tool, command, used with the meanings in the term list. A panel is dockable; a dialog blocks.
7. **File formats and extensions.** The format name in the case the table gives, the extension lowercase with the dot.
8. **Unknown domain terms.** A word carrying domain meaning with no entry in the term list is a glossary candidate, not an error. List it with a one-line reason.

## Output format

Return a findings list, not a rewrite, unless the user asked for a rewrite. One line per finding, with the verdict visible.

```
line 12  fix        "Fontlab 8"       -> "FontLab 8"              product name, capital L
line 19  fix        "Vexy-Lines"      -> "Vexy Lines"             no hyphen in prose
line 24  fix        "TransType"       -> "TransType 5"            version on first mention
line 31  name app   "the mask"        -> "the Vexy Lines mask"    collision noun, two meanings
line 38  name app   "the Transform"   -> "the FontLab Transform panel"  panel, not tool
line 44  flag       "studio.fontlab.com"   draft name, no shipped manual attests it. Which service?
line 51  flag       "Strokes Maker"        retired name. Historical mention, or stale copy?
```

Then two closing blocks, either of which may be empty:

```
Glossary candidates
  line 27  "ink trap"   drawn feature, used twice, no entry in the term list

Open questions
  line 44  studio.fontlab.com: ask which service runs there before this ships
```

For the partner site, the finding names the cause: `partners.fontlab.com` says TransType 4 throughout, the strings are keyed to asset filenames, and changing the prose alone breaks the pairing. Report it as one finding against the page, not as forty line-level corrections.

## Worked example

Draft:

> Fontlab Ltd. released Fontlab 8 last year. Open the Layers panel, pick a layer, and use Transform to scale the artwork. Strokes Maker users can import their old files.

Findings:

```
line 1  fix       "Fontlab 8"       -> "FontLab 8"     product name, capital L
line 1  keep      "Fontlab Ltd."                        company name, correct as written
line 2  name app  "the Layers panel"  -> "the FontLab Layers and Masters panel"
                                        or "the Vexy Lines Layers panel", depending on the product
line 2  name app  "use Transform"   -> "use the FontLab Transform panel"   panel in FontLab, tool elsewhere
line 3  flag      "Strokes Maker"    retired name for Vexy Lines. This reads like current copy
                                     rather than a migration note. Confirm before rewriting.
```

The `keep` line matters. A reviewer who sees FontLab and Fontlab in adjacent sentences will assume one is a typo, so a naming report says out loud which spellings were checked and found correct.

## Adding a term

When a draft needs a word the term list does not have, propose an entry rather than an opinion. An entry carries: a slug id, the term as written, a category, the products it applies to, a definition of 60 to 100 words in the house order (what it is, how it works, how you apply it, when it matters, technical specifics), one do example and one dont example, a collision note if another product uses the word differently, up to five related ids, and the document the definition came from.

Take the definition from the product documentation and cite the file it came from. A definition written from memory is the one nobody rechecks, and it will outlive the draft that prompted it.

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

**H9. Forbidden constructions, measured at zero in the corpus.** "It's not X, it's Y" (0 in 76,386 words). Comparison scaffolds: Before and After, The old way and The new way, Today versus With FontLab (0 instances; the corpus frame is "Previously, ... now ..."). Unanswered rhetorical questions (0). A question answered in the same breath is a different thing and it is a house device: "Need more? Get a lifetime licence." "Have an older TransType? Upgrade now." "Bought TransType 4 in 2026? Your upgrade is free." Question, then answer, in one line. What the house never does is ask a question and leave the reader holding it. A closing paragraph that adds no new fact (0 of 13 essays end with a summary or a call to action). A benefit clause standing alone as its own sentence: weld the benefit to the mechanism with "so you can", or drop it.

**H10a. The conditional frame is the house's default sentence.** `If you ...` opens 13.7 percent of sentences in the corpus, 463 instances, and zero percent of the pages an AI wrote for this company. It is the strongest single authorship marker measured. Write "If you don't want element references, first go to any glyph where the contours occur" rather than a comparison scaffold or a bare imperative. The parenthetical technical aside behaves the same way: 12 percent of house sentences carry one, against 2 percent on the AI pages. Do not flatten either into plainer syntax.

**H10. What to protect, because an editor will remove it.** Exclamation marks, at about one per 400 words in marketing and overview prose and one per 4,000 in reference prose. The rule of three, which is 7.6 percent of marketing sentences and the highest rate in the corpus. One travelling idiom per document. Self-undercutting asides ("it's up to you!", "this is just a suggestion"). Customer quotations with their repetition intact. The bare ampersand in headings. Bolded verbs rather than bolded nouns in marketing. Single-sentence paragraphs, which are 45 to 57 percent of neutral paragraphs: never merge them into developed paragraphs.

**H10b. House typographic conventions.** Interface labels take italics, not bold, in release notes and overview prose: choose _File > Add Instance_, turn on _Install Fonts_ in the _Destination_ dropdown. Table names, extensions and settings keys take code style: `gvar`, `.woff2`, `COLR`. Prices are written with both currencies and one number when they are equal, in the house's own shorthand: "€$ 99", "€$ 40". A release that ships localization may open in the languages it now speaks, as a greeting rather than as a translated paragraph.

**H11. Names.** FontLab is the product; Fontlab Ltd. is the company. Lowercase `fontlab` is correct only in the Python module name and in domains. Product names never translate. FontLab and the Vexy products share nouns that mean different things: Layers, Masks, Groups, Fills, Brush, Knife, Transform, and at least Pencil, Eraser, Scissors. Name the app whenever a reader could be confused. A document may declare its own short form once, then must use it.

**H12. Do not touch** quotations, code, code blocks, command lines, file paths, identifiers, API names, URLs, licence text, interface strings, or data inside table cells.

**H13. Registers differ, and the rules bend with them.** Documentation and reference prose take sentence case, effectively no exclamation marks, and no title case. The marketing surface uses title case for pillar names and capitals for eyebrows, and it carries exclamation marks. Applying the documentation rules to a landing page produces prose the house did not write.

**H14. Two passes, always.** Pass one drafts. Pass two rereads the draft as a skeptic asking one question: what in this still reads as machine-written? Then sweep for the forbidden constructions in H9 and check that nothing in H10 was quietly removed.

**H15. Very short pieces.** Below roughly 40 words, H5 and H6 do not apply. H1, H2, H3, H4, H7, H8, H9 and H11 apply at every length, tooltips and button labels included.

**H16. The override.** Break any rule here sooner than write something worse. If a flagged word is the right word, keep it. Small roughness that carries rhythm, including the occasional comma splice, is not a defect to repair.
<!-- fontlab:shared:end -->
