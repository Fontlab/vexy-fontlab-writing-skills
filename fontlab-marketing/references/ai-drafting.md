<!-- this_file: fontlab-marketing/references/ai-drafting.md -->

# Drafting marketing copy with a model

A model writes the average of what it has read. The house voice is the part the
average leaves out: the named object, the condition, the honest limit, the
detail someone noticed. These cases show how to brief, mark and review.

## Material, not adjectives

> **Weak brief:** Write a friendly, professional, exciting product page for our
> font editor.
>
> **Working brief:** Write the opening section of a product page for owners of
> version 4. Use only the attached fact sheet, the version 5 changelog and the
> two approved pages in `examples/`. If a fact you need is not in them, write
> [NEED: what is missing]. Do not state a price, date, compatibility or
> performance claim that is not in the fact sheet. Before drafting, ask me up to
> five questions about the reader and the offer.

Adjectives describe a voice; examples demonstrate it. A few approved
pieces in the same register teach more than any list of tone words.

## A fixed set of markers

Use the same markers in every brief so drafts can be scanned:

| Marker | Meaning |
|---|---|
| `[NEED: …]` | A fact is missing |
| `[CLAIM: …]` | A claim needs evidence before publication |
| `[DECIDE: …]` | A policy or offer decision belongs to a person |
| `[ASK ME: …]` | The writer's own input was too vague |

The house placeholders `[VERIFY CLAIM]`, `[CONFIRM LABEL]` and `[CONFIRM OFFER]`
work the same way; use whichever the brief names, consistently. A draft from
thin material that contains no markers is a warning sign: the model has filled
the gaps. Before publication, a named person clears every marker. Count markers before reading the prose.

## Ask where each sentence came from

Instead of “are you sure?”, ask the model to label each sentence with its
source document, or “not in sources”. Then delete or verify every unsourced
sentence.

## The strip pass

Search every AI-assisted draft for:

- numbers, percentages and counts;
- guarantees, “free”, “always”, “lifetime”, “instantly”, and “will” in a
  promise about results;
- dates and version numbers;
- social proof (“trusted by”, “loved by”, “thousands of”);
- superlatives and adjectives any competitor could use.

Each hit stays only with a source. “Trusted by foundries worldwide” is deleted
unless a named, permissioned foundry can be cited.

## Five silent failures

Before sending a draft on, check for: an invented detail; a guess presented as
fact; quiet truncation of the requested content; a dropped instruction; an
answer to a different question than the one asked.

## A separate reviewer

Run review in a fresh session that sees only the draft, the fact sheet and the
house rules. Ask it to flag, not rewrite, and to name the rule behind each flag.
One useful reviewer prompt:

> You own version 4 and doubt you should pay for version 5. Read the draft.
> Which sentence fails to answer you, and which claim would you not believe?

The writer keeps the flags that are real and ignores the rest.

## What people write

A person writes or approves: the lead claim and headline; the offer and its
terms; any quotation, testimonial or case study; launch announcements; license
summaries. License and legal text is never paraphrased by a model.

## Voice rules from real edits

Collect pairs of first drafts and their edited versions. Ask a model to list
the differences as candidate rules. A person approves each rule, writes it as
an observable behavior (“name the object in the first sentence”, not “be
warm”) and records the date. Delete rules nobody needs. Keep a review list of
struck phrases with the reason and the usual repair; it is a prompt for
attention, not a ban that forces a worse synonym.
