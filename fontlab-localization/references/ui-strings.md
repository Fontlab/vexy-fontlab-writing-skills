<!-- this_file: fontlab-localization/references/ui-strings.md -->

# Interface strings

*Portable copy of the FontLab writing guide's localization page of the same name, snapshot of 28 September 2026. The live page and the term tables it links to are in the `vexy-fontlab-writing-styleguide` repository; use newer supplied project data when it disagrees.*


The localization principles say how a term is chosen and how
long a label may be. This page covers the mechanics of a Qt catalog string that
a reviewer must check whatever the language: mnemonics, shortcuts, placeholders,
reused words, whitespace, framework strings and the strings that should never
have been translatable. It draws on the localization literature the company
keeps (Esselink, Uren, Roturier, Jiménez-Crespo, Microsoft's *Developing
International Software*) and on the FontLab 9 review.

## The English text is the key

Qt looks a translation up by context, source text and disambiguation comment.
Rewording a shipped English string, even to fix a typo, orphans its translation
in every catalog: the old entry becomes *vanished* and a new unfinished entry
appears. A source edit therefore needs a behavioral reason, and the
source review records it. When the
English is wrong but the control's behavior is clear, translate the behavior
and file the source defect; do not wait for the English to change.

Two English strings that differ only in a trailing space, an ellipsis or a
capital are two entries. Keep the difference in the translation: the ellipsis
announces a dialog, the trailing space means the application appends text.

## One word, several meanings

*None*, *All*, *Auto*, *Default*, *Copy*, *Scale*, *Fill* and *Close* are
nouns, verbs or adjectives depending on the control. German *Keine* or *Kein*
follows the gender of a noun the string never mentions; Spanish *primero*,
*primera*, *primer* agree with something off-screen. When one English entry
serves several controls with different grammar, do not pick the form that fits
most of them. Ask the developer for a disambiguation comment or a split string,
and record the request in the source review. Until it lands, choose the form
that fits the most visible control and note the compromise in the ledger.

The reverse failure is silent: two source strings in one context collapsing
into one translation. *Cancel* and *Undo* must not both become *Annuler*. The
verification scripts flag duplicate targets within a context; treat each hit as
a question, not an error, because *Font* and *Fonts* may legitimately share a
form in a language without number agreement.

## Mnemonics

An ampersand marks the mnemonic letter of a menu item, button or label. The
German catalog carries about four hundred of them.

- Keep exactly one ampersand per label. A literal ampersand in running text is
  written `&&`.
- Choose a letter that exists in the translation. *File* takes *D* in *Datei*,
  not *F*. It need not be the first letter.
- Keep the letter unique within its menu or dialog. Items inserted at runtime
  count: context menus, *Show* and *Hide* pairs, toggles. Only the running
  build shows these collisions, so review the working interface.
- Prefer letters without descenders. The underline vanishes into *g*, *j*,
  *p*, *q* and *y*.
- Avoid accented letters and letters that move between keyboard layouts.
- Standard commands keep the letter the platform uses in that language. Check
  the localized operating system, not the English one.
- If the translator comment fixes the mnemonic position, respect it or flag
  the string as impossible. Do not move the marker quietly.
- Chinese, Japanese and Korean keep the source letter in parentheses after the
  translation: *ファイル(F)*.

## Shortcuts and key names

Never change a function-key combination. Change a letter or symbol combination
only when the key cannot be typed on the local layout: `@`, `$`, `{`, `}`,
`[`, `]`, `\`, `~` and `|` are the usual problems, and French keyboards need
Shift for digits, so a Ctrl+digit shortcut needs testing. A changed shortcut
is an engineering change: the label and the binding move together, and the
change is recorded as a source defect, not a translation choice.

Key names come from the platform, not from the catalog: German *Umschalt*,
French *Maj*, Polish *Shift* on macOS but *Shift* or *Wielkie litery* by
context. A shortcut named in prose (*press Ctrl+Q*) keeps the platform's
spelling of the modifier.

## Placeholders and assembled sentences

Qt's numbered placeholders (`%1`, `%2`, `%L1`, `%n`) may be reordered; anonymous
`%s` may not. Reorder freely where target grammar needs it. Never change the
placeholder syntax during a prose edit.

Which value fills `%1` is fixed by the code. A translator cannot infer it from
the sentence and cannot swap two values because the target reads better. Ask
what each value is before translating the words between placeholders: *%1 to
%2* is a date range, a copy destination or a numeric span, and each takes a
different preposition.

A placeholder that stands for a noun breaks agreement: *This is not a valid
%1*, *%1 already exists. Replace it?* The adjective and the pronoun depend on
a gender the string does not know. Recast as label and value (*%1: invalid
value*), choose a verb that does not agree, or ask for one string per case.
Report the source; do not guess.

A trailing space or a string that is obviously the first half of a sentence
means the application assembles text at runtime. Verb-final German and
case-marking Polish cannot survive that. When the prefix cannot be reordered,
a colon rescues the grammar (*Widerrufen: Ausschneiden*), and the source review
records the fragment. Punctuation may also be appended by code: check the
running interface before adding or removing a final period, or the user sees
two.

## Plural forms

Qt numerus strings carry one form per Qt plural rule, which is not the CLDR
category list. Polish has three Qt forms (1; 2 to 4 except 12 to 14; the rest)
while CLDR has four, the fourth being fractions, which take the genitive
singular. Test 0, 1, 2, 5, 12, 22 and 25 in every numerus string. Reject a
*one* branch that prints a literal *1* in a language where *one* covers other
values (French *one* includes 0). Keep an explicit *=0* branch separate from
the plural category when the source has one.

## Whitespace, punctuation and literal characters

- Keep leading and trailing spaces. A dropped trailing space before an inserted
  name glues two words on screen.
- Keep ellipses and tab-separated shortcut suffixes.
- Escape inner quotation marks as the file format requires, or use the target
  language's own marks: „…“ in German, « … » with no-break spaces in French,
  „…” in Polish.
- Keep `\n` and `\t`. They are syntax.
- Type diacritics as precomposed characters (NFC). Decomposed forms and
  presentation ligatures (ﬁ, ﬂ) break search, sorting and glyph lookup.

## Strings that are not text

Leave untouched: date-pattern letters (`dddd`, `yyyy`), registry and preference
keys, file and folder names, config-file names, internal command tokens,
command-line switches, OpenType tags, glyph names, Python identifiers, paths and
URLs. Treat a word in all capitals, a word with underscores and a run-together
word as an identifier until an engineer confirms otherwise. Debug-only messages
stay in English so a developer can read a bug report from any locale; if one
reaches the catalog, mark it in the source review rather than translating it.

## Accessibility and hidden strings

Tooltips, status tips, *What's This* text, accessible names and accessible
descriptions are catalog strings the reviewer never sees on screen. They must be
translated, and they must agree with the visible label they describe. A
localized build is often less accessible than the English one for no better
reason than that nobody looked.

## Framework strings

Qt's own dialogs, button boxes and messages come from the `qtbase_<code>`
catalog, not from FontLab's. A build that ships without it shows an English
*Cancel* beside a German *Öffnen*. The release checklist includes the framework
catalogs, and translators receive the framework's terms so that FontLab's
strings match them: *Abbrechen* is Qt's word and the platform's, and the FontLab
catalog uses it too.

Standard operating-system commands (*Copy*, *Paste*, *Quit*, *Undo*, *Show in
Finder*, *Preferences* versus *Settings*) follow the localized platform. This is
the one place where Apple and Microsoft rank above Glyphs and FontForge: users
expect the OS word, and platform owners enforce it.

## The product's voice and the company's voice

A catalog mixes messages in which the application speaks to the user with
prose in which the company speaks. *Cannot open %1* is the product; *Thank you
for trying FontLab* is the company. Each has its own register in every
language, and both arrive out of context. Identify which voice a string uses
before choosing address, tense and warmth. Drop the first person from product
messages, do not copy exclamation marks by reflex, and remove chatty openers
where the target register is more formal.

## Consistency the user can feel

A command and the dialog it opens share one wording: *Save As…* and its title
bar are one translation. Menus and repeated controls give the whole product
its coherence through repetition, so render them identically everywhere; a
help paragraph may vary. Commands, buttons and status-bar texts each use one
grammatical form throughout, following the target platform's convention
(German infinitives for commands, Spanish infinitives, French infinitives for
menu items and imperatives for steps). Every label quoted in the Help Panel or
the manual is the label in the catalog, verified by script rather than memory.
