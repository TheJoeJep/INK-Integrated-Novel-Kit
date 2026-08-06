---
name: promises
description: Audit every promise the story makes to the reader and check whether each one is paid off. Use when an ending feels unearned or predictable, when readers report being misled or disappointed, when checking whether an opening sets up the right expectations, or before finishing a draft. Also use when the author asks about setup and payoff, foreshadowing, or whether the book delivers what it advertises.
---

# /promises: promise and payoff audit

> **Tier 1. Mechanical check**, with one judgement call flagged inline. Finding promises and
> matching them to payoffs is bookkeeping. Deciding whether a payoff is *satisfying* is not.
> mark that separately.

**Say this on invocation:** *Running a promise audit. The matching is mechanical; any judgement
about whether a payoff lands, I'll mark as opinion.*

---

## The rule being checked

Read [`craft/plot/promises.md`](../../craft/plot/promises.md) and
[`craft/plot/payoff-and-twists.md`](../../craft/plot/payoff-and-twists.md) first.

**A promise is something the opening does whether the author intended it or not.** Five kinds:

| Kind | Made by |
|---|---|
| **Tone** | Early jokes, an opening brutality, character names, prose register |
| **Story** | Showing the shape of the eventual conflict |
| **Character / conflict** | Want, need, and why they can't have it |
| **Structural** | Genre conventions, length, series packaging |
| **Cold open** | A microcosm of the whole story |

**Payoff = surprising yet inevitable.** Both halves required.

---

## Procedure

**1. Scope.** Whole book by default. Can also run on an act, a chapter, or a single subplot.

**2. Read.** `plot/` docs, `story/outline.md`, `manuscript/` prose if it exists, and the first
pages of anything drafted. **Promises live disproportionately in openings.**

**3. Inventory promises.** For each: kind, where made, and what it commits the book to. Include
promises made **accidentally**. That's most of the value here. A prologue that opens on a battle
promises a book with battles in it.

**4. Match payoffs.** For each promise: is it paid, where, and does the payoff answer *that*
promise or a different one?

**5. Check the reverse.** Any payoff with no promise behind it? That's the *ghost army* problem:
a rescue nobody was set up to expect reads as relief rather than triumph.

**6. Report.**

---

## Output format

```
── PROMISES ── whole book, 7 tracked

  ✓  Tone       delight, not terror       ch01 opening        → held throughout
  ✓  Character  he wants the truth        ch01 → Act 2B payoff
  ✗  Story      "the good guys lost"      ch01 prologue       → NOT PAID
  ⚠  Structural epic-fantasy length       packaging           → book is 70k; scope may under-deliver
  !  PAYOFF WITH NO PROMISE. The Rider extraction (beat 7) arrives unset up

── FINDINGS ──
  1 unpaid · 1 scope mismatch · 1 unpromised payoff
```

`✓` paid · `✗` unpaid · `⚠` partial or mismatched · `!` payoff lacking a promise

---

## Judgement calls: mark these separately

After the mechanical table, a short section headed **`── OPINION ──`** for anything that isn't
verifiable:

- Whether a payoff is *satisfying*, not merely present
- Whether a promise is strong enough to carry the reader
- Whether a twist earns itself

**Keep it short and label it.** The value of this skill is the table; the opinion section is a
courtesy and should read as one.

---

## Rules for reporting

- **Accidental promises are the point.** The author knows what they meant to promise. Look for
  what the text promises regardless.
- **Check the promise the book actually made**, not the better one the author thought of in act
  two. That substitution is the commonest cause of an unsatisfying ending.
- **Apply the Gandalf test where relevant:** could a *kept promise*, timed so the reader forgot
  it, outperform the twist being planned? Flag it as an option, not a correction.
- **Don't fix.** Findings only.
- **Report clean audits plainly.**


**Delegation:** this check fans out. Dispatch Sonnet subagents per file or per sub-check rather than working sequentially in the main thread. See [skills/_CONVENTIONS.md](../_CONVENTIONS.md). Delegate gathering; keep judgement.

## Related

- `/threads`. A thread that closes without paying its promise is a distinct failure
- [`craft/reference/problem-to-technique.md`](../../craft/reference/problem-to-technique.md)
