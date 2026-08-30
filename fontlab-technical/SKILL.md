---
name: fontlab-technical
description: >-
  Write and edit technical prose for FontLab and Vexy products: user manuals,
  reference pages, procedures, how-to steps, getting-started guides, help-centre
  and troubleshooting articles, tooltips, help-panel blurbs, API and scripting
  documentation, and concept explanations. Use it whenever the output tells a reader how something
  works or what to do next, including in-app help strings. Routing: any piece containing numbered
  steps belongs here whatever else it is. For release notes, what's-new pages and announcements use
  fontlab-neutral. For copy that sells use fontlab-marketing.
license: MIT
metadata:
  version: "1.0.0"
  family: fontlab-writing
---

# FontLab technical writing

## What the reader is doing

The reader is not reading. The reader is holding a mouse in one hand, has a
half-drawn glyph on screen, and has come here to unblock one action. They will
scan, take the one line they need, and leave. Everything you write is judged by
how fast that happens.

So the writing has two jobs that pull apart, and this skill keeps them apart.
Steps must be executable without interpretation. The prose around the steps must
be worth reading by a person who already knows the product exists. Four
influences are combined here, each doing one job:

- **ASD-STE100 Simplified Technical English** governs steps. Mechanics only.
- **Stephen King's advice in *On Writing*** governs prose. Concepts and
  troubleshooting narratives only.
- **The Apple Style Guide and the Microsoft Writing Style Guide** govern how
  interface elements are named and how a reader scans a page.
- **The house corpus** governs everything else, and wins every tie about voice.

A note on STE, stated once and honestly. ASD-STE100 is a controlled language
written for aircraft maintenance manuals: a fixed dictionary of about 900
approved words, each with one approved meaning, plus about 65 writing rules. We
are not compliant with it and do not claim to be. We take the discipline, not
the certificate. Where a rule below cites STE, it means "STE has a rule here and
the rule is good", never "the house standard is ASD-STE100".

## The four shapes

Decide which shape you are writing before the first sentence, because the rules
below apply per shape, not per document. A long page contains several shapes and
switches between them at a heading.

| shape | the reader wants | the test |
|---|---|---|
| **Procedure** | to do a thing now | can it be numbered? |
| **Reference** | one fact, exactly | would a table hold it? |
| **Concept** | to understand a model | does it answer "why does it work that way"? |
| **Troubleshooting** | to recover | does it start from a symptom the reader already has? |

If you cannot tell, ask what the reader has on screen. A dialog open and a
decision pending is a procedure. A field they cannot name is reference. A result
they did not expect is troubleshooting. A tool they distrust is concept.

Tooltips and help-panel blurbs are reference at 15 words. Scripting and API
documentation is reference plus one concept paragraph on the object model.

## The STE layer: steps

These apply to a numbered step, to an imperative instruction inside prose, and
to nothing else.

1. **One instruction per sentence.** Two actions in one sentence is two steps.
2. **Start with the verb.** "Click ==Apply==", not "You should now click Apply".
3. **Cap a procedural sentence at 20 words**, and a descriptive sentence inside
   a procedure at 25. This cap does not leave the step and does not govern the
   prose around it.
4. **Active voice, present tense, simple present.** "FontLab rebuilds the
   glyph", not "the glyph will be rebuilt".
5. **One word, one meaning.** *Select* means to add to a selection.
   *Choose* means to pick a menu command. *Set* means to give a value. Do not
   use *select* for a menu, and do not use *choose* for a checkbox.
6. **No ambiguous participles.** "Using the Contour tool, the nodes move" has no
   actor. Write "With the ==Contour== tool active, drag the node."
7. **Condition first, action second.** "If the panel is closed, press
   ++Shift+F1++." STE puts the condition where the reader can abandon the step
   before performing it.
8. **Name the actual thing.** A menu path, a key, a panel, a value, an issue
   number. Never "the appropriate option".
9. **No noun clusters over three.** "Variable font instance export dialog
   preferences" is not a name; find the real label.
10. **Warnings before the step, never after.** A consequence the reader cannot
    undo is announced first.

## The King layer: prose

These apply to concept explanations and to the narrative half of a
troubleshooting article. They do not apply to steps, tables, or reference rows.

- **The reader is a friend you are telling something to.** Not a student, not a
  buyer. You already know the answer and you are saving them the afternoon.
- **The road to hell is paved with adverbs.** An adverb propping up a verb is a
  symptom: the verb is wrong. "Moves smoothly" wants a better verb or a number.
- **The story is the boss.** In documentation the story is the mechanism. If a
  paragraph does not advance the reader's model of how the thing works, it is
  not a weak paragraph, it is a paragraph about nothing.
- **Cut ten percent.** Second draft equals first draft minus ten percent. Apply
  it to prose only; cutting ten percent of a step list deletes a step.
- **Write with the door closed, rewrite with the door open.** Draft for
  yourself, at speed, in one register. Then reread as the reader who has the
  half-drawn glyph, and cut everything they would not stop for.

Two places King must be overruled, and the corpus overrules him.

**No opening scene.** King opens on a person in trouble. Every one of the
thirteen house what's-new essays opens on a flat declarative whose subject is
the product or you. Keep that. The mechanism starts in sentence one.

**No closing beat.** King ends on a turn. Zero of the thirteen essays end with a
summary, a recap, or a call to action; the last sentence is the last technical
fact, and three of them end on a restriction. A terminal paragraph that adds no
new fact is not house prose. Stop when the facts stop.

## Interface conventions

From Apple and Microsoft, reconciled against what the house actually ships.

- **Second person, present tense.** "You can specify", "press", "drag". The
  reader is the actor of every action; the app is the actor of every response.
- **Sentence case in every UI reference, heading, and label** you write. Match
  the interface string exactly when you quote one, even if it is title case.
- **Menu paths run in one string with a greater-than sign** and the house
  highlight marker: `==Tools > Commands & Shortcuts==`. Never "the Tools menu,
  then the Commands item".
- **Keys use the house key notation** and carry both platforms where they
  differ: `++Shift+Cmd+P++` for macOS beside `++Shift+Ctrl+P++` for Windows.
- **The verb tells the reader which input to use.** *Choose* a menu command.
  *Click* a named control: a button, an icon, a tab. *Press* a key. *Drag* a
  node, a handle, a panel edge. *Turn on* and *turn off* a toggle or a
  checkbox; never "check" or "uncheck". *Select* glyphs, nodes, and text.
  Microsoft prefers input-agnostic *select* everywhere and Apple prefers *click*
  plus *choose*; the house sides with Apple, and the corpus is consistent about
  it across tens of thousands of words.
- **Name the element by its class**: panel, property bar, window, dialog, pane.
  These are not interchangeable in FontLab and readers use them to navigate.
- **Bold is for emphasis inside marketing prose, on verbs.** In technical prose
  a UI string carries the highlight marker instead, and bold is left alone. Two
  emphasis systems on one line make neither readable.
- **Write for scanning.** A heading every screenful. A list where there is a
  list. The fact in the first half of the sentence. No paragraph opening that
  previews what the section will cover: a heading is followed by the mechanism.

## The metaphor budget

The house voice permits exactly one image per H2 section, and spends it early.
Rules, all of them hard:

- One vehicle per image. A workhorse does not later shine, and an orchestra does
  not have a back.
- Two sentences maximum, and it does not recur after that.
- Never inside a numbered step, a warning, a limitation, or a reference table.
- It is a metaphor of work, not of feeling. "Workhorse", "maestro of your glyph
  orchestra", "ship in a breeze" are house. "Delightful", "effortless",
  "magical" are not, because they assert how the reader feels.
- If the section has no natural image, it gets none. The budget is a ceiling,
  not a quota.

## Hard limits

- Never invent a menu label, shortcut, default, version, metric, or issue
  number. Missing specifics ship as a visible placeholder such as
  `[CONFIRM LABEL]`.
- Never convert a limitation into a positioning. State what the product does not
  do, in the same sentence weight as what it does.
- No rhetorical question in body copy. A question is a real FAQ heading or a
  two-word audience tag answered in the next breath.
- No sentence asserting the reader's emotion or workload.
- No comparison scaffold. The house change frame is "Previously, ... now ...".
- Steps obey the 20-word cap. Prose does not: an enumerating sentence naming
  nine snap targets is correct at 40 words, and shortening it loses the list.
- Do not merge single-sentence paragraphs. A paragraph carrying one fact is
  finished.

## When the input is an existing document

1. **Read it whole before editing anything.** Mark where each of the four shapes
   starts and ends. Most bad house documents are one shape wearing another's
   clothes: a concept explanation numbered as steps, or a procedure buried in a
   paragraph.
2. **Fix the shape first.** Renumbering and resplitting fixes more than
   rewriting does, and it does not touch the author's voice.
3. **Then apply the layer that matches each span**, and only that layer. Running
   the 20-word cap over a concept paragraph destroys the register.
4. **Verify every specific against the source.** Menu labels get renamed between
   versions; an old label in a new document is worse than no label.
5. **Reread as a skeptic.** What still reads as machine-written? Then check what
   you quietly removed: exclamation marks, a tricolon, a self-undercutting
   aside, an issue number, an ampersand in a heading.

If the document is already correct, say so and change nothing. An edit pass that
must produce a diff will produce a worse document.

## Output contract

- Return the document, in Markdown, complete. No preamble, no summary of what
  you changed unless asked.
- Preserve every UI string, code span, path, identifier, URL, and table cell
  exactly.
- Placeholders in brackets for every fact you could not verify, listed once at
  the end under a short heading if there is more than one.
- When editing, keep the author's headings and heading level unless the shape
  changed.
- State the shape of each section in your own head, not in the document.


## Before you return the draft

Count these. Do not estimate them.

1. **Dashes.** Reference and procedural prose in the corpus is effectively dash-free, at 0.3 per 1,000 words. The commonest slip is a pair of dashes around a list inside a sentence: use a colon, or parentheses, or split the sentence. Aim for zero.
2. **Second person.** Count the words you, your, yours. Aim for at least 5 per 1,000 words. Apple and Microsoft both write to the reader, and so does the house corpus, at 19 per 1,000. A procedure written in the third person reads as a specification, not as help.
3. **The last paragraph.** Does it add a fact? If not, delete it.
4. **Benefit clauses.** Search for "This means you", "allows you to", "makes it easy to". Weld each to its mechanism with "so you can", or cut it.
5. **Placeholders.** Every specific you could not source is visible in the text, not silently omitted.

## Related skills

`fontlab-neutral` for release notes and general product prose, `fontlab-marketing`
for landing pages and campaign copy, `fontlab-terminology` for the term list and
product naming, `fontlab-localization` for text that will be translated.

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
