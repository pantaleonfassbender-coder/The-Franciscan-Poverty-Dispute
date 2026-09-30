"""Build data/clareno.json: Angelo Clareno, Historia septem tribulationum (Ehrle 1886).

Conventions in tools/clareno_text.py.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from clareno_text import SECTIONS  # noqa: E402

OUT = Path(__file__).resolve().parent.parent / "data" / "clareno.json"


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
        "titel": "Angelo Clareno, the seven tribulations",
        "autor": "Angelo Clareno (c. 1250–1337), Spiritual Franciscan, from 1317 a Celestine hermit, writing in Italy",
        "jahr": "c. 1323–1330",
        "orig_sprache": "la",
        "pg_label": "Ehrle p.",
        "quelle": "Historia septem tribulationum ordinis minorum, sixth tribulation and the beginning of the seventh, ed. Franz Ehrle in 'Die Spiritualen, ihr Verhältniss zum Franciscanerorden und zu den Fraticellen', Archiv für Litteratur- und Kirchengeschichte des Mittelalters II (Berlin: Weidmann, 1886), pp. 125–155. Internet Archive, gri_33125006414433 (Getty Research Institute). Public domain.",
        "hinweis": "Ehrle printed this part of the Historia from a manuscript of the Biblioteca Laurenziana, with the variants of a second Latin manuscript and of an early Italian translation; his text is kept with its medieval spelling, without his folio marks and apparatus. The OCR of this printing is good, and each excerpt was read against the page images. A modern critical edition of the whole work exists and is in copyright; it is not used. Twelve excerpts; cuts are marked […]. The English is this site's working translation (CC0).",
        "sections": sections,
    }
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{OUT.name}: {sum(len(s['units']) for s in sections)} units in {len(sections)} sections")


if __name__ == "__main__":
    build()
