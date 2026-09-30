/* The Franciscan Poverty Dispute — a documentary apparatus. Vanilla JS, hash routes. */
"use strict";

const view = document.getElementById("view");
const D = { mods: null, plates: null, timeline: null, compare: null, texts: {} };
const SIDES = { papacy: "The Pope", order: "The Order", spirituals: "Spirituals and Beguins", empire: "The Emperor", reception: "Reception" };
const LANGS = { la: "Latin", it: "Italian", fr: "French", de: "German" };

const esc = s => String(s ?? "").replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
const side = s => `<span class="side ${s}">${esc(SIDES[s] || s)}</span>`;
const plateOf = id => (D.plates.plates || []).find(p => p.id === id);
const getJSON = url => fetch(url).then(r => { if (!r.ok) throw new Error(url); return r.json(); });

let langPref = "both";
try { langPref = localStorage.getItem("poverty_lang") || "both"; } catch (e) { /* storage blocked */ }

async function boot() {
  [D.mods, D.plates, D.timeline, D.compare] = await Promise.all(
    ["data/modules.json", "data/plates.json", "data/timeline.json", "data/compare.json"].map(getJSON));
  document.getElementById("navCompare").hidden = !(D.compare.pairs || []).length;
  document.getElementById("navPlates").hidden = !(D.plates.plates || []).length;
  window.addEventListener("hashchange", route);
  route();
}

async function text(id) {
  if (!D.texts[id]) D.texts[id] = await getJSON(`data/${id}.json`);
  return D.texts[id];
}

function route() {
  const parts = (location.hash.replace(/^#\/?/, "") || "").split("/").filter(Boolean);
  const [page, ...args] = parts;
  document.querySelectorAll(".top nav a").forEach(a => {
    const t = a.getAttribute("href").replace(/^#\/?/, "");
    a.classList.toggle("on", (t || "") === (page === "text" ? "texts" : page || ""));
  });
  view.innerHTML = "";
  window.scrollTo(0, 0);
  const pages = { "": overview, texts, text: reader, compare, timeline, plates, sources };
  (pages[page || ""] || overview)(args);
}

/* ------------------------------------------------------------ overview */
function overview() {
  view.innerHTML = `
  <div class="hero one">
    <div>
      <span class="tag">1316–1329 · John XXII · Michael of Cesena · William of Ockham</span>
      <h1>Did Christ own anything?</h1>
      <p class="lede">In the 1320s the question divided the Church. The Franciscans held that Christ and the apostles had owned nothing, individually or in common, and that the friars, like them, only used what others owned. Pope John XXII declared this heretical. The minister general of the order and its best theologians fled to the emperor, and the argument about poverty became an argument about the power of popes.</p>
      <p class="readable">This apparatus follows the dispute through its documents, in public-domain editions with the Latin beside a working English translation: the pope's decretals, the friars' declarations and appeals, the emperor's appeal that took up their cause, the chroniclers of the order and of its Spirituals, the inquisitor, Ockham, and the poet who wrote of Francis marrying Lady Poverty. It begins with the two papal dossiers: the decretals of 1279 and 1312 that defined Franciscan poverty, and the five decretals of John XXII that undid the definition. The Compare page sets them side by side.</p>
      <p class="quote">"… that our Redeemer and Lord Jesus Christ and his apostles had nothing individually, nor even in common …"
      <br><span class="fine">The assertion John XXII declared heretical in 1323 ·
      <a href="#/text/decretals/nonnullos/1">Decr. Nonnullos [1]</a></span></p>
    </div>
  </div>

  <h2>What the apparatus carries</h2>
  <div class="grid g2">${D.mods.shipped.map(card).join("")}</div>

  <h2>The questions it asks</h2>
  <div class="grid g2">
    <div class="panel"><h3>What was the dispute about?</h3>
      <p>Not whether the friars should be poor, which no one denied, but what their poverty was in law. Since 1279 the Roman Church owned the order's houses, books and bread, and the friars had only the "simple use of fact". John XXII held that this was a fiction: no one can use bread without consuming it, and so owning it. In 1322 he handed the ownership back (<a href="#/text/decretals/conditorem/1">Decr. Conditorem [1]</a>), after the Franciscan chapter at Perugia had declared the opposite 'sound, catholic and faithful' (<a href="#/text/chronicle/perugia/2">Chron. Perugia [2]</a>).</p></div>
    <div class="panel"><h3>Could a pope revoke a pope?</h3>
      <p>The friars answered that what one pope had defined by the "key of knowledge" in matters of faith, his successors could not undo. John XXII called this a doctrine of the father of lies (<a href="#/text/decretals/quorundam/1">Decr. Quorundam [1]</a>). The question outlived the dispute.</p></div>
    <div class="panel"><h3>Who paid?</h3>
      <p>The Spiritual friars who would not wear the habits their superiors gave them were ordered to obey (<a href="#/text/decretals/exigit/1">Decr. Exigit [1]</a>); four of them were burned at Marseille in 1318, and the Beguins of Languedoc who venerated them went to the inquisitors' fires. In September 1322 Bernard Gui handed four more to the secular arm at Toulouse: one had kept a litany with the names of seventy condemned (<a href="#/text/sentences/dominici/5">Sent. Dominici [5]</a>). The argument of the schools had a price in the streets.</p></div>
    <div class="panel"><h3>Can the story be played?</h3>
      <p>The companion game <a href="https://nec-in-communi.netlify.app/" target="_blank" rel="noopener"><em>Nec in communi</em></a> (also on <a href="https://leofassb.itch.io/nec-in-communi" target="_blank" rel="noopener">itch.io</a>) is built on these texts: as the minister general you hold the order together between the pope, the Spirituals, the masters and the emperor, and lead its arguments before the curia and the pope; as the pope you issue the decretals and bring the order to obedience without losing it. Every card cites a passage carried here. The dispute is also the historical setting of Umberto Eco's novel of 1980, which is not quoted here; the poet of the same years is (<a href="#/text/dante/xi/6">Par. XI [6]</a>).</p></div>
  </div>`;
}

function card(m) {
  return `<a class="card" href="#/text/${m.id}">
    <div>${side(m.side)} <span class="fine">${esc(m.zk)}</span></div>
    <h3>${esc(m.kurz)}</h3><p class="fine">${esc(m.warum)}</p></a>`;
}

/* ------------------------------------------------------------ texts */
function texts() {
  view.innerHTML = `
    <span class="tag">Texts</span><h1>The corpus</h1>
    <p class="lede">Stage 1 of the collection is closed: ten modules, each readable in full, Latin or Italian beside the English. What is not carried, and why, is listed below.</p>
    <h2>Carried</h2><div class="grid g2">${D.mods.shipped.map(card).join("")}</div>
    ${(D.mods.planned || []).length ? `<h2>Planned</h2><div class="grid g2">${D.mods.planned.map(m => `
      <div class="card planned"><div>${side(m.side)} <span class="fine">planned</span></div>
      <h3>${esc(m.kurz)}</h3><p class="fine">${esc(m.warum)}</p><p class="fine"><b>Source:</b> ${esc(m.quelle)}</p></div>`).join("")}</div>` : ""}
    ${(D.mods.missing || []).length ? `<h2 id="missing">Not carried</h2><div class="grid g2">${D.mods.missing.map(m => `
      <div class="card planned"><div>${side(m.side)} <span class="fine">not carried</span></div>
      <h3>${esc(m.kurz)}</h3><p class="fine">${esc(m.warum)}</p><p class="fine"><b>Source:</b> ${esc(m.quelle)}</p></div>`).join("")}</div>` : ""}`;
}

async function reader([id, secId, unitN]) {
  const m = D.mods.shipped.find(x => x.id === id);
  if (!m) { location.hash = "#/texts"; return; }
  view.innerHTML = `<p class="fine">Loading…</p>`;
  const t = await text(m.datei);
  const sec = t.sections.find(s => s.id === secId) || t.sections[0];
  const bilingual = sec.units.some(u => u.orig);
  const lang = bilingual ? langPref : "en";
  const origName = LANGS[t.orig_sprache] || "Original";
  view.innerHTML = `
    <p class="fine"><a href="#/texts">← All texts</a></p>
    <span class="tag">${side(m.side)} ${esc(t.jahr)} · cited as ${esc(sec.zk)} [n]</span>
    <h1>${esc(t.titel)}</h1>
    <p class="fine">${esc(t.autor)}</p>
    <nav class="toc">${t.sections.map(s => `<a href="#/text/${id}/${s.id}" class="${s.id === sec.id ? "on" : ""}">${esc(s.titel)}</a>`).join("")}</nav>
    <div class="panel readable"><h3>${esc(sec.titel)}</h3><p>${esc(sec.blurb)}</p></div>
    ${bilingual ? `<div class="langbar" id="langbar">
      ${[["both", `${origName} + English`], ["orig", origName], ["en", "English"]].map(([k, l]) =>
        `<button data-l="${k}" class="${k === lang ? "on" : ""}">${l}</button>`).join("")}</div>` : ""}
    <div id="units"></div>
    <div class="panel readable hinweis"><span class="tag">Source and editorial note</span>
      <p><b>Source.</b> ${esc(t.quelle)}</p><p>${esc(t.hinweis)}</p></div>`;
  const box = view.querySelector("#units");
  for (const u of sec.units) {
    const showO = u.orig && lang !== "en", showE = !u.orig || lang !== "orig";
    const cls = ["unit", String(u.n) === unitN ? "hl" : ""].join(" ");
    box.insertAdjacentHTML("beforeend", `
      <div class="${cls}" id="u${u.n}">
        <div class="num"><a href="#/text/${id}/${sec.id}/${u.n}" title="Cite as ${esc(sec.zk)} [${u.n}]">[${u.n}]</a>
          ${u.pg ? `<span class="pg" title="${esc(t.pg_label || "")} page.line">${esc(t.pg_label || "")} ${esc(u.pg)}</span>` : ""}</div>
        <div>${u.titel ? `<h4>${esc(u.titel)}</h4>` : ""}
          <div class="cols ${showO && showE ? "" : "one"}">
            ${showO ? `<div class="origcol"><div class="orig" lang="${esc(t.orig_sprache)}"${t.rtl ? ' dir="rtl"' : ""}>${esc(u.orig)}</div>${u.tr ? `<div class="translit">${esc(u.tr)}</div>` : ""}</div>` : ""}
            ${showE ? `<div class="text">${esc(u.en)}</div>` : ""}
          </div></div>
        ${u.note ? `<div class="note">${esc(u.note)}</div>` : ""}
      </div>`);
  }
  view.querySelectorAll("#langbar button").forEach(b => b.onclick = () => {
    langPref = b.dataset.l;
    try { localStorage.setItem("poverty_lang", langPref); } catch (e) { /* storage blocked */ }
    route();
  });
  if (unitN) { const el = document.getElementById("u" + unitN); if (el) el.scrollIntoView({ block: "center" }); }
}

/* ------------------------------------------------------------ compare */
async function compare([pid]) {
  const CMP = D.compare;
  const pair = (CMP.pairs || []).find(p => p.id === pid);
  if (!pair) {
    view.innerHTML = `
      <span class="tag">Compare</span><h1>Pope against pope</h1>
      <p class="lede">${esc(CMP.lede)}</p>
      <div class="grid g2">${(CMP.pairs || []).map(p => `<a class="card" href="#/compare/${p.id}">
        <div>${p.voices.map(v => side((D.mods.shipped.find(m => m.id === v.text) || {}).side)).join(" ")}</div>
        <h3>${esc(p.titel)}</h3><p class="fine">${esc(p.frage)}</p></a>`).join("")}</div>`;
    return;
  }
  view.innerHTML = `<p class="fine"><a href="#/compare">← All comparisons</a></p><p class="fine">Loading…</p>`;
  const docs = await Promise.all(pair.voices.map(v => {
    const m = D.mods.shipped.find(x => x.id === v.text);
    return text(m.datei).then(t => ({ v, m, t }));
  }));
  const col = ({ v, m, t }) => {
    const sec = t.sections.find(s => s.id === v.sec);
    const units = v.n.map(n => sec.units.find(u => u.n === n)).filter(Boolean);
    return `<div class="voice">
      <div class="vhead">${side(m.side)} <b>${esc(t.autor)}</b><br><span class="fine">${esc(t.jahr)} · ${esc(sec.titel)}</span></div>
      ${units.map(u => `<div class="vunit">
        <div class="fine"><a href="#/text/${m.id}/${sec.id}/${u.n}">${esc(sec.zk)} [${u.n}]</a>${u.titel ? ` · ${esc(u.titel)}` : ""}</div>
        <div class="text">${esc(u.en)}</div></div>`).join("")}
    </div>`;
  };
  view.innerHTML = `
    <p class="fine"><a href="#/compare">← All comparisons</a></p>
    <span class="tag">Compare</span><h1>${esc(pair.titel)}</h1>
    <p class="lede">${esc(pair.frage)}</p>
    <div class="panel readable"><p>${esc(pair.note)}</p></div>
    <div class="cmp n${docs.length}">${docs.map(col).join("")}</div>`;
}

/* ------------------------------------------------------------ timeline */
function timeline() {
  const T = D.timeline;
  view.innerHTML = `
    <span class="tag">Timeline</span><h1>1209–1347</h1>
    <p class="lede">${esc(T.lede)}</p>
    <div class="legend">${Object.keys(SIDES).map(side).join(" ")}</div>
    <div class="tl">${T.stations.map(s => {
      const p = s.plate && plateOf(s.plate);
      return `<div class="st" style="--c:var(--${s.side})">
        <div><div class="d">${esc(s.d)} · ${side(s.side)}</div><h3>${esc(s.titel)}</h3><p>${esc(s.text)}</p>
        ${s.cite ? `<p class="fine"><a href="${s.cite}">✦ ${esc(s.citeLabel)}</a></p>` : ""}</div>
        ${p ? `<img src="assets/plates/${p.id}_t.jpg" alt="${esc(p.titel)}" title="${esc(p.titel)}">` : "<span></span>"}
      </div>`;
    }).join("")}</div>`;
}

/* ------------------------------------------------------------ plates */
function plates() {
  view.innerHTML = `
    <span class="tag">Plates</span><h1>Poverty painted</h1>
    <p class="lede">${esc(D.plates.lede || "")}</p>
    <div class="grid g4">${D.plates.plates.map(p => `
      <figure class="plate card"><a href="#" data-p="${p.id}"><img src="assets/plates/${p.id}_t.jpg" alt="${esc(p.titel)}"></a>
      <figcaption>${side(p.side)} <b>${esc(p.titel)}</b><br>${esc(p.caption)}<br><i>${esc(p.source)}</i></figcaption></figure>`).join("")}</div>
    <p class="fine">${esc(D.plates.credit)}</p>`;
  view.querySelectorAll("[data-p]").forEach(a => a.onclick = e => {
    e.preventDefault();
    const p = plateOf(a.dataset.p);
    const lb = document.createElement("div");
    lb.className = "lightbox";
    lb.innerHTML = `<figure><img src="assets/plates/${p.id}.jpg" alt="${esc(p.titel)}"><figcaption class="cap"><b>${esc(p.titel)}.</b> ${esc(p.caption)}</figcaption></figure>`;
    lb.onclick = () => lb.remove();
    document.body.append(lb);
  });
}

/* ------------------------------------------------------------ sources */
function sources() {
  view.innerHTML = `
    <span class="tag">Sources, method, limits</span><h1>How this apparatus is made</h1>
    <div class="readable">
    <p><b>Public domain only.</b> Every text is carried from a printing that is out of copyright, and its source is named on its page. Modern critical editions and translations in copyright are not used; where the only good edition is modern, the module says so.</p>
    <p><b>The page is the authority.</b> The Latin comes from nineteenth-century editions, above all Friedberg's <i>Corpus iuris canonici</i> (Leipzig 1879–81). The machine reading of the scan is corrected against the page image, column by column, and every correction that goes beyond the obvious is named in the notes. The editor's text is kept with his spelling (<i>quum</i>, <i>ae</i>), his punctuation and his brackets; his apparatus of variant readings is not carried, except where a variant matters.</p>
    <p><b>Working translations.</b> Almost none of these texts has a public-domain English translation. The site gives its own, close to the Latin and dedicated to the public domain (CC0). It is an aid to reading, not a critical translation, and the legal Latin of the decretals is rendered for sense, with the technical terms (<i>dominium</i>, <i>usus facti</i>, <i>proprietas</i>) given in brackets where they carry the argument.</p>
    <p><b>Summaries are not the text.</b> Friedberg prints before each decretal the medieval summary (<i>summarium</i>) of the glossators. The site gives it in the notes, marked as later, and does not treat it as the pope's words.</p>
    <p><b>The one English not made here.</b> Dante's Paradiso XI is given in Moore's Oxford text (1904) and Longfellow's translation (1867), both public domain; the modern critical text of the Commedia (Petrocchi, 1966–67) is not used.</p>
    <p><b>Voices and distances.</b> The pope's decretals speak with authority and say what he wished to be the law; the friars' declarations and appeals were written by men defending their order and themselves; the chronicles of the order were written after the defeat. Each module says who wrote, when and for whom.</p>
    <p><b>Dates.</b> The texts' own dates are given as printed (Roman calendar, pontifical year) with the modern equivalent.</p>
    </div>
    <h2>Sources carried</h2>
    <div class="grid g2">${D.mods.shipped.map(m => `<div class="panel"><b>${esc(m.kurz)}</b><p class="fine" id="src-${m.id}">…</p></div>`).join("")}</div>
    ${(D.plates.plates || []).length ? `<h2>Plates</h2><p class="fine readable">${esc(D.plates.credit)}</p>` : ""}`;
  D.mods.shipped.forEach(async m => {
    const t = await text(m.datei);
    const el = document.getElementById("src-" + m.id);
    if (el) el.textContent = t.quelle;
  });
}

boot().catch(e => { view.innerHTML = `<p>Could not load the apparatus: ${esc(e.message)}</p>`; });
