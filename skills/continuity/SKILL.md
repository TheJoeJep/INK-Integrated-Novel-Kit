---
name: continuity
description: Check prose and documentation against the continuity ledger for contradictions. Use after drafting, before finishing a chapter, when revising something already written, or when the author suspects an inconsistency. Also use when a structural change might invalidate text that already exists.
---

# /continuity — continuity check

> **Tier 1 — mechanical check.** Comparing statements against a ledger is verification, not
> judgement. Report contradictions flatly with both sources cited.

**Say this on invocation:** *Running a continuity check against the ledger — mechanical, so
findings are as good as the ledger is.*

---

## What's being checked

`canon/continuity-ledger.md` is the append-only record of every hard fact the manuscript has
established. This skill checks everything else against it.

**Three directions, and all three matter:**

1. **Prose vs. ledger** — does the text contradict a recorded fact?
2. **Docs vs. ledger** — does a character/place/world doc contradict one?
3. **Prose vs. docs** — has the text established something the docs don't know about?

**Direction 3 is the one that finds the most**, because it catches facts that were never
recorded rather than facts recorded wrongly.

---

## Procedure

**1. Read the ledger.** `canon/continuity-ledger.md`. Note struck-through entries — those are
retcons, and the replacement is authoritative.

**2. Scope.** Default to the current chapter plus every doc it touches. Whole-manuscript on
request.

**3. Extract assertions** from the material in scope. Physical facts, timeline, capabilities,
relationships, names, what characters know and when.

**4. Compare** in all three directions.

**5. Check timeline separately.** Sequence errors are the commonest continuity failure and the
easiest to miss — who knew what, when, and could they have.

**6. Report.**

---

## Output format

```
── CONTINUITY ── ch01 + 6 docs, 23 assertions checked

  ✗  CONTRADICTS LEDGER
     "he backed the truck out"           ch01/03-the-choice
     ledger: "protagonist owns no vehicle" (ch01/01, 2026-08-04)

  ✗  DOC CONTRADICTS PROSE
     the-shed.md: "no power out here"
     ch01/04-the-shed: "he clicked the work light on"

  !  UNRECORDED — established in prose, absent from docs and ledger
     dragon's left wing torn at the third joint   ch01/02-the-crash
     → belongs in characters/the-dragon.md ## Visual + the ledger

  ⚠  TIMELINE
     he learns her name in 04; uses it in 03

── FINDINGS ──
  2 contradictions · 1 timeline · 4 unrecorded
```

`✗` contradiction · `⚠` timeline · `!` unrecorded fact

---

## Rules for reporting

- **Cite both sides.** Every contradiction names the two sources and quotes the conflicting
  fragments. A finding the author can't verify in ten seconds is not useful.
- **Don't resolve.** Which side is right is the author's call. Resolving is `/write` in Structure
  Mode.
- **Unrecorded facts are findings, not errors.** They're the doc-maintenance backlog. Say where
  each belongs.
- **Respect retcons.** A struck ledger row is not a contradiction; it's a decision. Never
  re-flag one.
- **Never edit the ledger from this skill.** Ledger writes happen through the documentation
  protocol at scene end, so they're logged. This skill reads only.
- **Report clean checks plainly.** *23 assertions, no contradictions, 4 unrecorded facts.*


**Delegation:** this check fans out. Dispatch Sonnet subagents per file or per sub-check rather than working sequentially in the main thread — see [skills/_CONVENTIONS.md](../_CONVENTIONS.md). Delegate gathering; keep judgement.

## Related

- [`.claude/skills/write/references/doc-protocol.md`](../write/references/doc-protocol.md) — how
  facts reach the ledger in the first place
- `/names` — a narrower check, for proper nouns specifically
