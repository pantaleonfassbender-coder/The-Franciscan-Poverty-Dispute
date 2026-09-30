"""Build data/chronicle.json: Glassberger's Chronica on 1322-1329 (Analecta Franciscana II, 1887).

Conventions in tools/chronicle_text.py.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from chronicle_text import SECTIONS  # noqa: E402

OUT = Path(__file__).resolve().parent.parent / "data" / "chronicle.json"


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
        "titel": "The order's chronicle: Perugia, the appeal, the flight (1322–1329)",
        "autor": "Nicholas Glassberger (d. c. 1520), Franciscan of the Observance at Nuremberg, Chronica, written c. 1491–1508 and drawing for these years on the fourteenth-century Chronicle of the Twenty-Four Generals",
        "jahr": "1322–1329, written c. 1500",
        "orig_sprache": "la",
        "pg_label": "Anal. Franc. II p.",
        "quelle": "Chronica fratris Nicolai Glassberger, in Analecta Franciscana, tom. II (Ad Claras Aquas [Quaracchi]: Collegium S. Bonaventurae, 1887), pp. 129–133, 140, 145–146. Internet Archive, analectafrancisc02coll. Public domain.",
        "hinweis": "The Latin is the Quaracchi editors' text, read against every page image; their footnotes supply dates and parallels in the notes. Glassberger copies the Chronicle of the Twenty-Four Generals for these years, and with it the text of the Perugia letter of 4 June 1322, which is also printed by Wadding and in Baluze's Miscellanea; the editors give their variants. The chronicler writes from inside an order that had submitted: he blames Michael's want of reverence and the Dominicans' suggestions for the pope's anger. His year for the flight (1327) is counted from the Incarnation. Cuts are marked […]. The English is this site's working translation (CC0).",
        "sections": sections,
    }
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{OUT.name}: {sum(len(s['units']) for s in sections)} units in {len(sections)} sections")


if __name__ == "__main__":
    build()
