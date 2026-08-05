---
name: visuals
description: Find every character, place, and faction that appears in the manuscript prose but has an empty or stale Visual block in its dossier — the blocks that feed later AI image generation. Use before finishing a chapter, when adding a new character or place, when preparing for image generation, or when the author asks what's missing from a dossier. Also use as a running doc-maintenance backlog.
---

# /visuals — visual block audit

> **Tier 1 — mechanical check.** Whether a `## Visual` block exists, and whether what the prose
> established is actually recorded in it, is verification against a template requirement — not
> judgement. Report findings flatly.

**Say this on invocation:** *Running a visual block audit — mechanical, checking prose against
dossiers.*

**Source:** [`templates/character.md`](../../templates/character.md) ·
[`templates/place.md`](../../templates/place.md) ·
[`templates/faction.md`](../../templates/faction.md)

---

## What's being checked

Every character, place, and faction dossier ships with a `## Visual` block:

| Template | Visual fields |
|---|---|
| `character.md` | Build/height/age, Face, Hair, Dress, Distinguishing marks, Movement |
| `place.md` | Scale, Architecture/structure, Condition, Light, Weather/climate, Distinguishing features |
| `faction.md` | Iconography, dress, markings, how a member is recognized |

The documentation protocol requires updating these **every scene end**: *"Update `## Visual`
blocks for anything the prose described."* This skill is the check that that actually happened.
These blocks exist for one downstream reason — **they feed AI image generation** — so a field
being non-empty isn't enough. It has to be concrete enough to render.

**Three states an entity's block can be in:**

| State | Meaning |
|---|---|
| **MISSING** | Template scaffolding untouched — blank fields or `<>` placeholders |
| **STALE** | Has content, but the prose has since established details not reflected there |
| **CURRENT** | Matches what the prose has established |

A fourth, worse case: an entity **with no dossier at all** appearing in prose.

---

## Procedure

**1. Scope.** Whole manuscript by default — visual debt accumulates silently across chapters, so
there's little reason to limit this the way a continuity check would.

**2. Build the entity list.** Every file in `characters/`, `places/`, `factions/`, plus any named
person, place, or faction that appears in prose but has no dossier at all.

**3. For each entity, find every appearance in the prose.** Cite chapter/scene locations.

**4. Per appearance, extract concrete renderable detail** — physical build, clothing, wounds or
marks, lighting, weather, architecture, material, color, condition. Not personality, not backstory
— only what a person drawing the scene would need.

**5. Read the dossier's `## Visual` block** and compare, field by field.

**6. Report per entity** — appears in prose at [locations], block state, what's established but
unrecorded.

---

## Output format

```
── VISUALS ── whole manuscript, 4 entities checked

  ✗  MISSING     the-dragon.md            appears ch01/02, ch01/04, ch01/06
                 Visual block: template scaffolding, untouched
                 prose establishes: left wing torn at the third joint (02);
                 scales "the color of wet asphalt" (02); a burn scar along
                 the jaw (04)

  ⚠  STALE       protagonist.md           appears ch01/01–07
                 Visual block: "average build, dark hair, wears his father's coat"
                 prose since establishes: coat sleeve torn at the crash (02);
                 three days unshaven by 06 — neither recorded

  !  NO DOSSIER  "the woman at the overpass"     appears ch01/01
                 no characters/ file exists for this entity

  ✓  CURRENT     the-shed.md              appears ch01/04, ch01/06
                 Visual block matches prose

── FINDINGS ──
  1 missing · 1 stale · 1 no dossier · 1 current
```

`✗` block untouched · `⚠` stale · `!` no dossier exists · `✓` current

---

## Rules

- **Report per entity, always with exact locations and the specific detail** the prose
  established. A finding without a citation isn't useful.
- **Presence of a field isn't enough.** A Visual block with every header filled in but generic
  prose-contradicting content is STALE, not CURRENT — check the content, not the scaffolding.
- **Don't invent detail.** Only what the prose actually establishes counts. If the prose hasn't
  described something, its absence from the dossier isn't a finding.
- **No-dossier entities rank above stale ones.** A missing file is a bigger gap than an outdated
  block — flag it first.
- **Never write to a Visual block from this skill.** This is the backlog made visible, not the
  fix. Promoting facts into dossiers happens through the documentation protocol at scene end, or
  through `/write` in Structure Mode when catching up a backlog deliberately.
- **Report clean runs plainly.** *4 entities, all current.* Don't manufacture a gap to justify
  the audit.
- **Treat this as a running list**, not a one-time pass — rerun it as chapters accumulate.


**Delegation:** this check fans out. Dispatch Sonnet subagents per file or per sub-check rather than working sequentially in the main thread — see [skills/_CONVENTIONS.md](../_CONVENTIONS.md). Delegate gathering; keep judgement.

## Related

- `/continuity` — the broader unrecorded-fact check; visuals is the narrower, render-focused case
- `/new-character` · `/new-place` — for building a missing dossier from scratch
- [`.claude/skills/write/references/doc-protocol.md`](../write/references/doc-protocol.md) — how
  Visual blocks are supposed to get updated in the first place
