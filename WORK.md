---
this_file: WORK.md
---

# Work log

## 2026-10-07: marketing skill expansion

Expanded `fontlab-marketing` from the writing guide's October 2026 marketing
work (new guide page and chapters 311–315, sourced from the Marketing2 video
corpus and seven books). Added four reference files and short additions to
`fontlab-write` and `fontlab-rewrite`. Shared house-rules block untouched;
`sync_shared.py --check` and `check_all.sh` pass. Nothing committed; the skills
site in `docs/` was not rebuilt, and installed copies need reinstalling.


## 2026-10-01: fl10n issue 154, fifteen machine-drafted language skills

Added `fontlab-localization-<code>` skills for Simplified Chinese (zh),
Traditional Chinese (zh-hant), Russian, Brazilian Portuguese (pt), Arabic,
Hindi, Japanese, Italian, Indonesian, Korean, Turkish, Vietnamese, Thai,
Ukrainian and Czech. The new `tools/scripts/new_language_skills.py` writes each
SKILL.md from the language's localization guide in the writing guide: front
matter, a statement of the draft status, the guide's introduction and its
sections before "Current terminology", and a pointer to `references/terms.md`.
Relative links become plain text. The script keeps a synced house-rules block,
so a second run changes nothing, and it refuses de, es, fr and pl.

Each new term table holds 286 terms from the language's core memory: 232
proposed translations and 54 protected names. No term is approved and no
native reviewer has read any of the fifteen languages. The interface catalogs
are unfinished machine drafts. No runtime test is claimed.

`export_terms.py` now covers all nineteen languages by default, and
`check_paths.py` checks the fifteen new skills. The SKILL.md files and term
tables of German, Spanish, French and Polish were not regenerated. README
lists the new skills and documents the generator.

`bash tools/scripts/check_all.sh` passes: the shared block is in sync in all
28 skills, every path resolves, and 12 tests pass, seven of them new in
`tests/test_new_language_skills.py`. Not done: the description of
`fontlab-localization` still names only the four reviewed language skills.


## 2026-10-01: issue 305 master matching terminology

Polish now uses dopasować/pasować and Swatka, Spanish casar and Casamentero,
and French accorder/accord and Accordeur. Each language skill records command,
state, participle, noun and agreement rules, the naming rationale, and exclusions
for other senses and literal compatible. Updated the shared wordplay example
and regenerated the three portable term tables from the core memories.
German guidance and terminology remain unchanged.


## 2026-10-01: German sharp-node terminology

Added approved canonical entries sharp → spitz and sharp node → spitzer Knoten.
Corrected six catalog messages with adjective inflection (spitze Ecken, einen
spitzen Knoten, an spitzen Knoten). Reviewed all 13 whole-word sharp messages;
all use spitz forms, and no German translation contains Spitzenknoten. Image
sharpening remains schärfen. Updated German guidance and its portable skill.

The 33 styleguide tests and five skill tests pass. The complete application
verifier checks 72,614 strings and all seven ordered edit ledgers; the expanded
application diff now contains 1,164 strings. German lrelease compiles 10,517
translations. Sync rebuilt 988 phrases and 71,500 UI/help units. Evidence:
fl10n/private-data/issue-153/expanded/de-sharp-{changes,verification}.json.
This specific correction is verified; the broader issue-153 review remains open.


## 2026-10-01: issue 153 contextual application review, in progress

Applied 175 initial label revisions in DE/ES/FR/PL, followed by German panel,
selector and nonspacing corrections. The user's follow-ups exposed overly broad
label substitutions. Corrected them by reading the source controls and complete
help text, and recorded the subsequent corrections separately in the edit chain.

Polish application Stroke is obrys. Tęgość is limited to confirmed stroke
thickness; stem controls use grubość trzonu. German uses Dicke generally,
Strichdicke for stroke controls and Stammstärke for stem controls. All 15 standalone
Thickness controls in each DE/PL catalog were classified and checked. The
extrusion field was confirmed as outline-stroke width after inspecting
ActionBase::_extrude and its help. General engraving-line and brush-size fields
retain general thickness wording. Polish panel/group/history headings use
Transformacja, the command Przekształć; crop uses Kadruj and the font checkbox
uses singular Nieproporcjonalny. Guidance and canonical notes now record these
contextual distinctions; the original issue-list test fixture includes the
user's later overrides for Polish stroke and general thickness.

Current application diff: 1,158 complete strings against the expanded-scope
snapshot. Six ordered ledgers explain every change. The verifier checks all
72,614 strings across 16 files, preserves all source text, XML metadata, JSON
structure, placeholders, HTML and URLs, and proves the ledger replay matches
current files. All four Qt catalogs compile to 10,517 translations each.
The fl10n suite passes 252 tests with extraction enabled; styleguide tests pass
32 cases and writing-skill checks pass 5. Sync regenerated 986 phrases and
71,501 UI/help units. No native layout or menu-collision review is claimed.

Evidence: fl10n/private-data/issue-153/expanded/{application-verification,
context-verification}.json and its six *-changes.json ledgers. The styleguide's
dev/issue-153/context-amendments.md records the user's contextual overrides.
The broader four-language contextual review, contradictory prose/related-term
reconciliation and final build/acceptance audit remain open. This checkpoint
does not establish completion of issue 153.


## 2026-09-30: issue 153 expanded terminology, in progress

The current issue contains 149 explicit DE/ES/FR/PL term pairs beyond the earlier
Nudge delivery. All 149 now match the canonical core memories, including approval
from the explicit request. Added 29 English source entries and retained the prior
Nudge decisions. The new complete-pair regression failed on 117 cases before the
update and passes afterward. The historical Nudge verification does not cover
this expanded scope and must not be used as its completion evidence.

Regenerated glossary pages and all four portable skill term tables. Fixed the
skills exporter, whose obsolete localization/tm path caused all four exports to
fail; its isolated CLI regression reproduces the failure and passes with the fix.
Ran localization/sync_all.py: 986 QPH entries and 71,501 derived UI/help units.
These derived memories still reflect application translations pending review.

Preserved current application inputs and hashes under
fl10n/private-data/issue-153/expanded/. Source-term triage found 22,468 candidate
rows (DE 6,310; ES 5,825; FR 5,169; PL 5,164). This is a review queue, not a
linguistic completeness claim: inflections, compound words, protected literals
and related terms need contextual review. No application translation was changed
in this checkpoint. Checks pass: 31 styleguide tests, 8 sync tests, 5 skill
tests, terminology schema and core/project separation. The fl10n baseline has
251 passing tests and one environment-dependent extraction skip. Language-guide and skill prose reconciliation, application
retranslation, final rebuild and final acceptance remain open.


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

## Localization checkpoint 068

Added action-label/tooltip naming follow-through to ES/FR/PL skills, preserving
grammatical functional descriptions. Four tests and all skill checks pass.

## 2026-10-01 — Issue 153: French metrics and redo/repeat review

Changed 522 French UI/help strings from the old métriques terminology to mesures.
Preserved feminine plural agreement; recast données métriques as données de mesure,
window/tab labels with de mesures, and the comparison with celles du calque actuel.
Added contextual examples to the French guide and portable language skill.
Recorded 108 Spanish/French redo/repeat rows with retained wording and review
reasons; other terms within those rows remain in the broader review scope.

French lrelease: 10,517 finished translations. Full structural/provenance check:
72,614 strings, 16 files, 1,878 changes from baseline, all accounted for.
sync_all.py regenerated the four UI memories. Broader contextual retranslation
and final acceptance remain pending.

## 2026-10-01 — Issue 153: French nonspacing and canonical notes

Corrected 17 French UI/help strings for the Sans-chasse property. The action
help now explains exclusion of elements from metrics calculations, rather than
claiming to set glyph advance width to zero. Descriptive prose retains the
grammatical phrase élément sans chasse; property references name Sans-chasse.
Updated Spanish/French core notes with the precise command names and behavior;
removed the obsolete Spanish Detectar exclusión de métricas instruction.
Rebuilt the glossary pages, exported portable skill term references and ran
sync_all.py. The initial system-Python invocation lacked PyYAML; the locked
project environment successfully performed canonical writes and generation.

Fresh checks: French lrelease 10,517 finished entries; full application audit
72,614 strings / 16 files / 1,937 changes; 33 guide tests and all skill checks
(including five tests) passed. Contextual review and final Proteus commit/push
remain pending.

## 2026-10-01 — Issue 153: Polish nonspacing

Corrected 44 Polish strings to bezmetryczny/bezmetryczność and contextual
komponent forms. A second grammatical pass corrected component genitives,
plurals and adjective agreement. Removed false claims that the action sets
glyph advance width to zero. Updated the canonical note and its existing
regression test to the current command Wyłącz bezmetryczność and explicit
behavior, rebuilt glossary/skill references and synchronized UI memories.
Validation: 33 guide tests pass; Polish compiles 10,517 finished strings; full
16-file audit passes on 72,614 strings and 2,498 baseline differences. Broader
review and final Proteus commit/push remain pending.


## 2026-10-01 — Issue 153 stroke-context note

Regenerated locale term references after correcting Proportional Thickness in German stroke controls to Proportionale Strichdicke. All skill checks and five tests passed. Broader issue review remains pending.


## 2026-10-01 — Issue 153 contextual terminology completion

- Reconciled Polish object references versus geometric reference points, diacritics, guides and components; applied grammatical case and command phrasing. Distinguished stroke, stem and general thickness in German and Polish, and sharp nodes from image sharpening.
- Reconciled autohinting labels, French weight and OpenType compounds, German OpenType feature grammar, glyph variants, cusp/crop labels, Spanish defaults, and German/Polish Nudge help. Preserved literal code, identifiers and legitimate general-language meanings.
- Regenerated canonical term pages, skill reference tables, all four UI memories and phrasebooks. Removed contradictory recommendations from the language guides and skills.
- Verification: 72,614 strings across 16 resources; 4,722 differ from the saved baseline, with every edit accounted for by ordered ledgers. Source metadata, placeholders, markup and URLs preserved. All four Qt catalogs compile: 10,517 finished, zero unfinished each. Localization tests: 252 passed; styleguide tests: 33 passed; skills tests: 5 passed. Built 225 HTML pages with local links/assets and publication checks passing. All generated memory pairs match sources and synchronization is idempotent.
- Proteus delivery: a6568d22c and 4a7c0b911. Issue 304 is the next user-requested task and includes another final Proteus push. The candidate-string inventory remains a regex discovery aid, not evidence that every unrelated UI sentence has received complete linguistic proofreading.

## 2026-10-04: issue 160 terminology and review workflow

Updated all 19 localization skills and portable term tables from the reconciled cores. Added lookup/procedure exceptions, phonetic FontAudit (including both Chinese scripts), Welder fallback, compact labels, uppercase/metric conventions and Russian/Ukrainian Smart Filter exceptions. Generated skills now describe per-term approval states accurately. Added draft preservation and English-based upstream merge guidance. Validation: check_all.sh passes all 12 tests, shared-rule checks and path checks.
