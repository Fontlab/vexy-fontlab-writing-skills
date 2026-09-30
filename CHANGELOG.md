---
this_file: CHANGELOG.md
---

# Changelog

## 2026-09-30: ES/FR/PL compact UI guidance

Updated the three language skills to version 1.1.0 with contextual shortening,
sentence casing, inflection, terminology and actual-menu mnemonic checks.
Regenerated all three term references from canonical core memories.
Verification: four tests, shared-rule synchronization and path checks pass.
The full editorial review remains ongoing in Proteus.


## 2026-09-30: German UI review preferences

Integrated the supplied German catalog diff: 547 translation changes after
excluding XML and location churn. German guidance now covers compact hinzu,
the synchron family and Synchronsprecher, weight/thickness/stem distinctions,
readable tool/window compounds, contextual omissions and separator wordplay.
Regenerated German terminology outputs with existing review statuses intact.
Apparent typos and partial plural edits remain evidence, not general rules.
The writing guide retains the complete before/after ledger and review scope in
`dev/german-ui-2026-09-30/`. No application catalog or dependency was changed
by this task.

Verification: 27 writing-guide tests, four skill tests, both strict site builds,
and direct TMX/table/QPH parity checks. Runtime UI review is not claimed.


## 2026-09-29: German weight and thickness

Clarified Weight as Stärke in UI strings, with Strichstärke permitted in
clarifying strings; Thickness is Dicke and Stroke thickness is Strichdicke.
Stem thickness may be translated as Stammstärke.
Removed the conflicting stroke-thickness example from the canonical German
core note and regenerated its term table and portable skill reference.
The Proteus German prompt, phrase book and i18n README carry the same rule.

Verification: 26 styleguide tests and all four skill tests pass; generated
term tables, QPH notes and the rendered AI prompt match the canonical rule.

## 2026-09-29: Follower nodes follow movement

Supersedes the earlier fan/supporter naming decision. The fallback original
term is now exactly `Follower node`, defined as physically following a leader:
a node follows the movement of neighboring key nodes under Power Nudge.
Current terms: German Folgeknoten (also the compact label; Folgeknoten X/Y),
Spanish nodo seguidor (seguidor X/Y), French nœud suiveur (suiveur X/Y),
Polish węzeł naśladowca (type label Naśladowca; Naśladowca X/Y).
Spanish already expresses physical following, so its UI and project-memory
strings are retained after review; its definition and translator guidance change.
Updated canonical fallback/definition, core notes, guides, skills, generated
term tables, project memories, application glossary and all four QPH/prompt
pairs. The DE/FR/PL application changes cover 21 catalog strings, 16 extended
helptips and three Help Panel entries per language. English source keys stay
unchanged. Dictionary links document physical senses; Folgeknoten is the house
compound and the Polish term is the user's explicit choice.

Verification: the updated meaning/target/fallback regression failed before
the data changes. All 26 styleguide tests pass; strict documentation build
and link/asset checks on 225 HTML pages pass. All four skill tests and shared
block/path checks pass. Four Qt catalogs compile. Independent baseline
comparisons verify unchanged source text, message metadata/states, unrelated
translations, English help, placeholders, markup and mnemonic counts; German
and French X/Y mnemonics remain on X/Y. All 897 phrase pairs match core TMX,
and prompt embeddings match QPH bytes. The before/after ledger and verification
counts are in `Proteus/i18n/review/follower-motion-2026-09-29.json`.

## 2026-09-29: Follower node translations

Retired the servant meaning in DE/ES/FR/PL localization. The legacy source now
maps to Anhänger-Knoten, nodo seguidor, nœud adepte and węzeł zwolennik, using
the fan/supporter meaning. Updated canonical data, current guides, portable
skills, derived memories and phrase books. English lookup keys remain stable.
Documented singular/plural and X/Y forms, with a regression for all four terms.
The application catalogs and localized help use the same terminology.


## 2026-09-29: current localization guidance

Language skills now present current rules and proposal status without stale
review-progress summaries. Corrected Polish lookup guidance, French feature
names and master usage, and shared mnemonic/collision rules. Regenerated all
four portable tables after removing superseded terms from core-memory notes
and synchronizing definitions with the current glossary. All checks pass.


## 2026-09-29: terms in the house voice and the fallback original term

`fontlab-localization` 1.2.0 adds "Choose terms in the house voice": the
fallback original term, humor and wordplay, playful Power names, plain words
for Smart features, down-to-earth terms, handyman verbs, do-not-translate with
restraint, and derivation from the chosen noun, all from the founder's reviews
in fl10n issues 133 and 146. `fontlab-terminology` 1.1.0 asks for a fallback
when proposing a coinage. The German, Spanish and French skills replace their
"product operation names stay" rule with the house-voice rule; the Polish
skill (1.1.0) carries the 29 September decisions (*trzon*, *podprogram
zecerski*, *klasa kernowa*, *interlinia*, *diakrytyk*, *jednostka unikodu*,
*kuzynostwo*, *szkicownik*, *Pędzel mocy* and the rest). The four term tables
are regenerated with a Fallback column by `export_terms.py`.

## 2026-09-28: localization knowledge and four language skills

`fontlab-localization` 1.1.0 adds three sections and three references
(interface strings, memories and machine drafts, quality) condensed from the
writing guide's new localization pages, which in turn come from eight
localization textbooks and the FontLab 9 review. Four new skills,
`fontlab-localization-de`, `-es`, `-fr` and `-pl`, each carry the language's
register, compression rules, terminology decisions, plural categories, number
and date formats, mnemonics, key names, quotation marks, false friends and a
portable term table generated by `tools/scripts/export_terms.py` from the
guide's core memories. `check_paths.py` knows the new skills; all checks pass.


## 2026-09-23: style-reference rewrite completed

Completed both passes across all 36 book chapters, 11 guide pages and nine
skills, with applicable resources and prompt variants. The last batch rewrites
balanced writing/editing, partner and terminology guidance. It adds developed
and compact examples, preserves the writer's stance and qualified judgments,
and checks a resource's use and an interface term's role. All 151 portable
glossary records remain unchanged and match their canonical fields.

The final whole-set review checks subject continuity, useful detail, cadence,
meaningful recurrence and task-specific restraint. Thirteen new direct trials
join the earlier register and TLDR trials. These are same-agent editorial
checks; no independent reader or model evaluation is claimed.

Fresh verification: strict build 7.52 seconds; 18 unit tests; local links/assets
across 212 HTML pages; 47 requested pages and 3,643 rendered text blocks;
16 exact rendered prompt payloads; all eight long-prompt component checks;
70 source/resource/evaluation files checked against all ten supplied bodies.
All skill checks, four CLI tests and both whitespace checks pass.

The Browser runtime had no available browser. HTML content and links were
verified; no visual screenshot review is claimed. Evidence and page-level
hashes are in the styleguide's `dev/style-reference-rewrite/final-review.md`
and adjacent records. The rewrite is complete locally; publication is not
claimed. No dependency changed.

## 2026-09-23: marketing and technical skills and prompts rewritten

Rewrote both skill cores, their worked cases and both variants of chapters
401–404. The marketing instructions develop a useful detail into a supported
offer; technical explanations follow an object through an operation while
keeping steps literal. Separate second passes compare direct and developed
versions, check openings against endings and preserve state at every cut.

Corrected recipient-only register routing and removed stale length and pronoun
formulas. Long prompt variants exactly match their operation instructions,
skill core, shared rules and cases. Technical variants preserve nested code
fences; the Python example was checked against official documentation and
executed with output 3. Fresh direct trials cover all four writing operations.

The final strict build completed in 7.47 seconds. All 18 unit tests and local
link/asset checks for 212 HTML pages passed. Source/render checks cover 45 pages
and 3,631 text blocks with no full-attachment 12-word overlap or source-name hit.
All 12 completed prompt payloads match their rendered text exactly. Skill checks
and four CLI tests pass. The private reviews record scope and evaluation limits.

Both passes are verified for 50 of 56 entrypoints. The balanced prompt pair,
balanced writing/editing skills, partner and terminology skills, their resources
and final whole-set review remain.

## 2026-09-23: localization skill rewritten

Rewrote localization instructions and case explanations to preserve connected
thought, tone and meaningful recurrence through natural target-language syntax.
Added an English–Polish worked proposal with a short-notice counterpart. The
second pass teaches sentence-function comparison without imposing English
sentence boundaries. Placeholders, labels, scope, terminology statuses and
review-evidence safeguards remain explicit.

Four fresh direct trials cover a Polish explanation, duration, positional
placeholders and an unknown unit. Source-overlap, name and shared-block checks
pass, as do all skill checks, four CLI tests and whitespace checks. No independent
language approval or runtime test is claimed. Public sources did not change in
this batch; the latest strict build remains the verified TLDR build.

Both passes are verified for 44 of 56 entrypoints. Six prompt chapters and six
skill cores remain, with resources, parity and final whole-set review.

## 2026-09-23: TLDR voice-preserving condensation

Rewrote the TLDR core and reference cases to preserve paragraph movement,
qualifications, delayed discoveries and recurring details. Added two evaluation
packets, now eight in total, and reviewed direct outputs with actual counts.
The three-round, six-step, fixed-20% contract and final-only output remain.

Both copied prompts match their built text; the long one matches the skill core
and reference notes. Full-reference overlap checks, all skill checks, four CLI
tests and whitespace checks pass. The styleguide’s private rewrite record holds
hashes, trials and explicit same-agent evaluation limits. No dependency changed.
Seven other skill cores and their applicable resources remain.

## 2026-09-23: reference-informed neutral voice and shared craft rules

Rewrote the neutral core and worked cases around patient observation, connected
thought, meaningful recurrence and task-sensitive rhythm. The second pass adds
private comparison of direct and patient versions using the same facts. Updated
shared rules H5, H6, H9 and H14 at their source and synchronized all nine skills.

The neutral prompt in the styleguide matches the core, shared block and cases;
both copied variants match their rendered text. Three fresh direct trials cover
search scope, a typo-only request and missing offer terms. All skill checks and
four CLI tests pass; whitespace checks pass. The styleguide stores exact hashes,
full-reference overlap checks and direct-review limits in its private rewrite
record. No dependency changed.

Eight other skill cores and their resources remain in the active rewrite.
Changing their shared block does not complete their individual work.

## 2026-09-13: partner guidance and contextual measurements

Corrected partner source paths, generated content behavior, offer verification
and asset-check limits. Updated measurement output to report contextual review
signals and removed the unsupported closing-paragraph heuristic and dash ban.
Four CLI tests and all skill checks pass. Eight other complete skills and all
shared blocks remain unchanged.

## 2026-09-13: balanced instruction parity

Updated balanced writing and editing to preserve factual timing and useful
passive wording without sentence-length quotas. The corresponding long prompts
match the skill core and bundled examples exactly. Existing checks and four
direct trial reviews pass; references and other skills remain unchanged.

## 2026-09-13: localization and terminology parity

Reconciled source preparation, placeholder handling, terminology status and
historical naming with the guide. Replaced the local term reference with all
151 current glossary entries and self-contained related links. Removed unsafe
format changes, invented facts in examples and the definition-length minimum.
Structural checks and eight direct trial reviews pass; broader parity remains
open.

## 2026-09-13: core rule reconciliation

Reconciled the shared house rules with the styleguide and synchronized all nine
skills. Updated neutral, marketing, and technical workflows and worked cases.
Removed quotas, authorship inference, unscoped claims and invented facts in
examples. Clarified measurements as diagnostics and retained literal-source
safeguards. Existing structural checks and eight direct output trials pass;
remaining skill-specific parity work is documented in WORK.md.

## 2026-09-12: shorter writing skill names

Renamed `fontlab-balanced-editing` to `fontlab-rewrite` and
`fontlab-balanced-writing` to `fontlab-write`. Updated directory names,
metadata, file-path records, evaluation identifiers, README entries, and
default path checks. Writing and editing behavior is unchanged.

## 2026-09-12: TLDR

Added `fontlab-tldr`: literary condensation at about 20% of the source length,
with source voice, structure, identities, and exact signature phrases intact.
Three private rounds each use six steps and the same target. The skill returns
only the final text and applies neutral craft without imposing a new narrator.

Added the ASD-STE100 fallback, local reference notes, six evaluation inputs,
README entry, and default path-check coverage. Metadata validation and the
full nine-skill checks pass. Existing skill files remain unchanged.

## 2026-09-12

Added `fontlab-balanced-writing` and `fontlab-balanced-editing`, each with a
self-contained workflow, synchronized house rules, local worked cases, and
three evaluation inputs. Balanced joins emotional marketing passages to
technical explanations; neutral retains its existing meaning.

The editing skill recognizes intent down to the clause and returns transformed
text only. Both skills check transitions for continuity, terminology, honest
causality, and visible limitations. Default path checks now include both skills.

Verified metadata, shared-rule synchronization, paths, a negative missing-path
case, and six direct writing/editing trials. Existing skills remain unchanged.

## 2026-09-30: proposed Polish transformation term

Regenerated the Polish term reference: utrwal przekształcenie agrees with
Przekształcenie. The term remains proposed. Four tests and all shared-rule/path
checks pass.

## 2026-09-30: dialog-local compact labels

Added Spanish, French and Polish examples for concise dialog questions and
checkbox labels while preserving standalone warning scope. Canonical guides
and portable skills agree. Four tests and all synchronization/path checks pass.

## Localization checkpoint 016

Added an exact-navigation-path check to the ES/FR/PL localization guidance,
with verified current page-title examples. Embedded paths require a separate
check from same-source groups. Guide and portable-skill wording matches.
Styleguide project memories contain all eight current sentence corrections;
core terms and approval statuses are unchanged. Verification: 28 styleguide
tests, four skill tests, strict site build and 225-page link/asset check pass.

## Localization checkpoint 017

Added a source-effect rule to all three localization guides and portable skills:
clearing follower state preserves the nodes, so translation must not imply node
deletion. Refreshed project memories with the 17 reviewed catalog corrections.
All changed memory targets and mirrored catalogs match; core terms and approval
statuses remain unchanged.

## Localization checkpoint 018

Added a concrete noun/verb-role check: Export Profiles names the settings
window's profiles, rather than commanding profile export. The ES/FR/PL
guides and portable skills use the verified localized titles. Project memories
carry the 16 French/Polish catalog corrections, including the completed Polish
follower-property wording. Core terminology and approval status are unchanged.

## 2026-09-30: localization checkpoint 019

Added role-based casing guidance for lowercase English sources to Spanish,
French and Polish guides/skills. Four tests and synchronization checks pass; new paragraphs match the canonical guides.

## 2026-09-30: localization checkpoint 020

Documented inline-selector casing exceptions and preservation of conditions,
allowed characters and format exceptions when shortening hints. Guide/skill paragraphs match; four tests and synchronization checks pass.

## 2026-09-30: localization checkpoint 021

Documented compact PANOSE no-fit definitions while preserving numeric states
and updating every disambiguated occurrence. Guide/skill paragraphs match; four tests and synchronization checks pass.

## 2026-09-30: Localization checkpoint 022

Documented source-verified navigation paths when English UI hints are stale.
The loop-fill setting now points to Font Dimensions in ES/FR/PL; preserve
the Qt source key while translating the verified current route.
Updated all three portable localization skills. Verification: four tests and
shared-rule synchronization checks pass.
Catalog/memory parity passes; the wider editorial review continues.

## 2026-09-30: Localization checkpoint 031

Added the source-verified rule that tr() strings may still be literal program
parameters: preserve .round exactly in TrueType link commands. All three guides
and skills agree; rendered guide text verified. ES/FR project memories reflect
the corrected tokens and Spanish standard-stem wording. Verification: four tests and shared-rule synchronization checks pass. Core terms and approval states unchanged.
