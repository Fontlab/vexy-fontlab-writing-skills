<!-- this_file: fontlab-localization/references/memories.md -->

# Memories, glossaries and machine drafts

*Portable copy of the FontLab writing guide's localization page of the same name, snapshot of 28 September 2026. The live page and the term tables it links to are in the `vexy-fontlab-writing-styleguide` repository; use newer supplied project data when it disagrees.*


Every FontLab language has a core memory and, once its catalog has been
reviewed, a project memory. This page says what each is for, how a match is
judged, how a glossary entry is written, and what a machine or model draft may
and may not do. The rules come from the localization literature the company
keeps and from the FontLab 9 review; the principles say where
the files live.

## Two memories, two jobs

The **core memory** (`<code>-core.tmx`) fixes concepts. One unit per glossary
term, with the English term, the translation, the status, the definition and a
note. A translation engine receives it as a glossary: a hint on how to render
the term inside any sentence, inflected as the sentence requires. It changes
slowly and by decision.

The **project memory** (`<code>-fontlab-ui.tmx`) recycles whole strings. One
unit per reviewed FontLab message. When a new catalog contains a source string
that matches a unit verbatim, the reviewed translation is reused without
asking anyone. It changes with every review and decays if nobody prunes it.

A term lives in the core memory only. A build fails if a core source segment is
repeated in the project memory, because two answers for one string is how a
memory starts contradicting itself.

## What a match is worth

A verbatim match of the whole string, in the same context, is reused as it is.
A source change that alters the behavior, values or audience reopens review even
when the words match. Check the message contract, source
revision and current terminology decisions before carrying approval forward.
A verbatim match of the string in a different context is a proposal: *Close*
on a button and *Close* as a path state are different words in German.

A fuzzy match is a draft, never an answer. Judge it by meaning, not by score:
a string that shares most of its words with the new one can describe a
different action. In German and Polish an identical English phrase can need a
different case depending on whether it is subject or object, so a high score
can carry the wrong ending. Fix the difference, and put the corrected pair
back into the memory; a memory that is not fed the final text goes stale.

Prefer an exact match whose neighbours also match when translating running
text such as help topics. A sentence match with different neighbours can
break the coherence of a paragraph.

Leverage only what meets today's quality bar. When an old translation is bad,
retranslating is cheaper than repairing it, and the ledger
records the replacement rather than the patch.

Keep the memory's metadata when exporting: creation date, who translated, who
reviewed, and how often a unit was used. They are what lets someone prune the
memory later without rereading it.

## Writing a glossary entry

Use the language's appropriate citation form: often a singular noun or an
infinitive, but a fixed phrase, plural-only term or language without that form
needs its own treatment. Record a multiword term as its own
entry; the translations of *kerning* and *class* do not compose into the
translation of *kerning class*. Record the short form a dense panel uses as a
variant of the entry, so every panel abbreviates the same way.

Establish an equivalent by research, not by translating the word. A proposed
equivalent counts when target-language references attest it: the type-design
literature, the localized competitor, the platform glossary. A poorly
translated website is not attestation. The audience decides whether a term
stays English: an established professional loan (*Kerning*, *Master*,
*Hinting*) is correct; an unattested calque (*kreieren*, *supporter*) is a
terminology error even when a reader would understand it.

Coin a frequent new term at the start of a language, with a context sentence
for the reviewer. Fixing it after variants have spread costs a second review.
Push a changed term into the core memory the same day; a decision that lives
only in a chat message is not a decision.

An extracted or statistically aligned term is a candidate. Frequency and a
high alignment score cannot establish the concept or its preferred translation.
Review the context and evidence, then use the existing proposal and approval
states. After a decision changes, regenerate the exports and identify the
translations that used the superseded form.

When combining term lists, compare the definitions and usage contexts before
merging entries. Identical English spelling can name different concepts. Keep
those senses distinct and preserve their evidence and review state; neither a
UI extract nor an index entry is automatically an approved general term.

When comparing usage, choose material for the same professional audience, kind
of text and task. Record its origin and date. Repeated navigation or copied
passages can make a word look common without providing independent support.
Inspect the actual examples before treating a frequency count as evidence.

Glossary lookup and omission checks must understand inflection, or they stay
silent in German and Polish. A check that matches only the dictionary form
reports a missing *Kerning-Klasse* whenever the text says *Kerning-Klassen*.

## Machine and model drafts

FontLab uses a translation engine driven by a large language model, fed the
core memory as glossary and the project memory as cache. The draft is a draft.

- **Declare the editing level before work starts.** Full post-editing for UI
  and help, which ship and live for years. Nothing lighter reaches a catalog.
- **Pin the prompt, the model and the settings** and record them beside the
  output. Model output varies between runs; a review that cannot name what it
  reviewed cannot be repeated.
- **Compare against the source, not against fluency.** A fluent draft hides
  omissions, shifted conditions and invented specificity. Read the English
  first, then the draft.
- **Send only relevant glossary entries with each batch.** A glossary of two
  hundred terms attached to a ten-string batch drowns the terms that matter.
- **Rotate reviewers.** After long exposure to machine phrasing an editor stops
  seeing it. A fresh pair of eyes reads the last pass.
- **Mine the diff.** The recurring edits between draft and final text are the
  next core-memory entries or the next post-processing rule. Fix a systematic
  error at the source of the draft, not by hand in every string.
  Test any automatic replacement on both intended matches and valid
  counterexamples; a recurring edit is not sufficient evidence for a global rule.
- **Do not draft marketing from one suggestion.** A single proposal steers the
  wording and lowers the range of what the writer considers. Draft prose by
  hand or from several candidates.
- **Use quality estimation to triage, not to approve.** A score can point the
  reviewer at risky strings. It cannot say that a string is right.
- **Check the provider's data terms** before sending unreleased strings. A
  tool whose terms allow retention or training conflicts with the release
  schedule and with the confidentiality FontLab owes its own roadmap.
- **A machine can help with context.** Asking a model what a short string most
  likely labels, or whether a draft follows the style guide, is a sound use.
  The human still decides.

There is no quota of machine wording to retain. Replace an unusable suggestion
when rewriting gives a clearer, accurate result. After comparing with the source,
read the target alone and in the assembled document. Edit distance describes
surface changes; it does not measure all the effort or establish quality.

## Update cycles

A delta needs an identified source revision and a plan for review. Agree when
new material is ready for translation and how updates will be grouped. Choose
the update method from the actual changes to meaning, resource identity,
structure and context. A percentage of changed strings cannot tell whether a
small patch is safe. Preserve reviewed work, review affected dependencies and
check the assembled result even when only a few strings changed.

A string freeze gives reviewers a stable source but can delay source repairs.
Agree the date and how necessary fixes will be handled. Freeze UI
terminology after the translator has seen the strings in the running build,
before finalizing help, manuals and screenshots that quote the labels. If those
tasks begin earlier, mark provisional references and reconcile them with the
reviewed interface before delivery.

Feed late fixes into the reviewed catalog, then regenerate its project memory.
Update terminology through the core memory's decision process. A correction
made only in an exported file can disappear at the next regeneration.

## The upgrade of a catalog

When a new build regenerates the catalog, the reviewed one is not thrown away.
The upgrade tool ports every translation whose context, source and comment
are unchanged, marks near-identical strings as needing review, sends the rest
through the engine with the core memory as glossary, writes the retired
messages to a separate file so nothing reviewed is lost, and reports the counts
of each category. The review then reads only what changed. The command and its
report format are documented in the `vexy-localizzy` repository.
