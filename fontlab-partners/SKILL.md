---
name: fontlab-partners
description: >-
  Write and update content in the fontlab-partners repository, source for partners.fontlab.com,
  FontLab's affiliate and press site. Use for a partner site page, an affiliate page, partners.fontlab.com
  copy, a press kit page, a download page, a FAQ entry, commission copy, join flow copy, or a
  marketing pack description. Covers where content lives versus what is generated, required
  frontmatter by content type, the FAQ system, the duplicated call-to-action band, the asset
  whitelist, and the site's naming and register conventions.
license: MIT
metadata:
  version: "1.0.0"
  family: fontlab-writing
---

# FontLab Partners site

This skill is about the `fontlab-partners` repository, source for **partners.fontlab.com**. Read `README.md` in that repo before any non-trivial change; it is more current than `CLAUDE.md`.

## What the site is, who reads it

Affiliates and press deciding whether to promote FontLab products. Three pages plus a FAQ: the landing page (`/`), the affiliate join flow (`/join/`), and the press kit download page (`/downloads/`). Nobody here is a FontLab user looking for help. This is a business proposition, not a product manual: benefit-first, concrete numbers, no feature-tour tone.

## Where content lives, what is generated

Never hand-edit `docs/`. It is the full build output, wiped and regenerated on every `./build.sh build`.

Live source:
- `src_docs/md/`: `index.md` (landing), `join.md`, `downloads.md`, `404.md`, plus `CNAME` and `robots.txt` copied verbatim.
- `src_docs/faq/<category>/*.md`: one FAQ question per file, six category folders.

Generated, never hand-edit:
- `src_docs/_partials/_faq_partial.md`: built by `./build.sh faq` from `src_docs/faq/`, pulled into `index.md` via `--8<-- "_faq_partial.md"`. Edit the FAQ source files and rebuild instead.
- `docs/`: the whole rendered site.

Ignore `md/` at the repo root (a separate, legacy tree; `src_docs/md/` is the live one, and the two should not be confused).

`README.md`'s architecture section is current: everything is ProperDocs, `index.md` renders like any other page, there is no separate landing-page HTML assembly step. `CLAUDE.md` still describes a `src_docs/landing/` scaffold and a splice-the-FAQ-into-HTML build order; that directory does not exist on disk. Trust `README.md` over `CLAUDE.md` on architecture and build order.

## Frontmatter by content type

Nothing validates frontmatter here. A wrong field name fails silently: the page still builds, just wrong or missing content.

- **Landing and sub-pages** (`src_docs/md/*.md`): `title` (required), `description` (SEO meta, one sentence, marketing-toned, used verbatim as the meta description). `index.md` also carries `hide: [toc]`. `404.md` has only `title`.
- **FAQ entries** (`src_docs/faq/<category>/*.md`): `question:` only. The body is the answer. Using `title` instead of `question` here will not error; it will just not render as a question.

## The FAQ system

One question per file, plain 1-3 paragraph answers (occasionally a table or bullet list), direct and reassuring tone. Six category folders, assembled in this fixed, hardcoded order: `general → commissions → payouts → tracking → promotion → legal`. It is not alphabetical and not folder-listing order.

Adding a question: drop a new Markdown file with a `question:` field into the right category folder, then rebuild. Adding a new category is not a content change: it needs a code change in `src/fontlab_partners/cli.py`, where `FAQ_CATEGORY_ORDER` and `FAQ_CATEGORY_LABELS` are hardcoded.

## The duplicated call-to-action band

The bottom CTA band (`<section id="join" class="fl-band fl-cta-band">`) appears verbatim, independently, in `index.md`, `join.md`, and `downloads.md`. There is no shared partial for it; each copy is hand-maintained. This is exactly how two real drift bugs happened here:

- the support email differs by page: `partners@fontlab.com` on `404.md`, `partnersupport@fontlab.com` in the CTA bands
- the cookie window figure disagrees between a design document and the live site: `SPEC.md` cites "180-day cookie" while every live CTA band says "30-day cookie"

Any change to the CTA band's wording (support contact, commission rate, cookie window, fineprint) must be applied to all three files. Find every copy with:

```
grep -rn "fl-cta-band" src_docs/md/*.md
```

Do not treat one occurrence as the canonical source and let the others drift.

## Assets

Downloadable packs are per-product ZIPs (`fontlab-banners.zip`, `fontlab-marketingpack-fontlab-8.zip`, `fontlab-marketingpack-transtype-4.zip`, `fontlab-marketingpack-company.zip`) built from `src_assets/`, not a single bundle file. `README.md`'s own text says the whitelist lives at `assets/assets.txt`, but on disk it is `src_assets/assets.txt` (a list of pack folder names) plus one `assets.csv` per pack under `src_assets/<pack-name>/assets.csv` (one file path per row). Trust the code (`src/fontlab_partners/cli.py`, `_read_pack_list` and `_read_pack_csv`) over that README passage.

- Adding a file to an **existing** pack: drop it in `src_assets/<pack-name>/` and add its relative path as a new row in `src_assets/<pack-name>/assets.csv`.
- Adding a **new** pack: create `src_assets/<new-pack-name>/assets.csv`, put the files there, and add `<new-pack-name>` as a new line in `src_assets/assets.txt`.

Writing the Markdown for a new download without a matching pack/whitelist entry passes locally but fails `./build.sh build --strict-assets`, which CI runs on every tag push.

## Naming traps

**TransType 4 vs 5.** The site says "TransType 4" everywhere: page copy, FAQ commission tables, filenames, asset paths (`fontlab-marketingpack-transtype-4.zip`, `icon-transtype4-512x512.png`). If you know the current product is TransType 5, do not silently rename it in this repo. Surface the mismatch to a human first: the whole asset pipeline (pack name, CSV, icon filenames) is keyed to "4", so a rename is a multi-file, cross-checked change, not a find-and-replace.

**Non-breaking spaces.** Product name and version number are joined with `&nbsp;` in the source Markdown/HTML: `FontLab&nbsp;8`, `TransType&nbsp;4`, `Vexy&nbsp;Lines`. Nothing enforces this; it is easy to drop when typing new copy by hand. Keep it.

## Stale guidance in the repo

`CLAUDE.md` is the file explicitly aimed at AI assistants, but its "High-level architecture" section describes a `src_docs/landing/` directory that does not exist. `README.md` is current. `issues/101.md`, which both files call "the canonical spec," is 39 lines and only documents the asset-pack build mechanics. It is not a content or copy spec; don't expect writing guidance there.

## Register

Direct, benefit-first, concrete numbers. No hype, no feature-tour language. Real lines from the live copy:

> Recommend the font editor professionals trust. Earn on every sale.

> Our affiliate partnership program offers 15% commission on every transaction: $75 with the $500 FontLab lifetime license list price, or $15 with Vexy Lines, TransType or 3-month FontLab.

> The program is free to join and takes less than 24 hours to get started.

State the number, not the adjective. "15% commission," "30-day cookie," "$75 per sale," "less than 24 hours" carry the pitch; words like "amazing" or "seamless" do not appear in the live copy and should not appear in new copy either.

## Related skills

`fontlab-neutral` for informational FontLab prose. `fontlab-marketing` for copy that sells FontLab products themselves (not this affiliate site). `fontlab-terminology` for product names and terms.

Trap checklist: `references/traps.md`.

<!-- fontlab:shared:start -->
## House rules

This block is identical in every FontLab writing skill. It is calibrated against a measured corpus of 76,386 words that Adam Twardoch wrote himself: the FontLab 8 "what's new" essays and release notes, and the FontLab and TransType landing pages. Where a rule cites a number, the number came from counting that corpus, not from taste.

**H1. Agency.** You act. The app responds. Apps apply. Fonts and files have no agency. Write "FontLab stores the kerning in the font's `kern` feature", not "kerning is stored". Write "you adjust spacing with Alt and the arrow keys", not "spacing can be adjusted". A font can have a feature; it cannot do anything.

**H2. Never invent a fact.** Every number, name, date, menu label, keyboard shortcut, default, error string, version, and quotation comes from the source or from the user. Nothing else does. When a needed specific is missing, leave a visible placeholder: `[ADD VERIFIED METRIC]`, `[CONFIRM LABEL]`, `[CONFIRM DEFAULT]`. A plausible guess is the worst possible output, because it is the one nobody checks.

**H3. Never inflate certainty past the source.** "May reduce" does not become "eliminates". Keep every load-bearing caveat, especially about compatibility, licensing, data loss, and platform differences. **Never convert a limitation into a positioning.** "TransType does not export a new variable font" must not become "TransType focuses on static output".

**H4. Do not install a personality that is not there,** and do not remove the one that is. Manufactured stakes, performed candor, invented reader emotion ("you feel it by five o'clock"), and forced contrarianism are a new fingerprint. So is stripping the writer's own habits. You may reorder sentences, split paragraphs, and move a conclusion up. You may not add a fact, an attribution, a stake, or a stance the source did not have.

**H5. Cadence, with measured targets.** In neutral product prose the corpus runs a mean sentence length near 20 words with a standard deviation near 12, and 15 percent of sentences exceed 30 words. Do not cap sentences at 25 words: long enumerating sentences are part of the register. In marketing the mean drops to 11 to 15 words and a third of sentences run under 8. Match the register, and vary hard inside it.

**H6. One concrete specific per paragraph, minimum.** A name, a number, a mechanism, a tradeoff, a menu path, a version, an issue number. Issue numbers, build numbers, menu paths and version strings are load-bearing: never trim them for flow.

**H7. Dashes have a shape rule, not a ban.** The corpus prefers a colon over an em dash by about 47 to 1 in neutral prose. So prefer the colon. What is forbidden is the appositive gloss dash, the machine tell: `noun phrase, em dash, two adjectives of atmosphere`. What is permitted is the turn dash, where what follows the dash carries a finite verb or negates what preceded it, at roughly one per 3,000 words of neutral prose and one per 400 words of marketing. En dashes between words: no.

**H8. Banned vocabulary.** delve, leverage, seamless, robust, pivotal, crucial, comprehensive, transformative, game-changing, cutting-edge, meticulous, vibrant, intricate, nuanced, holistic, ever-evolving, tapestry, realm, elevate, unlock, unleash, harness, empower, foster, underscore, showcase, garner, bolster. Also the constructions "serves as", "stands as", "is a testament to", "boasts", and participle analysis tails such as ", highlighting its importance". A banned word inside a quotation or a product's own interface string stays.

**H9. Forbidden constructions, measured at zero in the corpus.** "It's not X, it's Y" (0 in 76,386 words). Comparison scaffolds: Before and After, The old way and The new way, Today versus With FontLab (0 instances; the corpus frame is "Previously, ... now ..."). Rhetorical questions in marketing body copy (0). A closing paragraph that adds no new fact (0 of 13 essays end with a summary or a call to action). A benefit clause standing alone as its own sentence: weld the benefit to the mechanism with "so you can", or drop it.

**H10. What to protect, because an editor will remove it.** Exclamation marks, at about one per 400 words in marketing and overview prose and one per 4,000 in reference prose. The rule of three, which is 7.6 percent of marketing sentences and the highest rate in the corpus. One travelling idiom per document. Self-undercutting asides ("it's up to you!", "this is just a suggestion"). Customer quotations with their repetition intact. The bare ampersand in headings. Bolded verbs rather than bolded nouns in marketing. Single-sentence paragraphs, which are 45 to 57 percent of neutral paragraphs: never merge them into developed paragraphs.

**H11. Names.** FontLab is the product; Fontlab Ltd. is the company. Lowercase `fontlab` is correct only in the Python module name and in domains. Product names never translate. FontLab and the Vexy products share nouns that mean different things: Layers, Masks, Groups, Fills, Brush, Knife, Transform, and at least Pencil, Eraser, Scissors. Name the app whenever a reader could be confused. A document may declare its own short form once, then must use it.

**H12. Do not touch** quotations, code, code blocks, command lines, file paths, identifiers, API names, URLs, licence text, interface strings, or data inside table cells.

**H13. Registers differ, and the rules bend with them.** Documentation and reference prose take sentence case, effectively no exclamation marks, and no title case. The marketing surface uses title case for pillar names and capitals for eyebrows, and it carries exclamation marks. Applying the documentation rules to a landing page produces prose the house did not write.

**H14. Two passes, always.** Pass one drafts. Pass two rereads the draft as a skeptic asking one question: what in this still reads as machine-written? Then sweep for the forbidden constructions in H9 and check that nothing in H10 was quietly removed.

**H15. Very short pieces.** Below roughly 40 words, H5 and H6 do not apply. H1, H2, H3, H4, H7, H8, H9 and H11 apply at every length, tooltips and button labels included.

**H16. The override.** Break any rule here sooner than write something worse. If a flagged word is the right word, keep it. Small roughness that carries rhythm, including the occasional comma splice, is not a defect to repair.
<!-- fontlab:shared:end -->
