# Skill conventions

Shared rules every skill follows. Referenced rather than repeated.

---

## Delegate to subagents — default to Sonnet

**Most skill work is independent, read-heavy, and parallelisable.** Reading six scene files to
count signposts, or scanning a chapter for unlisted proper nouns, does not need the main model and
does not need to happen sequentially.

> **Use subagents wherever the work fans out. Default them to Sonnet.**
> **Unless the author specifies a different model — then use what they asked for.**

### Why it matters

- **Time.** Six checks in parallel finish in the time of the slowest, not the sum
- **Cost.** Sonnet is materially cheaper, and scanning files for pattern matches doesn't need
  more
- **Context.** The main thread stays clear for synthesis instead of filling with raw file
  contents — which is what actually degrades quality on a long review

### When to delegate

| Delegate | Keep in the main thread |
|---|---|
| Scanning many files for one thing | Deciding what the findings *mean* |
| Running an independent check per scene or chapter | Reconciling findings that contradict each other |
| Extracting entities, facts, terms from prose | Anything needing the conversation's history |
| Any two checks that don't depend on each other | Talking to the author |

**The dividing line:** delegate *gathering*, keep *judgement*.

### When not to

- **The task is one file and one question.** Dispatch overhead exceeds the work
- **The subagent would need the conversation's context.** It doesn't have it
- **The work is inherently sequential** — each step depends on the last
- **It writes to a shared file.** Parallel writes to the same document clobber each other.
  **Subagents may write to their own scratch outputs; the main thread does the merging**

### How

```
Agent(
  subagent_type: "general-purpose",
  model: "sonnet",
  prompt: "<the exact files to read, the exact check to run,
           the exact output shape, and: do not edit any file>"
)
```

**Give each subagent a precise, closed task.** They don't share your context, so tell them the
paths, the rule they're checking, and the format you want back. Vague delegation returns vague
findings.

**Say what you're doing.** One line — *running six checks in parallel* — so the author knows why
there's a pause and what's happening.

---

## Every skill

1. **Declare the tier** on invocation
2. **Name the craft doc** the guidance comes from
3. **Load only what's needed** — never the whole craft base
4. **Tier 1 and 2 never edit.** Findings only; repair goes through `/write`
5. **Segregate opinion** into a labelled block, never mixed into findings
6. **Report clean runs plainly.** No manufactured concerns to justify the invocation
7. **Name the technique** when using one — the writer learns the vocabulary by watching it work
8. **Attribute honestly** — Kowal, Mull and Wolverton where due

## Tiers

| | | Behaviour |
|---|---|---|
| **1 · Mechanical** | Verifies against a documented rule | Report flatly. Cite both sides. Never fix |
| **2 · Diagnostic** | Symptom → cause via documented base rates | Ranked hypotheses, not verdicts |
| **3 · Procedural** | Runs a documented process | Stages in order. Don't skip ahead |
| **4 · Generative** | Produces raw material | **Say so.** Options, never one answer |
