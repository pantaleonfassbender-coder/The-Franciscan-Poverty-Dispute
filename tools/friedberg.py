"""Compare two independent OCRs of Friedberg, Corpus iuris canonici II.

Both are scans of the unaltered photomechanical reprints of the Leipzig
edition of 1881 (Graz 1955, Internet Archive BD1141952; Graz 1959, Internet
Archive CorpusIurisCanoniciIAemiliusFriedberg1959), i.e. of the same type.
Save their djvu.txt files as tools/src/fr1955.txt and tools/src/fr1959.txt.

    python tools/friedberg.py "Quia  nonnunquam," "Ad  conditorem  canonum  non"

prints the running text between the two incipits as read by the 1955 OCR,
with the words where the 1959 OCR disagrees marked [1955|1959]. Running
heads, column numbers and Friedberg's apparatus of variants are removed;
his footnote marks (digits, with or without an asterisk) are stripped.
The page image decides every disagreement.
"""
import difflib
import re
import sys
from pathlib import Path

SRC = Path(__file__).resolve().parent / "src"


def load(name):
    return (SRC / name).read_text(encoding="utf-8", errors="replace")


def segment(text, start, end):
    s = norm_space(text)
    a = s.index(norm_space(start))
    b = s.index(norm_space(end), a + 1) if end else len(s)
    return s[a:b]


def norm_space(t):
    return re.sub(r"[ \t]+", " ", t)


APPARATUS = re.compile(r"(^|\s)\d{1,2}\s?\)\s")          # "3) et:" entries
HEAD = re.compile(r"EXTRA\s?VAG|DE VERBORUM|^\s*\d{3,4}\s*$|^\s*c\.\s*[\dim]", re.I)


def clean(seg):
    out = []
    skip = False
    for line in seg.splitlines():
        l = line.strip()
        if not l:
            continue
        if re.match(r"^T\s*[il1I]\s*t\.\s*X", l) or re.match(r"^(Cap|!ap|oap|CAP)\.?\s*[IVXivx]+\.?\s*\d\)", l):
            skip = True          # start of the apparatus block
        if skip:
            if len(APPARATUS.findall(l)) == 0 and len(l) > 45 and not re.search(r"[A-Z]{2,}\s*$", l):
                skip = False     # back in the text
            else:
                continue
        if HEAD.search(l):
            continue
        if len(APPARATUS.findall(l)) >= 2:
            continue
        out.append(l)
    t = "\n".join(out)
    t = re.sub(r"[-¬]\s*\n\s*", "", t)                  # joined hyphenations
    t = re.sub(r"\s*\n\s*", " ", t)
    t = t.replace("ſ", "s")
    t = re.sub(r"(?<=[A-Za-zäöü,.;:)])\s?\d{1,2}\s?[*•°®]?(?=[\s,.;:)])", "", t)   # footnote marks
    t = re.sub(r"\s+", " ", t)
    return t.strip()


def words(t):
    return t.split(" ")


def main(start, end):
    a = clean(segment(load("fr1955.txt"), start, end))
    b = clean(segment(load("fr1959.txt"), start, end))
    A, B = words(a), words(b)
    key = lambda w: re.sub(r"[^a-z]", "", w.lower())
    sm = difflib.SequenceMatcher(None, [key(w) for w in A], [key(w) for w in B], autojunk=False)
    out, n = [], 0
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal":
            out.extend(A[i1:i2])
        else:
            n += 1
            out.append("[" + " ".join(A[i1:i2]) + "|" + " ".join(B[j1:j2]) + "]")
    print(" ".join(out))
    print(f"\n-- {n} disagreements", file=sys.stderr)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
