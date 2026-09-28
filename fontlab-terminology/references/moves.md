---
this_file: fontlab-terminology/references/moves.md
---

# Terminology: worked cases

## Keep the name, develop the thought

The snapshot distinguishes a FontLab mask layer, which carries a reference
drawing, from a Vexy Lines mask, which governs where fills appear. Use these
scoped meanings in a naming check; verify current product behavior separately
when preparing new operational documentation.

Compact distinction:

> In FontLab, a mask layer carries a reference drawing. In Vexy Lines, a mask
> defines where a layer's fills appear.

Developed explanation:

> Start with the drawing you want to compare. A FontLab mask layer can carry
> that reference while you examine the live outline against it. The reference
> gives the comparison another drawing to look at; it does not conceal the
> live outline.
>
> In Vexy Lines, a mask serves a different purpose. Its transparent areas let
> a layer's fill appear, and its opaque areas hold the fill back. Here the
> useful question is where the fill appears.

The first version supports lookup. The second follows a reference drawing,
then a fill, to show why the same noun cannot carry one definition across
both products. It adds no interface sequence, default, automatic comparison
or claim that the app judges a drawing. Accurate actors keep the concept clear.

## Let three spellings name three things

Supplied context: a passage refers to the desktop product, its Python module
and the company. Draft: “Fontlab opens the project. The example imports FontLab.
FontLab Ltd. is named in the agreement.”

Terminology findings:

- Fix the product spelling to FontLab in the first sentence, without claiming
  that this naming check verified the described operation.
- Keep the literal import identifier lowercase: `fontlab`. If the supplied code
  is protected or its intended module is unclear, flag it before editing code.
- Fix the company spelling to Fontlab Ltd. in the third sentence.

The distinction survives a fluent paragraph because the subject remains clear
at every return. Substituting “the platform” for one of these names would leave
the reader to work out which entity the sentence means.

## Preserve the time of a name

A supplied historical caption reads: “The Strokes Maker interface shown here
belongs to the archived release.” Keep Strokes Maker. The catalog's deprecated
status guides current naming; it does not rename the archived interface.

If a current marketing draft uses that name for today's product, inspect the
context and apply the current name when supported. These are different verdicts
because the passages refer to different moments.

## Leave an unresolved sense visible

Draft: “Open Transform and adjust the selection.” No app or interface surface
is supplied. Flag the missing application and control type. Do not choose
“panel” because it makes a complete sentence. Continue any independent spelling
corrections elsewhere in the draft.

## Practice the second pass

Compare the compact and developed mask explanations. Mark the object in each
sentence and the relationship it adds. Confirm the two product senses remain
distinct. Then imagine the request was only “fix the capitalization”: retain
the surrounding prose and make the supported correction. Craft includes knowing
how much change the task allows.
