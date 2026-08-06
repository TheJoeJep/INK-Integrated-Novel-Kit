---
name: plants
description: Audit setups and payoffs. Find plants that never pay off and payoffs that were never planted. Use before finishing a draft, when a reveal feels unearned or arbitrary, when checking whether foreshadowing lands, or when a structural change might have orphaned a setup. Also use when the author asks about foreshadowing or setup.
---

# /plants: plant and payoff audit

> **Tier 1. Mechanical check.** Matching setups to payoffs is bookkeeping. Whether a plant is
> *subtle enough* is not. Marked separately.

**Say this on invocation:** *Auditing plants and payoffs. Matching is mechanical; calibration
judgements I'll mark.*

**Source:** [`craft/story/structural-rules.md`](../../story/structural-rules.md) (project rules) ·
[`craft/plot/payoff-and-twists.md`](../../craft/plot/payoff-and-twists.md)

---

## The rule

**Every reveal should reinterpret something the reader already saw**, rather than introduce new
information.

**The practical test:** for every reveal, **name the earlier scene it reinterprets.** If you
can't, it isn't planted.

**And the corollary that catches more problems:** if a twist requires introducing a person, place
or object the reader has never met, it has failed regardless of how well it's written.

---

## Procedure

**1. Scope.** Whole book by default. Works on an outline. This is a check you should run *before*
drafting, not after.

**2. Inventory payoffs.** Every reveal, twist, reversal, and moment where something earlier
becomes newly meaningful. Include each rung of the reveal ladder if the project uses one.

**3. For each payoff, find its plant.** Where was this laid? Cite the location.

**4. Inventory plants.** Everything that looks deliberately placed. An object noticed, a name
mentioned, a capability demonstrated, a person introduced who doesn't do anything yet.

**5. For each plant, find its payoff.** If none, it's orphaned.

**6. Check distance.** A plant in the same chapter as its payoff isn't a plant, it's setup. Note
the gap.

**7. Report both directions.**

---

## Output format

```
── PLANTS & PAYOFFS ── whole book, 14 tracked

  PAYOFFS WITHOUT PLANTS  ✗. The serious direction
    Rung 4: "the families ARE the Custodians"        Act 2C
      → requires the Curator and the Heir to be known
      → the Curator currently first appears in Act 2B
      → NOT PLANTED IN ACT 1

    The Elder's argument                              Act 2C
      → nothing in Act 1 or 2 sets up a Custodian who could be sympathetic

  PLANTS WITHOUT PAYOFFS  ⚠
    the neighbour's security camera        ch01/04     → never used
    his sister's phone call                ch01/01     → never returns

  MATCHED  ✓
    "reptilian" used as a joke   ch01/01 → Act 2C, 40 chapters   ✓ good distance
    the specimen drawer          Act 1 mention → Act 2B          ✓
    ...

── FINDINGS ──
  2 unplanted payoffs · 2 orphaned plants · 10 matched

── OPINION ──
  The camera and the sister are cheap to convert. Either could carry
  the leak in beat 5, which is currently undecided.
```

`✓` matched · `✗` payoff with no plant · `⚠` plant with no payoff

---

## Rules

- **Unplanted payoffs are the serious finding.** An orphaned plant is a loose thread; an unplanted
  payoff is a reveal that won't land. Rank accordingly
- **Orphaned plants aren't always errors.** They can be texture, or a series setup. **Say which
  you think it is and mark it as your read**
- **Report the distance.** A plant three pages before its payoff isn't doing the job
- **Don't invent plants.** If you can't cite a location, it isn't one
- **Don't fix.** Findings only. Repair is `/write` in Structure Mode
- **Check the reveal ladder specifically** if the project has one. Each rung must reinterpret,
  not inform


**Delegation:** this check fans out. Dispatch Sonnet subagents per file or per sub-check rather than working sequentially in the main thread. See [skills/_CONVENTIONS.md](../_CONVENTIONS.md). Delegate gathering; keep judgement.

## Related

`/promises` · `/threads` · `/write`
