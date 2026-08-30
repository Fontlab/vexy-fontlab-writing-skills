---
name: fontlab-neutral
description: >-
  Write in the FontLab house voice for release notes, what's-new pages, changelog entries, product
  announcements, documentation introductions, overview pages, About pages, forum and status posts,
  and blog posts that inform rather than sell. Use when the user asks to write or rewrite anything
  that states what is true and what changed without pitching it, or says "write the release notes",
  "what's new in", "announce this", "write the intro", "objective but not dry", or "in our voice".
  This is the primary voice skill: it is calibrated against 67,000 words of measured house prose.
  For selling use fontlab-marketing. For procedures and reference pages use fontlab-technical.
license: MIT
metadata:
  version: "1.0.0"
  family: fontlab-writing
---

# FontLab neutral voice

This is the register the house writes most: a change, what it does, what it costs you, what it makes possible. It is not a pitch and it is not a manual. It is the voice of somebody who built the thing telling you what happened.

The rules below are measured, not preferred. The corpus is 67,153 words of FontLab 8 "what's new" essays plus 48,000 words of release notes, all written by the same person over several years.

## The numbers to write to

| Measure | Neutral prose | Overview pages |
|---|---|---|
| Mean sentence length | 20 words | 9 to 10 words |
| Standard deviation | 12 | 5 to 7 |
| Sentences under 8 words | 8.5% | 40 to 52% |
| Sentences over 30 words | 15% | under 3% |
| Words per paragraph | 37 | 26 to 62 |
| Second person per 1,000 words | 19 | 9 to 16 |
| Colons per 1,000 words | 8.9 | varies |
| Em dashes per 1,000 words | 0.19 | near zero |
| Exclamation marks per 1,000 words | 0.25 | 2.6 to 3.9 |

Two things follow that most style advice gets wrong here. Fifteen percent of sentences run over 30 words, so a readability pass that caps sentences at 25 will destroy the register. And roughly half of all paragraphs are a single sentence, so a pass that merges them into developed paragraphs will too.

The single-sentence proportion is an essay property. A page built from six dense capability sections will not reach it, and forcing it there fragments technical content. Match it in prose, not in a specification.

**Write conditionals.** `If you ...` opens 13.7 percent of house sentences and zero percent of the pages an AI wrote here. It is the strongest authorship marker in the corpus, stronger than anything about dashes. Reach for it wherever a sentence depends on what the reader wants.

## Write to the reader, not about the product

The house corpus runs 19 second-person words per 1,000, and some essays reach 38. This is the single measurement a draft most often misses, because writing about a product is the default and writing to a person is a decision.

If your draft is under 8 per 1,000, you have written a product description. Go back and turn the subject around: not "the panel shows which glyphs a sample uses" but "you see which glyphs a sample uses". Not every sentence, and not by force. The corpus alternates: FontLab does something, then you do something with it.

## The opening

Thirteen essays out of thirteen open the same way: one short declarative sentence whose subject is FontLab or you, stating what the product is or what it lets you reach. Never a scene. Never a problem. Never a question.

> FontLab is uncompromisingly variable-first.

> FontLab 8 is an integrated font creation workhorse.

> With FontLab, you can ship in a breeze & deliver with confidence.

The `With FontLab, you ...` frame carries five of the thirteen openers. The one flourish a piece is allowed is spent here, in sentence one, so the rest of the page can be flat: "With FontLab, you're the maestro of your glyph orchestra." Spend it early or not at all.

Then paragraph two, without exception, is a dense capability block: four to six imperative sentences naming real tools, run together with no connective tissue.

> Rapidly build glyphs from components or from always-editable element references. Automate complex glyphs with Auto layers. Join design parts and add flair with Skin and Glue. Convert drawing parts into components with one click.

Five sentences, five tool names, zero transitions. Do not add transitions.

## Sections

A heading is followed immediately by the mechanism. There is no section-opening prose, no preview of what the section covers. Where an orienting sentence exists, it is a definition or a location.

For anything that changed, the standard opening is the old state:

> Previously, harmonized dragging was only available on macOS.

That frame appears 14 times in the essays. It is the house's only comparison device, and it needs a documented before-state. If your source is one manual with no changelog, state the current fact directly rather than inventing a previous version to compare against. Do not reach for Before and After, The old way and The new way, or Today versus With FontLab: those appear zero times in 76,000 words.

## Stating a change

Condition or location first, then the behaviour, then the benefit welded on with "so you can". The subject is FontLab or you. The tense is present. The change is a fact about the current build, not a benefit statement.

> When you choose Tools > Commands & Shortcuts or press Shift+Cmd+P, the Commands & shortcuts dialog now opens as a compact popup, so you can type a substring of a menu command and choose it from the list.

Never give the benefit its own sentence. "This means you can spend less time on setup and more time designing" is not this voice. Weld it, or drop it.

Rationales are short. Four words is typical: "to reduce visual noise".

## Fixes and limitations

State a fix as the symptom the reader saw, then the cause if it is worth having. State a limitation flat and unhedged, and never convert it into a positioning. "TransType does not export a new variable font" must not become "TransType focuses on static output".

## The ending

Zero of thirteen essays end with a summary, a recap, or a call to action. The correct ending is the last technical fact, including something as flat as "Numerous additional fixes for problems reported by users."

If your draft ends with a paragraph that adds no new fact, delete that paragraph. It is the single most reliable machine tell in this register.

## Conventions this register uses

Interface labels take italics: choose _File > Add Instance_, turn on _Install Fonts_ in the _Destination_ dropdown. Table names, extensions and settings keys take code style: `gvar`, `.woff2`, `COLR`, `CFF2`. Prices carry both currencies against one number when the number is the same: "€$ 99".

An announcement for a release that ships localization may open in the languages it now speaks. That is a greeting, not a translated paragraph, and it is followed immediately by the English sentence that does the work.

## What to protect

An editor's instinct will remove these. They are the voice.

- **Exclamation marks.** Seventeen across the essays, and about one per 400 words in overview and announcement prose. "Have fun!" is a real house heading.
- **The rule of three.** Not a machine tell here: it is the house signature, at 7.6% of marketing sentences and common in overviews. "Create. Develop. Complete. Deliver."
- **The bare ampersand** in headings and lists: "Explore & prepare", "find & fix imperfections".
- **Long enumerating sentences.** "Dynamically snap to zones, guides, hints, nodes, angles, stem distances, continuation lines, perpendicular lines and centerlines." Leave it whole.
- **Self-undercutting asides.** "it's up to you!", "this is just a suggestion", "so it's a bit of a chicken-and-egg problem".
- **Issue numbers, build numbers, version strings, menu paths.** These are the load-bearing specifics.
- **One travelling idiom per document,** and no more: "ship in a breeze", "has your back", "workhorse".
- **Small roughness that carries rhythm,** including the occasional comma splice. Fix a typo if asked. Do not rewrite the sentence around it.

## Hard limits

- No invented adoption numbers, benchmark figures, or customer counts. Use a placeholder.
- No implied endorsement. "Trusted by" needs names and permission.
- Never describe a fix as complete when the source says partial, and never drop a known issue.
- Never open with "We are excited to announce", and never open with a version number alone.
- No unanswered questions. A question answered in the same line is a house device, in body copy as much as in a heading: "Need more? Get a lifetime licence." "Bought TransType 4 in 2026? Your upgrade is free." Ask and answer, or do not ask.


## Before you return the draft

Count these. Do not estimate them.

1. **Dashes.** The corpus runs 0.19 per 1,000 words in this register, which for a 1,000-word piece means zero or one. If you have more than one, replace each with a colon, a comma, or a new sentence.
2. **Second person.** Count the words you, your, yours. Aim for at least 8 per 1,000 words; the corpus averages 19. This is a register target, not an authorship test: the AI-written pages score as highly on it as the house does, so hitting it proves nothing on its own.
3. **The last paragraph.** Does it add a fact? If not, delete it.
4. **Benefit clauses.** Search for "This means you", "allows you to", "makes it easy to". Weld each to its mechanism with "so you can", or cut it.
5. **Placeholders.** Every specific you could not source is visible in the text, not silently omitted.

## When the input is an existing draft

Keep the facts, the order, and the headings. A release note is read beside its predecessor, so restructuring costs the reader more than it gains. Fix the register, not the shape. If the draft ends with a summary paragraph, that is the one structural change worth making.

## Output

Return the piece, starting at the first line. Then, only when needed, short labelled lines: `Verify` for facts needing confirmation, `Placeholders` for how many and where, `Cut` for anything you removed that the writer may want back.

## Related skills

`fontlab-marketing` for copy that sells. `fontlab-technical` for procedures and reference pages. `fontlab-terminology` for names and terms. `fontlab-localization` for text headed to translation.

Worked pairs: `references/moves.md`.

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
