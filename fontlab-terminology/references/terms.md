# FontLab and Vexy term list

This file is the portable term list for the `fontlab-terminology` skill. It travels with the skill and needs nothing else installed. Read it before ruling on a word.

Five sections: the settled names, the domains, the collision nouns, the names that carry no house form yet, and the domain vocabulary table.

## 1. Settled names

| Written form | What it names | Notes |
| --- | --- | --- |
| FontLab | The desktop font editor | Capital F and capital L in every position |
| Fontlab Ltd. | The company | Lowercase l, full stop after Ltd. Both spellings sit in one sentence in the shipped trademark notices, on purpose |
| FontLab 8 | The current release of the editor | One space before the number |
| FontLab Studio 5 | The editor that preceded the rewrite | Attested in shipped interface text. Historical mentions only |
| FontLab Pass | The identity and licensing service | Lives at `pass.fontlab.com` |
| FontLab account | The single identity across the products | Lowercase account |
| `fontlab` | The Python module | Lowercase, code font. Python module names are lowercase |
| TransType 5 | The font conversion application | One word, two capitals, version on first mention. Its own manual declares the short form TrT; use that only inside that manual |
| Fontographer | The browser based font editor | One word, capital F, no space, no version number in the name |
| Vexy | The family prefix | Never a product on its own. Also an Illustrator effect category |
| Vexy Lines | The standalone desktop application | Two words, both capitalized, never hyphenated |
| Vexy Linestra | The Illustrator plug-in for parametric line work | Two words. `VexyLinestra.aip` is a filename, not prose |
| Vexy Playlines | The web application at `playlines.vexy.art` | Two words. A different product from Vexy Lines |
| Vexy Vextra | The Illustrator plug-in for contour editing | Two words. Its manual declares the short form Vextra |
| Vexy coins | The credits that pay for charged operations | Capital V, lowercase coins |
| Adobe Illustrator | The host application for the Vexy plug-ins | Full name on first mention, then Illustrator |
| Photofont | A trademark of Fontlab Ltd. | One word |
| TypeTool | A trademark of Fontlab Ltd. | One word, two capitals |
| Dream Up | The Fontographer shape generator | Two words. Dream Up Font generates a whole font |

**Vexy Lines and Vexy Playlines are different products.** Lines is the desktop application; Playlines is the web application. They share vocabulary and are easy to confuse, so every mention carries enough context to tell them apart.

**A document may declare its own short form once**, then must use it consistently: "This manual calls it Vextra." Silent alternation between the long and short name is a defect.

## 2. Domains

Domains are lowercase, take no `www`, and go in code font in prose.

| Domain | What runs there |
| --- | --- |
| `fontlab.com` | The main website |
| `help.fontlab.com` | FontLab and TransType documentation |
| `pass.fontlab.com` | Sign-in and licence management |
| `forum.fontlab.com` | The user forum |
| `app.fontographer.net` | Where Fontographer runs |
| `help.vexy.art` | Documentation for the four Vexy products |
| `playlines.vexy.art` | Where Vexy Playlines runs |

## 3. Collision nouns

FontLab and the Vexy products use these ten words for different things. The list is open, so the working rule is broader than the list: name the application whenever a reader who knows only one product could misread the sentence.

**Layers.** FontLab: a layer of a glyph, holding a master, a mask, or a background, listed in the Layers and Masters panel. Vexy Lines: a transparent sheet holding one or more fills, and the basic unit of a document. Vexy Vextra, following Illustrator: a stacking level of artwork.

**Masks.** FontLab: a glyph layer carrying a previous version or a reference shape that you edit against. It conceals nothing, and the full phrase is mask layer. Vexy Lines: a vector stencil that decides where a layer's fills can draw, letting fill through its transparent areas. Illustrator's clipping mask is a third sense.

**Groups.** FontLab: a kerning group, the same idea as a kerning class. Vexy Vextra and Illustrator: artwork bound into a single object. Vexy Lines: a bundle of layers carrying its own source image, behaving like a folder, with the document itself as the top-level group. TransType: a styling group that links the styles of a family. Never write group alone. Write kerning group, artwork group, layer group, or styling group.

**Fills.** FontLab: the Fill tool colours a closed contour, and winding direction decides what fills. Vexy Lines, Linestra, and Playlines: a fill is a generative technique such as Linear, Wave, Halftone, or Stipple. In the Vexy products prefer the phrase fill mode.

**Brush.** FontLab and Fontographer: a calligraphic tool that keeps the drawn path as a centreline and generates the outline from it, becoming ordinary contours only when you expand it. FontLab adds a Brush panel for angle and width; Fontographer groups Brush with Pencil and Thickness on one toolbar button. Vexy Lines: a tool that paints masks freehand, not artwork. Name the app and say what the stroke becomes.

**Knife.** FontLab: one tool with three sub-tools, Add nodes, Break contour, and Slice contour, so only Slice leaves two closed shapes. Fontographer: cuts through contours along a drawn path, sharing the grouped cutting toolbar button with Scissors. Vexy Lines: inserts points and splits curves on Handmade fills and mask contours. Vexy Vextra: adds nodes and breaks a path at a node. Name the app and the mode.

**Transform.** FontLab: the Transform panel, a numeric transformation applied to a selection or across a font. Fontographer and Vexy Lines: a Transform tool on the canvas. Say whether you mean the panel or the tool.

**Pencil.** FontLab and Fontographer: a freehand tool that draws glyph contours, grouped in Fontographer with Brush and Thickness on one toolbar button. Vexy Lines: draws the vector lines of a Handmade fill. Vexy Vextra: the Correcting Pencil, which redraws part of an existing path. In Vextra use the full name Correcting Pencil.

**Eraser.** FontLab: removes nodes and handles from a contour and can simplify a path, so it edits points rather than erasing shape. Vexy Vextra: removes points from a path or cleans a curve while holding its shape. Fontographer: grouped with Trowel on one toolbar button, so a procedure says which mode is active first. Say that points go, not ink.

**Scissors.** FontLab: disconnects nodes, creates overlaps, adds ink traps, and builds looped corners. Fontographer: breaks a contour at a chosen point or segment, sharing the grouped cutting button with Knife. Vexy Vextra: extends and rebuilds path parts, joining open ends. The name suggests cutting everywhere and means something different in each.

The test: could a reader who knows only one of the two products misread this sentence? If yes, name the app.

## 4. Names with no house form yet

These four are flagged, never rewritten. They come in two kinds.

**Three draft names.** No house form has been decided. Flag the occurrence and ask which version or service the page means. Do not invent a form.

- **FontLab 9.** The shipped Fontographer manual prints it: the import and export tables name VFJ as the format for moving source data to FontLab 9. The FontLab manuals and the Python API reference still name FontLab 8, so both numbers are in circulation. Ask which version a page describes before you print a number.
- **Fontographer.net.** The name the FontLab interface gives a Fontographer project, in the tooltip behind File: Open Fontographer.net project. The manuals write Fontographer for the software and `app.fontographer.net` for the address. Keep Fontographer.net only when quoting the interface label.
- **studio.fontlab.com.** Named in project briefs, mentioned in no shipped manual. The attested domains are in section 2 and this is not among them.

**One retired name.** **Strokes Maker** is the former name of Vexy Lines. The house form is Vexy Lines, including when you describe what the old version did. Strokes Maker is correct only in a historical statement or a migration note: "Vexy Lines, released earlier as Strokes Maker, reads a bitmap and draws vector fills." Flag every occurrence anyway, because whether a given sentence is a legitimate historical mention or copy nobody has touched since the rename is the author's call, not yours. A retired name in current copy tells a reader the page is stale.

**A version mismatch, not a naming error.** The partner site at `partners.fontlab.com` currently says TransType 4 throughout, and those strings are keyed to asset filenames. Flag it as a mismatch against TransType 5 and say that the filenames are the reason. Do not correct it in place: changing the prose without the assets breaks the pairing.

## 5. Domain vocabulary

One line each. Where a term appears in section 3, this table gives the short form and section 3 gives the collision.

### Type design

| Term | Meaning |
| --- | --- |
| glyph | One drawn shape in a font: a letter, a figure, a mark, or a piece of a composite |
| character | A unit of text as Unicode defines it, identified by a codepoint and a name |
| contour | A closed or open chain of nodes and segments that bounds a shape |
| node | A point on a contour where segments meet; its type decides how they meet |
| handle | The control point that sets the direction and depth of a curve segment leaving a node |
| segment | The piece of contour between two nodes, straight or curved |
| extremum | The point where a curve reaches its leftmost, rightmost, topmost, or bottommost position |
| stem | A main stroke of a letter, usually the vertical one |
| serif | The finishing stroke at the end of a stem or arm |
| terminal | The end of a stroke that carries no serif |
| bowl | The rounded stroke that encloses a counter, as in b, d, p, and o |
| counter | The enclosed or partly enclosed space inside a letter |
| baseline | The horizontal line the letters sit on, and the origin for vertical measurement |
| x-height | The height of a lowercase x above the baseline |
| cap height | The height of a flat topped capital above the baseline |
| ascender | The part of a lowercase letter that rises above the x-height |
| descender | The part of a lowercase letter that falls below the baseline |
| overshoot | The small amount by which a round shape passes an alignment line so it looks level |
| UPM | Units per em: the size of the design grid a font is drawn on |
| winding direction | The order a contour runs, clockwise or counter-clockwise, deciding what fills |

### Font engineering

| Term | Meaning |
| --- | --- |
| advance width | How far the text cursor moves after a glyph, measured in font units |
| sidebearing | The space between a glyph's outline and the edge of its advance width, left and right |
| metrics | The measurements that place a glyph in a line: advance width and the two sidebearings |
| kerning | A correction to the space between two particular glyphs, on top of their sidebearings |
| kerning pair | Two glyphs and the value that adjusts the space between them |
| kerning class | A group of glyphs that need the same kerning |
| kern exception | A pair value that overrides what the classes would otherwise apply |
| visual kerning | Kerning FontLab proposes by measuring the shapes |
| tracking | A uniform change to the space between all glyphs in a run of text |
| master | One complete set of drawings at a defined position in the design space |
| instance | A named position in the design space that ships as a style |
| axis | One dimension of variation in a family: weight, width, optical size, or a custom one |
| design space | The whole territory the axes define, with the masters as fixed points in it |
| interpolation | Calculation of the shapes between masters, node by node |
| master compatibility | The condition every glyph must meet before it can interpolate |
| variable font | One file covering a whole design space, with axes a reader can move |
| component | A reference to another glyph placed inside this one |
| composite glyph | A glyph built from references to other glyphs rather than its own outlines |
| element | FontLab's container for a piece of drawing inside a glyph |
| element reference | A placed copy of an element that still points at the original |
| anchor | A named attachment point in a glyph that says where a mark belongs |
| mark attachment | The OpenType mechanism that positions a combining mark against a base glyph |
| hinting | The extra information a font carries so its outlines land predictably on a pixel grid |
| autohinting | Generation of hints from the outlines, stems, and zones in one pass |
| alignment zone | A band around an alignment line wide enough to hold the overshoot of round shapes |
| stem link | A tie between two edges of a stroke so hinting can hold their distance |
| typographic family name | The name grouping every style of a family under one entry |
| styling group name | The name tying together the styles an application reaches through bold and italic |
| conversion profile | The saved set of choices TransType applies to a conversion |
| font target | What TransType produces from a source: the output font with its format and names |

### OpenType

| Term | Meaning |
| --- | --- |
| OpenType feature | A named piece of typographic behaviour a font offers, such as `liga` |
| feature code | The text syntax describing OpenType features: classes, lookups, rules |
| lookup | One group of rules inside GSUB or GPOS, of a single type, applied as a unit |
| OpenType class | A named group of glyphs feature code can address at once, written with an at sign |
| GSUB | The table holding substitutions: one glyph for another, one for many, many for one |
| GPOS | The table holding positioning: kerning, mark attachment, cursive attachment |
| cmap | The table mapping Unicode codepoints to glyphs |
| OS/2 table | The table carrying metadata for applications: vertical metrics, weight and width classes |
| CVT table | The control values TrueType hinting instructions refer to |
| colour font table | The extra tables a colour font carries; several formats, because platforms disagreed |
| glyph name | The identifier of a glyph inside the font and inside every feature you write |
| glyph index | The number a glyph occupies in the font's own order, counting from zero |
| Unicode codepoint | The number Unicode assigns to a character, written with a U plus prefix |
| Private Use Area | The Unicode range reserved for meanings no standard assigns |
| Adobe Glyph List | The map from standard glyph names to Unicode codepoints |
| ligature | One glyph standing for two or more characters, such as fi or ffl |
| small caps | Capital shapes at roughly lowercase height, with their own weight and width |
| oldstyle figures | Numerals drawn with ascenders and descenders so they sit in running text |
| tabular figures | Figures all carrying the same advance width, so columns line up |
| fractions | The `frac` feature, building fractions from figures and a slash |
| stylistic set | A numbered group of alternate glyphs, `ss01` through `ss20` |
| contextual alternates | The `calt` feature: substitutions made because of what sits around a glyph |
| localized forms | The `locl` feature: substitutions made because of the language of the text |

### File formats

| Term | Meaning |
| --- | --- |
| VFC | FontLab's native binary format, and the one you work in |
| VFJ | The text form of FontLab's native format, the same content as readable JSON |
| VFB | The native format of FontLab Studio 5; FontLab 8 opens it |
| UFO | The open, tool independent source format for a single font, a folder of XML files |
| Glyphs file | The source format of the Glyphs editor, which FontLab reads and writes |
| Fog.net | Fontographer's project data format; `fognet` is the Python module that reads it |
| OTF | An OpenType font with PostScript flavoured outlines in a CFF table, cubic curves |
| TTF | An OpenType font with TrueType flavoured outlines, quadratic curves in `glyf` |
| TTC | A collection file holding several fonts in one binary, sharing common tables |
| WOFF2 | The web font format: an OpenType font wrapped and compressed with Brotli |
| Type 1 | Adobe's original PostScript format, shipped as PFB or PFA with separate metrics |
| AI file | An Adobe Illustrator document, the container the Vexy plug-ins work inside |
| AIP | An Adobe Illustrator plug-in binary, how Linestra and Vextra reach Illustrator |
| Lines file | The native document of Vexy Lines: source image, fills, and masks |
| SVG | The vector graphics format; also names an OpenType colour table |
| FLREQ | The licence request file written when a machine cannot reach the licensing service |

Write an extension lowercase with the dot: `.vfc`, `.ufo`, `.otf`. Write the format name in the case the table gives.

### Interface and vector

| Term | Meaning |
| --- | --- |
| panel | A dockable area holding controls for one subject, such as the Kerning panel |
| dialog | A modal box that waits for an answer before anything else continues |
| property bar | The strip of controls that changes with the current tool and selection |
| Sketchboard | FontLab's unlimited canvas for placing glyphs, drawings, and notes |
| FontAudit | The FontLab panel that inspects outlines and reports problems |
| Matchmaker | The FontLab tool that repairs master compatibility |
| Power Nudge | Moving a node while adjusting the surrounding handles so the curve keeps its shape |
| Smart Corner | A live treatment at a node: rounded, cut, or turned into an ink trap |
| Remove Overlap | Merging overlapping contours into one outline |
| Sigma | The Fontographer tool for variable font interpolation paths |
| stroke | The line drawn along a path, with a weight, a colour, and an alignment |
| centerline | A path down the middle of a stroke rather than around its edge |
| autotrace | Conversion of a bitmap into vector paths by finding edges and fitting curves |
| fill mode | One of the named Vexy techniques turning a source image into line work |
| Fill Grid | The area of the Linestra panel where you choose a fill mode from previews |
| tonal map | The reading of brightness across a source image that a fill uses |
| Live Effect | An Illustrator effect that stays editable on the object it is applied to |
| Appearance panel | Illustrator's list of what is applied to the selected object |
| Tunni line | The line joining the two handles of a curve segment, with a control on it |
| G2 continuity | Two segments meeting with matching curvature, not merely matching direction |
