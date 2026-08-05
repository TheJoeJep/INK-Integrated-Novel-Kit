# Documentation protocol

The rule: **nothing lives only in the prose.** If a scene establishes it, a document holds it.

The problem: doing a full documentation pass after every 200 words makes the loop unusable.
So it's split — cheap logging every exchange, real promotion at scene end, with an escape
hatch for facts too important to wait.

---

## The scene header — keep it current

Every scene file opens with a header comment. **The dashboard's context sidebar is driven by it**,
so a stale header means a reader scrolling that scene sees the wrong people in the panel.

```markdown
<!--
SCENE: The Crash
CHAPTER: 1
BEAT: 2
POV: the protagonist
SETTING: The Shed
PRESENT: the protagonist, the dragon
GOAL: give him the problem
STATUS: drafting
-->
```

**Update `PRESENT` and `SETTING` the moment they change** — when someone enters or leaves, or the
scene moves somewhere else. It's a one-line edit and it belongs to writing the beat, not to a
separate pass.

Names must match the document titles in `characters/`, `places/` and `factions/` exactly, or they
won't resolve. Anything unlisted still shows in the sidebar under *Mentioned* if the prose names
it — but *Present* and *Setting* come only from here.

---

## Every exchange — log

Append to `sessions/log/YYYY-MM-DD.md`. Create it if today's file doesn't exist.

Format — one line per fact, source scene in brackets, destination doc, then the fact:

```
- [ch01/02-the-crash] characters/the-dragon.md → Visual: left wing torn at the third joint
- [ch01/02-the-crash] places/boston/the-shed.md → corrugated roof, one bulb, no lock
- [ch01/02-the-crash] canon/continuity-ledger.md → dragon cannot fly; duration TBD
```

Log the fact, not the sentence. "He notices the wing is bent wrong" is prose. "Left wing torn
at the third joint" is a fact.

## Every exchange — write through, but only if canon-changing

Some facts are too structural to sit in a log until scene end. Write these into their real
document immediately:

- **A new proper noun** → `canon/names-and-terms.md`, immediately, or the next exchange will
  contradict it
- **A rule about how the world works** → the relevant `world/` doc
- **A revealed plot fact** — something the reader now knows → the `plot/` doc and the ledger
- **A new character or place** → create the doc from the template, minimum viable fill
- **Anything ledger-worthy** — a hard physical or situational fact the next scene must respect

Everything else waits. Eye color, the weather, what he had for lunch — log it, promote later.

**Test:** would writing the *next* beat go wrong if this weren't recorded yet? If yes, write
it through now.

---

## Scene end — promote

In order:

1. **Read the log** entries since the last promotion.
2. **Route each one** into its document, in the correct template section. Not appended to the
   bottom — into the section where that kind of fact belongs. A physical detail goes under
   `## Visual`, a relationship change under `## Relationships`, a hard fact under
   `## Established facts` with its scene reference.
3. **Append to `canon/continuity-ledger.md`** — every hard fact, with source and date.
4. **Update `## Visual` blocks** for every entity the scene physically described. This is the
   step that makes image generation possible later; it is not optional.
5. **Update `_chapter.md`** — beat status, and the scene file's row in the beat sheet.
6. **Update `manuscript/_status.md`** — word counts, chapter status.
7. **Update `sessions/_current.md`** — see below.
8. **Mark the log** with a `--- promoted <date> ---` line so the next promotion knows where
   to start.
9. **Ship it.** Run the project's ship command so the work is committed and pushed. The novel
   should never be more than one scene behind its repository. If the project has no such
   command, commit manually — but don't leave a finished scene uncommitted.

---

## `sessions/_current.md`

This is the resume pointer. It must be good enough that a session starting cold, with no
memory of this conversation, can pick up without asking the author what was happening.

```markdown
# Current position

**Updated:** 2026-08-04
**Mode last used:** Chapter
**Chapter:** ch01 — Reveal Day
**Scene:** 02-the-crash.md
**Beat:** 3 of 6 — he decides not to call anyone

## Last written
> "...and I stood there in the wet grass with my phone in my hand, not
> dialing it, for what the record will say was four minutes."

## Pending
Offered directions for beat 4. The author hasn't answered:
  A) He goes inside for supplies
  B) The dragon speaks
  C) A car slows on the street

## Notes
Voice is running longer-sentenced than the sample. Watch it.
```

---

## The continuity ledger

`canon/continuity-ledger.md` is **append-only**. Entries are never deleted.

If a fact is retconned, strike the row and point at what replaced it:

```
| ~~Protagonist owns a truck~~ | ch01/01 | 2026-08-04 | Retconned 2026-08-11 → he has no vehicle |
```

The history of a decision is worth more than a clean file. A struck row tells you the option
was considered and rejected; a deleted row tells you nothing, and the idea comes back.

---

## What does not go in documents

Don't document the prose itself. Documents hold **facts, decisions, and constraints** — not
retellings of scenes. If a doc entry could be replaced by "go read the scene," it shouldn't
be there.

Plot docs describe what a beat is *for*. The manuscript describes what happens.
