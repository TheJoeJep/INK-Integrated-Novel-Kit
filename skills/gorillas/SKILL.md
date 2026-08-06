---
name: gorillas
description: Find "gorillas in the phone booth". Unsignalled oddities that pull a reader out of the story to ask a question the narrative hasn't promised to answer. Use after drafting a scene, when a beta reader reports getting confused or distracted at a specific spot, before finishing a chapter, or when the author asks whether something needs a lantern hung on it. Also use to judge whether a recurring oddity should become the book's tone promise instead of being explained away.
---

# /gorillas: gorilla-in-the-phone-booth audit

> **Tier 1/2 hybrid.** Finding a candidate. An unexplained, unacknowledged oddity dropped into a
> scene. Is mechanical: either the text acknowledges it or it doesn't. Whether it actually kicks
> readers out, and which fix suits it, is judgement. Marked separately.

**Say this on invocation:** *Hunting gorillas. The candidates are mechanical to find; whether
each one actually kicks readers out is a judgement call I'll mark.*

**Source:** [`craft/scene/scene-craft.md`](../../craft/scene/scene-craft.md)

---

## The rule being checked

**The name's origin, from Sanderson's college friend:** a character is on the phone with their
partner, mid-breakup, tense. And the narrative says *he passed a gorilla in the phone booth*,
and keeps going. The reader stops following the breakup. They're thinking about the gorilla.

**A gorilla is anything that makes a reader stop following the story to ask a question the
narrative hasn't signalled it will answer.** Naming it makes it findable.

**Four responses, and this skill's job is to name which fits. Not to write the fix:**

| Fix | What it does |
|---|---|
| **Cut it** | Don't put the gorilla there |
| **Explain in passing (the Charlie fix)** | One clause explains the oddity *and* does other work. Plants a character, seeds a payoff. *"His friend Charlie, home from his shift dancing with the sign on the corner"* explains the gorilla and introduces Charlie in the same breath |
| **Hang a lantern** | Acknowledge without explaining. A character notices and defers it. Signals the author is in control and will return to it |
| **Make it the tone promise** | Keep the gorilla on purpose, repeatedly, as a genre signal. *Guardians of the Galaxy* runs one every few pages, usually paired with a **Watson character** who asks and doesn't get an answer |

### The only test that matters

**Does it kick the majority of readers out of the story?** Not whether it's logically airtight.
Not whether a forum could construct an objection years later. Sanderson's example: the Eagles in
*The Lord of the Rings*. Never bothered him, clearly bothers some readers. **If a significant
number of beta readers snag on the same spot, that's the real signal.** A hypothetical objection
nobody has actually raised is not.

---

## Procedure

**1. Scope.** Current chapter by default; a single scene on request.

**2. Scan for unsignalled oddities:** a detail, coincidence, capability, or event dropped into a
scene without narrative acknowledgment. Weight anything sitting inside a tense or emotional beat
where the detail is orthogonal to what's actually happening. That's the classic setup.

**3. Classify each candidate:**
   - **Acknowledged:** the narrative or a character remarks on it. Not a live gorilla (may still
     be an open lantern. Check whether it's paid off yet).
   - **Unacknowledged:** a live gorilla.

**4. Check for reader evidence.** If the author has beta or alpha feedback naming a snag at this
location, note it. That upgrades a candidate from a maybe to a real finding. Note its absence
too; don't imply evidence that doesn't exist.

**5. For each live gorilla, name all four fix options** with a one-line read on which fits and
why. **Do not pick one for the author and do not rewrite the passage.**

**6. Check for a deliberate pattern.** If the manuscript already runs recurring, unexplained
oddities, especially with a Watson-style character asking and not getting answers, a new
instance may belong to that pattern rather than being an error. Flag this as opinion, not a
mechanical finding.

**7. Report.**

---

## Output format

```
── GORILLAS ── ch01, 3 candidates

  ✗  UNACKNOWLEDGED   ch01/02. The dragon's eyes are "wrong, somehow, in a way
                       he'd itemized before". No character reaction, no
                       narrative follow-through in this scene
                       reader-reported: no beta feedback yet on this passage

  ⚠  OPEN LANTERN      ch01/04. The shed's second lock is mentioned once;
                       protagonist thinks "later". Acknowledged, not yet paid

  ✓  ACKNOWLEDGED      ch01/06. The neighbour's dog goes silent; protagonist
                       notices and remarks on it in the same paragraph

── FINDINGS ──
  1 unacknowledged · 1 open lantern (unpaid) · 1 clean

── OPINION ──
  ✗  ch01/02. "Itemized before" implies research the reader hasn't been shown,
     which is likelier to read as an unearned callback than a gorilla. But if
     it does snag readers, it's cheap to fix well. A Charlie fix (one clause
     naming what the itemizing refers to) resolves it and plants the research
     angle ch02 needs; a full cut costs you that plant; a lantern ("he'd get to
     that") works if you'd rather defer than pay now.

  •  No recurring pattern of tone-promise gorillas in this manuscript yet:
     nothing here reads as a deliberate Guardians-style choice, so the default
     ladder (cut / explain / lantern) applies rather than "leave it as tone."
```

`✗` unacknowledged (live gorilla) · `⚠` lantern hung but unpaid · `✓` acknowledged and clean

---

## Rules

- **The only test that matters is stated every time an opinion judgement is made:** does it kick
  the *majority* of readers out. Not whether an objection could be constructed later. Say this
  explicitly rather than assuming it's understood.
- **Beta and alpha snags are the real signal.** If the author reports readers catching the same
  spot, that's a finding, not a hunch. A hypothetical forum objection is never elevated to one.
- **List all four fix options for every live gorilla.** Never select one. That's the author's
  call, and it's also `/write`'s job, not this skill's.
- **Don't fix the prose.** Findings and named options only.
- **An open lantern is tracked like an unpaid plant** (see `/plants`). Not resolved just because
  it was acknowledged. If it's still unpaid by the end of the book, that's a real finding.
- **A deliberate recurring pattern is not an error.** Say when you think that's what's happening,
  and mark it as your read rather than a finding.
- **Report clean scenes plainly.** Don't manufacture a gorilla to justify the run.


**Delegation:** this check fans out. Dispatch Sonnet subagents per file or per sub-check rather than working sequentially in the main thread. See [skills/_CONVENTIONS.md](../_CONVENTIONS.md). Delegate gathering; keep judgement.

## Related

- `/scene`. Obstacle and ending design; gorillas are a specific scene-craft failure mode
- `/plants`. An open lantern that's never paid off is functionally an orphaned plant
- `/beta-read`. The actual source of "did this kick readers out," which this skill can only
  infer without it
- `/diagnose`. For a confusion complaint that hasn't yet been narrowed to a specific passage
