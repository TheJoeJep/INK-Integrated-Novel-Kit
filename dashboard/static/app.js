let D = null, BY = {};

const $ = s => document.querySelector(s);
const esc = s => (s || "").replace(/[&<>]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;" }[c]));

async function load() {
  const r = await fetch("data.json?" + Date.now());
  D = await r.json();
  D.entities.forEach(e => BY[e.id] = e);
  render();
}

function render() {
  $("#brand").textContent = D.project;
  const s = D.stats;
  $("#stats").innerHTML =
    `<b>${s.words.toLocaleString()}</b> words<br>
     <b>${s.chapters}</b> chapters · <b>${s.scenes}</b> scenes<br>
     <b>${s.characters}</b> characters · <b>${s.places}</b> places<br>
     <b>${s.factions}</b> factions · <b>${D.plot.length}</b> beats`;
  $("#gen").textContent = "built " + D.generated;

  renderManuscript();
  renderCards("#cast", D.entities.filter(e => e.kind === "character"));
  renderCards("#places", D.entities.filter(e => e.kind === "place" || e.kind === "faction"));
  renderPlot();
  renderCanon();
  observe();
}

function renderManuscript() {
  const m = $("#manuscript");
  if (!D.chapters.length || !D.stats.words) {
    m.innerHTML = `<h1>${esc(D.project)}</h1>
      <div class="sub">No prose yet.</div>
      <div class="empty"><h3>Nothing drafted so far</h3>
      <p>This view fills in as scenes are written to <code>manuscript/</code>. The dashboard
      rebuilds within a couple of seconds of a file changing — leave it open while you work.</p>
      <p>Meanwhile <b>Cast</b>, <b>Places</b>, <b>Plot</b> and <b>Canon</b> are already populated
      from the project documents.</p></div>`;
    return;
  }
  m.innerHTML = `<h1>${esc(D.project)}</h1>
    <div class="sub">${D.stats.words.toLocaleString()} words</div>` +
    D.chapters.map(c => `
      <section class="chapter">
        <div class="chhead"><h2>${esc(c.title)}</h2>
          <div class="chmeta">${c.scenes.length} scene${c.scenes.length === 1 ? "" : "s"} ·
          ${c.words.toLocaleString()} words${c.status ? " · " + esc(c.status) : ""}</div></div>
        ${c.scenes.map(sc => `
          <div class="scene" id="sc-${sc.id}" data-scene="${sc.id}">
            <div class="scenehead">${esc(sc.title)}${sc.pov ? " · " + esc(sc.pov) : ""}</div>
            ${sc.html}
          </div>`).join("")}
      </section>`).join("");
}

function renderCards(sel, list) {
  const el = $(sel);
  if (!list.length) { el.innerHTML = `<p class="hint">Nothing here yet.</p>`; return; }
  el.innerHTML = list.map(e => `
    <div class="card ${e.kind}" data-ent="${e.id}">
      <div class="kind">${e.kind}</div>
      <h3>${esc(e.name)}</h3>
      <div class="desc">${esc(e.summary) || "<i>No summary yet.</i>"}</div>
      ${e.has_visual ? "" : '<span class="flag">no visual block</span>'}
    </div>`).join("");
}

function renderPlot() {
  const acts = {};
  D.plot.forEach(b => (acts[b.act] = acts[b.act] || []).push(b));
  $("#plot").innerHTML = `<h1>Plot</h1><div class="sub">${D.plot.length} beats</div>` +
    Object.keys(acts).sort().map(a => `
      <h2 style="margin-top:26px">${esc(a)}</h2>
      ${acts[a].map(b => `<div class="beat" data-beat="${b.id}">
        <h3><span class="act">${esc(b.act)}</span>${esc(b.title)}
        ${b.status ? `<span class="st">${esc(b.status)}</span>` : ""}</h3></div>`).join("")}
    `).join("");
}

function renderCanon() {
  const t = D.terms.length ? `<h2>Names &amp; terms</h2><table><thead><tr>
      <th>Term</th><th>What</th><th>Register</th><th>Status</th></tr></thead><tbody>` +
    D.terms.map(x => `<tr><td><b>${esc(x.term)}</b></td><td>${esc(x.what)}</td>
      <td>${esc(x.register)}</td><td>${esc(x.status)}</td></tr>`).join("") +
    `</tbody></table>` : "";
  const l = D.ledger.length ? `<h2>Continuity ledger</h2><table><thead><tr>
      <th>Fact</th><th>Established in</th><th>Date</th><th>Note</th></tr></thead><tbody>` +
    D.ledger.map(x => `<tr><td>${esc(x.fact)}</td><td>${esc(x.where)}</td>
      <td>${esc(x.when)}</td><td>${esc(x.note)}</td></tr>`).join("") +
    `</tbody></table>` : `<h2>Continuity ledger</h2><p class="hint">Empty — no prose written yet.</p>`;
  $("#canon").innerHTML = `<h1>Canon</h1><div class="sub">The constraints layer</div>` + t + l;
}

/* ── sidebar follows the scroll ── */
function observe() {
  const scenes = [...document.querySelectorAll(".scene")];
  if (!scenes.length) return;
  const io = new IntersectionObserver(entries => {
    const vis = entries.filter(e => e.isIntersecting)
      .sort((a, b) => a.boundingClientRect.top - b.boundingClientRect.top);
    if (vis.length) setContext(vis[0].target.dataset.scene);
  }, { rootMargin: "-15% 0px -55% 0px", threshold: 0 });
  scenes.forEach(s => io.observe(s));
}

function findScene(id) {
  for (const c of D.chapters) for (const s of c.scenes) if (s.id === id) return [s, c];
  return [null, null];
}

function setContext(id) {
  const [sc, ch] = findScene(id);
  if (!sc) return;
  document.querySelectorAll(".scene").forEach(e => e.classList.toggle("active", e.dataset.scene === id));
  $("#side-scene").textContent = `${ch.title} — ${sc.title}`;

  const seen = new Set();
  const block = (label, ids) => {
    const list = ids.map(i => BY[i]).filter(e => e && !seen.has(e.id));
    list.forEach(e => seen.add(e.id));
    if (!list.length) return "";
    return `<div class="sgroup">${label}</div>` + list.map(card).join("");
  };
  const body =
    block("Present", sc.present) +
    block("Setting", sc.setting) +
    block("Mentioned", sc.mentioned);

  $("#side-body").innerHTML = body ||
    `<p class="hint">Nothing linked to this scene yet. Add <code>PRESENT</code> and
     <code>SETTING</code> to the scene's header comment and it'll populate.</p>`;
}

function card(e) {
  const vis = e.visual && e.visual.replace(/<[^>]+>/g, "").trim()
    ? `<div class="svis">${e.visual}</div>` : "";
  return `<div class="sent ${e.kind}" data-ent="${e.id}">
    <div class="sname">${esc(e.name)}</div>
    <div class="sbit">${e.role || "<p>" + esc(e.summary) + "</p>"}</div>
    ${vis}</div>`;
}

/* ── nav, modal ── */
document.addEventListener("click", ev => {
  const nav = ev.target.closest("#rail button");
  if (nav) {
    document.querySelectorAll("#rail button").forEach(b => b.classList.toggle("on", b === nav));
    document.querySelectorAll(".view").forEach(v => v.classList.toggle("on", v.id === "view-" + nav.dataset.view));
    return;
  }
  const ent = ev.target.closest("[data-ent]");
  if (ent) { openSheet(BY[ent.dataset.ent].body); return; }
  const beat = ev.target.closest("[data-beat]");
  if (beat) { openSheet(D.plot.find(b => b.id === beat.dataset.beat).body); return; }
  if (ev.target.id === "close" || ev.target.id === "modal") $("#modal").hidden = true;
});
document.addEventListener("keydown", e => { if (e.key === "Escape") $("#modal").hidden = true; });

function openSheet(html) { $("#sheet-body").innerHTML = html; $("#modal").hidden = false; }

/* ── poll for rebuilds ── */
let stamp = null;
setInterval(async () => {
  try {
    const r = await fetch("data.json?" + Date.now());
    const d = await r.json();
    if (stamp && d.generated !== stamp) { D = d; BY = {}; D.entities.forEach(e => BY[e.id] = e); render(); }
    stamp = d.generated;
  } catch (e) { }
}, 3000);

load();
