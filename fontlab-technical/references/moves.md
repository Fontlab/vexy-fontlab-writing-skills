<!-- this_file: fontlab-technical/references/moves.md -->

# Technical writing: worked cases

The application packets below are fictional and define the scope of each example.
The Python sample is a separate, executable language example. None establishes
FontLab or Vexy behavior.

## Follow the same object through a change

Facts: a viewer shows a selected drawing. Zoom changes its display scale without
changing the drawing data. The viewer does not assess whether detail is readable.

Flat draft:

> Zoom changes the scale. Data stays unchanged. Readability is not assessed.

Concept revision:

> Zoom changes how large the selected drawing appears. Follow a detail as the
> display scale changes: you are inspecting the same drawing data in a different
> view. You judge whether the detail remains readable; the viewer does not
> assess it.

The drawing carries the explanation from operation to boundary. The middle
sentence develops a relationship instead of adding a list of controls. It does
not promise sharper detail or a change to saved artwork.

For a local reference note:

> Zoom changes the display scale, not the drawing data.

The short version answers a local question. It does not need the introduction’s
patient pace. Neither version supplies an undocumented zoom gesture.

## Separate actions at useful checkpoints

Facts: in Shape Editor, choose Edit > Preferences, turn on Show grid and choose
Apply. The destination supports plain Markdown.

Draft:

> Open the preferences and show the grid and apply it.

Revision:

> 1. Choose **Edit > Preferences**.
> 2. Turn on **Show grid**.
> 3. Choose **Apply**.

The ordered steps expose the exact route. No shortcut, confirmation message or
unsupported highlight notation is added. A result can follow a step when the
packet establishes it; this one supplies only the actions.

## Let an unknown method remain unknown

Facts: spacing is adjustable, but the source names no control or input method.

Capability statement:

> Spacing can be adjusted.

Working procedural text:

> [CONFIRM METHOD: control or command for adjusting spacing]

The first sentence may be sufficient for an overview. It cannot become a usable
step by adding “press the arrow keys”. A requested procedure remains unfinished
until its method is known.

## Preserve the interval

Facts: preview updates remain paused for the whole time the Settings dialog is open.

Draft:

> Preview updates pause when Settings opens.

Revision:

> Preview updates stay paused while the Settings dialog is open.

The revised sentence holds the state across the open interval. It adds no claim
about what happens after closing. A conjunction should express supplied timing,
not invent it.

## Put the consequence before the action

Facts: Clear notes permanently removes all notes from the current document and
cannot be undone. No backup command is supplied.

Revision:

> **Warning:** Clear notes permanently removes all notes from this document.
> You cannot undo the command.
>
> Choose **Clear notes**.

The reader meets the consequence before the command. A decorative metaphor or
an invented backup route would make this passage less dependable, not warmer.
The example describes the operation; it does not claim the command was run.

## Give the condition and the result a subject

Facts: in a fictional drawing app, Sketcher, the Auto Fill command fills each
layer of the current drawing separately. The destination links terms to a
glossary that defines *layer*.

Draft:

> Filling works separately for each layer, a stacked drawing surface such as
> Background or Ink.

Revision, with *layer* linked to its glossary entry:

> If you run Auto Fill on a drawing, Sketcher fills each layer independently.

The draft hides both actors. “Filling” could be the reader's action or the
app's, and the apposition interrupts the relationship to define a term the
glossary already covers. The revision restates the action compactly, so a reader
who lands on this sentence alone knows what triggers the behavior. The packet
names no narrower surface than the app, so Sketcher responds; if it said the
Layers panel reported progress, that panel would be the subject of that result.
The result is immediate, so both clauses stay in present tense.

## Give a next step without inventing a cause

Facts: export stops with E17. Its cause is unknown. The supported next step is
to send the error code and file version to support.

Draft:

> A damaged font causes E17. Reinstall the app to fix it.

Revision:

> If export stops with E17, send the error code and file version to support.
> The cause has not been established.

The revised passage retains a useful action while removing the diagnosis and
remedy that the packet cannot support. Unknown cause does not mean there is
nothing useful to tell the reader.

## Keep polarity and scope

Facts: turning on Include stroke includes stroke thickness in the bounds
calculation.

Tooltip:

> Include stroke thickness when calculating bounds.

Keep “include” distinct from “ignore”. Shortening cannot reverse an option.

Separate fictional facts: Quick Find searches names and notes except archived
notes. A supported sentence is:

> Quick Find searches names and notes, except archived notes.

The last three words carry the boundary. Removing them to reach a length target
changes the expected search scope.

## Keep reference values attached to their meaning

Fictional facts: a parameter has a range of 0 to 100 percent and a default of
50 percent. No recommended value or out-of-range behavior is supplied.

| Property | Value |
|---|---|
| Unit | Percent |
| Range | 0 to 100 |
| Default | 50 |

This table does not explain what either endpoint does, or whether an invalid
input is rejected or clamped. Keep those questions open. If you reorder the
table, compare whole rows so that 50 remains a default rather than a limit.

## Give a code sample an inspectable result

Prerequisite: Python 3. This example counts three supplied names; it does not
read a font or modify a file. Python’s built-in [len function](https://docs.python.org/3/builtins/functions.html#len)
reports the number of items in the list.

```python
# this_file: count_glyph_names.py
glyph_names = ["A", "Adieresis", "B"]
print(len(glyph_names))
```

Output:

```text
3
```

The sample’s scope is small and visible. It does not establish a product API or
count glyphs in an open document. A prose edit must not replace these literals
or invent a FontLab method to make the example look more relevant.

## Practice the instructional second pass

Fictional facts: a viewer’s Show names option displays object names in the
preview. Exported artwork omits those names. No renaming operation or menu path
is supplied.

Write a concept paragraph and a tooltip. Let the paragraph follow the names
from preview to export; let the tooltip answer the option’s local question.
A possible pair:

> **Concept:** Show names adds object names to the preview, giving you a way to
> identify what you are looking at. The names belong to that view; exported
> artwork omits them.
>
> **Tooltip:** Display object names in the preview. Exported artwork omits them.

The paragraph follows the names from their visible role to their absence in
output. The tooltip keeps that distinction without a separate introduction.
Neither adds renaming or an undocumented menu route.

Then compare the two against the same facts. Retain the boundary while choosing
a different amount of explanation. If a procedure is requested, mark the missing
route instead of constructing one from the option’s name.
