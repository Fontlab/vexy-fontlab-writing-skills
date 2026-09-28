<!-- this_file: fontlab-localization/references/moves.md -->

# Localization: worked cases

A translation needs the source’s relationships as well as its words. These
fictional exercises establish their facts before revision. They demonstrate
source preparation and editorial choices; they do not certify a language review
or behavior tested in an application.

## Give a comparison its two subjects

Facts: A procedure compares the node counts of Light and Bold masters. The
source requires matching counts before interpolation; it says nothing about
other compatibility conditions.

Draft:
> Compare Light with Bold and check that it has the same node count before interpolating.

Revision:
> Before interpolating, check that the Light and Bold masters have the same node count.

Both masters now share the same grammatical task. The reader can compare them
without deciding what “it” meant. Matching counts remains a prerequisite in this
packet; the revision does not make it a complete compatibility test.

## Remove a promise the facts cannot carry

Facts: The brief says only that Shape Editor supports manual image cleanup.
No automatic noise reduction or timing measurement is supplied.

Draft:
> Shape Editor has your back: blaze through cleanup and ship in a breeze.

Revision:
> Use Shape Editor for manual image cleanup.

The shorter revision has less flourish because the brief supplies little to
develop. If the piece needs more interest, obtain a useful detail about the
manual work. A translator should not have to invent automatic cleanup or a
speed claim to make the original excitement plausible.

## Preserve positional placeholders

Facts: The existing parser uses `%1`, `%2`, and `%3` for exported count, total
count, and output folder. The task permits prose editing but no format migration.

Source string:
```text
Exported %1 of %2 instances to %3.
```

Keep the resource syntax. Explain that `%1` is the exported count, `%2` is the
total count and `%3` is a folder path. The translator needs these relationships
before arranging the sentence. Check whether the parser permits reordering;
brace syntax would require a format change, even if its names look clearer.

## Distinguish message design from translation

Facts: A developer proposes a new count message. The message framework and
plural syntax have not been chosen.

Draft design:
```text
prefix = "The document contains"
suffix = "objects."
```

Review: specify one complete grammatical message, the meaning of its count and
the required plural cases. Then choose syntax the selected framework supports.
Until that choice is made, `{count}` is a schematic label in the discussion,
not an executable resource. Do not give a translator three fragments and ask
them to recover the grammar between them.

## Preserve duration

Facts: Updates remain paused throughout the time the Settings dialog is open.

Draft:
> Updates pause when Settings opens.

Revision:
> Updates remain paused while the Settings dialog is open.

The revised sentence holds the pause across the entire open interval. Preserve
that duration in the target language; no particular English word is a universal
solution. A shorter sentence that describes only the opening event loses it.

## Do not invent a unit

Facts: A record gives “1250.5 units” without identifying the unit. The expiry
date is explicitly 30 August 2026.

Draft:
> The license expires 08/30/26. The measured value is 1250.5 units.

Working revision:
> The license expires on 30 August 2026. The measured value is 1250.5
> [CONFIRM UNIT].

The spelled-out date resolves a known fact. The marker preserves an unknown one.
The target can use its normal display conventions once the unit is established,
while retaining the actual quantity. Fluent wording cannot supply the unit.

## Review contractions as wording

Facts: The file is unsaved. The user asks for formal English wording; this is
plain text, with no parser change.

Draft:
> The file hasn't been saved. Don't close it yet.

Revision:
> The file has not been saved. Do not close the file yet.

The expanded verbs fit the requested formality, and “the file” makes the final
reference explicit. This is a wording revision. It establishes nothing about
string extraction, parser behavior or whether contractions suit another surface.

## Test expansion instead of predicting it

Facts: A button fits its English label exactly. Target translations have not
yet been measured.

Review: put the actual translated labels in the component at its supported
widths and text sizes. If they do not fit, let the control grow or revise the
wording without removing its meaning. An estimated expansion allowance is a
planning aid, not an observed result.

## Keep a proposal separate from approval

Facts: A fictional catalog contains four terms: two approved translations, one
proposed translation, and one decision to keep the source term. The project
counts approved and do-not-translate terms as settled.

Result: 3 of the 4 terms meet this project’s settled-status definition, giving
75% terminology coverage. Keep the proposed translation visibly proposed. The
count says which statuses exist; it does not independently establish their
correctness, prose coverage or completed native review.

## Keep an introduction’s movement

Fictional facts: a viewer displays the same drawing against two background
colors. Changing the background does not change the drawing data. Its interface
label Background remains English in the target locale. No assessment or export
behavior is supplied.

Source introduction:

> Follow the same line against two backgrounds. Background changes the preview
> color while leaving the drawing data unchanged. The line is the same; its
> surroundings have changed.

Proposed Polish rendering, for editorial review:

> Obejrzyj tę samą linię na dwóch tłach. Ustawienie Background zmienia kolor tła
> podglądu, ale nie zmienia danych rysunku. Linia pozostaje ta sama; zmienia się
> jej otoczenie.

The proposal follows the line through a changed setting and retains the final
contrast. Its sentence structure fits the target without adding a contrast
assessment or export claim. Background remains the actual interface label.
This is a worked proposal, not an approved project translation.

For a local notice, both languages should answer more directly:

> Background changes the preview background, not the drawing data.
>
> Ustawienie Background zmienia tło podglądu, ale nie dane rysunku.

The shorter surface needs the boundary. The introduction gives the reader time
to look. Do not preserve the introduction’s length merely to make the target
resemble the source on the page.

## Practice the second review

Take a fresh fictional packet: a viewer shows a map with or without labels.
Show labels is the exact untranslated control name. Source map data is unchanged;
no editing or navigation behavior is supplied.

Write a source introduction and a target-language proposal for an identified
locale. First compare facts, labels and scope. Then read for the subject carried
between sentences and the pace of the ending. Finally recheck the facts: a
more natural phrase must not turn a viewing control into a map editor.
