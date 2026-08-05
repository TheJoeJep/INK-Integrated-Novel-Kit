---
name: chapter-plan
description: Build a chapter's shape against the _chapter.md template — POV, chapter goal, entering and exiting state, and the beat sheet. Use when starting a new chapter, when a chapter's shape feels unclear before drafting, when deciding how long a chapter should run, or when an existing chapter's beats need re-sequencing. Also use when the author asks how many scenes a chapter needs or where its natural break point falls.
---

# /chapter-plan — build the chapter's shape

> **Tier 3 — procedural.** Follows the `_chapter.md` template's fields in order. An unclear field
> is a finding, not something to skip past.

**Say this on invocation:** *Building the chapter plan off the template — POV and states first,
beats after that, length as a deliberate choice rather than a default.*

**Source:** [`templates/chapter.md`](../../templates/chapter.md) ·
[`craft/structure/scale-and-length.md`](../../craft/structure/scale-and-length.md) ·
[`craft/plot/progress-and-signposting.md`](../../craft/plot/progress-and-signposting.md)

---

## The template drives this

Every field in `templates/chapter.md` gets filled, in order. Nothing gets skipped for feeling
premature — a field that comes out vague is itself a finding worth reporting, not a reason to move
on and hope drafting resolves it.

## Stage 1 — POV

Whose head is this chapter in. If it's genuinely uncertain, say so rather than defaulting to
whoever's convenient — POV is a frame decision, not an afterthought filled in once the rest is
settled.

## Stage 2 — Chapter goal

One or two sentences: what this chapter has to accomplish. Test it against progress-and-
signposting — is this something a reader could eventually point at as having happened, or is it a
mood rather than a goal?

## Stage 3 — Entering state

As of the first page: what the protagonist knows, wants, and believes.

## Stage 4 — Exiting state

The same three things, at the close.

**The difference between entering and exiting IS the chapter** — that's the template's own
framing, and it's the load-bearing line of this whole skill. If Stage 3 and Stage 4 come out
identical, the chapter doesn't have a job yet, and the beat sheet shouldn't be built until that's
fixed.

## Stage 5 — Beat sheet

Build the table — beat, scene file, status. Let the beat count fall out of what's actually needed
to close the gap between entering and exiting, rather than reaching for a fixed number out of
habit. Each beat should be checkable against the obstacle rule, but **this skill doesn't re-run
that check** — it names which beats look thin and hands them to `/beat`.

## Stage 6 — Length as a pacing control

Chapter length is one of the few controls that works at the structural level rather than the
sentence level, and it should be chosen, not defaulted:

| Want | Length |
|---|---|
| The reader able to stop here comfortably | Long — a complete unit of story |
| The reader unable to put it down | Short — pulls people through faster than long chapters do |

Long chapters are the right call almost everywhere in a longer book — they give the reader a
finished piece of story to stop on. Reserve short chapters for climactic stretches, where the goal
is specifically to deny a comfortable exit. **Ask which effect this chapter wants** before letting
it default to house average.

## Stage 7 — Notes

Voice reminders, plants to lay, things not to reveal yet — carried forward into drafting.

---

## Output format

```
── CHAPTER PLAN ── ch04 — [working title]

  POV            [character]                                       ✓ stated
  GOAL           he has to decide whether to feed it or report it

  ENTERING       knows it's wounded; wants proof before acting;
                 believes he still has a choice
  EXITING        knows it recognizes him; wants to keep it alive;
                 believes the choice was already made for him
                 → gap: choice collapses into commitment            ✓ real gap

  BEAT SHEET
    #   beat                              scene file        status
    1   he brings food, it doesn't eat    04-food.md        not started
    2   he finds the torn ledger page     04-ledger.md      not started
    3   it lets him touch the wing        04-touch.md       not started

  LENGTH         long — this is a stopping point, not a climax beat  ✓ deliberate

── FINDINGS ──
  Beat 2 has no obstacle stated yet — confirm it forces, reinforces,
  or shows failure before drafting. Run /beat.

── NEXT ──
  Run /beat on beat 2, then /write to draft.
```

---

## Rules

- **Fill every template field.** An empty or vague one is a finding, not something to leave blank
- **Entering and exiting must differ in a stateable way**, or the chapter doesn't have a job yet
  and the beat sheet shouldn't be built until it does
- **Beat count follows from the gap, not a house default number**
- **Chapter length is a decision, not a habit.** Name which effect — stop-here or pull-through —
  is wanted before setting it
- **Hand obstacle-level checking to `/beat`.** Don't re-litigate it here; flag and refer
- **Don't draft scene prose.** This produces the plan's shape only — drafting is `/write`
- **Don't write the plan into the actual `_chapter.md` unasked** — that's `/write` in Structure
  Mode, same as every other doc in this suite

## Related

`/beat` · `/scene` · `/outline` · `/pacing` · `/write`
