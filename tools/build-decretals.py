"""Build data/decretals.json: the decretals of John XXII, Extrav. Ioann. XXII 14.1-5.

Source: Friedberg, Corpus iuris canonici II (Leipzig 1881), cols. 1220-1236.
Conventions in tools/decretals_text.py; OCR comparison in tools/friedberg.py.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from decretals_text import SECTIONS  # noqa: E402

OUT = Path(__file__).resolve().parent.parent / "data" / "decretals.json"


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
        "titel": "The pope's dossier: the decretals of John XXII, 1317–1324",
        "autor": "Pope John XXII (Jacques Duèze, pope 1316–1334), five decretals collected among his Extravagantes under the title 'On the meaning of words' (De verborum significatione)",
        "jahr": "1317–1324",
        "orig_sprache": "la",
        "pg_label": "Friedberg col.",
        "quelle": "Corpus iuris canonici, ed. Emil Friedberg, vol. II: Decretalium collectiones (Leipzig: Tauchnitz, 1881), Extravagantes Ioannis XXII, tit. XIV De verborum significatione, c. 1–5, cols. 1220–1236. Read from the unaltered photomechanical reprint (Graz: Akademische Druck- und Verlagsanstalt, 1955), Internet Archive BD1141952; checked against the second reprint (Graz 1959). Public domain.",
        "hinweis": "The Latin is Friedberg's text. Two independent OCRs of the reprint were compared word by word, and every disagreement, every rare word form and every column carried was read against the page image; errors the two OCRs shared (concordandae for concordantiae, sea for sed, elavem for clavem, and letters lost at line ends) were corrected from the page. Friedberg's spelling (quum, diffinire), punctuation and brackets are kept; his footnote marks and apparatus are dropped, and the variants that matter are given in the notes (among them the manuscripts' 'Nicholas III' where his text prints 'Nicholas IV'). Quia nonnunquam, Ad conditorem canonum and Quum inter nonnullos are carried in full; Quorundam exigit and Quia quorundam in excerpts, the cuts marked […]. The medieval summaries (summaria) Friedberg prints before each chapter are translated in the notes, as later additions. The English is this site's working translation (CC0), rendering the legal terms for sense and giving the Latin in brackets where the argument turns on them.",
        "sections": sections,
    }
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{OUT.name}: {sum(len(s['units']) for s in sections)} units in {len(sections)} sections")


if __name__ == "__main__":
    build()
