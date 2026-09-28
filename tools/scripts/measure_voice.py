#!/usr/bin/env python3
# this_file: tools/scripts/measure_voice.py
"""Report approximate prose measurements and contextual review candidates.

The stored register bands are legacy comparison data, not writing requirements.
This lightweight Markdown cleanup is not a complete parser: select a coherent
prose passage and review protected quotations, labels and examples separately.
Counts do not establish correctness, usability, provenance or authorship.

Usage:
    python3 measure_voice.py FILE [FILE ...] [--register neutral|marketing|reference]
"""
import argparse
import re
import statistics
import sys
from pathlib import Path

COMPARISON_BANDS = {
    # Retained for comparisons with earlier reports. These ranges do not
    # establish the right cadence for a new document or its author.
    "neutral":   dict(mean=(10, 22), sd=(5, 15), short=(8, 30), long=(0, 21),
                      you=(8, 39), em=(0.0, 1.0), bang=(0.0, 2.5), hedge=(0.0, 1.5)),
    # Overview and announcement samples use a separate comparison group.
    "announcement": dict(mean=(8, 18), sd=(5, 15), short=(20, 55), long=(0, 12),
                         you=(8, 40), em=(0.0, 1.0), bang=(0.0, 4.5), hedge=(0.0, 2.0)),
    "marketing": dict(mean=(8, 18), sd=(5, 14), short=(15, 50), long=(0, 10),
                      you=(6, 32), em=(0.0, 3.0), bang=(0.0, 4.0), hedge=(0.0, 1.5)),
    "reference": dict(mean=(12, 24), sd=(6, 15), short=(3, 25), long=(0, 20),
                      you=(5, 40), em=(0.0, 0.5), bang=(0.0, 0.5), hedge=(0.0, 1.5)),
}

MIN_COMPARISON_WORDS = 40

REVIEW_PATTERNS = [
    (r"(?i)\bit'?s not (just )?(a |an )?\w+[^.]{0,40}, it'?s\b", "It's not X, it's Y"),
    (r"(?i)\bthis means (that )?you\b", "standalone benefit clause"),
    (r"(?i)\b(before and after|the old way|today,? with)\b", "comparison scaffold"),
    (r"(?i)\b(delve|leverage|seamless|robust|pivotal|transformative|game.changing|"
     r"cutting.edge|meticulous|vibrant|intricate|nuanced|holistic|tapestry|elevate|"
     r"unlock|unleash|harness|empower|foster|underscore|showcase)\b", "word needing context"),
    (r"(?i)\b(serves as|stands as|is a testament to|boasts)\b", "construction needing context"),
    (r"(?i)\bwe are (excited|thrilled|pleased) to\b", "excited-to-announce opener"),
    (r"(?i)\btrusted by\b(?![^.]{0,60}[A-Z][a-z]+,)", "unnamed social proof"),
    (r"[—–]\s*\w+(ly)?[, ]+\w+(ly)?\.", "possible appositive gloss dash"),
    (r"(?i)\b(today|the old way)[^.]{0,30}\bwith \w+", "Today-versus-With comparison scaffold"),
]

SENT_END = re.compile(r"(?<=[.!?])\s+")


def clean(text):
    text = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.S)          # frontmatter
    text = re.sub(r"```.*?```", " ", text, flags=re.S)                  # code fences
    text = re.sub(r"^\s*\|.*\|\s*$", " ", text, flags=re.M)             # tables
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", text)                   # images
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)                # links
    text = re.sub(r"^\s*(!{3}|\?{3})[+-]?\s+\w+.*$", " ", text, flags=re.M)  # admonition markers
    text = re.sub(r"<[^>]+>", " ", text)                                # html tags
    text = re.sub(r"\{[^}]*\}", " ", text)                              # attribute lists
    text = re.sub(r"\^\^[^^]*\^\^", " ", text)                          # badges
    text = re.sub(r"==([^=]*)==", r"\1", text)                          # ui highlight
    text = re.sub(r"\+\+([^+]*)\+\+", r"\1", text)                      # key spans
    text = re.sub(r"[*_`#>]", "", text)
    return text


def paragraphs(text):
    return [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]


def sentences(text):
    out = []
    for para in paragraphs(text):
        if para.lstrip().startswith(("-", "1.", "2.", "|")):
            out.extend(s for s in SENT_END.split(para) if s.strip())
        else:
            out.extend(s for s in SENT_END.split(para.replace("\n", " ")) if s.strip())
    return [s for s in out if len(s.split()) > 1]


def report(path, register):
    raw = Path(path).read_text(encoding="utf-8")
    text = clean(raw)
    sents = sentences(text)
    words = text.split()
    n = len(words) or 1
    lens = [len(s.split()) for s in sents]
    paras = paragraphs(text)
    single = sum(1 for p in paras if len(sentences(p)) == 1)
    t = COMPARISON_BANDS[register]

    print(f"\n{path}  register={register}")
    print("  Approximate measurements; review signals are not errors or authorship evidence.")
    if not words:
        print("  No prose to measure.")
        return 0
    if len(words) < MIN_COMPARISON_WORDS:
        print(f"  Under {MIN_COMPARISON_WORDS} words: comparison bands omitted; inspect meaning directly.")

    def per_k(pattern):
        return round(len(re.findall(pattern, text, re.I)) * 1000 / n, 2)

    rows = [
        ("words", len(words), None),
        ("sentences", len(sents), None),
        ("mean sentence", round(statistics.mean(lens), 1) if lens else 0, t["mean"]),
        ("stdev", round(statistics.pstdev(lens), 1) if len(lens) > 1 else 0, t["sd"]),
        ("pct under 8 words", round(100 * sum(1 for x in lens if x < 8) / max(1, len(lens)), 1), t["short"]),
        ("pct over 30 words", round(100 * sum(1 for x in lens if x > 30) / max(1, len(lens)), 1), t["long"]),
        ("single-sentence paras pct", round(100 * single / max(1, len(paras)), 1), None),
        ("you per 1k", per_k(r"\byou(r|rs|rself)?\b"), t["you"]),
        ("em or en dash per 1k", per_k(r"[—–]"), t["em"]),
        ("exclamations per 1k", per_k(r"!"), t["bang"]),
        ("colons per 1k", per_k(r":(?!\d)"), None),
        ("just or simply per 1k", per_k(r"\b(just|simply)\b"), t["hedge"]),
    ]
    signals = 0
    for label, value, band in rows:
        flag = ""
        if len(words) >= MIN_COMPARISON_WORDS and band and not (band[0] <= value <= band[1]):
            flag = f"  <- outside comparison range {band[0]} to {band[1]}; review context"
            signals += 1
        print(f"  {label:<28} {value:>7}{flag}")
    for pattern, name in REVIEW_PATTERNS:
        hits = re.findall(pattern, text)
        if hits:
            signals += 1
            print(f"  REVIEW     {name}: {len(hits)}")
            for h in hits[:2]:
                snippet = h if isinstance(h, str) else " ".join(x for x in h if x)
                print(f"             {snippet.strip()[:70]}")
    return signals


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+")
    ap.add_argument("--register", default="neutral", choices=sorted(COMPARISON_BANDS))
    args = ap.parse_args()
    total = sum(report(f, args.register) for f in args.files)
    print(f"\n{total} review signal(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
