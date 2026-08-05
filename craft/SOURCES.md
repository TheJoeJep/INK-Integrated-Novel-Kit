# Craft Sources and Coverage Map

Every craft document traces to a source listed here. See [../CREDITS.md](../CREDITS.md) for
attribution.

---

## Source tiers

- **PRIMARY (transcript)** — built from the full lecture transcript. Highest confidence, highest
  detail. This is the target state for every document.
- **PRIMARY (recap)** — built from Sanderson's official written lecture notes on his site.
  Accurate but heavily condensed — roughly 3,500 words where a transcript runs 13,000. Anything
  still at this tier is **due for rebuild**.
- **SECONDARY** — published community notes on video lectures. Someone else's compression.
- **SYNTHESIS** — this project's own earlier working draft. ⚠️ **Verified and largely did not hold
  up — see below.**

### ⚠️ SYNTHESIS tier — verified 2026-08-03, and it failed

The 2025 Lecture 1 transcript was checked directly against the prior working draft. Verdicts on
the six frameworks that had been built into the craft base on its authority:

| Claim | Verdict |
|---|---|
| Revision bias by drafting style | **PARTIALLY PRESENT** — the pattern is real (outliners skip second drafts; discovery writers loop on early chapters and stall). The itemized warning-sign lists are not his |
| Five-question **diagnostic habit** | **NOT PRESENT** — no such checklist exists in the lecture |
| Ordered **revision queue** (motivation → scenes → midpoint → seeding → prose last) | **NOT PRESENT** — he describes a general prioritized "bug list," not this sequence |
| Three tiers of feedback: reaction / diagnosis / prescription | **PARTIALLY PRESENT** — the descriptive-vs-prescriptive distinction is real. There is **no** middle "diagnosis" tier and no authority hierarchy |
| "Design systems for the parts you dislike," five-step | **PARTIALLY PRESENT** — carrots/sticks, habit bundling and bug-list prioritization are real; the numbered packaging is not |
| Reframe *is this true?* → *what problem does it solve?* | **NOT PRESENT** — the underlying idea (advice is individual) is real; this framing is not |

**What happened.** The prior draft was a good-faith summary that tidied his material into
frameworks he never taught. The ideas mostly trace to something real; the structures do not.

**How it's handled:** useful items are kept and labelled **`[not from the lectures]`** in place,
with the Sanderson attribution stripped. Nothing was deleted — the tools work — but nothing
invented is credited to him.

**The general lesson, which now governs this project:** a tidy numbered framework that appears in
a summary but not in the transcript is a *summarizer's artifact*. Real lectures are messier than
that. **Treat suspicious neatness as a signal to check the source** — and never build on a summary
when a transcript is available.
- **GAP** — known missing, not filled with substitute advice.

---

## Transcripts

`docs/sources/transcripts/` — **39 lectures, ~440,000 words.** Auto-generated captions, cleaned
and de-duplicated; raw `.vtt` preserved in `raw-vtt/`.

**Caveat that applies to every transcript-derived doc:** these are machine captions. No
punctuation, unreliable speaker attribution, mangled proper nouns (*saaron*, *froto*, *Callin*).
Substance is intact; **exact quotation is not safe.** Craft docs paraphrase and attribute the
concept — they do not quote wording.

| Course | Lectures | Notes |
|---|---|---|
| 2025 | 16 | Complete, including 4.5, 6.5, 9.5, 11.5 and Lecture 12 |
| 2020 | 13 | Complete, including Mary Robinette Kowal on short fiction |
| 2016 | 10 of 12 | See gaps |

---

## Rebuild status

| Area | Tier | Source |
|---|---|---|
| **plot/** — all 4 docs | ✅ **PRIMARY (transcript)** | 2025 L2 |
| structure/ | PRIMARY (recap) | 2025 L3 — **rebuild pending**, transcript available |
| character/ | PRIMARY (recap) | 2025 L5, L6 — **rebuild pending**, transcripts available (incl. L6.5 on arc types, not covered at all yet) |
| worldbuilding/ | PRIMARY (recap) | 2025 L7, L8 — **rebuild pending** |
| viewpoint/ | SECONDARY | 2020 L4 transcript now available — **rebuild pending** |
| prose/ | PRIMARY (recap) + SECONDARY | **rebuild pending** |
| scene/ | PRIMARY (recap) | **rebuild pending** |
| revision/ | SECONDARY + SYNTHESIS | **rebuild pending** |
| process/ | PRIMARY (recap) + SYNTHESIS | 2025 L1 transcript available — **rebuild pending** |
| publishing/ | PRIMARY (recap) | 2025 L10, L11, L11.5 — **rebuild pending** |

**Newly available, no doc yet:** How to Worldbuild on Earth (2025 L9 — contemporary/real-world
settings), Types of Character Arcs (2025 L6.5), Short Stories (2020 L7), Story Structure: The Box
(2016 L5), Dialogue (2016 L11), the 2016 Brandon Mull guest lecture.

---

## Official written recaps

Still useful as a cross-check — they're his own summaries, so where a recap and a transcript
disagree in emphasis, that's signal.

[2025 lecture notes index](https://www.brandonsanderson.com/blogs/blog/tagged/2025-lecture-notes) ·
[L1](https://www.brandonsanderson.com/blogs/blog/brandon-sandersons-writing-class-2025-week-1) ·
[L2](https://www.brandonsanderson.com/blogs/blog/brandon-sandersons-2025-guide-to-plot-lecture-2) ·
[L3](https://www.brandonsanderson.com/blogs/blog/brandon-sandersons-2025-overview-of-story-structure-lecture-3) ·
[L4](https://www.brandonsanderson.com/blogs/blog/plot-q-a-brandon-sandersons-writing-lectures-2025) ·
[L5](https://www.brandonsanderson.com/blogs/blog/creating-proactive-relatable-and-capable-characters-brandon-sandersons-writing-lecture-5-2025) ·
[L6](https://www.brandonsanderson.com/blogs/blog/customizing-your-character-brandon-sandersons-writing-lecture-6-2025) ·
[L7](https://www.brandonsanderson.com/blogs/blog/guide-to-sandersons-laws-of-magic-lecture-notes) ·
[L8](https://www.brandonsanderson.com/blogs/blog/worldbuilding-tools-lecture-2025) ·
[L10](https://www.brandonsanderson.com/blogs/blog/publishing-industry-lecture-2025) ·
[L11](https://www.brandonsanderson.com/blogs/blog/what-publishing-does-for-you-brandon-sandersons-writing-lecture-11-2025)

## Community notes (SECONDARY)

[Nicole van der Hoeven, 2020](https://notes.nicolevanderhoeven.com/sources/Course/Brandon+Sanderson+on+Writing+BYU+2020) ·
[community gist, 2020](https://gist.github.com/jake9696/86f1f9d65af275d77435f6b33c78d64b)

Now largely superseded by the transcripts. Retain only where they add something.

## Prior working draft (SYNTHESIS)

`docs/sources/sanderson-craft-handbook-working-draft.md` — deep treatment of 2025 Lecture 1 only,
drawn from both video and recap. Its own note calls it a practical interpretation rather than a
transcript.

**Update:** the 2025 L1 transcript is now available, so this can be **verified rather than
trusted.** One of its items has already been confirmed — the warning against endlessly revising
chapter one is genuinely in the lecture (he uses a recurring student as the example). The others
should be checked during the `process/` rebuild.

---

## GAPS — known, unfilled, deliberate

| Gap | Why | Closable? |
|---|---|---|
| **2016 L4 — Worldbuilding** | **No captions exist** — not manual, not auto-generated | Only by transcribing audio |
| **2016 L8 — Magic Systems** | Same | Same |
| Guest lectures on revision and prose | Not identified in the source playlists | Possibly — needs a search |

Two videos out of 41 sought. Everything else is in hand.

### How to close a gap

Watch it, take notes in your own words, drop the file in `docs/sources/transcripts/`, and tell
the system to extract from it.

---

## Evolution across courses

The rebuild uses **2025 as the spine, 2020 as supplement, 2016 as cross-check** — differences
called out rather than blended.

To be filled in as each area is rebuilt.

| Concept | 2016 | 2020 | 2025 |
|---|---|---|---|
| Promise types | — | tone / character arc / plot | tone / story / character-and-conflict / structural, plus cold open |
| Structure models | The Box | — | states a preference for Harmon's Story Circle over strict Campbell |
| Iconic characters | — | present | substantially fuller |
