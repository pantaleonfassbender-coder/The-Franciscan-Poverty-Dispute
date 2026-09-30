"""Build data/gui.json: Bernard Gui, Practica, part V ch. IV on the Beguins (Douais 1886).

Conventions in tools/gui_text.py.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from gui_text import SECTIONS  # noqa: E402

OUT = Path(__file__).resolve().parent.parent / "data" / "gui.json"


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
        "titel": "Bernard Gui's manual: the sect of the Beguins",
        "autor": "Bernard Gui (c. 1261–1331), Dominican, inquisitor of Toulouse 1307–1324, then bishop of Lodève",
        "jahr": "c. 1323–1324",
        "orig_sprache": "la",
        "pg_label": "Douais p.",
        "quelle": "Practica inquisitionis heretice pravitatis auctore Bernardo Guidonis, ed. C. Douais (Paris: Alphonse Picard, 1886), part V, ch. IV, pp. 264–278. Internet Archive, practicainquisit00bern (University of Toronto, Pontifical Institute of Mediaeval Studies). Public domain.",
        "hinweis": "Douais edited the manual from the Toulouse manuscript; his text is kept with its medieval spelling and his restorations in brackets, without the manuscript folio marks. The OCR of this printing is good, and each excerpt was read against the page images. Eleven excerpts from the chapter on the Beguins; the chapter goes on with their teaching on the Antichrist and the carnal Church, and with further questions, not carried here; cuts are marked […]. The English is this site's working translation (CC0).",
        "sections": sections,
    }
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{OUT.name}: {sum(len(s['units']) for s in sections)} units in {len(sections)} sections")


if __name__ == "__main__":
    build()
