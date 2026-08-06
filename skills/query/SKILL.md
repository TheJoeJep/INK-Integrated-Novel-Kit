---
name: query
description: Draft a query letter. Hook, comp titles, brief credentials, and housekeeping (title, word count, genre). Use when preparing to query literary agents, when the manuscript is finished and ready to submit, or when practicing the hook paragraph. Flags that specific market conventions drift and directs the author to the target agent's current guidelines rather than asserting norms.
---

# /query: the query letter

> **Tier 4. Generative, with a documented-staleness warning attached.** The four-part *shape* of
> a query is durable. The *specifics*. Expected word-count ranges, simultaneous-submission norms,
> formatting quirks, whether comps are wanted. Drift by year and by agency, and the craft base
> behind this skill is a dated snapshot, not live market data.

**Say this on invocation:** *Drafting a query letter. The shape is standard, but the specific
conventions move year to year. I'll flag where you should check the target agent's current
guidelines instead of trusting my defaults.*

**Source:** [`craft/publishing/publishing.md`](../../craft/publishing/publishing.md). Note that
its figures (agent commission, royalty percentages, submission timelines) come from a 2025
lecture and are explicitly a snapshot in time, not a live feed.

---

## Read this before drafting

Publishing convention is one of the fastest-moving parts of the craft base. Word-count
expectations by genre and category, whether an agent wants comp titles at all, personalization
requirements, simultaneous-submission etiquette, and format (pasted into the email body vs:
attached) all vary **by agency and change over time.**

**Don't assert any of these as current fact.** Where a convention matters to the letter, say what
this skill assumes, flag it, and point the author at the target agent's own current submission
guidelines. Their agency website, a recent Manuscript Wish List post, or a submissions-tracking
resource. Rather than treating this skill's defaults as settled.

---

## The four parts

### 1. The hook

The pitch paragraph, condensed to roughly 150–250 words. No throat-clearing, no biography before
the book. The premise comes first. Can draw on `/pitch`'s genre-familiar or genre-unfamiliar
opening, tightened to prose the agent reads cold.

**Offer at least two hook drafts.** The right register (voicey vs. plain, opening on the
protagonist vs. opening on the premise) is a judgement call the author makes, not one this skill
should settle by producing only one option.

### 2. Comp titles

One or two, chosen deliberately. See `/pitch`'s comp-title guidance. **Only propose titles the
author has confirmed reading**; never assert a comparison on the system's behalf.

**Flag:** whether comps belong in a query at all, and how many, is exactly the kind of convention
that varies by agent. Check guidelines before assuming they're wanted.

### 3. Credentials

Brief. A sentence, sometimes none. Should not overshadow the manuscript. If the author has
nothing formal (prior publication, relevant expertise, a platform), it's standard to have no
credentials paragraph at all. Say so rather than padding one out.

### 4. Housekeeping

Title, word count, genre/category. Pull the word count from `manuscript/_status.md` rather than
estimating. This is the one part of the letter that should never be approximate.

**Flag:** acceptable word-count ranges by genre and category shift and vary by agent; don't state
that a count is "in range" as settled fact. Say what the manuscript's count is and note that the
author should confirm it against the target agent's stated preferences.

---

## Output format

```
── QUERY DRAFT ── raw material

  HOOK
    A. [~200 words, option A]
    B. [~180 words, option B. Different opening beat]

  COMP TITLES
    • [title]. Confirm you've read this
    • [title]. Confirm you've read this
    (flag: whether this agent wants comps at all is worth checking)

  CREDENTIALS
    [one sentence, or: none included. No forced padding]

  HOUSEKEEPING
    Title: [from manuscript/_status.md or ask]
    Word count: [pulled from manuscript/_status.md]
    Genre/category: [ask if not established]

── STALENESS FLAG ──
   Word-count norms, comp-title expectations, and submission format vary by
   agent and drift over time. Check [agent]'s current guidelines before
   sending rather than trusting these defaults.
```

---

## Rules

- **Never state a current market convention as settled fact.** Word counts, comp-title
  expectations, simultaneous-submission norms, format. Flag all of these and point at the
  target agent's own guidelines.
- **Pull the word count from the manuscript's own record**, not an estimate.
- **Offer at least two hook drafts.** Never a single locked hook.
- **Don't propose a comp title the author hasn't confirmed reading.**
- **Don't pad a credentials paragraph that isn't needed.** None is a valid answer.
- **Never invent a proper noun, plot detail, or character not already established** in `canon/`
  or `story/`.
- **This produces a draft letter, not a document to file.** Don't write it into `canon/` or
  `story/` unless the author asks it saved somewhere specific.

## Related

`/pitch` · `/synopsis` · `/scale`
