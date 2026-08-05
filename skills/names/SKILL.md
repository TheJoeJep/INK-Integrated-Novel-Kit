---
name: names
description: Check every proper noun and coined term in the manuscript against the canonical names list, and check that terms are used by the right characters. Use after drafting, when adding a character or place, when naming decisions have changed, or before a revision pass. Also use when the author asks about naming consistency, placeholder names, or in-world terminology.
---

# /names — terminology check

> **Tier 1 — mechanical check.** Matching nouns against a list is verification. The one
> judgement call — whether a term suits its speaker — is marked separately.

**Say this on invocation:** *Checking terminology against the names list — mechanical, plus a
short register check I'll mark as opinion.*

---

## What's being checked

`canon/names-and-terms.md` is the authority. **Nothing may appear in the prose that isn't in it.**

Each entry carries three things, and all three get checked:

| Field | Checked for |
|---|---|
| **Term** | Does it appear in the prose at all? Is it spelled consistently? |
| **Register** | *Who uses it and who doesn't* |
| **Status** | `LOCKED` or `PLACEHOLDER` |

**Register is the part people forget**, and it's where the real errors are. In this project
*"reptilian"* is a fringe-conspiracy slur used by outsiders — the hybrids never use it of
themselves. A character using the wrong word for their own kind is a characterization error that
reads as an author error.

---

## Procedure

**1. Read** `canon/names-and-terms.md`.

**2. Scope.** Current chapter by default; whole manuscript on request.

**3. Extract every proper noun and coined term** from the prose — people, places, factions,
events, invented terminology, in-world jargon.

**4. Check four things:**
   - **Unlisted** — appears in prose, absent from the list. Either add it or it's an invention
   - **Unused** — listed but never appears. Fine, but worth knowing
   - **Inconsistent** — spelling or capitalization drift
   - **Register** — is the speaker someone who would use that word?

**5. Flag placeholders in prose.** Any `PLACEHOLDER` term appearing in drafted text is a
find-and-replace debt. **List every occurrence with its location** — that list is the deliverable
when names are finally decided.

**6. Report.**

---

## Output format

```
── TERMINOLOGY ── ch01, 14 terms found

  ✗  UNLISTED       "the Ossuary"          ch01/05, ×2
                    → add to names-and-terms.md, or remove

  ⚠  INCONSISTENT   "Reveal Day" / "reveal day"    ×7 / ×2

  ⚠  REGISTER       the Curator says "reptilian" of himself    ch01/06
                    list: outsider slur — they never self-apply it

  ◷  PLACEHOLDER IN PROSE — replace when named
     [CUSTODIANS]   ×11   ch01/02, 04, 06, 07
     [THE CONCORD]  ×2    ch01/07

── FINDINGS ──
  1 unlisted · 1 inconsistent · 1 register · 13 placeholder occurrences
```

`✗` unlisted · `⚠` inconsistency or register · `◷` placeholder debt

---

## Rules for reporting

- **Never add a term to the list from this skill.** Naming is an authorial decision and goes
  through `/write` in Structure Mode. Report and stop.
- **Placeholder counts are the point.** They tell the author what a naming decision will cost in
  edits. Always give exact occurrence counts and locations.
- **Register findings are marked as opinion** — a character *can* use the wrong word deliberately,
  and that's characterization rather than error. Say what the list implies and let the author
  decide.
- **Don't flag ordinary proper nouns** — real places, real institutions, common names — unless
  they're doing in-world work.
- **Report clean checks plainly.**


**Delegation:** this check fans out. Dispatch Sonnet subagents per file or per sub-check rather than working sequentially in the main thread — see [skills/_CONVENTIONS.md](../_CONVENTIONS.md). Delegate gathering; keep judgement.

## Related

- `/continuity` — the broader fact check
- [`craft/character/voice-quirks-and-dialogue.md`](../../craft/character/voice-quirks-and-dialogue.md)
  — register as characterization
