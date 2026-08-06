---
name: revision-map
description: Build the tiered revision to-do list used by stage 2.0 of the five-stage framework. Top tier (pervasive, book-spanning), middle (scene/sequence), bottom (local, checkable). Use when starting self-revision after a straight-through draft, when alpha feedback has arrived and needs sorting, when revision feels too big to start, or before running /revise at stage 2.0 or after an alpha read.
---

# /revision-map: the tiered revision map

> **Tier 3, procedural.** This runs a documented multi-stage process, gather, sort, sequence.
> in that order. The stages aren't optional and the tiers aren't a suggestion: working out of
> order wastes work, which is the whole reason this exists as its own step.

**Say this on invocation:** *Building a revision map. I'll gather items, sort them into top,
middle, and bottom tier, and hand you the top tier first. Nothing below it is worth touching yet.*

**Source:** [`craft/revision/revision-and-diagnosis.md`](../../craft/revision/revision-and-diagnosis.md)

---

## What this produces

A single prioritized list, hard-sorted into three tiers, per Sanderson's 2.0 self-revision method
and the same structure alpha feedback gets re-sorted into afterward.

| Tier | Contains | His example |
|---|---|---|
| **Top** | Pervasive, book-spanning problems too large to spot-check | An entire character arc doesn't work |
| **Middle** | Scene- and sequence-level fixes | A beat resolves too easily; a chapter's POV is wrong |
| **Bottom** | Local, checkable items | A line of dialogue is flat; a continuity slip |

**The rule that makes the tiers worth having:** work top tier first, completely, before touching
the middle. A book-spanning fix invalidates everything below it. There's no point polishing a
scene that belongs to an arc you're about to rebuild.

---

## Sources of items

Pull from whichever of these exist. Don't skip a source because it's inconvenient to check.

| Source | What it gives you |
|---|---|
| **The author's own drafting notes** | Placeholder flags from 1.0, *remember a bucket*, and anything you already knew was wrong while writing it |
| **Tier-1 check skills** | `/threads`, `/promises`, `/continuity`, `/names`, `/plants`. Run any that haven't been run recently; their findings are mechanical, not opinion, and slot straight into a tier |
| **Alpha feedback** | Diagnosis from industry-savvy readers. See `/beta-read` alpha mode. This is the source that produces a *fresh* map, not an addition to the 2.0 map: unresolved 2.0 items carry forward onto it |

---

## Procedure

**1. Gather.** Ask which sources apply. Pull items from each. The author's notes, any Tier-1
skill findings on hand, alpha feedback if this is a post-alpha map. Don't summarize yet; just
collect.

**2. Sort.** For every item, classify it top, middle, or bottom using the scope test:

- **Would fixing this change what happens in scenes other than where it's found?** → top
- **Is it contained to one scene or a short sequence, but requires more than a line-edit?** → middle
- **Can it be checked and fixed without touching anything upstream or downstream?** → bottom

**When unsure, classify up, not down.** A misclassified bottom-tier item wastes a revision pass
finding out it was actually structural; a misclassified top-tier item just gets confirmed small
and demoted.

**3. Sequence.** Within the top tier, order by how many downstream items each one would
invalidate if changed. Highest first. Don't bother sequencing middle or bottom; they're worked
after the top tier is fully resolved anyway, and their order may change once it is.

**4. Present the map**, top tier only expanded in full; middle and bottom listed but not detailed
until the top tier closes.

---

## Output format

```
── REVISION MAP ── 17 items · sources: drafting notes, /threads, /continuity, alpha read

  TOP TIER. 3 items · work these first, completely
    1. [alpha] The antagonist's motivation is never shown on the page. Every
       scene with him reads as arbitrary cruelty until ch19, which recontextualizes
       nothing before it.
    2. [notes] The protagonist has no want established before ch04.
    3. [/threads] The Inquiry thread "who shot her down" never closes.

  MIDDLE. 8 items · after the top tier, not before
    4. [alpha] ch07 resolves its obstacle with no real cost.
    5. [/continuity] ch11 states the shed door was locked; ch03 shows it open.
    … (5 more)

  BOTTOM. 6 items · after the middle
    11. [/names] "Curator" used once where "the Custodian" is meant.
    … (5 more)

── NOW ──
   Item 1. Nothing in the middle or bottom tier is safe to work until the
   antagonist's motivation is settled. Several middle-tier scenes exist to
   service him and may not survive the fix.
```

---

## Rules

- **Work top tier first, completely.** Don't present a flattened list, and don't let the author
  cherry-pick a satisfying bottom-tier fix instead of the top-tier item they're avoiding:
  name that if you see it happening.
- **Re-sort after each top-tier item closes.** A resolved top-tier item can upgrade or downgrade
  what's below it; don't assume the middle and bottom tiers are stable once set.
- **Don't invent items.** Every entry traces to a source. A drafting note, a named Tier-1
  finding, or a specific alpha comment. If you can't cite where it came from, it doesn't go on
  the map.
- **Tag each item with its source** (`[notes]`, `[/threads]`, `[alpha]`, …) so the author can
  weigh it appropriately. A mechanical `/continuity` finding and an alpha reader's hunch aren't
  the same grade of evidence.
- **This skill sorts and sequences. It doesn't fix.** Repair happens in `/write`.
- **A fresh alpha map absorbs unresolved 2.0 items** rather than replacing them. Carry forward,
  don't drop.


**Delegation:** this check fans out. Dispatch Sonnet subagents per file or per sub-check rather than working sequentially in the main thread. See [skills/_CONVENTIONS.md](../_CONVENTIONS.md). Delegate gathering; keep judgement.

## Related

`/revise` · `/beta-read` · `/polish` · `/threads` · `/promises` · `/continuity` · `/names` ·
`/plants`
