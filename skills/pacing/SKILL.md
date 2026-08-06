---
name: pacing
description: Audit where progress becomes invisible to the reader and where pacing goes uniform. Use when the middle sags, when a reader reports getting bored or skimming, when a section feels slow, or before finishing an act. Also use when the author asks about pacing, momentum, or signposting.
---

# /pacing: progress and signposting audit

> **Tier 2. Diagnostic**, with a mechanical core. Counting signposts is verification; judging
> whether the pace *feels* right is not, and I'll mark that.

**Say this on invocation:** *Auditing signposts and pacing. The counts are mechanical, the feel
judgements I'll mark.*

**Source:** [`craft/plot/progress-and-signposting.md`](../../craft/plot/progress-and-signposting.md)
· [`craft/structure/scale-and-length.md`](../../craft/structure/scale-and-length.md)

---

## The rule

> Your job is not to make things progress. It is to give a **sense of satisfying progression.**

Those are different jobs, and the second is the one readers experience.

**The failure this skill exists to catch:**

> A big reason people drop a book is that there weren't enough signposts of progress.

Not that nothing was happening. That the reader **couldn't see** it. This is usually fixed by
making visible what's already there, **not by adding plot.**

---

## Procedure

**1. Scope.** An act by default. Works on an outline as well as on prose.

**2. Per chapter, identify what progressed.** Plot, character understanding, or the underlying
conflict. One is enough.

**3. Then the harder question. Point at where the reader can SEE it.** A specific line. If you
can't find one, the chapter has invisible progress, which is the finding.

**4. Check the four signpost types:**
   - Critical information revealed
   - A new obstacle introduced
   - A character making a real decision
   - The story visibly changing direction

**5. Check the stealth thesis paragraph.** Does each chapter open by establishing its subject and
close on resolution or forward pressure?

**6. Check pace variation.** Chapter lengths, beat density. **Uniformity is itself a finding**:
variation is noticeable, and its absence reads as coasting.

**7. Check thriller-pacing limits.** If running short chapters with end hooks: that mode runs out
at **~70,000 words.** Past that without entering the climax, readers are lost.

**8. Look for the specific cause of a sagging stretch:** a promise was made, then the writer got
interested in something else. A subplot that doesn't appear to advance the main line reads as a
diversion however good it is.

---

## Output format

```
── PACING ── Act 2A, ch08–ch14

  ch   progressed                     visible at              signposts
  ──   ─────────────────────────────  ──────────────────────  ─────────
  08   plot. The archive lead        "the drawer was empty"    2
  09   character, he stops trusting, NOT VISIBLE            0   ✗
  10   nothing identified. 0   ✗
  11   plot. The funding trail       "the name on the plaque"  3
  12   character, grief, NOT VISIBLE            1   ⚠
  13   plot. The Curator             "he'd catalogued it"      2
  14   conflict. They're exposed     "someone had been there"  2

── FINDINGS ──
  ✗  ch09–ch10. Two consecutive chapters with no visible progress
     This is where readers will stop. ch09 DOES progress; it isn't signposted.
     Fix by making it visible, not by adding events.
  ⚠  ch10. Nothing progresses at all. Candidate for cutting or merging
  ⚠  Uniform pace: ch08–ch14 all 2,900–3,300 words, similar beat density

── OPINION ──
  The Act reads as slower than its content warrants. My read is this is
  a visibility problem rather than a content problem. There's plenty
  happening in ch09.
```

---

## Rules

- **Distinguish "nothing progressed" from "progress isn't visible."** Completely different fixes,
  and conflating them leads authors to add plot they don't need
- **Two consecutive invisible chapters is the alarm.** Flag it explicitly
- **Uniformity is a finding**, not an absence of findings
- **Don't prescribe events.** The fix for invisible progress is signposting
- **Mark feel judgements as opinion**


**Delegation:** this check fans out. Dispatch Sonnet subagents per file or per sub-check rather than working sequentially in the main thread. See [skills/_CONVENTIONS.md](../_CONVENTIONS.md). Delegate gathering; keep judgement.

## Related

`/diagnose` · `/scene` · `/threads` · `/promises`
