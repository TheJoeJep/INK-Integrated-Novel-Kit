"""
Derive the dashboard index from a story workspace.

The markdown IS the database. This reads it and emits data.json.
Nothing here writes to the workspace — it is strictly read-only.
"""
import io, os, re, json, html, glob, sys

# ── minimal markdown → html (no dependencies) ────────────────────────────────

def md(text):
    if not text:
        return ""
    out, lines = [], text.split("\n")
    i, in_ul, in_ol = 0, False, False

    def close():
        nonlocal in_ul, in_ol
        if in_ul: out.append("</ul>"); in_ul = False
        if in_ol: out.append("</ol>"); in_ol = False

    while i < len(lines):
        ln = lines[i]
        s = ln.strip()

        if not s:
            close(); i += 1; continue

        if s.startswith("```"):
            close(); i += 1; buf = []
            while i < len(lines) and not lines[i].strip().startswith("```"):
                buf.append(html.escape(lines[i])); i += 1
            i += 1
            out.append("<pre><code>" + "\n".join(buf) + "</code></pre>")
            continue

        if re.match(r"^(-{3,}|\*{3,}|_{3,})$", s):
            close(); out.append("<hr>"); i += 1; continue

        h = re.match(r"^(#{1,6})\s+(.*)$", s)
        if h:
            close(); n = len(h.group(1))
            out.append(f"<h{n}>{inline(h.group(2))}</h{n}>"); i += 1; continue

        if s.startswith("|") and i + 1 < len(lines) and re.match(r"^\|[\s:|-]+\|$", lines[i+1].strip()):
            close()
            hdr = [c.strip() for c in s.strip("|").split("|")]
            i += 2; rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")]); i += 1
            t = "<table><thead><tr>" + "".join(f"<th>{inline(c)}</th>" for c in hdr) + "</tr></thead><tbody>"
            for r in rows:
                t += "<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>"
            out.append(t + "</tbody></table>"); continue

        if s.startswith(">"):
            close(); buf = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                buf.append(lines[i].strip().lstrip("> ").rstrip()); i += 1
            out.append("<blockquote>" + inline(" ".join(buf)) + "</blockquote>"); continue

        m = re.match(r"^[-*+]\s+(.*)$", s)
        if m:
            if in_ol: out.append("</ol>"); in_ol = False
            if not in_ul: out.append("<ul>"); in_ul = True
            out.append(f"<li>{inline(m.group(1))}</li>"); i += 1; continue

        m = re.match(r"^\d+\.\s+(.*)$", s)
        if m:
            if in_ul: out.append("</ul>"); in_ul = False
            if not in_ol: out.append("<ol>"); in_ol = True
            out.append(f"<li>{inline(m.group(1))}</li>"); i += 1; continue

        close()
        buf = []
        while i < len(lines) and lines[i].strip() and not re.match(
                r"^\s*(#{1,6}\s|[-*+]\s|\d+\.\s|>|\||```|-{3,}$)", lines[i]):
            buf.append(lines[i].strip()); i += 1
        if buf:
            out.append("<p>" + inline(" ".join(buf)) + "</p>")
        else:
            i += 1
    close()
    return "\n".join(out)

def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"\*\*\*(.+?)\*\*\*", r"<strong><em>\1</em></strong>", t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", t)
    t = re.sub(r"~~(.+?)~~", r"<del>\1</del>", t)
    t = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", _link, t)
    return t

_SAFE = re.compile(r"^(https?:|mailto:|#|\.{0,2}/|[\w.\-]+\.md|[\w.\-]+/)", re.I)

def _link(m):
    """Render a link, dropping any scheme that isn't plainly safe.

    Everything rendered here is escaped upstream, so the one remaining
    injection vector is a `javascript:`-style href. Refuse those.
    """
    text, href = m.group(1), m.group(2).strip()
    if not _SAFE.match(href):
        return text
    return f'<a href="{html.escape(href, quote=True)}">{text}</a>'

# ── helpers ──────────────────────────────────────────────────────────────────

def read(p):
    # utf-8-sig strips a BOM if present. Files written by PowerShell's
    # Out-File carry one, and it breaks leading-anchor regexes like ^#.
    try:
        return io.open(p, encoding="utf-8-sig").read()
    except Exception:
        return ""

def section(text, name):
    """Return the body of a `## name` section."""
    m = re.search(rf"^##\s+{re.escape(name)}\s*\n(.*?)(?=^##\s|\Z)", text, re.M | re.S)
    return m.group(1).strip() if m else ""

def first_para(text):
    body = re.sub(r"^#.*$", "", text, flags=re.M)
    body = re.sub(r"^\*\*.*?\*\*.*$", "", body, flags=re.M)
    for para in body.split("\n\n"):
        p = para.strip()
        if p and not p.startswith(("|", ">", "-", "*", "#")) and len(p) > 30:
            return " ".join(p.split())
    return ""

def title_of(text, fallback):
    m = re.search(r"^#\s+(.+)$", text, re.M)
    return m.group(1).strip() if m else fallback

def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")

def words(s):
    return len(re.findall(r"\b[\w']+\b", s))

# ── entity loading ───────────────────────────────────────────────────────────

def load_entities(root, folder, kind):
    ents = []
    for p in glob.glob(os.path.join(root, folder, "**", "*.md"), recursive=True):
        base = os.path.basename(p)
        if base.startswith("_") or "images" in p.replace("\\", "/").split("/"):
            continue
        raw = read(p)
        if not raw.strip():
            continue
        name = title_of(raw, base[:-3])
        ents.append({
            "id": slug(name),
            "kind": kind,
            "name": name,
            "file": os.path.relpath(p, root).replace("\\", "/"),
            "summary": first_para(raw),
            "role": md(section(raw, "Role in the story")),
            "visual": md(section(raw, "Visual")),
            "voice": md(section(raw, "Voice")),
            "facts": md(section(raw, "Established facts")),
            "open": md(section(raw, "Open questions")),
            "body": md(raw),
            "has_visual": bool(re.sub(r"[\s*\-:|]", "", re.sub(r"<[^>]+>", "", section(raw, "Visual")))),
        })
    return ents

def load_terms(root):
    raw = read(os.path.join(root, "canon", "names-and-terms.md"))
    terms = []
    for row in re.findall(r"^\|\s*\*{0,2}([^|*]+?)\*{0,2}\s*\|([^|]*)\|([^|]*)\|([^|]*)\|\s*$", raw, re.M):
        term, what, reg, status = (c.strip() for c in row)
        if term.lower() in ("term", "") or set(term) <= set("-: "):
            continue
        terms.append({"term": term, "what": what, "register": reg, "status": status})
    return terms

def load_ledger(root):
    raw = read(os.path.join(root, "canon", "continuity-ledger.md"))
    rows = []
    for m in re.finditer(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]*?)\s*\|\s*([^|]*?)\s*\|\s*$", raw, re.M):
        fact, where, when, note = (c.strip() for c in m.groups())
        if fact.lower() == "fact" or set(fact) <= set("-: "):
            continue
        rows.append({"fact": fact, "where": where, "when": when, "note": note})
    return rows

def load_plot(root):
    beats = []
    for p in sorted(glob.glob(os.path.join(root, "plot", "**", "*.md"), recursive=True)):
        base = os.path.basename(p)
        if base.startswith("_"):
            continue
        raw = read(p)
        act = os.path.basename(os.path.dirname(p))
        beats.append({
            "id": slug(act + "-" + base[:-3]),
            "act": act,
            "title": title_of(raw, base[:-3]),
            "status": (re.search(r"\*\*Status:\*\*\s*([^\n·|]+)", raw) or [None, ""])[1].strip(),
            "what": md(section(raw, "What happens")),
            "why": md(section(raw, "Why it must happen")),
            "body": md(raw),
        })
    return beats

# ── manuscript ───────────────────────────────────────────────────────────────

HDR = re.compile(r"<!--(.*?)-->", re.S)

def parse_scene(raw):
    meta, prose = {}, raw
    m = HDR.search(raw)
    if m:
        for line in m.group(1).split("\n"):
            kv = re.match(r"\s*([A-Za-z ]+):\s*(.*)$", line)
            if kv:
                meta[kv.group(1).strip().lower()] = kv.group(2).strip()
        prose = raw[m.end():]
    return meta, prose.strip()

def split_list(v):
    if not v:
        return []
    return [x.strip() for x in re.split(r"[,;]", v) if x.strip() and x.strip() != "<>"]

def load_manuscript(root, entities):
    by_name = {}
    for e in entities:
        by_name[e["name"].lower()] = e["id"]
        short = e["name"].replace("The ", "").strip().lower()
        by_name.setdefault(short, e["id"])

    chapters = []
    for cdir in sorted(glob.glob(os.path.join(root, "manuscript", "ch*"))):
        if not os.path.isdir(cdir):
            continue
        chraw = read(os.path.join(cdir, "_chapter.md"))
        scenes = []
        for sp in sorted(glob.glob(os.path.join(cdir, "*.md"))):
            if os.path.basename(sp).startswith("_"):
                continue
            raw = read(sp)
            meta, prose = parse_scene(raw)
            if not prose:
                continue
            mentioned = set()
            low = prose.lower()
            for nm, eid in by_name.items():
                if len(nm) > 3 and re.search(r"\b" + re.escape(nm) + r"\b", low):
                    mentioned.add(eid)
            present = [by_name.get(x.lower()) for x in split_list(meta.get("present", ""))]
            setting = [by_name.get(x.lower()) for x in split_list(meta.get("setting", ""))]
            scenes.append({
                "id": slug(os.path.basename(cdir) + "-" + os.path.basename(sp)[:-3]),
                "title": meta.get("scene") or os.path.basename(sp)[:-3],
                "pov": meta.get("pov", ""),
                "goal": meta.get("goal", ""),
                "status": meta.get("status", ""),
                "present": [x for x in present if x],
                "setting": [x for x in setting if x],
                "mentioned": sorted(mentioned),
                "words": words(prose),
                "html": md(prose),
            })
        chapters.append({
            "id": os.path.basename(cdir),
            "title": title_of(chraw, os.path.basename(cdir)),
            "status": (re.search(r"\*\*Status:\*\*\s*([^\n·|]+)", chraw) or [None, ""])[1].strip(),
            "goal": md(section(chraw, "Chapter goal")),
            "words": sum(s["words"] for s in scenes),
            "scenes": scenes,
        })
    return chapters

# ── build ────────────────────────────────────────────────────────────────────

def build(root):
    chars = load_entities(root, "characters", "character")
    places = load_entities(root, "places", "place")
    facs = load_entities(root, "factions", "faction")
    world = load_entities(root, "world", "world")
    ents = chars + places + facs + world
    chapters = load_manuscript(root, ents)

    return {
        "generated": __import__("datetime").datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "root": root,
        "project": os.path.basename(root.rstrip("\\/")),
        "stats": {
            "words": sum(c["words"] for c in chapters),
            "chapters": len(chapters),
            "scenes": sum(len(c["scenes"]) for c in chapters),
            "characters": len(chars), "places": len(places),
            "factions": len(facs), "world": len(world),
        },
        "chapters": chapters,
        "entities": ents,
        "terms": load_terms(root),
        "ledger": load_ledger(root),
        "plot": load_plot(root),
    }

if __name__ == "__main__":
    root = sys.argv[1] if len(sys.argv) > 1 else r"path\to\your-novel"
    out = sys.argv[2] if len(sys.argv) > 2 else os.path.join(os.path.dirname(__file__), "static", "data.json")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    data = build(root)
    io.open(out, "w", encoding="utf-8").write(json.dumps(data, ensure_ascii=False))
    s = data["stats"]
    print(f"built  {s['words']:,} words · {s['chapters']} ch · {s['scenes']} scenes · "
          f"{s['characters']}c {s['places']}p {s['factions']}f {s['world']}w · "
          f"{len(data['plot'])} beats · {len(data['terms'])} terms")
