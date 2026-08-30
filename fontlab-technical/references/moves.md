# Moves

Before and after pairs from real FontLab material. Each pair ends with one line
saying what changed and why.

## 1. Two actions in one step

**Before:** Press Shift+F1 to open the Help panel and place it where you can
conveniently read the text, then open Tools > Commands & Shortcuts.

**After:** Press ++Shift+F1++ to open the ==Help== panel. Place it so that you
can conveniently read the text. Then open ==Tools > Commands & Shortcuts==.

*Changed:* three instructions, three sentences, house notation on the key and
the path. A reader who is executing cannot hold two actions in one line.

## 2. The verb tells the reader which input to use

**Before:** Select Tools > Commands & Shortcuts, then select the Apply checkbox
and select the command from the list.

**After:** Choose ==Tools > Commands & Shortcuts==. Turn on ==Apply==. Click the
command in the list.

*Changed:* one word, one meaning. Choose a menu command, turn on a checkbox,
click a control. Microsoft's input-agnostic *select* hides three different
gestures behind one verb.

## 3. Agency

**Before:** Kerning is stored in the kern feature and spacing can be adjusted
using the arrow keys.

**After:** FontLab stores the kerning in the font's `kern` feature. You adjust
spacing with ++Alt++ and the arrow keys.

*Changed:* the app acts, or you act. Passive voice removes the actor, and in a
procedure the actor is the whole point.

## 4. Ambiguous participle

**Before:** Using the Contour tool, the nodes can be moved along the italic
angle.

**After:** If ==Contour > Coordinates > Follow Italic Angle== is turned on, and
you move an anchor with the ++Up++ or ++Down++ arrow keys, the anchor movement
follows the italic angle.

*Changed:* the participle had no subject. The rewrite names the setting, the
actor, the keys, and the result, in that order.

## 5. Condition before action

**Before:** Double-click the Contour tool icon in the toolbar to open the
toolbox and turn on the first icon, if Power Nudge is not already on.

**After:** To toggle Power Nudge, double-click the ==Contour== tool icon in the
toolbar to open the toolbox, and turn on the first icon, or press ++Shift+C++.

*Changed:* the goal moved to the front so a reader who does not want it can
abandon the step before performing it.

## 6. A sentence that is correctly long

**Before:** Snapping works with zones and guides. It also works with hints and
nodes. Angles, stem distances, continuation lines, perpendicular lines and
centerlines are supported too.

**After:** Dynamically snap to zones, guides, hints, nodes, angles, stem
distances, continuation lines, perpendicular lines and centerlines.

*Changed:* nothing was too long. One enumerating sentence at 20 words reads as a
list of what the feature covers; three sentences read as three separate
features. Do not chop an enumeration to hit a cap.

## 7. STE and the house corpus pulling apart

**Before, an STE-style rewrite:** Stroke allows different thickness on either
side. Stroke does not allow diagonal contrast. Diagonal contrast is global
thickness modulation along a diagonal axis. A broad-nib pen makes it.

**After, the house sentence:** Stroke allows different thickness on either side,
but does not allow diagonal contrast (global thickness modulation along a
diagonal axis, like made by a broad-nib pen).

*Changed:* nothing, and that is the point. STE's 20-word cap would win if this
were a numbered step. It is a concept paragraph, so the corpus wins: capability
and limit in one sentence joined by "but", with the definition of the missing
thing parked in a parenthesis the reader can skip. The rule: the cap stops the
moment the sentence stops being something the reader executes.

## 8. A limitation reframed as a positioning

**Before:** TransType focuses on producing reliable static output.

**After:** TransType does not export a new variable font. The output is always
static.

*Changed:* the negation came back. A buyer needs the restriction, and the
reframe reads as a feature wearing a limitation's grammar.

## 9. The invented closing paragraph

**Before:** For precise control of the naming, please use ==File > Font Info==.
#4933

With these improvements, FontLab 8 gives you more control over glyph naming than
ever before, so you can focus on what matters most: your design.

**After:** For precise control of the naming, please use ==File > Font Info==.
#4933

*Changed:* the terminal paragraph added no fact. House documents end on the last
technical item, including a restriction or an issue number.

## 10. Adverbs as a symptom

**Before:** The new stroke engine works really smoothly and handles complex
contours very efficiently.

**After:** The all-new stroke engine adds flexibility to how you specify outline
strokes for existing contours, and allows you to create skeleton-based drawings.

*Changed:* "really smoothly" and "very efficiently" were propping up verbs that
said nothing. The replacement names what the engine does, which is what the
adverbs were pretending to.

## 11. The metaphor budget

**Before:** FontLab is an integrated font creation workhorse. It puts you in the
driver's seat, gives you a Swiss army knife of drawing tools, and lets your
creativity take flight.

**After:** FontLab 8 is an integrated font creation workhorse.

Rapidly build glyphs from components or from always-editable element references.
Automate complex glyphs with ==Auto layers==. Join design parts and add flair
with ==Skin== and ==Glue==.

*Changed:* one image, one vehicle, spent in sentence one. The three that
followed were three vehicles fighting. The energy is paid back with named tools
rather than more pictures.

## 12. Troubleshooting starts at the symptom

**Before:** FontLab's font naming validation is designed to help you catch
problems in a font's name records before conversion. When a font is flagged, it
means the naming may require attention.

**After:** If TransType marks a font red, it wants you to review that font's
naming. Check it before you convert.

*Changed:* the reader arrives holding a red row, not a curiosity about
validation design. Start where they are, then say what to do.

## 13. A tooltip is reference at fifteen words

**Before:** This useful option lets you control whether or not the stroke
thickness will be taken into account when FontLab is calculating sidebearings.

**After:** Ignore stroke thickness when calculating sidebearings.

*Changed:* a tooltip has one job. The cadence rules do not apply below roughly
40 words, but agency, accuracy and the interface conventions still do.

## 14. Reference prose that hides the fact

**Before:** It is generally considered to be the case that the ascender
dimension is something that can be described as the distance measured from the
baseline up to the ascender line, and it can be important for spacing.

**After:** The distance from the baseline to the ascender line defines the
ascender dimension. It may extend above cap height, depending on the design.
FontLab uses it for vertical metrics and line spacing.

*Changed:* the fact moved into the first half of the first sentence, the hedge
became a real caveat with a reason, and the vague "important for spacing" became
the two things it is actually used for.
