"""Build data/dante.json: Paradiso XI, Moore (1904) and Longfellow (1867).

Conventions in tools/dante_text.py.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from dante_text import SECTIONS  # noqa: E402

OUT = Path(__file__).resolve().parent.parent / "data" / "dante.json"


def build():
    sections = []
    for s in SECTIONS:
        units = []
        for i, u in enumerate(s["units"], 1):
            unit = {"n": i, "pg": u["pg"], "titel": u["titel"], "orig": u["orig"], "en": u["en"]}
            if u.get("note"):
                unit["note"] = u["note"]
            units.append(unit)
        sections.append({"id": s["id"], "zk": s["zk"], "titel": s["titel"], "blurb": s["blurb"], "units": units})
    data = {
        "titel": "Dante, Paradiso XI: Francis and Lady Poverty",
        "autor": "Dante Alighieri (1265–1321), Commedia, Paradiso XI, written c. 1316–1321; English by Henry Wadsworth Longfellow (1867)",
        "jahr": "c. 1316–1321",
        "orig_sprache": "it",
        "pg_label": "Moore p.",
        "quelle": "Tutte le opere di Dante Alighieri, ed. Edward Moore, 3rd ed. (Oxford: Nella stamperia dell' Università, 1904), pp. 118–119, Internet Archive tutteleoperedida00dant; The Divine Comedy of Dante Alighieri, tr. Henry Wadsworth Longfellow, vol. III: Paradiso (Boston: Ticknor and Fields, 1867), Canto XI. Both public domain.",
        "hinweis": "The Italian is Moore's Oxford text, transcribed from the page images; the widely circulated etext follows the modern critical edition of Giorgio Petrocchi (1966–67) and is not used. The English is Longfellow's line-for-line blank-verse translation, taken from the Project Gutenberg etext and checked against the 1867 printing, whose American spelling is restored. The whole canto is carried, in ten groups of tercets; each unit gives Moore's page and the line numbers. This is the one module not translated for this site.",
        "sections": sections,
    }
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{OUT.name}: {sum(len(s['units']) for s in sections)} units in {len(sections)} sections")


if __name__ == "__main__":
    build()
