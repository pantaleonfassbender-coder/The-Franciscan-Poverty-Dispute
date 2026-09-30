# The Franciscan Poverty Dispute

A documentary apparatus for the Franciscan poverty dispute, 1316–1329: did Christ and the apostles own anything, individually or in common? Public-domain sources with the Latin beside a working English translation, a timeline linked into the texts, and a list of what is still to come.

Its thesis: the argument was won and the order was lost. Pope John XXII did not refute the Franciscan doctrine of poverty; he abolished its legal basis (1322), declared its central claim heretical (1323) and its defenders heretics (1324). The minister general Michael of Cesena fled to the emperor with William of Ockham in 1328 and died excommunicated in Munich; the order submitted. The argument about poverty became an argument about the power of popes.

Stage 1 (September 2026, in progress) carries two modules:

- **The old decretals: Exiit qui seminat and Exivi de paradiso** — Nicholas III (1279, Sext 5.12.3) and Clement V at Vienne (1312, Clem. 5.11.1), in Friedberg's *Corpus iuris canonici* II, cols. 1109–1121 and 1193–1199: the definition of Franciscan poverty, Christ's purse, the five degrees from property to the simple use of fact, the Roman Church's ownership, money through a third hand, the ban on glossing; the Spirituals' complaints and the ruling on 'poor use'. Excerpts, Latin read against the page images, with a working translation.
- **The pope's dossier: the decretals of John XXII** — Extravagantes Ioannis XXII, tit. XIV *De verborum significatione*, c. 1–5 (1317–1324), in Friedberg's *Corpus iuris canonici* II (Leipzig 1881), cols. 1220–1236: *Quorundam exigit* (excerpts), *Quia nonnunquam*, *Ad conditorem canonum*, *Quum inter nonnullos* (in full), *Quia quorundam* (excerpts). Latin from two OCRs of the photomechanical reprint compared word by word and read against the page images, with a working translation.

A **Compare** page sets Nicholas III beside John XXII on five questions (the purse, use without ownership, the owner of the friars' bread, the ban on discussion, whether a pope can revoke a pope).

Planned modules and their sources (the chapter of Perugia, the order's chronicle, Michael's appeal, the emperor's appeal of Sachsenhausen, Ockham, Bernard Gui, Angelo Clareno, Dante's *Paradiso* XI) are listed on the Texts page (`data/modules.json`).

The companion game *Nec in communi* takes its title from the condemned sentence of 1323: that Christ and the apostles had nothing *in speciali … nec in communi etiam*.

## Building the data

```
python tools/build-exiit.py
python tools/build-decretals.py
```

The texts are kept in `tools/exiit_text.py` and `tools/decretals_text.py`. `tools/friedberg.py "incipit" "end"` prints the two OCRs of Friedberg's volume II side by side with their disagreements marked; it expects the OCR files in `tools/src/` (Internet Archive `BD1141952_djvu.txt` saved as `fr1955.txt`, and the volume II text of `CorpusIurisCanoniciIAemiliusFriedberg1959` as `fr1959.txt`).

## Running locally

Any static server, e.g. `python -m http.server 8137`.

Licences: see `LICENSES.md`.
