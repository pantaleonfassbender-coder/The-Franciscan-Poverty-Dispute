# The Franciscan Poverty Dispute

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23066129.svg)](https://doi.org/10.5281/zenodo.23066129)

A documentary apparatus for the Franciscan poverty dispute, 1316–1329: did Christ and the apostles own anything, individually or in common? Public-domain sources with the Latin beside a working English translation, a timeline linked into the texts, a Compare page, and a list of what is not carried and why.

Its thesis: the argument was won and the order was lost. Pope John XXII did not refute the Franciscan doctrine of poverty; he abolished its legal basis (1322), declared its central claim heretical (1323) and its defenders heretics (1324). The minister general Michael of Cesena fled to the emperor with William of Ockham in 1328 and died excommunicated in Munich; the order submitted. The argument about poverty became an argument about the power of popes.

**Stage 1 is closed (September 2026).** It carries ten modules:

- **The old decretals: Exiit qui seminat and Exivi de paradiso** — Nicholas III (1279, Sext 5.12.3) and Clement V at Vienne (1312, Clem. 5.11.1), in Friedberg's *Corpus iuris canonici* II, cols. 1109–1121 and 1193–1199: the definition of Franciscan poverty, Christ's purse, the five degrees from property to the simple use of fact, the Roman Church's ownership, money through a third hand, the ban on glossing; the Spirituals' complaints and the ruling on 'poor use'. Excerpts, Latin read against the page images, with a working translation.
- **The pope's dossier: the decretals of John XXII** — Extravagantes Ioannis XXII, tit. XIV *De verborum significatione*, c. 1–5 (1317–1324), in Friedberg's *Corpus iuris canonici* II (Leipzig 1881), cols. 1220–1236: *Quorundam exigit* (excerpts), *Quia nonnunquam*, *Ad conditorem canonum*, *Quum inter nonnullos* (in full), *Quia quorundam* (excerpts). Latin from two OCRs of the photomechanical reprint compared word by word and read against the page images, with a working translation.
- **The Book of Sentences: four Beguins handed to the secular arm** — Bernard Gui's general sermon at Toulouse, 12 September 1322, from the *Liber sententiarum inquisitionis Tholosanae* printed by Limborch (Amsterdam 1692), pp. 334 and 381–393: Guillaume Ruffi, Pierre Dominici, Pierre Hospitalis and Pierre Guiraud, their articles and their sentences. Latin transcribed from the page images, with a working translation.
- **The order's chronicle: Perugia, the appeal, the flight** — Nicholas Glassberger's chronicle in *Analecta Franciscana* II (Quaracchi 1887), pp. 129–133, 140, 145–146: the Perugia letter of 4 June 1322, Bonagratia's appeal and imprisonment, the flight of Michael, Ockham and Bonagratia, the deposition and the submission of the order. Latin read against the page images, with a working translation.
- **Michael of Cesena's appeal (Avignon, 13 April 1328)** — Baluze, *Miscellanea*, ed. Mansi, III (Lucca 1762), pp. 238–239: the summons, the audience of 9 April 1328, and the appeal 'from a just fear'. Latin transcribed from the page images, with a working translation.
- **Dante, Paradiso XI** — the whole canto in Moore's Oxford text (1904), read from the page images, with Longfellow's translation (1867).
- **The appeal of Sachsenhausen (22 May 1324)** — Louis the Bavarian against John XXII, first form (drafted with Friars Minor), *MGH Constitutiones* V, ed. Schwalm (1909–13), nr. 909, pp. 723–744: the king's charges, the chapter on the highest poverty, the oath and the appeal to a council. Excerpts, Latin read from the page images, with a working translation.
- **Ockham, Opus nonaginta dierum (c. 1332–1334)** — Goldast, *Monarchia S. Romani Imperii* II (Frankfurt 1614), pp. 993–1231: the prologue, use of fact and the right of using, the power to appropriate after the fall, Judas's purse, what a pope may change, the pertinacious heretic. Seven excerpts, Latin read from the page images, with a working translation.
- **Bernard Gui's manual: the sect of the Beguins** — *Practica inquisitionis heretice pravitatis*, ed. Douais (Paris 1886), part V ch. IV, pp. 264–278: origins and burnings, Olivi in the vernacular, houses of poverty, the articles on poverty and papal power, the martyrs of Marseille, relics, and the interrogation. Eleven excerpts, read against the page images, with a working translation.
- **Angelo Clareno, the seven tribulations** — *Historia septem tribulationum ordinis minorum*, ed. Ehrle, *Archiv für Litteratur- und Kirchengeschichte* II (1886), pp. 125–155: the sixth tribulation and the beginning of the seventh, from Olivi's violated grave through the audiences before John XXII in 1317 and the burning at Marseille to the question of 1321. Twelve excerpts, read against the page images, with a working translation.

A **Compare** page sets Nicholas III beside John XXII on five questions (the purse, use without ownership, the owner of the friars' bread, the ban on discussion, whether a pope can revoke a pope), the king's Franciscans beside John XXII on two (the seal of the rule, and the key of knowledge), Ockham beside the pope on use without a right, the Beguins beside the king's appeal on the same argument, Clareno beside the Perugia chapter, the condemned Beguins beside both on two more (granaries, and who is the heretic), and the Perugia chapter between Nicholas III and John XXII on the sentence itself.

The Texts page lists what is carried and what is not, with the reason (`data/modules.json`): above all Peter John Olivi's own writings, available in full only in modern editions in copyright; *Quia vir reprobus*, carried only through Ockham's quotations; Michael's long appeal of Pisa; the Chronicle of the Twenty-Four Generals; Marsilius of Padua; and Umberto Eco's novel, which is named and never quoted.

The companion game [*Nec in communi*](https://nec-in-communi.netlify.app/) (also on [itch.io](https://leofassb.itch.io/nec-in-communi)) takes its title from the condemned sentence of 1323: that Christ and the apostles had nothing *in speciali … nec in communi etiam*.

## Citation

Fassbender, Pantaleon. *The Franciscan Poverty Dispute: A Documentary Apparatus, 1316–1329.* 2026. https://doi.org/10.5281/zenodo.23066129 (all versions; version 1.0.1: https://doi.org/10.5281/zenodo.23067724; version 1.0.0: https://doi.org/10.5281/zenodo.23066130). Please also cite the printed source of any passage you quote. Metadata: `CITATION.cff`, `.zenodo.json`.

## Building the data

```
python tools/build-exiit.py
python tools/build-decretals.py
python tools/build-sentences.py
python tools/build-chronicle.py
python tools/build-appeal.py
python tools/build-dante.py
python tools/build-sachsenhausen.py
python tools/build-ockham.py
python tools/build-gui.py
python tools/build-clareno.py
```

The texts are kept in `tools/exiit_text.py`, `tools/decretals_text.py`, `tools/sentences_text.py`, `tools/chronicle_text.py`, `tools/appeal_text.py`, `tools/dante_text.py`, `tools/sachsenhausen_text.py`, `tools/ockham_text.py`, `tools/gui_text.py` and `tools/clareno_text.py`. `tools/friedberg.py "incipit" "end"` prints the two OCRs of Friedberg's volume II side by side with their disagreements marked; it expects the OCR files in `tools/src/` (Internet Archive `BD1141952_djvu.txt` saved as `fr1955.txt`, and the volume II text of `CorpusIurisCanoniciIAemiliusFriedberg1959` as `fr1959.txt`).

## Running locally

Any static server, e.g. `python -m http.server 8137`.

Licences: see `LICENSES.md`.
