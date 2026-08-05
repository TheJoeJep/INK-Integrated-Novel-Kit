import io, os, re, html, glob

SK = r"E:\Writing\story-engine\skills"
OUT = r"E:\Writing\story-engine\docs\skills-guide.html"

PHASES = [
    ("Starting", "Idea to premise, before there's a project",
     ["new-story", "brainstorm", "premise-test", "scale"]),
    ("Building", "Characters, places, factions, worlds",
     ["new-character", "character-arc", "new-place", "new-faction", "worldbuild", "real-world", "magic-system"]),
    ("Structuring", "Outline, models, beats, chapters",
     ["outline", "structure", "genre-mine", "beat", "chapter-plan"]),
    ("Drafting", "Writing the prose",
     ["write", "scene", "dialogue"]),
    ("Checking", "Mechanical verification &mdash; these have right answers",
     ["threads", "promises", "continuity", "names", "plants", "visuals"]),
    ("Diagnosing", "Symptom to cause, using documented base rates",
     ["diagnose", "pacing", "motivation", "viewpoint-check", "gorillas"]),
    ("Revising", "Structured passes over a finished draft",
     ["revise", "revision-map", "beta-read", "polish"]),
    ("Finishing", "Getting it in front of people",
     ["pitch", "query", "synopsis"]),
]

TIERCLASS = {"1": "t1", "2": "t2", "3": "t3", "4": "t4"}
TIERNAME = {
    "1": "Mechanical", "2": "Diagnostic", "3": "Procedural", "4": "Generative",
}

def esc(t):
    return html.escape(t or "", quote=False)

def parse(path):
    raw = io.open(path, encoding="utf-8").read()
    fm = re.search(r"^---\s*\n(.*?)\n---", raw, re.S)
    body = raw[fm.end():] if fm else raw
    meta = fm.group(1) if fm else ""
    name = re.search(r"^name:\s*(.+)$", meta, re.M)
    desc = re.search(r"^description:\s*(.+?)(?=\n\w+:|\Z)", meta, re.M | re.S)
    name = name.group(1).strip() if name else os.path.basename(os.path.dirname(path))
    desc = " ".join(desc.group(1).split()) if desc else ""

    # tier from the blockquote
    tb = re.search(r">\s*\*\*Tier\s*([0-9](?:/[0-9])?)[^*]*\*\*\s*(?:&mdash;|—|-)?\s*([^.\n]*)", body)
    tier = tb.group(1) if tb else "?"
    # full tier blockquote paragraph
    tq = re.search(r"^(>\s.*(?:\n>.*)*)", body.lstrip(), re.M)
    tquote = ""
    if tq:
        tquote = " ".join(l.lstrip("> ").strip() for l in tq.group(1).split("\n"))
        tquote = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", esc(tquote))
        tquote = re.sub(r"\*(.+?)\*", r"<i>\1</i>", tquote)

    # sources
    srcs = []
    sm = re.search(r"^\*\*Source:?\*\*(.+?)(?=\n\n)", body, re.M | re.S)
    if sm:
        srcs = re.findall(r"`([^`]+\.md)`", sm.group(1))
        if not srcs:
            srcs = re.findall(r"\]\(\.\./\.\./([^)]+\.md)\)", sm.group(1))
    if not srcs:
        srcs = re.findall(r"\]\(\.\./\.\./craft/([^)]+\.md)\)", body)[:3]

    # split description into what / when
    m = re.split(r"(?:^|\s)Use when ", desc, maxsplit=1)
    what = m[0].strip()
    when = ("Use when " + m[1]).strip() if len(m) > 1 else ""
    return dict(name=name, what=what, when=when, tier=tier, tquote=tquote, srcs=srcs)

skills = {}
for p in glob.glob(os.path.join(SK, "*", "SKILL.md")):
    d = parse(p)
    skills[d["name"]] = d

listed = {n for _, _, names in PHASES for n in names}
missing = sorted(set(skills) - listed)

def card(s):
    t = s["tier"].split("/")[0]
    cls = TIERCLASS.get(t, "t3")
    tname = TIERNAME.get(t, "")
    if "/" in s["tier"]:
        tname += " / " + TIERNAME.get(s["tier"].split("/")[1], "")
    srcs = "".join(f'<code>{esc(x)}</code>' for x in s["srcs"][:3])
    srcline = f'<div class="srcs"><span class="lbl">reads</span>{srcs}</div>' if srcs else ""
    when = f'<div class="when"><span class="lbl">when</span>{esc(s["when"])}</div>' if s["when"] else ""
    return f"""<div class="card {cls}">
<div class="chead"><code class="cmd">/{esc(s['name'])}</code>
<span class="tier {cls}">Tier {esc(s['tier'])} &middot; {tname}</span></div>
<div class="what">{esc(s['what'])}</div>
{when}
<details class="more"><summary>what it promises</summary>
<div class="tq">{s['tquote']}</div>{srcline}</details>
</div>"""

sections = ""
for title, blurb, names in PHASES:
    cards = "".join(card(skills[n]) for n in names if n in skills)
    sections += f"""<section class="phase">
<h2>{title}</h2><p class="blurb">{blurb}</p>
<div class="grid">{cards}</div></section>"""

if missing:
    cards = "".join(card(skills[n]) for n in missing)
    sections += f'<section class="phase"><h2>Other</h2><div class="grid">{cards}</div></section>'

CSS = """
:root{--bg:#faf9f7;--panel:#fff;--ink:#1a1a1a;--muted:#6b6560;--line:#e2ded8;--accent:#8a3324;
--soft:#f3e9e6;--chip:#efece7;
--t1:#2d5f3a;--t1b:#e4f0e6;--t2:#2d4f6b;--t2b:#e2ecf5;--t3:#7a5a1a;--t3b:#f5ecd8;--t4:#7a3a5a;--t4b:#f7e6ef}
@media (prefers-color-scheme:dark){:root{--bg:#16151a;--panel:#1e1d23;--ink:#eceaf0;--muted:#9a95a2;
--line:#33313b;--accent:#e2836c;--soft:#2c2226;--chip:#2a2830;
--t1:#9dd6a8;--t1b:#1d2f22;--t2:#8fc0e8;--t2b:#1a2733;--t3:#e0c07a;--t3b:#302716;--t4:#e2a0c4;--t4b:#2e1c26}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.55 ui-serif,Georgia,serif}
.wrap{max-width:1140px;margin:0 auto;padding:34px 20px 80px}
header{border-bottom:2px solid var(--line);padding-bottom:22px;margin-bottom:26px}
h1{font-size:2rem;margin:0 0 8px;letter-spacing:-.02em}
.sub{color:var(--muted);font-size:.92rem;font-family:ui-sans-serif,system-ui,sans-serif;max-width:70ch}
h2{font-size:1.3rem;margin:0 0 3px;letter-spacing:-.01em}
.blurb{color:var(--muted);font-size:.85rem;font-family:ui-sans-serif,system-ui,sans-serif;margin:0 0 14px}
.phase{margin-bottom:38px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(310px,1fr));gap:12px}
.card{background:var(--panel);border:1px solid var(--line);border-left:4px solid var(--tc);
border-radius:9px;padding:14px 16px}
.card.t1{--tc:var(--t1)}.card.t2{--tc:var(--t2)}.card.t3{--tc:var(--t3)}.card.t4{--tc:var(--t4)}
.chead{display:flex;align-items:center;gap:9px;flex-wrap:wrap;margin-bottom:7px}
.cmd{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:1rem;font-weight:600;
background:var(--soft);color:var(--accent);padding:2px 8px;border-radius:5px}
.tier{font-family:ui-sans-serif,system-ui,sans-serif;font-size:.62rem;letter-spacing:.05em;
text-transform:uppercase;padding:3px 7px;border-radius:4px;margin-left:auto;white-space:nowrap}
.tier.t1{background:var(--t1b);color:var(--t1)}.tier.t2{background:var(--t2b);color:var(--t2)}
.tier.t3{background:var(--t3b);color:var(--t3)}.tier.t4{background:var(--t4b);color:var(--t4)}
.what{font-size:.94rem}
.when{margin-top:8px;font-size:.85rem;color:var(--muted);
font-family:ui-sans-serif,system-ui,sans-serif}
.lbl{font-size:.6rem;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);
display:block;margin-bottom:2px;font-family:ui-sans-serif,system-ui,sans-serif}
.more{margin-top:9px}
.more summary{font-family:ui-sans-serif,system-ui,sans-serif;font-size:.74rem;color:var(--muted);
cursor:pointer;list-style:none}
.more summary::-webkit-details-marker{display:none}
.more summary::before{content:"\\25B8 ";font-size:.8em}
.more[open] summary::before{content:"\\25BE "}
.tq{margin-top:8px;font-size:.85rem;color:var(--muted);border-left:2px solid var(--line);
padding-left:10px}
.srcs{margin-top:8px}
.srcs code{display:inline-block;font-size:.68rem;background:var(--chip);color:var(--muted);
padding:2px 6px;border-radius:3px;margin:2px 3px 0 0;font-family:ui-monospace,Menlo,monospace}
.tiers{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:18px 20px;margin:0 0 30px}
.tiers h3{margin:0 0 10px;font-size:1.05rem}
table{width:100%;border-collapse:collapse;font-size:.88rem}
th,td{text-align:left;padding:7px 10px;border-bottom:1px solid var(--line);vertical-align:top}
th{font-family:ui-sans-serif,system-ui,sans-serif;font-size:.68rem;letter-spacing:.05em;
text-transform:uppercase;color:var(--muted)}
tr:last-child td{border-bottom:0}
.badge{font-family:ui-sans-serif,system-ui,sans-serif;font-size:.62rem;letter-spacing:.05em;
text-transform:uppercase;padding:3px 7px;border-radius:4px;white-space:nowrap}
.flow{background:var(--soft);border-radius:10px;padding:16px 20px;margin:0 0 30px;
font-family:ui-sans-serif,system-ui,sans-serif;font-size:.88rem}
.flow code{background:var(--panel);color:var(--accent);padding:1px 6px;border-radius:4px;
font-family:ui-monospace,Menlo,monospace}
.flow ol{margin:8px 0 0;padding-left:20px}.flow li{margin-bottom:5px}
footer{margin-top:44px;padding-top:18px;border-top:1px solid var(--line);color:var(--muted);
font-size:.82rem;font-family:ui-sans-serif,system-ui,sans-serif}
@media print{.more{display:none}.card{break-inside:avoid}}
"""

DOC = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Skills Guide &mdash; Story Engine</title><style>{CSS}</style></head><body>
<div class="wrap">
<header><h1>Skills Guide</h1>
<div class="sub">{len(skills)} skills for writing a novel, built on a craft base extracted from 39
writing lectures. Type the command in chat. Each skill loads only the craft documents it needs,
so you never carry the whole base while drafting.</div></header>

<div class="tiers"><h3>Read the tier before you trust the output</h3>
<p class="blurb">Every skill declares its tier when you run it. This is the most important thing
on this page &mdash; a system equally confident about everything will mislead you.</p>
<table>
<tr><th>Tier</th><th>What it does</th><th>How much to trust it</th></tr>
<tr><td><span class="badge tier t1">1 &middot; Mechanical</span></td>
<td>Verifies against a documented rule</td>
<td><b>High.</b> There's a right answer. It reports findings flatly and never fixes anything</td></tr>
<tr><td><span class="badge tier t2">2 &middot; Diagnostic</span></td>
<td>Maps a symptom to likely causes using documented base rates</td>
<td><b>Good.</b> Gives ranked hypotheses, not verdicts. You confirm which is real</td></tr>
<tr><td><span class="badge tier t3">3 &middot; Procedural</span></td>
<td>Runs a documented multi-stage process in order</td>
<td><b>Good for the process.</b> The stages are the value; it won't let you skip ahead</td></tr>
<tr><td><span class="badge tier t4">4 &middot; Generative</span></td>
<td>Produces raw material</td>
<td><b>Lowest.</b> It says so. Output is material to react against, never an answer</td></tr>
</table></div>

<div class="flow"><b>If you're starting from nothing</b>
<ol>
<li><code>/brainstorm</code> &rarr; <code>/new-story</code> &rarr; <code>/premise-test</code>
&mdash; is this a novel or just a setting?</li>
<li><code>/magic-system</code>, <code>/worldbuild</code>, <code>/new-character</code>
&mdash; build what the story needs, not everything</li>
<li><code>/outline</code> or <code>/structure</code> &mdash; as much plan as you actually want</li>
<li><code>/write</code> &mdash; the drafting loop. This is where most time goes</li>
<li><code>/threads</code>, <code>/promises</code>, <code>/plants</code> &mdash; run these on the
<i>outline</i>, before drafting. They work without prose</li>
<li>Something's wrong &rarr; <code>/diagnose</code>. It's the front door and routes to the rest</li>
<li>Draft done &rarr; <code>/revise</code> &mdash; and it will stop you polishing too early</li>
</ol></div>

{sections}

<footer>
Craft derived from Brandon Sanderson's published writing lectures, with guest material by
<b>Mary Robinette Kowal</b> (short fiction, MICE, yes-but/no-and) and <b>Brandon Mull</b>
(middle grade / YA). Several core techniques &mdash; try-fail cycles, prose as a pane of glass
&mdash; are credited by Sanderson to <b>Dave Wolverton</b>. See <code>CREDITS.md</code>.<br><br>
Generated from the skill files themselves &mdash; regenerate after changing any skill.
Full craft base in <code>craft/</code>; skill definitions in <code>skills/</code>.
</footer></div></body></html>"""

io.open(OUT, "w", encoding="utf-8").write(DOC)
print(f"wrote {len(DOC):,} chars | {len(skills)} skills | {len(PHASES)} phases")
if missing:
    print("unlisted (added to 'Other'):", ", ".join(missing))
