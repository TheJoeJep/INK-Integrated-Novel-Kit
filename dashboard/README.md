# Dashboard

A local, read-only reading view of a story workspace, with a context sidebar that follows the
scroll.

```
python serve.py "path\to\your-novel"
```

Then open **http://localhost:8778**. Add `--open` to launch a browser automatically.
Second argument sets the port.

---

## The one design decision that matters

**The markdown is the database.** This tool derives everything it shows by reading the workspace,
and never writes to it.

That means:

- **No sync problem.** The dashboard cannot disagree with the docs, because it *is* the docs
- **No skill had to change.** Skills keep writing markdown exactly as before
- **No second source of truth** to drift or need reconciling

A real database would have bought nothing here and cost the thing that matters most — a single
place where a fact lives.

---

## How the sidebar decides what's relevant

Two sources, in priority order:

**1. The scene header** — authoritative.

```markdown
<!--
SCENE: The Crash
POV: the protagonist
SETTING: The Shed
PRESENT: the protagonist, the dragon
-->
```

**2. Name matching** against entity titles, for anything mentioned but not in the header.

Where they disagree, the header wins. Anything matched only by name appears under **Mentioned**
rather than **Present**.

**Keeping headers current is part of the documentation protocol.** A scene with no header still
renders — it just gets no sidebar context.

---

## What it reads

| Source | Becomes |
|---|---|
| `manuscript/chNN-*/` | The reading view. Scene header comments become metadata |
| `characters/`, `places/`, `factions/`, `world/` | Sidebar cards and browsable views. `## Visual`, `## Role in the story` and `## Established facts` are pulled out specifically |
| `plot/` | The Plot view, grouped by act |
| `canon/names-and-terms.md` | The terms table |
| `canon/continuity-ledger.md` | The ledger table |

Anything in an `images/` folder or beginning with `_` is skipped.

---

## Auto-rebuild

The server polls the workspace every 1.5s and rebuilds when any markdown changes. The page polls
`data.json` every 3s and re-renders when the build stamp moves.

So: write a scene, and the tab updates within a few seconds. Leave it open on a second monitor.

---

## Files

| | |
|---|---|
| `build.py` | Reads a workspace, emits `static/data.json`. Runnable alone |
| `serve.py` | Server + file watcher. Read-only |
| `static/` | The page. `data.json` is generated — gitignored |

`build.py` includes a small dependency-free markdown renderer. It escapes HTML and refuses link
schemes other than `http`, `https`, `mailto`, and relative paths — the content is your own, but
the page renders it, so it shouldn't be a way to execute anything.

**Known quirk it handles:** files written by PowerShell's `Out-File` carry a UTF-8 BOM, which
breaks leading-anchor regexes and silently turns document titles into filenames. Files are read
as `utf-8-sig`.
