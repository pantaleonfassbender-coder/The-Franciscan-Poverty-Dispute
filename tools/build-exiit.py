"""Build data/exiit.json: Exiit qui seminat (Sext 5.12.3) and Exivi de paradiso (Clem. 5.11.1).

Source: Friedberg, Corpus iuris canonici II (Leipzig 1881), cols. 1109-1121 and 1193-1199.
Conventions in tools/exiit_text.py; OCR comparison in tools/friedberg.py.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from exiit_text import SECTIONS  # noqa: E402

OUT = Path(__file__).resolve().parent.parent / "data" / "exiit.json"


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
        "titel": "The old decretals: Exiit qui seminat and Exivi de paradiso",
        "autor": "Pope Nicholas III (1277–1280), Exiit qui seminat, and Pope Clement V (1305–1314) at the Council of Vienne, Exivi de paradiso: the two papal declarations on the Franciscan rule that the dispute of the 1320s was about",
        "jahr": "1279 and 1312",
        "orig_sprache": "la",
        "pg_label": "Friedberg col.",
        "quelle": "Corpus iuris canonici, ed. Emil Friedberg, vol. II (Leipzig: Tauchnitz, 1881): Liber Sextus 5.12.3 (Exiit qui seminat), cols. 1109–1121; Clementinae 5.11.1 (Exivi de paradiso), cols. 1193–1199. Read from the unaltered photomechanical reprint (Graz 1955), Internet Archive BD1141952. Public domain.",
        "hinweis": "The Latin is Friedberg's text in excerpts: eight from Exiit (about a fifth of it) and four from Exivi. It was taken from the OCR of the 1959 reprint and read against the page image excerpt by excerpt; the corrections made from the page are listed in the build file. Friedberg's spelling, punctuation and brackets are kept, his footnote marks dropped; cuts are marked […]. The medieval summaries printed before each decretal are translated in the notes. The English is this site's working translation (CC0), with the Latin technical terms in brackets where the argument turns on them.",
        "sections": sections,
    }
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{OUT.name}: {sum(len(s['units']) for s in sections)} units in {len(sections)} sections")


if __name__ == "__main__":
    build()
