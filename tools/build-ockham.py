"""Build data/ockham.json: Ockham, Opus nonaginta dierum (Goldast, Monarchia II, 1614).

Conventions in tools/ockham_text.py.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ockham_text import SECTIONS  # noqa: E402

OUT = Path(__file__).resolve().parent.parent / "data" / "ockham.json"


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
        "titel": "Ockham, Opus nonaginta dierum",
        "autor": "William of Ockham (c. 1287–1347), Friar Minor, in exile at the court of Louis the Bavarian in Munich",
        "jahr": "c. 1332–1334",
        "orig_sprache": "la",
        "pg_label": "Goldast II p.",
        "quelle": "Monarchia S. Romani Imperii, sive tractatus de iurisdictione imperiali seu regia et pontificia seu sacerdotali, ed. Melchior Goldast, tom. II (Frankfurt, 1614), pp. 993–1231. Internet Archive, bub_gb_wCH1hULfLpkC (Google scan of the Bibliothèque municipale de Lyon copy). Public domain.",
        "hinweis": "Goldast's printing, three centuries older than the critical edition, is the only public-domain text of the work; the critical edition (Guillelmi de Ockham Opera politica I–II, Manchester 1940–1963) is in copyright and is not used. The Latin was transcribed from the page images, with u and v, the ae ligature and the common abbreviations normalized; the words of the bull are kept in Goldast's brackets. Seven excerpts from a work of 124 chapters; cuts are marked […]. The English is this site's working translation (CC0).",
        "sections": sections,
    }
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{OUT.name}: {sum(len(s['units']) for s in sections)} units in {len(sections)} sections")


if __name__ == "__main__":
    build()
