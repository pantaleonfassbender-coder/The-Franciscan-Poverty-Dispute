"""Build data/appeal.json: Michael of Cesena's appeal of Avignon, 13 April 1328 (Baluze-Mansi III, 1762).

Conventions in tools/appeal_text.py.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from appeal_text import SECTIONS  # noqa: E402

OUT = Path(__file__).resolve().parent.parent / "data" / "appeal.json"


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
        "titel": "Michael of Cesena's appeal (Avignon, 13 April 1328)",
        "autor": "Michael of Cesena (c. 1270–1342), minister general of the Friars Minor 1316–1328, in a notarial instrument drawn up in the Franciscan convent of Avignon",
        "jahr": "13 April 1328",
        "orig_sprache": "la",
        "pg_label": "Mansi III p.",
        "quelle": "Stephani Baluzii Tutelensis Miscellanea novo ordine digesta, ed. Joannes Dominicus Mansi, tom. III (Lucca: apud Vincentium Junctinium, sumptibus Joannis Riccomini, 1762), pp. 238–239. Internet Archive, bub_gb_rPboqzeWk5QC (Google scan). Public domain.",
        "hinweis": "Mansi printed the appeal from a manuscript copy that still contains the copyist's instruction to insert the Perugia letter ('see above on folio …'). The machine reading of the two-column long-s type is unusable; the Latin was transcribed from the page images, with the long s set as s and the quotation marks at the head of every line dropped. The appeal is carried almost in full; the cuts are marked […]. The longer appeal Michael issued at Pisa in 1328 follows in the same volume (pp. 246 ff.) and is not carried. The English is this site's working translation (CC0).",
        "sections": sections,
    }
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{OUT.name}: {sum(len(s['units']) for s in sections)} units in {len(sections)} sections")


if __name__ == "__main__":
    build()
