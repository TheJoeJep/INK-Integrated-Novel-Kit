# Skill Routing — invoking without being asked

**The arbitration layer.** Skill `description:` fields say *when a skill applies*. This says
**which one wins, when to fire, and — most importantly — when to stay quiet.**

This is written to be pasted into a project's `CLAUDE.md`. It is behavioural instruction, not
craft.

---

## The governing rule

> **Never interrupt drafting to run a check.**

Inside a `/write` loop, the writer is holding a scene in their head. A continuity finding — however
correct — costs more than it's worth mid-beat. **Note it silently in the session log and raise it
at the scene boundary.**

The only exceptions, because they get *harder* to fix with every sentence written:

- A **proper noun not in `canon/names-and-terms.md`** is about to be used
- The beat about to be written **contradicts `canon/continuity-ledger.md`**

Both get one line before writing, not a check afterwards.

---

## Arbitration — which skill wins

**When several match, the general one goes first.** A narrow check run on the wrong hypothesis
wastes the writer's time and produces confident findings about the wrong thing.

| The writer says | Invoke | Not |
|---|---|---|
| Any symptom — *flat, boring, slow, doesn't work* | **`/diagnose`** | The specific check. `/diagnose` routes |
| *This character doesn't work* | **`/motivation`** first | `/dialogue` — motivation is the cause ~60% of the time |
| *The dialogue is bad* | **`/motivation`**, then `/dialogue` | Dialogue rarely fails on its own |
| *The ending doesn't land* | **`/promises`**, then `/plants` | `/scene` |
| *Chapter N drags* | **`/pacing`** | `/scene` — pacing is act-scale |
| *This scene isn't working* | **`/scene`** | `/pacing` — scene-scale |
| *I don't know where to start revising* | **`/revision-map`** | `/revise` — it needs a map first |
| *Is this idea any good?* | **`/premise-test`** | `/brainstorm` — that's for having no idea yet |

**Two hard precedence rules:**

1. **`/diagnose` before any Tier 2 check** when the writer reports a *symptom* rather than naming
   a suspected cause. It exists to prevent guessing.
2. **`/motivation` before `/dialogue` or `/scene`** on any character complaint. The base rate
   justifies it.

---

## Fire automatically at boundaries

These run without being asked, because the writer can't see what they'd catch.

**At scene end** — as part of the documentation promotion pass:

- `/visuals` if the scene described any character, place or faction
- `/continuity` if it established hard facts
- `/names` if any new proper noun appeared

Report these **inside the existing receipt block**, not as separate output.

**At chapter end:**

- `/threads` — what opened in this chapter, what closed
- `/promises` — what this chapter promised

**At act end:**

- `/pacing` across the act
- `/plants` — orphaned setups and unplanted payoffs
- `/threads` at act scope

**Before drafting a new chapter:**

- `/chapter-plan` if no `_chapter.md` exists. Don't draft into an unplanned chapter

---

## Fire on creation

| Writer does | Offer |
|---|---|
| Names a new character | `/new-character` — offer, don't assume. They may just be mentioning someone |
| Names a new place or faction | `/new-place` / `/new-faction` |
| Introduces a speculative capability | `/magic-system` |
| Starts a chapter with no beat sheet | `/chapter-plan` |

**Offer, don't run.** Creation skills are Tier 4 and take the writer's time. One line: *want me
to build this out properly?*

---

## Fire on blocked work

- A **BLOCKING open question** stands between the writer and what they're trying to do →
  say which, and offer the skill that resolves it (`/magic-system`, `/new-character`, etc.)
- A **Tier 1 check found something** that invalidates the current plan → raise it *before*
  writing, not after

---

## When to stay quiet

**Say nothing and run nothing when:**

- Mid-beat inside a drafting loop
- The writer is thinking out loud rather than asking
- A check was run on this material within the session and nothing has changed
- The finding is cosmetic and the writer is working on structure
- You've already raised it once and they moved on. **Don't raise it twice**

**Never run more than two checks unprompted at once.** A wall of findings reads as noise and
trains the writer to ignore all of it.

---

## How to announce an unprompted invocation

One line, before the output, naming the trigger:

> *Chapter end — running `/threads` and `/promises`.*

> *That's a symptom rather than a cause, so I'm starting with `/diagnose` rather than guessing.*

> *Before I write this: "the Ossuary" isn't in `names-and-terms.md`.*

**Never invoke silently.** The writer must be able to tell when they're getting a skill's
structured output versus ordinary conversation — and to say *don't* next time.

---

## The anti-pattern this exists to prevent

A system that runs every applicable check at every opportunity is worse than one that runs none.
The writer stops reading the output, and the genuinely important finding — the unplanted payoff,
the contradicted ledger entry — is buried in a list of things they didn't ask about.

**Bias toward silence. Earn the interruptions.**
