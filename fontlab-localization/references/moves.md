# Moves: English that survives translation

Ten worked pairs. Each one is about the English, not about any translation. The source sentence is plausible English that a reviewer would pass. The rewrite says the same thing and survives.

The line after each pair names the mechanism. "Confusing for translators" is not a mechanism. Word order, gender resolution, a slot with no readable name: those are mechanisms.

## 1. The long sentence

**Source.** When you have finished adjusting the sidebearings of the glyph and you are satisfied that the spacing looks even across the whole alphabet, you can open the Kerning panel and begin adding the pair values that correct the combinations the sidebearings cannot handle on their own.

**Rewrite.** Adjust the sidebearings of the glyph. Check that the spacing looks even across the alphabet. Then open the Kerning panel and add pair values. Pair values correct the combinations that sidebearings cannot handle.

**What would have broken.** German holds the finite verb of a subordinate clause at the end, so a translator has to carry four stacked conditions before the verb arrives and tells the reader what to do with them. The sentence is readable in English only because English resolves early.

## 2. The idiom

**Source.** Vexy Lines has your back when the source image is noisy, so you can blaze through the cleanup and ship in a breeze.

**Rewrite.** Vexy Lines removes most of the noise from a source image automatically, so the cleanup takes less time.

**What would have broken.** "Has your back", "blaze through", and "ship in a breeze" have no equivalent in most target languages. A translator renders them literally, producing a sentence about someone standing behind you, or drops them and returns a sentence with no content, because the claim was carried entirely by the figures.

## 3. The pronoun across clauses

**Source.** Open the Layers and Masters panel, select the Light master, and check that it matches the number of nodes in the Bold master before you interpolate, because otherwise it will fail.

**Rewrite.** Open the Layers and Masters panel and select the Light master. Check that the Light master has the same number of nodes as the Bold master. If the node counts differ, the interpolation fails.

**What would have broken.** The first "it" points at the Light master and the second at the interpolation, four and eight words back. German assigns each pronoun by grammatical gender, so both resolve to whichever preceding noun matches, and neither translator nor reviewer can see the error from the target text alone.

## 4. The stacked nouns

**Source.** Set the font family name field label width in the export options dialog.

**Rewrite.** In the Export options dialog, set the width of the label of the Font family name field.

**What would have broken.** Six nouns in a row carry their relationships only in English word order. Every translator has to reconstruct which noun modifies which, and three translators reconstruct it three ways. The rewrite spells the relationships out with prepositions, so nothing is left to reconstruct.

## 5. If against when

**Source.** When the font contains no kerning, FontLab writes an empty `kern` feature.

**Rewrite.** If the font contains no kerning, FontLab writes an empty `kern` feature.

**What would have broken.** English "when" covers both the temporal sense and the conditional one. German has to choose between wenn and als, Polish between jeśli and kiedy, and a translator reading "when" will often pick the temporal word. The sentence then promises that a font will eventually contain no kerning, which is not what it says.

## 6. The sentence assembled from separate strings

**Source.** Two interface strings, concatenated at run time.

```
string_1 = "The font contains"
string_2 = "glyphs with open contours."
```

**Rewrite.** One string, one whole sentence, with a named placeholder.

```
string_1 = "The font contains {contour_error_count} glyphs with open contours."
```

**What would have broken.** German puts the verb at the end of a subordinate clause and Japanese puts it at the end of the sentence, so the two halves cannot stay in the order the concatenation forces. Neither string is a sentence, so neither translator sees the whole thing, and no reviewer sees the joined result until it ships.

## 7. The positional placeholder

**Source.** `"Exported %1 of %2 instances to %3."`

**Rewrite.** `"Exported {exported_count} of {total_count} instances to {output_folder}."`

**What would have broken.** A translator reading `%1` cannot tell whether it holds a number, a name, or a path, so any reordering the target language needs is a guess. A wrong guess swaps a count for a folder name and the string still compiles.

## 8. The tight button label

**Source.** A button sized to fit the English label Remove Overlap and nothing more.

**Rewrite.** A button sized for the longest target string, with the English label filling roughly two thirds of it, and the control set to grow rather than truncate.

**What would have broken.** German runs 20 to 35 percent longer than English, so the German label needs close to double the width. A control measured against English truncates it, and a truncated label reads as a different command. The English wording was never the problem; the English measurement was.

## 9. The contraction in an interface string

**Source.** `"The font hasn't been saved. Don't close it yet."`

**Rewrite.** `"The font has not been saved. Do not close the font yet."`

**What would have broken.** Contractions break string extraction and matching, and the apostrophe arrives as three different characters depending on the editor that touched the file last. The rewrite also drops the "it", which had the same across-clause problem as move 3.

## 10. The ambiguous date and the bare number

**Source.** The license expires 08/30/26, and the export finished in 1,250.5 units.

**Rewrite.** The license expires 2026-08-30. The export finished in 1250.5 font units.

**What would have broken.** `08/30/26` reads as 30 August 2026 in the United States and as an impossible date almost everywhere else, so a translator either guesses or leaves it wrong. The comma in `1,250.5` is a decimal separator in German and Polish, which turns the number into something a thousand times smaller. Naming the unit as font units removes the second guess.
