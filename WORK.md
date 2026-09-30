---
this_file: WORK.md
---

# Work log

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

## 2026-09-29: Follower node terminology

The user retired the servant metaphor for localization. Interpret the legacy
English Servant node/Servant source as Follower node/Follower, in the sense of
a fan or supporter. Targets: German Anhänger-Knoten; Spanish nodo seguidor;
French nœud adepte; Polish węzeł zwolennik. Each language guide and skill
records short labels, X/Y forms and inflection. Dictionary links support the
lexical senses; this is the requested naming decision, not a claim of a new
native review. Source labels and identifiers stay compatible.

Updated the canonical definition, alias list, fallback and four core targets,
plus the related Genius definition and term seeding records. Regenerated core
memories, generated guides and portable term tables. Refreshed only affected
project-memory target records from the edited application catalogs through
Localizzy's TMX reader/writer: 21 records per language; other records and all
source text/properties are unchanged. Application delivery includes 84 TS
translations, 64 extended helptips, 12 Help Panel entries, regenerated JSON
glossary, four rebuilt QPH files and refreshed prompt instructions/embeddings.
The exact before/after ledger is Proteus/i18n/review/follower-terminology-2026-09-29.json.

Verification: the new four-language meaning/target regression failed before
the data update, then passed; all 26 styleguide tests and four skill tests pass.
Strict build: 7.66 seconds, publication guard and 225 HTML-page link/asset
checks pass. All four TS catalogs compile with Qt 5 lrelease. One pre-existing
German unfinished translation is preserved. Independent comparisons confirm
unchanged English files, TS metadata and states, JSON keys, markup and tokens,
and unrelated translations (including ordinary French participles). QPH
embeddings are byte-identical. No publication or source-code rename performed.


## 2026-09-29: current localization rules and term tables

Updated all four language skills to use current terminology authority and
explicit proposal status, removing dated review-progress summaries. Removed
the Polish lookup loan contradiction, clarified current French feature names
and master terminology, and aligned shared mnemonic and French command-collision
rules with the writing guide. Regenerated all four portable term tables from
the refreshed core memories, including definitions and cleaned translator notes.
No target translation or approval status changed.

Verification: shared-block parity, local path checks and all four unit tests
pass. The styleguide's 25 tests and strict build pass. Scanned active guides,
core data, portable skills and rendered files for the identified superseded
terms: no hits. Qt Linguist prompts in Proteus/i18n carry these current rules
and the complete refreshed phrase books, verified byte for byte.


## 2026-09-29: fl10n issue 147, house-voice terminology rules

Added the shared "Choose terms in the house voice" section, updated the four
language skills and the terminology skill, regenerated the term tables with
the Fallback column (de/es/fr 222, pl 231). `bash tools/scripts/check_all.sh`
passes.

## 2026-09-28: fl10n issue 145, first localization pass

Added the shared localization references and the four per-language skills;
regenerated term tables (de 208, es 208, fr 208, pl 217 terms). The Polish
skill states its terminology as the working set for the first Polish catalog;
151 of its terms are still proposed. `bash tools/scripts/check_all.sh` passes.
Second pass: the French skill carries the September 2026 review decisions;
the term tables were regenerated after the French and Polish core-memory
updates (de/es/fr 222 terms, pl 231). The Polish skill's terminology reflects
the reviewed core memory; a native pass over the first Polish catalog is the
next step.


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

## 2026-09-13: partner sources and measurement output

Rewrote the partner skill and checklist against the current partner checkout.
Separate existing copy from confirmed commercial terms; document FAQ skips,
signup generation, per-pack CSV inputs and the limits of strict asset checks.
Preserve distinct CTA markup and destinations when updating shared wording.
Five temporary-fixture checks confirm actual generator behavior.

The measurement CLI now labels matches as review candidates, retains comparison
data without presenting targets, omits range comparisons below 40 words and
handles empty input without false flags. Removed the unsupported final-paragraph
heuristic and the structural check's unconditional dash ban. Four CLI regression
tests failed before the change and now pass in the combined check.

Wait, but approximate Markdown cleanup and legacy comparison data still limit
measurement. These checks do not prove commercial terms, whole-site parity or
deployment. Shared rules and eight other complete skills are unchanged.
Source hashes and bounded verification are recorded in the styleguide's
`dev/issue-106/` batch-12 evidence. No dependency added to this repository.

## 2026-09-13: balanced instruction parity

Reconciled balanced writing and editing with the current house rules. Preserve
fact timing and useful passive wording; remove numerical instruction budgets
and the sentence-average claim. Both long published prompts exactly match their
skill core plus bundled examples after heading conversion. Both reference files,
the shared block and seven other complete skills remain byte-identical.

Existing checks pass. Four direct same-agent cases preserve timing, an unknown
actor, a supported introduction and a long exact label. The styleguide retains
snapshots, exact edits, sixteen rendered prompt checks and browser evidence in
batch 10. No independent model or operating-system clipboard test is claimed.

Wait, but other prompt rules, partner guidance and measurement messages remain
open. No dependency or remote publication change.

## 2026-09-13: localization and terminology parity

Rewrote the localization and terminology instructions and localization cases.
Preserve existing placeholder formats, factual uncertainty, proposed status,
historical names and product scope. Replaced the portable term list with an
export of all 151 current glossary definitions and metadata; usage examples and
private research paths are excluded. The shared block and seven other complete
skills remain byte-identical to the batch-9 baseline.

Existing skill checks pass. Eight direct same-agent trials cover positional
placeholders, unknown units, unsupported automation, term coverage, naming,
history, dialogs and ambiguity. They are not native reviews or runtime tests.
The styleguide holds snapshots, exact revisions and field-by-field export
verification under `dev/issue-106/` for batch 9.

Wait, but partner operational guidance, balanced references, prompt parity,
measurement messages and remaining glossary examples still need work. No
remote publication or dependency change.

## 2026-09-13: reconcile core writing rules

Updated the shared rules and generated all nine copies from the source block.
Rewrote neutral, marketing, and technical instructions and their worked cases.
Removed numerical quotas, authorship claims, unsupported example details, and
rigid cuts. Fictional cases state their facts before the revision. README now
explains measurements as optional diagnostics rather than writing targets.

The existing check script passes. Eight direct same-agent output trials preserve
facts and output constraints; they are not independent model benchmarks. Six
other skill-specific cores remain byte-identical outside the shared block,
including TLDR's three-round contract. The styleguide checkout retains baseline
snapshots, exact edits, build/rendered checks and trial evidence under
`dev/issue-106/` for batch 8.

Wait, but localization, terminology, partner guidance, balanced references,
prompt-specific parity and measurement messages still need review. Structural
synchronization does not establish editorial agreement. No remote publication.

## 2026-09-12: rename balanced skills

Renamed balanced editing to `fontlab-rewrite` and balanced writing to
`fontlab-write`. Updated metadata, path records, evaluation identifiers,
README entries, and checker coverage. Verified all six moved files against
their originals: only identifier substitutions changed their contents.

Validation: both renamed skills pass metadata validation, all nine skill checks pass, and both repositories pass whitespace checks. No old identifiers remain in active skill files or the public catalog.

## 2026-09-12: TLDR skill

Completed the standalone TLDR skill, reference notes, evaluation inputs,
catalog entry, and checker coverage. The styleguide's chapter 408 carries the
same core plus a short variant. Both rendered prompt payloads match exactly.

Verified metadata, all nine skills, six direct output trials, consistent word
counts, and hashes preserving the eight earlier skills. Trial sources, final
outputs, and the direct review are in the styleguide's dated TLDR review
directory. These checks do not claim independent model performance or full
ASD-STE100 certification. No pending work remains in this addition.

## 2026-09-12: balanced skills

Completed two standalone skills, bundled examples, evaluation inputs, README
entries, and default path-check coverage. Both metadata validations and the
full eight-skill check pass. A missing-reference fixture fails as expected.

The six direct trials cover concept/procedure drafting, absent benchmark proof,
customer notice, protected quotation, unchanged mixed text, and eligibility
repair. They are same-agent sanity checks, not independent benchmarks. The
styleguide checkout holds the outputs in its dated balanced-skill trial record.

No dependency change, global install, or remote release was needed. All six
pre-existing SKILL.md files remain byte-identical. No pending task remains in
this addition.

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

Checkpoint 017 downstream validation: 28 styleguide tests, strict documentation
build and 225-page link/asset checks pass. The new rule is present in all three
built localization pages.

## Localization checkpoint 018

Added a concrete noun/verb-role check: Export Profiles names the settings
window's profiles, rather than commanding profile export. The ES/FR/PL
guides and portable skills use the verified localized titles. Project memories
carry the 16 French/Polish catalog corrections, including the completed Polish
follower-property wording. Core terminology and approval status are unchanged.

Checkpoint 018 downstream checks: 28 styleguide tests, strict site build and
225-page link/asset checks pass; all three rendered localization pages contain
the new noun/verb-role rule.

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

## Localization checkpoint 064

Added same-source follow-through guidance: review shorter counterparts after
every edit, align generated property descriptions, preserve genuine contextual
variants and compare plural forms by position. ES/FR/PL project memories hold
35 consistency fixes. Six writer, 28 styleguide and four skills tests pass;
strict documentation build verifies 225 pages and the rendered new rule.
Final catalog/UI acceptance remains open.

## Localization checkpoint 066

Added generated displayName/enum role checks and protected-identifier rules
to ES/FR/PL localization skills. Four tests and all skill checks pass.
