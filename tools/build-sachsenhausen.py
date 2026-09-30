"""Build data/sachsenhausen.json: the appeal of Sachsenhausen, 22 May 1324 (MGH Const. V nr. 909).

Conventions in tools/sachsenhausen_text.py.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from sachsenhausen_text import SECTIONS  # noqa: E402

OUT = Path(__file__).resolve().parent.parent / "data" / "sachsenhausen.json"


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
        "titel": "The appeal of Sachsenhausen (22 May 1324)",
        "autor": "Louis IV the Bavarian (king of the Romans 1314, emperor 1328, d. 1347); the chapter on poverty drafted by Friars Minor at his court",
        "jahr": "22 May 1324",
        "orig_sprache": "la",
        "pg_label": "MGH Const. V p.",
        "quelle": "Monumenta Germaniae Historica, Legum sectio IV: Constitutiones et acta publica imperatorum et regum, tom. V, ed. Iacobus Schwalm (Hannover and Leipzig: Hahn, 1909–1913), nr. 909 (Forma prior), pp. 722–745, and nr. 910, pp. 753–754. Internet Archive, monumentagerma05geseuoft. Public domain.",
        "hinweis": "The appeal survives in two forms: a first form that Friars Minor seem to have drafted for the king (nr. 909) and a second revised in the royal chancery (nr. 910); both carry the chapter on poverty. The excerpts are from the first form, read from the page images of Schwalm's edition, with his spelling; his apparatus of variants is not carried, and cuts are marked […]. Date and place are those of the chancery form. The English is this site's working translation (CC0).",
        "sections": sections,
    }
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{OUT.name}: {sum(len(s['units']) for s in sections)} units in {len(sections)} sections")


if __name__ == "__main__":
    build()
