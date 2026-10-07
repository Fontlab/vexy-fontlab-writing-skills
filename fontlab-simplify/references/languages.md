---
this_file: fontlab-simplify/references/languages.md
---

# Simplification in other languages

When the target text is not English, apply that locale's own easy-to-read or
plain-language conventions. Never carry English sentence rules over word for
word: Finnish has no articles to keep, Czech inflects its numbers, and a
Chinese sentence fails in different places from an English one.

Two rules hold in every language:

- **Plain** writing applies to all FontLab help. **Easy-to-read** is a separate
  product for dedicated material: onboarding, error recovery, accessibility
  notes, or a support reply to a reader who needs the simplest version.
- The FontLab locale's terminology, form of address and formatting rules win
  over a national easy-to-read edition in ordinary help. Use the edition's form
  only in dedicated easy-to-read material.

Most national editions of the Inclusion Europe rules share a baseline: one idea
per sentence, each sentence on a new line, a full stop instead of a comma plus
"and", no hyphenation at line ends, active and positive wording, initials
expanded, idioms avoided, numbers as digits, no Roman numerals, and dates
written out in full. In dedicated easy-to-read pages, mark interface labels with
the house highlight (bold as the fallback), never italics, and align text left.
Wherever the edition replaces a percentage or a large number with "few" or
"many", do so only for values the reader does not need exactly; a setting, limit or
measurement keeps its number.

## Albanian (sq)

Local name: **i lehtë për t'u lexuar** and **i lehtë për t'u kuptuar**.

- Prefer an active verb to a passive or reflexive one: **Mjeku do t'ju dërgojë
  një letër** rather than **do t'ju dërgohet një letër**.
- Replace ordinals such as **takimi i 7të** with a count of meetings held so
  far.
- Write **nuk** rather than the contracted **s'** in easy-to-read text only.
- Write dates out with lowercase weekday and month: **e martë, më 13 tetor
  2026**.
- Write out **p.sh.** and **etj.**

FontLab wins: **ti** address, and **s'është** and the abbreviations stay in
ordinary help.

## Chinese (zh)

Local name: **简明写作** (plain writing). Apply the ISO 24495-1 questions: can
the reader find, understand and act on the text?

- Lead with the result or action and give the reason after it. Cut empty
  openers such as **众所周知** and **如前所述**.
- Drop filler verbs that wrap the real action: **对字形进行缩放** becomes
  **缩放字形**, **加以确认** becomes **确认**. Keep **进行** only where the bare verb
  reads badly. Check **实现**, **相关**, **有关** and **方面** the same way: **相关设置**
  should name the settings.
- Give every **该**, **此** and **其** one identifiable referent. Split a sentence
  with three or more **的** or a long modifier before its noun.
- Replace stacked set phrases (**不可或缺**) and classical residue (**之**, **乃**)
  with plain modern words.
- In requirement text (submission specifications, API contracts, licence
  terms), use the GB/T 1.1-2020 modal verbs: **应**/**不应** for a requirement,
  **宜**/**不宜** for a recommendation, **可**/**不必** for a permission,
  **能**/**不能** for capability. Never write **可** for **能**; pair **尽量** and
  **通常** with **宜**, not **应**; *should* never becomes **必须**. Example:
  **字形名宜符合 AGL 规范。**

Character limits per sentence are rules of thumb, not standards. FontLab wins:
terminology, voice and tone rules, and the interface pattern **不能…** in
everyday help.

## Croatian (hr)

Local name: **lako razumljive informacije**.

- Prefer the active form: **Doktor će vam poslati pismo**, not **Pismo će vam
  biti poslano**.
- Repeat the name when a pronoun could refer to two people.
- Write the full word, not an apostrophe contraction: **kao**, not **k'o**.
- Dates go in figures with the weekday, **utorak, 13. 10. 2026.**, which reverses
  the usual month-as-word preference.
- Count instead of using an ordinal such as **7. sastanak**.

FontLab wins: formal **vi** address and the spaced numeric date typography.

## Czech (cs)

Local names: **snadno srozumitelné** information, **jednoduché čtení** style.

- Choose the everyday word, **rozesílat** over **distribuovat**, and keep it:
  a text that says **zaměstnání** does not switch to **práce**.
- Numbers follow inflection. Spell out an ordinal the reader would have to
  decline (**sedmá schůzka**), use digits elsewhere, and write **třikrát**, not
  **3x**.
- Dates in full: **úterý 13. října 2026**.
- Avoid **např.** and **atd.**; keep the nonbreaking space after one-letter
  prepositions.

FontLab wins: lowercase **vy** address; digits stay for exact values and
interface matches.

## Estonian (et)

Local name: **lihtsas keeles** or **lihtsalt loetav**.

- The active-voice rule becomes "personal over impersonal": **Arst saadab teile
  kirja**, not **Teile saadetakse kiri**.
- Write the full word instead of colloquial short forms such as **okei**.
- Write out **nt** and **jne**; prefer the present tense.
- Dates in full, weekday lowercase: **teisipäev, 13. oktoober 2026**.
- Keep correct case on every number: **2 faili**.

FontLab wins: **teie** address. The edition's **sina** belongs only in dedicated
material that has chosen it.

## Finnish (fi)

Local name: **selkokieli** (also **helppolukuinen**); Selkokeskus is the
national reference point.

- Name the actor even though the passive is idiomatic: **Lääkäri lähettää
  sinulle kirjeen** rather than **Sinulle lähetetään kirje**.
- Prefer affirmative sentences, but an affirmative rewrite must say the same
  thing.
- Write **esimerkiksi**, not **esim.**, and replace **&** with **ja**.
- Present a series as a bulleted list, not inside a sentence.

The Finnish edition has no language-specific section on numbers or dates, so
the FontLab locale rules apply there. FontLab wins: terminology; **sinä**
already matches.

## French (fr)

Local name: **facile à lire et à comprendre**, widely known as **FALC** (spell
the abbreviation out in easy-to-read text).

- Active and positive: **Le médecin vous enverra une lettre**.
- Avoid deep numbering such as **1.2.1** and write out **par ex.** and **etc.**
- No Roman numerals, including centuries: **le 21e siècle**.
- Dates with the weekday: **mardi 13 octobre 2026**, never the month alone.

FontLab wins: French spacing stays, including nonbreaking spaces before **:**
and **?** and inside **« … »**; **vous** already matches.

## German (de)

Local name: **Leichte Sprache**, capitalized as a name.

- Name the actor: **Peter hat die Besprechung abgesagt**, not **Die Besprechung
  wurde abgesagt**.
- Narrate the past in the Perfekt, not the Präteritum.
- Name mixed groups in both forms, feminine first (**Lehrerinnen und
  Lehrer**), or use a short neutral form.
- Break long compounds with a hyphen: **Gleichstellungs-Gesetz**.
- Avoid **z. B.**, **etc.**, footnotes, and ordinals such as **das 7. Treffen**.

FontLab wins: **Sie** address, and closed compounds such as **Dateiname** in
labels and ordinary help. Hyphenated compounds belong only in Leichte Sprache
text.

## Hungarian (hu)

Local name: **könnyen érthető kommunikáció**.

- Explain a **mozaikszó**: **EU** is **Európai Unió**.
- Replace an ordinal with a count: **Eddig 6 találkozónk volt.**
- Dates in full: **2026. október 13., kedd**.
- Number document pages as **1/15** so the reader knows the total.

Unlike most editions, the Hungarian one does not push the active voice; do not
force it. FontLab wins: polite third-person address (**Nyissa meg a fájlt.**),
and the suffix and article rules in every register.

## Italian (it)

Local name: **facile da leggere e da capire**.

- Use the **passato prossimo**, not the **passato remoto**: **ha salvato**, not
  **salvò**.
- Prefer indicative and imperative to conditional and subjunctive, but keep a
  hypothetical such as **se il file fosse aperto** when the meaning needs it.
- Positive instructions: **devi rimanere fino alla fine**.
- Avoid **ecc.**, **p.es.**, **&** and **§**; never put needed information in a
  footnote.

FontLab wins: **tu** address; interface dates keep their locale format.

## Lithuanian (lt)

Local name: **lengvai skaitoma informacija** or **lengvai suprantama
informacija**.

- The active-voice rule means avoiding participles: **Mes atsiųsime jums
  laišką**, not **Jums bus atsiųstas laiškas**.
- Prefer short words; the edition counts long words as an obstacle.
- Cardinals as digits (**2 sąsiuvinius**), ordinals as words (**pirmą kartą**).
- Dates spelled out without abbreviation: **2026 metų spalio 13 diena**.
- Avoid **pvz.**, **t. t.** and symbols such as **&**, **§** and **#**.

FontLab wins: lowercase **jūs**, usually carried by the verb; UI status strings
keep their neuter participles (**Diegiama**); interface dates keep ISO form.

## Polish (pl)

Local name: **tekst łatwy do czytania (i zrozumienia)**, also **ETR**.

- Active voice: **Doktor przyśle ci list**.
- Count instead of a suffixed ordinal: **W tym roku odbyło się już 5 spotkań**,
  not **5-te spotkanie**.
- Expand acronyms (**PCK** is **Polski Czerwony Krzyż**) and avoid **tzw.** and
  **m.in.**
- Dates in full: **wtorek, 13 października 2026**.

FontLab wins: the capitalized **Ty**/**Twój** convention and gender-neutral
forms, not the edition's lowercase **ty** and masculine **Powinieneś**; the
approved terms for **font** and **krój pisma**, which the edition treats as one
thing; interface dates keep their format.

## Portuguese, Brazilian (pt)

Local name: **linguagem simples**. Brazil's Lei nº 15.263/2025 set up a
national plain-language policy for public administration; the Brazilian adoption of
ISO 24495-1 is ABNT NBR ISO 24495-1:2024. Neither binds FontLab, but Brazilian
readers increasingly expect the practice.

- Turn noun-plus-verb pairs into the verb: **realizar a verificação** becomes
  **verificar**.
- Cut bureaucratic formulas such as **no que tange a** and **supracitado**;
  replace pronoun-like **o mesmo** with the noun.
- Remove gerundismo: **vamos estar enviando** becomes **vamos enviar**. A progress
  message such as **Salvando o arquivo.** is a different form and stays.
- Name the actor when it matters (**Ative a licença**), keep the passive when
  the actor is obvious (**O arquivo foi salvo.**).
- Keep **pode ter falhado**, **apenas**, **exceto** and **até**.

FontLab wins: **você** with third-person verbs, the terminology decisions and
exact interface labels.

## Portuguese, European (pt-pt)

Local name: **leitura fácil**.

- Active voice: **O João comeu o bolo**.
- Avoid clitic object pronouns; repeat the noun.
- Use spoken tenses: **Amanhã vou ao cinema**, not **irei**.
- Dates in full: **terça-feira, 13 de outubro de 2026**; write **número**, not
  **n.º**.

FontLab wins: third-person verbs without **você** (**Guarde o ficheiro.**), and
current spelling (**diretamente**, lowercase **outubro**) over the edition's
pre-agreement forms.

## Romanian (ro)

Local name: usually **ușor de citit** (și de înțeles). No Romanian edition of
the Inclusion Europe rules exists, so apply the shared baseline through the
Romanian locale's conventions.

- Active voice: **Echipa de asistență vă trimite un e-mail**, not **Vi se va
  trimite un e-mail**.
- Positive instructions: **Salvați fișierul înainte să închideți aplicația**.
- Replace **&** with **și** and **/** with **sau**; avoid **nr.** and **de ex.**
- Dates in full: **marți, 13 octombrie 2026**.
- Keep comma-below **ș** and **ț**, also in large-print layouts.

FontLab wins: the polite plural address, terminology and notation rules;
interface dates keep their locale format.

## Serbian (sr, sr-latn)

Local name: **лако разумљиве информације** / **lako razumljive informacije**.

- Active voice: **Doktor će vam poslati pismo**.
- Count instead of an ordinal: **Već smo imali 6 sastanaka.**
- Keep the full form: **je li**, not **je l'**.
- Dates in numbers with the weekday, **utorak, 13.10.2026.**, reversing the
  month-as-word baseline.
- Never copy the edition's **1,758,625**; it reads as a decimal in Serbian.

Check the script of every letter. Both editions mix scripts, and the Latin one
uses Cyrillic **ј** inside **lj**; such text fails search and spell-checking.
FontLab wins: formal **vi** (already matching), Serbian number notation.

## Slovak (sk)

Local names: **ľahko zrozumiteľné informácie**, **ľahko čitateľné texty**.

- Minimize words starting with the negative **ne-**: **Zostaňte až do konca
  stretnutia**.
- Active voice: **Lekár vám pošle list**.
- Dates with the month as a word, in the genitive: **utorok 13. októbra 2026**.
- Avoid **napr.** and **atď.**

The edition calls serif type **ozdobné písmo**; never carry that into FontLab
text, where serif and decorative type differ. FontLab wins: formal **vy**,
terminology, and notation such as **63 %**.

## Slovenian (sl)

Local name: **lahko berljiva in razumljiva informacija**.

- Replace symbols and abbreviations with words: **od … do** for a range dash,
  **ali** for a slash, **in** for **&**, **na primer** for **npr.**
- Break a two-line sentence at a comma.
- Replace an avoidable foreign word: **vsota**, not **suma**.

The edition allows, and itself uses, all capitals. FontLab wins: sentence case
in interface text and help, keeping **Č**, **Š** and **Ž** in any all-capitals
print version; the formal plural address; range and percent notation in
ordinary help.

## Spanish (es-es)

Local name: **lectura fácil** (lowercase in running text).

- Active voice: **el doctor te enviará una carta**.
- Rewrite ordinals: **la reunión número 7**, not **la 7ª reunión**.
- Prefer the present and avoid the subjunctive, but only in dedicated material
  and only when the condition or possibility survives.
- Dates in full: **martes 13 de octubre de 2026**; avoid **Gral.** and **etc.**

FontLab wins: regional vocabulary, terminology and the tense-and-mood
distinctions in ordinary help; **tú** already matches.

Sources: Inclusion Europe: Information for all
(https://inclusion.eu/easy-to-read/guidelines/), ISO 24495-1, GB/T 1.1-2020.
