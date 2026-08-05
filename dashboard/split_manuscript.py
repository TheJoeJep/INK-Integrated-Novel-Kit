"""
Split an existing manuscript into the workspace structure.

    python split_manuscript.py <input.md|.txt> <story-workspace> [--dry-run]

Detects chapter breaks, writes manuscript/chNN-slug/01-<slug>.md with a header
comment stub, and leaves every field blank for a human or a skill to fill.

It does NOT touch anything outside manuscript/, and it will not overwrite an
existing chapter folder without --force.
"""
import io, os, re, sys, argparse

CHAPTER_PATTERNS = [
    r"^#{1,3}\s*chapter\s+([\dIVXLC]+|[a-z]+)\b[:\s]*(.*)$",   # ## Chapter 4 — Title
    r"^#{1,3}\s+(\d+)\s*[.:—-]\s*(.+)$",                        # ## 4 — Title
    r"^\s*chapter\s+([\dIVXLC]+|[a-z]+)\b[:\s]*(.*)$",          # Chapter Four
    r"^#{1,2}\s+(.+)$",                                          # any H1/H2, last resort
]
SCENE_BREAK = re.compile(r"^\s*(\*\s*\*\s*\*|#{3,}|—{3,}|-{3,}|~{3,}|⁂|\*{3,})\s*$")


def slug(s, n=48):
    # Drop a leading chapter number / roman numeral — the folder is already
    # numbered, so "1 - The Overpass" should slug as "the-overpass".
    s = re.sub(r"^\s*(chapter\s+)?([\dIVXLC]+|one|two|three|four|five|six|seven|eight|nine|ten)"
               r"\s*[-—:.]*\s*", "", s.strip(), flags=re.I)
    s = re.sub(r"[^\w\s-]", "", s.lower()).strip()
    s = re.sub(r"[\s_]+", "-", s)
    s = re.sub(r"-{2,}", "-", s)
    return (s[:n].strip("-") or "untitled")


def find_chapters(lines):
    """Return [(line_index, title)] using the first pattern that finds >1 match."""
    for pat in CHAPTER_PATTERNS:
        rx = re.compile(pat, re.I)
        hits = []
        for i, ln in enumerate(lines):
            m = rx.match(ln.strip())
            if m:
                parts = [g for g in m.groups() if g]
                title = " ".join(parts).strip(" —-:")
                hits.append((i, title or f"Chapter {len(hits)+1}"))
        if len(hits) > 1:
            return hits
    return []


def split_scenes(body):
    scenes, cur = [], []
    for ln in body:
        if SCENE_BREAK.match(ln):
            if any(x.strip() for x in cur):
                scenes.append(cur)
            cur = []
        else:
            cur.append(ln)
    if any(x.strip() for x in cur):
        scenes.append(cur)
    return scenes or [body]


HEADER = """<!--
SCENE: {scene}
CHAPTER: {ch}
BEAT:
POV:
SETTING:
PRESENT:
GOAL:
STATUS: imported
-->

"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("source")
    ap.add_argument("workspace")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--force", action="store_true")
    a = ap.parse_args()

    if not os.path.isfile(a.source):
        sys.exit(f"not found: {a.source}")
    if not os.path.isdir(a.workspace):
        sys.exit(f"workspace not found: {a.workspace}")

    text = io.open(a.source, encoding="utf-8-sig", errors="replace").read()
    lines = text.split("\n")
    chapters = find_chapters(lines)

    if not chapters:
        print("No chapter breaks detected. Treating the whole file as one chapter.")
        chapters = [(0, "Chapter 1")]

    bounds = [c[0] for c in chapters] + [len(lines)]
    plan = []
    for n, (start, title) in enumerate(chapters, 1):
        body = lines[bounds[n - 1] + 1: bounds[n]]
        cdir = f"ch{n:02d}-{slug(title)}"
        scenes = split_scenes(body)
        plan.append((cdir, title, scenes))

    total_words = sum(len(" ".join(s).split()) for _, _, sc in plan for s in sc)
    print(f"\n  {len(plan)} chapters · {sum(len(s) for _,_,s in plan)} scenes · {total_words:,} words\n")
    for cdir, title, scenes in plan:
        w = sum(len(" ".join(s).split()) for s in scenes)
        print(f"  {cdir:<42} {len(scenes)} scene(s)  {w:>7,} words")

    if a.dry_run:
        print("\n  dry run - nothing written\n")
        return

    mroot = os.path.join(a.workspace, "manuscript")
    written = 0
    for cdir, title, scenes in plan:
        cpath = os.path.join(mroot, cdir)
        if os.path.isdir(cpath) and not a.force:
            print(f"\n  EXISTS, skipped: {cdir}  (use --force to overwrite)")
            continue
        os.makedirs(cpath, exist_ok=True)
        chfile = os.path.join(cpath, "_chapter.md")
        if not os.path.exists(chfile) or a.force:
            io.open(chfile, "w", encoding="utf-8").write(
                f"# {title}\n\n**POV:** \n**Status:** imported\n**Word count:** "
                f"{sum(len(' '.join(s).split()) for s in scenes)}\n\n"
                f"## Chapter goal\n\n## Entering state\n\n## Exiting state\n\n"
                f"## Beat sheet\n\n| # | Beat | Scene file | Status |\n|---|---|---|---|\n\n## Notes\n")
        for i, sc in enumerate(scenes, 1):
            body = "\n".join(sc).strip()
            first = next((l.strip() for l in sc if l.strip()), "scene")
            name = f"{i:02d}-{slug(first, 32)}.md"
            io.open(os.path.join(cpath, name), "w", encoding="utf-8").write(
                HEADER.format(scene=first[:60], ch=cdir) + body + "\n")
            written += 1

    print(f"\n  wrote {written} scene files into {mroot}")
    print("  headers are stubs - POV / SETTING / PRESENT are blank on purpose.")
    print("  Run /import in the story workspace to fill them and derive dossiers.\n")


if __name__ == "__main__":
    main()
