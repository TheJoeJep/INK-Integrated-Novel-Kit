---
name: chapter-check
description: Run a full review pass over a chapter — every mechanical check and diagnostic at once, then a single ranked report. Use when a chapter is drafted and ready for review, before moving to the next chapter, when the author asks for a full check or "review this chapter", or when something feels wrong but they can't say what. Defaults to the current chapter if none is named.
---

# /chapter-check — the full review pass

> **Orchestrator.** Runs the other skills and reconciles their findings. Individual checks keep
> their own tiers; **the synthesis is mine, and I'll mark it as such.**

**Say this on invocation:** *Full chapter review — dispatching the checks in parallel, then
reconciling. Individual findings carry their own reliability; the ranking is my judgement.*

**Conventions:** [`skills/_CONVENTIONS.md`](../_CONVENTIONS.md)

---

## Scope

**Default to the current chapter** from `sessions/_current.md`. If the author names one, use that.
Accept "the whole book" — but say it'll take longer and produce a lot.

**If the chapter isn't drafted**, say so and offer the outline-level subset instead: `/threads`,
`/promises`, `/plants` and `/subplot` all work without prose.

---

## Run it in parallel

**This is the skill where delegation matters most** — a dozen checks over the same files, all
independent.

**Dispatch Sonnet subagents, one per check, in two waves.** Don't run them sequentially and don't
run them in the main thread; the context fills with raw file contents and the synthesis suffers,
which is the exact failure this skill exists to avoid.

Unless the author asked for a different model, use Sonnet.

### Wave 1 — mechanical (Tier 1)

All independent. Dispatch together:

| Check | Looking for |
|---|---|
| `/threads` | Threads opened here and never closed; wrong closing order |
| `/promises` | Promises made here; promises this chapter should have paid |
| `/continuity` | Contradictions against the ledger; unrecorded facts |
| `/names` | Proper nouns not in the list; register errors; placeholder debt |
| `/plants` | Plants laid here with no payoff; payoffs with no plant |
| `/visuals` | Entities described in prose with empty or stale Visual blocks |

### Wave 2 — diagnostic (Tier 2)

Dispatch after wave 1 returns, because some depend on its findings:

| Check | Looking for |
|---|---|
| `/pacing` | Chapters where progress is invisible; uniform pacing |
| `/motivation` | Wants undocumented or undramatized |
| `/viewpoint-check` | Head-hopping, mode drift, dead viewpoints |
| `/gorillas` | Unsignalled oddities that eject a reader |
| `/subplot` | Threads running with no archetype or no MDQ connection |

### Wave 3 — per scene, only if warranted

`/scene` on any scene wave 2 flagged. `/dialogue` on any scene that is majority dialogue.
**Don't run these on every scene by default** — it's a wall of output nobody reads.

---

## Then reconcile — this is the actual job

The subagents return raw findings. **Your work is what they can't do:**

**1. Deduplicate.** One root cause surfaces in several checks. A character with no established
want will trip `/motivation`, `/pacing` and `/scene` separately. **Report it once**, and note it
explained three symptoms — that's stronger evidence than any of them alone.

**2. Rank by cost, not by count.** An unplanted payoff for a rung-four reveal outranks nine
placeholder occurrences. **The check that returned the most findings is rarely the most
important.**

**3. Find the causal chain.** Findings that look independent often aren't. *No want in ch01* →
*the choice in beat 3 reads as unmotivated* → *the arc doesn't land in Act 3.* **Say so** — one
fix, three symptoms.

**4. Separate blocking from cosmetic.** Blocking means it must be fixed before the next chapter,
because later work will build on it.

**5. Cut the noise.** If a check returned nothing, say so in one line. Don't pad.

---

## Output format

```
── CHAPTER CHECK ── ch01 · 4 scenes · 6,120 words
   11 checks, 2 waves. Clean: continuity, viewpoint, gorillas.

── BLOCKING ── fix before ch02
  1. The protagonist has no concrete want before beat 3
     Surfaced by: /motivation, /pacing, /scene
     One cause, three symptoms — the choice in beat 3 rests on a
     motivation the reader hasn't been given, so the beat reads as
     arbitrary and the scene reads as slow.
     → craft/character/proactive-relatable-capable.md

  2. Rung 4 has no plant in this chapter
     /plants · the Curator and the Corporate Heir must be established
     in Act 1 or the Act 2C reveal introduces rather than reinterprets.
     → craft/story/structural-rules.md §3

── WORTH FIXING ──
  3. Inquiry thread "who shot her down" opens ch01/02, never closes  /threads
  4. 13 placeholder occurrences across 4 scenes                      /names
  5. The dragon has no Visual block despite 3 described scenes       /visuals

── CLEAN ──
  /continuity  23 assertions, no contradictions
  /viewpoint-check  mode consistent, no head-hopping
  /gorillas  none

── OPINION ──
  Findings 1 and 2 are the chapter. The rest is bookkeeping and can wait
  until the revision map. If you fix only one thing, fix the want.
```

---

## Rules

- **Delegate the checks. Do the synthesis yourself.** That split is the whole design
- **Deduplicate before reporting.** Eleven checks reporting one root cause eleven times is worse
  than useless
- **Rank by cost.** Never by which check was loudest
- **Name the causal chains.** *One fix, three symptoms* is the most valuable thing this produces
- **Report clean checks in one line each.** They're evidence, not filler
- **Never fix anything.** This reports; `/write` and `/revise` repair
- **If everything is clean, say so in three lines and stop.** Don't manufacture concerns
- **Say what the chapter is missing that isn't in any check** — a subplot never started, a beat
  from `plot/` never written. Absence isn't findable by a check that only reads what's there

## Related

`/revision-map` — turn these findings into an ordered work list ·
`/diagnose` · `/revise` · `/write`
