---
name: motivation
description: Check every significant character's motivation against their actions. Use when a character feels wooden, flat, unlikable or unconvincing, when a reader says a character "just didn't work", when someone acts out of character, or before drafting a chapter with several people in it.
---

# /motivation — the 60% check

> **Tier 2 — diagnostic**, with a documented base rate that makes it unusually reliable for a
> Tier 2 skill.

**Say this on invocation:** *Running the motivation check — this is the first thing to check on
any character problem, roughly 60% of the time it's the answer.*

**Source:** [`craft/character/motivation-personality-values.md`](../../craft/character/motivation-personality-values.md)
· [`craft/character/proactive-relatable-capable.md`](../../craft/character/proactive-relatable-capable.md)

---

## Why this skill exists

> When a reader says a character "just didn't work," it is a motivation problem roughly **six
> times out of ten** — not dialogue, not prose.

That base rate is the single most actionable number in the craft base. **Any character complaint
gets this check first**, before dialogue, voice, or prose is touched.

**And the reason it hides:** readers *feel* structural problems and attribute them to character.
*I don't like the protagonist* is frequently a motivation or proactivity failure underneath, and
fixing the dialogue won't touch it.

---

## The three questions

Per character:

1. **Have you clearly shown what they want?** Concretely — not *stability* or *meaning*, but what
   they'd reach for today
2. **Do their actions align with the stated motivation?**
3. **Can readers understand why they make their decisions?**

**Kurt Vonnegut, credited:** make a character want something from the start, **even if it's just a
cup of coffee.**

---

## Procedure

**1. Scope.** Current chapter's cast by default; whole book on request.

**2. Per character, extract the stated want** — from the dossier in `characters/` and from what
the prose shows.

**3. Extract their actions** in scope.

**4. Test alignment.** Does each significant action follow from the want? Flag any that don't.

**5. Check visibility.** Is the want *shown to the reader*, or only recorded in the dossier?
**This is the commonest failure** — the author knows, the text doesn't say.

**6. Check first appearance.** Do they want something concrete in their first scene?

**7. Check for contradictory wants.** Characters *should* want multiple, sometimes
self-contradictory things — that's how people are. Absence of contradiction is a flatness signal,
not a virtue.

**8. Check the Michael problem.** Has one motivation become the character's *only* trait?

---

## Output format

```
── MOTIVATION ── ch01 cast, 4 characters

  THE PROTAGONIST
    stated want    to be right about something, once
    shown          ⚠  present in the dossier; the prose only implies it
    actions align  ✓
    first scene    ✗  he wants nothing concrete in ch01/01
    contradictory  ✓  also wants to not be the person who was right
    crowding       ✓

  THE DRAGON
    stated want    to not be seen
    shown          ✓  "she moved when the light did"
    actions align  ✓
    first scene    ✓
    contradictory  ✗  single-axis want — reads thinner than she should
    crowding       ⚠  fear is currently her only register

── FINDINGS ──
  ✗ protagonist wants nothing concrete in his first scene
    → the whole plot rests on a choice in beat 3; that choice needs
      a want established before it
  ⚠ protagonist's want is documented but not dramatized
  ⚠ the dragon is single-axis — one want, one register
```

---

## Rules

- **Lead with the base rate.** It tells the author how much weight to give the finding
- **"Documented but not shown" is the most common finding** — call it out specifically, because
  authors read their own dossiers into the text
- **Absence of contradictory wants is a finding**, not a clean result
- **Don't confuse a want with a goal.** *Save the world* is a plot objective; *be right about
  something once* is a motivation
- **Don't fix.** Findings only — `/new-character` or `/write` for repair
- **Report clean checks plainly**


**Delegation:** this check fans out. Dispatch Sonnet subagents per file or per sub-check rather than working sequentially in the main thread — see [skills/_CONVENTIONS.md](../_CONVENTIONS.md). Delegate gathering; keep judgement.

## Related

`/diagnose` · `/new-character` · `/character-arc` · `/dialogue`
