---
this_file: fontlab-simplify/references/moves.md
---

# Simplification: worked cases

Each case states its evidence first. The examples are fictional unless marked
otherwise and do not establish product behavior.

## Plain: stacked hedges and a hidden actor

**Evidence:** the source says interpolation can fail when masters are not
compatible, and that instances are then not generated.

> **Draft:** It should be noted that in the event that the masters are found to
> be incompatible, the interpolation process may potentially not be able to be
> performed successfully, which could result in instances not being generated.
>
> **Revised:** If the masters are not compatible, FontLab may not be able to
> interpolate them. It then cannot generate the instances.

Kept: the condition (*if*), the uncertainty (*may*). Removed: "it should be
noted that", "in the event that", "potentially", the nominalized "process".
Named the actor. Not added: a fix, because the source gives none. If the user
wants one, add `[CONFIRM FIX]` or ask.

## Controlled: one instruction per sentence

**Evidence:** a procedure with three actions in one sentence.

> **Draft:** Select all glyphs and then run Remove Overlap from the Contour menu,
> making sure to check the results afterwards since some contours might change
> direction.
>
> **Revised:**
>
> 1. Select all glyphs.
> 2. Choose Contour > Remove Overlap.
> 3. Check the result. Some contours might change direction.

The menu path stays exact. *Might* stays: the source does not say every contour
changes.

## Controlled: an error message that stays honest

**Evidence:** the application cannot tell whether a file is damaged or merely
in an unsupported version.

> **Draft:** An error may have occurred during file loading due to possible
> corruption or an unsupported format version.
>
> **Revised:** FontLab could not open the file. The file may be damaged, or it
> may use a format version that this FontLab version does not support.

Not written: "The file is damaged." The application does not know that.
Kept the compound uncertainty as two clear alternatives.

## Plain: noun stack

> **Draft:** Enable the glyph outline node coordinate rounding option.
>
> **Revised:** Turn on the option that rounds node coordinates in glyph
> outlines.

If the interface has a label for the option, quote it exactly instead:
"Turn on ==Round coordinates==" (`[CONFIRM LABEL]` until checked).

## Plain: synonym rotation

> **Draft:** Each master stores one design. When you edit a style, the other
> weights update automatically.
>
> **Revised:** Each master stores one design. When you edit one master, FontLab
> does not change the other masters.

*Style* and *weight* were names for the same object, and the draft's
"update automatically" was not supported by the source. Check the claim before
simplifying it; here the evidence said the reverse.

## Easy-to-read: one idea per line

**Evidence:** an onboarding note for a reader new to font editing.

> **Draft:** Variable fonts contain multiple masters along design axes, and
> FontLab interpolates intermediate instances.
>
> **Revised:**
>
> A variable font can change its shape.
> For example, letters can be thinner or bolder.
> FontLab makes these in-between shapes for you.
> To do this, it uses a few drawings of each letter.
> These drawings are called **masters**.

The term *master* is kept and explained, not replaced. The *axis* concept is
left out because this reader does not need it yet; add it on a later page.

## When not to change anything

> **Draft:** Choose File > Export Font As. Choose OpenType PS and click Export.

The text is already plain and controlled. Return it unchanged and say so.
