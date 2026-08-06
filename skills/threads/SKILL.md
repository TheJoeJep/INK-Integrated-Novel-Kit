---
name: threads
description: Audit every open narrative thread and verify each one closes, in the right order. Use when an ending feels unsatisfying, when a draft or outline feels like it's missing something you can't name, or before calling a chapter, act, or book finished. Also use when the author asks about loose ends, dangling plots, or unresolved subplots.
---

# /threads: thread audit

> **Tier 1. Mechanical check.** This is bookkeeping against a documented rule, not a judgement
> call. Report findings flatly. If a thread is unclosed, say so; don't soften it, and don't
> speculate about whether it "works anyway" unless asked.

**Say this on invocation:** *Running a thread audit. This is a mechanical check, so the findings
are as reliable as the source docs.*

---

## The rule being checked

From **Mary Robinette Kowal** (MICE Quotient, nesting) and **Sanderson** (bracketing). Two
teachers who arrived at it independently, four years apart, which is the strongest evidence in
the craft base that it's real.

Read [`craft/short-fiction/short-fiction.md`](../../craft/short-fiction/short-fiction.md) and
[`craft/structure/the-box.md`](../../craft/structure/the-box.md) before running this.

**Every thread opens one way and must close a matching way:**

| Type | Opens with | Closes with |
|---|---|---|
| **Milieu** | Entering a place | Exiting it |
| **Inquiry** | A question asked | The question answered |
| **Character** | An identity shift beginning | Self-definition solidifying |
| **Event** | Status quo disrupted | New status quo established |

**And nesting: last opened, first closed.** Open Inquiry inside Milieu and the Inquiry must close
first.

**Red herrings are Inquiry threads.** They still need closing.

---

## Procedure

**1. Establish scope.** Ask what to audit if unclear: a scene, chapter, act, or the whole book.
Default to the current chapter.

**2. Read the material.** For drafted prose, the scene files. For undrafted work, the `plot/`
docs and `story/outline.md`. **This audit works on an outline, before a word is written.**

**3. Build the thread table.** For each thread: type, where it opens, what its matching close
would be, and where (if anywhere) it closes.

**4. Check three things, in this order:**
   - **Unclosed:** opened, never closed. The commonest cause of an unsatisfying ending
   - **Mismatched:** closed the wrong way. An Inquiry answered when a Milieu was opened
   - **Out of order:** closed before something nested inside it

**5. Report.**

---

## Output format

```
── THREADS ── ch01, 4 open

  ✓  Milieu    the shed              opens 02-the-crash → closes 06-the-raid
  ✓  Event     Reveal Day            opens 01-the-overpass → closes ch01 exit state
  ✗  Inquiry   who shot her down     opens 02-the-crash → NEVER CLOSES
  ⚠  Character he decides to help    opens 03-the-choice → closes 08-recruitment
                                     ↳ nested inside Milieu(shed), but closes after it

── FINDINGS ──
  1 unclosed · 1 order violation · 0 mismatched
```

Use `✓` closed correctly, `✗` unclosed, `⚠` order or type problem.

---

## Rules for reporting

- **Don't propose fixes unless asked.** This skill finds; it doesn't repair. If the author wants
  a fix, that's `/write` in Structure Mode.
- **An unclosed thread is not automatically wrong.** In a series, a deliberately open thread is a
  promise for the next book. **Say which you think it is, and mark it as your read rather than a
  finding.**
- **Don't invent threads.** If you can't point at where something opens, it isn't a thread.
- **Report zero findings plainly.** *4 threads, all close correctly, order is clean.* Don't
  manufacture concerns.


**Delegation:** this check fans out. Dispatch Sonnet subagents per file or per sub-check rather than working sequentially in the main thread. See [skills/_CONVENTIONS.md](../_CONVENTIONS.md). Delegate gathering; keep judgement.

## Related

- [`craft/plot/promise-progress-payoff.md`](../../craft/plot/promise-progress-payoff.md). A
  thread that closes without paying its promise is a different failure; use `/promises`
- [`craft/reference/problem-to-technique.md`](../../craft/reference/problem-to-technique.md)
