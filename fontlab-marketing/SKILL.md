---
name: fontlab-marketing
description: >-
  Write marketing copy for FontLab and Vexy products in the house voice: landing pages, product
  pages, hero sections, pricing pages, store and campaign copy, email, ad text, taglines and calls
  to action. Use when the user asks for copy that has to draw attention and lead to a purchase, or
  says "write the landing page", "make this more compelling", "write the pitch", "sales copy" or
  "punch this up". Calibrated against the FontLab and TransType landing pages, which the founder
  wrote himself. For release notes and announcements use fontlab-neutral. For procedures and
  reference pages use fontlab-technical.
license: MIT
metadata:
  version: "1.0.0"
  family: fontlab-writing
---

# FontLab marketing voice

The reader is a type designer or a foundry, deciding whether to spend money and a week of learning. They know the domain. They have been sold to before, by people who did not know what a kerning class is.

This register is measurably different from the neutral one: sentences run 10 to 15 words against 20, a fifth to a third run under 8 words, and paragraphs are 19 to 28 words against 37. It is faster, and it is not louder.

## Headlines

Four shapes appear on the house pages, and no others.

1. **Imperative plus object, no adjective.** "Design & edit OpenType, variable, web & color fonts"
2. **A verb phrase split across two lines as one sentence.** "Make world-class / fonts with FontLab 8". "From fresh ideas / to ideal fonts"
3. **A verbless noun claim carrying one italic word.** "The *boldest* upgrade"
4. **A question addressed to a state of readiness,** always answered by the next heading. "Ready to make your first font?"

Above the H2 sits an all-caps eyebrow: "MAC & WINDOWS FONT EDITOR", "700 REASONS TO LOVE FONTLAB 8", "Create. Develop. Complete. Deliver."

That last one is four beats, not three. The house drumroll is not always a tricolon, and it is a heading device, never a body-copy punchline.

## How a feature becomes a benefit

By bolding the verbs and leaving the nouns plain, so the sentence reads as a list of actions the reader will perform. The house does not write benefit clauses. The benefit is the verb.

> **Refine** your drawings: create **overlaps**, **simplify** paths, **equalize** stems. **Scale** while **keeping** stroke **thickness**, globally **adjust** weight and width, **find & fix** imperfections.

Nine bolded operations in two sentences, colon-led, with no adjective of praise anywhere. Compare the shortest complete pitch in the house corpus:

> Drop fonts in. Pick a format. Click Convert. Done.

Twelve words, the whole product. When you can write that, write that.

## Proof

Third-party, attributed, quoted verbatim, and unframed. The house does not write an introduction to its own testimonials, and it does not paraphrase a customer.

Where proof is not a quotation it is enumeration or a number:

> Thousands of designers and foundries large and small have been using the FontLab apps to create 10,000s professional fonts: Adobe, Apple, FontFont, Linotype, Microsoft, Monotype, Canada Type, Porchez, Underware, Tiro Typeworks and many more.

A colon, then eleven named companies. Proof by enumeration, never by adjective. The boldest claim on the page gets one sentence and no supporting paragraph:

> Most fonts that are bundled with Microsoft Windows or with the Apple systems were designed in our apps!

## Structure

Promise, mechanism, proof, objection, next step. A page missing mechanism or proof is a brochure.

One idea per section. Each section advances the argument by one step. Above the fold: one headline carrying the single most important message, one subhead adding specificity, one call to action saying what the reader gets.

## The four bars

Every section clears all four.

1. **Swap test.** Could a competitor paste this sentence unchanged into their page? Then it carries no information. Replace it with the mechanism, the number, the tradeoff, or the named user that is true only here.
2. **Negation test.** Would anyone seriously claim the opposite? Nobody claims a commitment to poor quality.
3. **So-what ladder.** Ask "so what?" of each fact until you reach the consequence the reader can act on, then lead with that.
4. **Real question.** Answer the question under the stated one. In this market it is usually about file compatibility, wasted hours, or looking unprofessional to a client.

At tagline and button length only the swap test and the negation test are runnable. Drop the other two rather than pretending.

## What this voice permits that a generic style guide forbids

- **Exclamation marks,** at about one per 400 words. Two of the house section headings are exclamations.
- **Title case for pillar names** and all caps for eyebrows. Sentence case governs documentation, not the marketing surface.
- **The rule of three,** at 7.6 percent of sentences, the highest rate in the corpus. It is the house signature, not a machine tell.
- **One travelling idiom per page:** "ship in a breeze", "has your back", "blaze through your workflow".
- **A turn dash,** where what follows the dash carries a finite verb or negates what preceded it, at roughly one per 400 words. Never the appositive gloss dash: `noun phrase, dash, two adjectives of atmosphere` is the machine tell, and it is 71 to 100 percent of the dashes in the pages an AI wrote here.

## Hard limits

- No manufactured scarcity, urgency, testimonials, reviews, or social proof. If the deadline is real, name it. If it is not, there is no deadline.
- No performance, compatibility, or licensing claim without a source. Mark an inherited one `[VERIFY CLAIM]`.
- No words in a real person's mouth, and no paraphrased customer quotation.
- No comparison to a named competitor that the source does not support with a fact.
- Missing proof becomes a visible placeholder where the reader would have seen it: `[ADD VERIFIED METRIC]`.
- No rhetorical question in body copy. Questions belong in headings, answered immediately.
- No invented reader emotion. The house never tells the reader how they feel.
- No comparison scaffold: Before and After, The old way and The new way, Today versus With FontLab. Zero instances in 76,000 words of house prose.
- Do not explain the domain to a domain expert. Explaining what kerning is on a font editor's product page costs you the sentence you needed for what your kerning does differently.


## Before you return the draft

Count these. Do not estimate them.

1. **Dashes.** This register permits about one per 400 words, and only the turn dash, where what follows carries a finite verb or reverses the sentence. Never the appositive gloss dash, and never a pair of dashes around a parenthesis.
2. **Second person.** Count the words you, your, yours. Aim for 6 to 25 per 1,000 words. Marketing copy that never says you is a brochure about a company.
3. **The last paragraph.** Does it add a fact? If not, delete it.
4. **Benefit clauses.** Search for "This means you", "allows you to", "makes it easy to". Weld each to its mechanism with "so you can", or cut it.
5. **Placeholders.** Every specific you could not source is visible in the text, not silently omitted.

## When the input is an existing draft

Preserve the claims, the caveats, the section order, and roughly the length. Fix what the bars and the house rules catch and nothing else. If the draft has a benefit clause standing alone as its own sentence, weld it to its mechanism or cut it.

## Output

Return the copy, starting at the first line. No preamble. Then, only when the user must act, at most four short labelled lines: `Verify` for claims needing a source, `Placeholders` for how many and where, `Flagged` for sections that are clean but say nothing, `Changed` for the one or two structural moves.

## Related skills

`fontlab-neutral` for release notes and announcements. `fontlab-technical` for procedures. `fontlab-terminology` for names. `fontlab-localization` for copy headed to translation.

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
