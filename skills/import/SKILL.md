---
name: import
description: Bring an already-written manuscript into the system. Split it into chapters and scenes, then derive character, place, faction and canon documents from the existing prose. Use when starting with a book or partial book that was written outside this system, when migrating from Word/Scrivener/Google Docs, or when the author has drafted material that has no documentation behind it.
---

# /import: bring an existing manuscript in

> **Tier 2/4 hybrid, and the mix matters.** Extracting what the prose *states* is diagnostic and
> reasonably reliable. Inferring what it *implies*, motivation, arc, subtext, is generative
> guessing. **Everything I infer gets marked as inferred, and you confirm it before it becomes
> canon.**

**Say this on invocation:** *Importing existing prose. What the text states I'll extract; what it
implies I'll mark as inferred and ask you to confirm. I'd rather leave a doc thin than fill it
with my guesses about your book.*

---

## The governing principle

**The manuscript is the authority. Everything else is derived from it.**

That inverts the normal direction of this system, and it creates the one real hazard: **an
inferred fact written into `canon/` without confirmation becomes a constraint on every future
scene.** A wrong guess about a character's motivation doesn't sit quietly in a file. It starts
shaping prose.

So the rule is: **extract freely, infer visibly, confirm before committing to canon.**

---

## Stage 1: split the prose

If the manuscript is one file, split it first:

```
python E:\Writing\story-engine\dashboard\split_manuscript.py <book.md> <workspace> --dry-run
```

Run `--dry-run` first and show the author the chapter/scene breakdown before writing anything.
It detects chapter headings and scene breaks (`***`, `---`, `###`), writes
`manuscript/chNN-slug/NN-scene.md`, and leaves every header field **blank on purpose**.

**Word or Scrivener:** export to Markdown or plain text first. Don't try to parse `.docx`.

**If detection is wrong**, say so rather than proceeding. A bad split is worse than no split,
and it's much harder to unpick afterwards.

## Stage 2: inventory before extracting

**Read everything first, then report what's there.** Don't create documents as you go.

```
── INVENTORY ── 14 chapters · 61 scenes · 91,400 words

  NAMED CHARACTERS       23  (7 appear in 5+ scenes, 16 in 1–2)
  NAMED PLACES           11
  ORGANISATIONS           4
  INVENTED TERMS         18  (capitalised, non-dictionary)
  APPARENT POV            3rd limited, past. Shifts in ch09?

── PROPOSED ──
  Full dossiers for the 7 major characters
  Stubs for 16 minor ones
  Place docs for 6 recurring locations
  ⚠ ch09 POV shift needs your call before I record a mode
```

**Ask before creating.** Twenty-three character docs the author didn't want is a mess to clean up.

## Stage 3: extract, marking inference

Per entity, three tiers, and **the doc must show which is which**:

| Tier | Example | Goes in as |
|---|---|---|
| **Stated** | "she was tall, with a burn across one wrist" | Plain fact, cite the scene |
| **Implied** | Consistently avoids her brother | `*[inferred]*` |
| **Absent** | Her motivation is never stated | An **open question**, not a guess |

**Absent is a finding, not a gap to fill.** If the prose never says what someone wants, the doc
says so. That's exactly what `/motivation` needs to find later. And inventing a want would hide
the most useful thing the import discovered.

**Fill `## Visual` from the prose only.** These blocks drive image generation; a hallucinated
detail there propagates.

## Stage 4: canon, conservatively

**`canon/continuity-ledger.md`:** only hard, checkable facts, each with its scene. *He has no
car* goes in. *He seems lonely* does not.

**`canon/names-and-terms.md`:** every proper noun found, with an honest register guess marked as
a guess.

**`canon/voice-and-style.md`:** tense, person, and a genuine sample paragraph from the author's
own prose. **This is the highest-value artefact of the whole import**, because it's what stops the
system's future prose drifting from the voice already established.

## Stage 5: report what's missing

The import's real output. Run the Tier 1 checks against the imported material and report:

- Threads opened and never closed → `/threads`
- Promises made and unpaid → `/promises`
- Plants with no payoff → `/plants`
- Contradictions between scenes → `/continuity`
- Subplots running with no shape → `/subplot`
- Entities with no Visual block → `/visuals`

**This is the moment the system earns its place.** The author has never had these questions asked
of their own draft.

---

## Rules

- **`--dry-run` the split, always.** Show the breakdown before writing files
- **Inventory before creating.** Ask which docs the author actually wants
- **Never write an inferred fact into `canon/` unconfirmed.** Canon constrains future prose
- **Mark every inference `*[inferred]*`.** A doc the author can't audit is worse than no doc
- **Absent information is a finding.** Record the absence; don't fill it
- **Never edit the prose.** Import reads the manuscript and writes documents. It does not
  "improve" anything, fix typos, or restructure scenes
- **Report scale honestly.** A 90k import is dozens of files; say so before starting
- **Stop and ask on ambiguity.** A POV shift, an inconsistent name, an unclear timeline. Those
  are the author's calls


**Delegation:** this check fans out. Dispatch Sonnet subagents per file or per sub-check rather than working sequentially in the main thread. See [skills/_CONVENTIONS.md](../_CONVENTIONS.md). Delegate gathering; keep judgement.

## Related

`/threads` · `/promises` · `/plants` · `/continuity` · `/subplot` · `/visuals` · `/revision-map`
