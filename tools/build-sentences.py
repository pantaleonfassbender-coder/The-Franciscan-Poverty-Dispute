"""Build data/sentences.json: Bernard Gui's general sermon of Toulouse, 12 September 1322.

Source: Liber sententiarum inquisitionis Tholosanae, ed. Limborch (Amsterdam 1692), pp. 334, 381-393.
Conventions in tools/sentences_text.py.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from sentences_text import SECTIONS  # noqa: E402

OUT = Path(__file__).resolve().parent.parent / "data" / "sentences.json"


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
        "titel": "The Book of Sentences: four Beguins handed to the secular arm (Toulouse, 1322)",
        "autor": "Bernard Gui (c. 1261–1331), Dominican, inquisitor of Toulouse 1307–1323, with the vicars of the bishops of the province, in the Liber sententiarum inquisitionis Tholosanae written by the inquisition's notaries",
        "jahr": "12 September 1322",
        "orig_sprache": "la",
        "pg_label": "Limborch p.",
        "quelle": "Liber sententiarum inquisitionis Tholosanae ab anno Christi 1307 ad annum 1323, printed from the original manuscript by Philipp van Limborch, Historia inquisitionis (Amsterdam: Henricus Wetstenius, 1692), second part, pp. 334 and 381–393 (manuscript fols. 196–203 b). Internet Archive, per_witchcraft-in-europe-and-america_historia-inquisitionis_limborch-philippus_1692_2_578. Public domain.",
        "hinweis": "Limborch printed the book of sentences from the original register of the inquisition of Toulouse, then in private hands, now London, British Library, Add. MS 4697. His Latin is carried as he printed it, transcribed from the page images because the machine reading of the long s is unusable: the medieval spelling (conbustus, dyocesis, sentencia) and the ampersand are kept, the long s is set as s, and the manuscript folio numbers printed in his margin are given with each page. The excerpts follow the four persons sentenced to the secular arm in the last general sermon of Bernard Gui's register; cuts are marked […], and what is cut is summarized in the notes. The English is this site's working translation (CC0). These are the words of the court, not of the accused: the Beguins' beliefs reach us as articles drawn up by their judges from their confessions.",
        "sections": sections,
    }
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{OUT.name}: {sum(len(s['units']) for s in sections)} units in {len(sections)} sections")


if __name__ == "__main__":
    build()
