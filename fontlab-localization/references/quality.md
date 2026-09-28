<!-- this_file: fontlab-localization/references/quality.md -->

# Quality: what a review measures

*Portable copy of the FontLab writing guide's localization page of the same name, snapshot of 28 September 2026. The live page and the term tables it links to are in the `vexy-fontlab-writing-styleguide` repository; use newer supplied project data when it disagrees.*


A review can only measure against a specification it was given. This page
fixes the specification for FontLab and Vexy translations: the error types,
their weights, the passes a release goes through and the checks a script can
run. The ledger rules say how a
finding is recorded; the runtime review says how the
running application is checked.

Before review, identify the intended readers, their tasks, the delivered formats
and the evidence needed for acceptance. Agree how disagreements will be resolved.
A translator, product specialist and user may notice different problems; a vote
does not replace checking the disputed meaning against the working product.

## Levels and passes

Record a localization level per language, separately from the review tier in
the roster. *Enabled* means the application accepts the language's input while
the interface stays English. *Localized* means the interface and the Help Panel
are translated. *Adapted* means sample texts, tutorials and language tools are
rewritten for the culture. Tier A in the roster describes review depth; the
level describes scope. Both are written down so "done" means one thing.

Record support per feature as well. Input, search, sorting and language tools
can have different coverage; none of these levels proves that every feature
supports the language. State the tested build and any known limits.

A release runs four passes, each with its own sign-off:

1. **Linguistic.** Every string, including text inside images and hidden
   accessibility strings, read against its source by a proficient reviewer.
2. **Cosmetic.** Rendering: clipping, wrapping, mnemonics, fonts, diacritics on
   capitals at tight line heights, right-to-left mirroring where it applies.
3. **Functional.** Nothing the localization touched has stopped working:
   shortcuts, parsers that read localized numbers, file dialogs, help links.
4. **Accessibility.** Screen-reader names and descriptions are translated and
   agree with the visible labels.

Run ordinary functional cases with international data from the start, including
text supplied indirectly by a profile, path or imported file. Reuse relevant
cases across supported configurations and retain earlier failures as regression
cases. A localized interface and multilingual document support are separate
capabilities; test their interaction rather than certifying one from the other.

Functional testing is easy to score and tends to crowd out the linguistic pass.
Keep the linguistic sign-off separate and name who gave it.

Repeat the relevant cases against the actual delivery package in its supported
environment. A development copy can find fonts, catalogs or help files that an
installed copy lacks. Include installation, upgrade and removal where the brief
requires them; removal must follow the product's policy for retaining user data.
Record the configurations tested and the checks deferred. A signed checklist
establishes responsibility, not coverage beyond the evidence attached to it.

## Error types

Every ledger reason belongs to one of the house categories below. These draw
on [MQM's error typology](https://www.themqm.org/mqm-pillars/the-mqm-core-typology/);
the groupings, examples and weights here define this review's specification.

| Family | Examples in a FontLab catalog |
|---|---|
| Accuracy | omission, addition, mistranslation, untranslated text, invented specificity (*anchor cloud* for *cloud*) |
| Terminology | wrong term, term inconsistent with the core memory, one concept rendered two ways |
| Linguistic conventions | grammar, spelling, punctuation, register, wrong case after a placeholder |
| Locale conventions | number and date format, quotation marks, key names, units, measurement labels |
| Style | wording that is correct and reads as a translation, headline style not applied |
| Compliance | a platform command that does not match the localized operating system, a dialect mixed into another variety |
| Design and markup | broken placeholder, tag or escape, clipped label, duplicate mnemonic |
| Audience | a native word where professionals expect the loan, or a loan where the audience needs the word |

A preferential edit, such as a synonym the reviewer likes better, is recorded
with severity *null* so the ledger shows the change without counting it as an
error. An established professional loan is not a terminology error; an
unattested calque is.

## Severity

| Severity | Weight | Meaning |
|---|---|---|
| Critical | 100 | The user is misled or the software misbehaves: a wrong action name, a placeholder that breaks, a legal text that changes meaning |
| Major | 10 | The user notices and is slowed: a wrong term, a clipped label, a grammar error in a visible control |
| Minor | 1 | Noticeable to a careful reader, harmless: a spacing error, an inconsistent short form |
| Null | 0 | A preferential change |

A release ships with no critical findings open and with every major finding
either fixed or accepted by name. A count of minors is a planning figure, not a
gate.

Apply severity to the consequence in context. Record what the reader could
misunderstand or fail to do; the category alone does not establish the impact.
For example, a clipped final word can hide a destructive action's scope, while
clipping an optional explanation may leave that same task understandable.

## Checks a script runs

Automated checks compare tokens; they cannot approve language. They run before
a human reads anything, in both directions where the rule is symmetric:

- missing or empty target; untranslated target identical to a source that is
  translatable
- placeholder set, order constraints, `%n` presence in every numerus form
- tag and markup count; escapes; leading and trailing whitespace; ellipsis
- mnemonic count per label and duplicate mnemonic letters per context
- length ratio far outside the language's expected range, and any target
  longer than the source in a panel with a length cap
- two source strings in one context sharing one target
- one source string with two targets across the catalog
- core-memory terms present in the source and absent, in any inflected form,
  from the target
- a target that reintroduces a term the core memory retired
- non-translatable strings that changed: tags, glyph names, paths, identifiers
- diacritics not in NFC; presentation-form ligatures
- labels quoted in the Help Panel and the manual that do not match the catalog

Bilingual conditional rules catch false friends: forbid a target phrase only
when the source contains a given word. Tune the rules per project; a noisy rule
gets switched off and then catches nothing.

Treat automated hits as findings to inspect. An unchanged product name or a
valid inflection may be correct. Preserve the reason for an exception so that
the next run does not silently suppress a different defect.

Check catalog and message syntax with their actual parsers as described in the
message contract. Matching tag counts cannot prove valid
nesting. Give prose checkers the translatable text while preserving its mapping
to the source; check the markup separately rather than deleting its semantics.

## Roles in a review

Assign reviewers by their language, product and subject knowledge. Define each
pass's scope: a market reviewer may check audience suitability, an editor may
check meaning and terminology, and a proofreader may inspect the final layout.
None should ignore a meaning defect because it falls outside that pass. Record
it and send it to the person who can resolve it.

Keep the pre-edit version and distinguish a needed correction from a preferred
synonym. Let the translator see the reasons for accepted edits. Correct the
maintained source, regenerate the affected output and check the result there.
Rerun spelling and structural checks after changes. A repeated problem belongs
in a shared findings list; promote it to a terminology decision only after the
concept and proposed remedy have been reviewed.

## Sampling and triage

Send reviewers first to the strings that look least like the approved
translations: new contexts, long strings, strings with placeholders, strings
the engine drafted without a memory match. Record the sample's selection,
size, source revision and exclusions. A sample or corpus-level score cannot
certify every string. Back-translation can raise questions, but it introduces
another translation and cannot by itself establish accuracy; a proficient
reviewer resolves the meaning against the source and product context.

Stop a review early when its first pages fail. A catalog whose first hundred
strings show a systematic error is fixed at the source of the error, then
reviewed again, rather than corrected string by string.

## Defects that are not translation defects

Keep translation defects and localization defects apart in the ledger. A
clipped label the translator could not see is a layout defect. A string that
should never have been translatable is a source defect. A mnemonic collision
with a runtime-inserted item is an engineering defect. Each goes to its owner
with a tracked lifecycle: found, reported, fixed, regression-tested after the
fix.

Record the build, language settings, starting state, actions and observed result
before assigning a cause. Include the expected result and its basis. A screenshot
can show missing text; it cannot establish whether the catalog, resource lookup
or layout caused it. Mark an untested explanation as a hypothesis and retain the
reproduction steps when the finding moves to another owner.

Report an intermittent failure even when it cannot yet be repeated. Retain the
observed conditions and attempts to reproduce it, and mark that uncertainty.
Keep impact, investigation status and release disposition separate: accepting
a known issue for a release does not mean that it was fixed. Verify a fix with
the original case in the corrected build before closing the finding.

## Text that needs another reviewer

For license terms, warranties, notices and regulated claims, have the responsible
owner specify the required translation, adaptation and qualified legal review
for each market. A translator can identify an ambiguity or changed meaning;
language review alone does not establish legal suitability. Record the approved
source version, review responsibility and any unresolved question. Do not infer
a country's current requirements from an old localization example or silently
rewrite a claim to make it sound acceptable.

## After release

Give users a way to report a wrong term. The reports track shifting
preferences, such as anglicisms gaining or losing ground, better than any
review, and each accepted report becomes a core-memory entry with a reason.
