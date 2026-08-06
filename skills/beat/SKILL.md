---
name: beat
description: Design a single story beat. Its obstacle, what it forces, and what it plants and pays off. Use before writing a beat into an outline or chapter plan, when a beat feels like an event happening rather than a story beat, when deciding whether an obstacle earns its place, or when checking what a beat sets up and pays off. Also use when the author asks whether a plot point is doing enough work to justify itself.
---

# /beat: design a single beat

> **Tier 3. Procedural.** Stages run in order. The obstacle rule at Stage 1 gates everything
> after it. A beat that fails it doesn't get refined, it gets flagged.

**Say this on invocation:** *Designing the beat against the obstacle rule first. Everything else
depends on what the obstacle actually does.*

**Source:** [`craft/structure/structure-models.md`](../../craft/structure/structure-models.md)
(the obstacle rule) · [`craft/structure/try-fail-cycles.md`](../../craft/structure/try-fail-cycles.md)
· [`craft/plot/payoff-and-twists.md`](../../craft/plot/payoff-and-twists.md)

---

## The obstacle rule: the core check

Every obstacle in a beat has to do at least one of three jobs. **If it does none of them, what's
been designed is an event, not a story beat**, and no amount of polish fixes that. The beat needs
a different obstacle, or it needs to be cut.

| | What it does |
|---|---|
| **Force** | Growth is compelled. The character can no longer avoid changing |
| **Reinforce** | Confirms a breakthrough was real, or that a clue actually matters |
| **Show failure** | The character isn't ready yet, which highlights the actual problem |

**The reference case:** the group isn't ready to face Vader. He appears, Obi-Wan steps in and is
killed. The obstacle is survived, and growth is *forced*. Because the person who was holding them
together is now gone. Gandalf's fall does the same job in *The Lord of the Rings*.

---

## Stage 1: State the obstacle and which job it does

Name the obstacle in one line. Then classify it: force, reinforce, or show-failure. **If none
fits, stop here and say so**. That's the finding, and it's more valuable than anything the later
stages would produce for a beat that hasn't earned them yet.

## Stage 2: Entering and exiting state

What does the character know, want, and believe walking into this beat? What's different walking
out? Same three terms the chapter template uses, at beat scale.

**If entering and exiting come out identical, the beat isn't doing work:** the obstacle may have
been survived, but nothing about the character's position moved. That's usually a sign the
obstacle's classified job in Stage 1 was optimistic.

## Stage 3: Which reveal-ladder rung, if any

If the project runs a reveal ladder, check whether this beat sits on a rung. And if it does,
confirm the rung *reinterprets* something the reader already has rather than introducing new
information cold. Not every beat needs a rung. **Say plainly when none applies** rather than
forcing a beat onto the ladder to justify checking this stage.

## Stage 4: What it plants

Name anything laid here that a later beat is expected to reinterpret. An object noticed, a
capability shown, a name mentioned without weight yet. If nothing is planted, say so. Not every
beat has to plant something, but a beat that doesn't shouldn't get mistaken later for one that did.

## Stage 5: What it pays off

Cite the earlier beat this one cashes, if any. **A payoff with no plant on record is the specific
failure `/plants` exists to catch**. Flag it here as an open question rather than letting it pass
quietly into the outline.

## Stage 6: Ending: yes-but or no-and

Does the character solve the beat's problem? **Yes, but**. Solved, at a cost or with a
complication. **No, and**. Unsolved, and worse. Note if it's landing as **yes-and** instead:
that's the closing-mode signal, and it's the wrong call for anything before the story's final
movement.

---

## Output format

```
── BEAT ── he finds the dragon still in the yard at dawn

  OBSTACLE      it hasn't moved, and it's watching him
  JOB           force. He can no longer treat this as something to
                research; a decision is required today

  ENTERING      knows the sighting was real; wants confirmation;
                believes this is still an investigation
  EXITING       knows it's wounded and can't leave; wants to help it
                without anyone finding out; believes this is now
                his responsibility
                → the gap: investigation becomes custody

  REVEAL RUNG   none. This beat is character-only, no ladder rung
  PLANTS        the shed's size, and the loose board in its floor
  PAYS OFF      the backyard sighting, established earlier

  ENDING        yes-but. It doesn't attack him, but it won't let
                him near the wing

── VERDICT ── earns its place. The obstacle forces a real decision

── OPEN QUESTIONS ──
   No reveal-ladder rung assigned. Confirm that's deliberate rather than
   an oversight. Run /diagnose if this beat was meant to reveal something.
```

---

## Rules

- **Refuse to proceed past Stage 1 if the obstacle does none of the three jobs.** That's the
  finding. Don't soften it into a suggestion
- **Entering and exiting must both be stated in know / want / believe terms**, or the gap between
  them can't actually be checked
- **"None" is an acceptable answer at the reveal-ladder and plant/payoff stages.** Don't manufacture
  one to fill the slot
- **A payoff with no recorded plant is a finding, not something to quietly fix here:** hand it to
  `/plants` or `/write`
- **Name the yes-but/no-and call explicitly**, and flag a yes-and outside a deliberate closing
  sequence
- **Don't draft the beat's prose.** This is design; drafting is `/write`

## Related

`/scene` · `/structure` · `/chapter-plan` · `/plants` · `/write`
