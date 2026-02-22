# Balance Parameters

> **Authority:** Rank 6
> **Layer:** Reference
> **Conforms to:** [design/design-doc.md](../design/design-doc.md)

---

## Purpose

Master registry of all tunable numbers in the game. Every threshold, rate, timing value, and capacity that affects game balance is defined here. This is the single source of truth for "what are the numbers?" — designers tune here, engineers read from here.

## Parameters

<!-- Group by system or category. One row per tunable value. -->

*None yet.*

<!-- Example entries:

### Colonist Needs

| Parameter | Value | Unit | Range | System | Notes |
|-----------|-------|------|-------|--------|-------|
| hunger_rate | 0.5 | per hour | 0.1–2.0 | SYS-002 Needs | How fast hunger increases |
| rest_rate | 0.4 | per hour | 0.1–2.0 | SYS-002 Needs | How fast rest need increases |
| mood_break_threshold | 0.15 | normalized | 0.0–1.0 | SYS-002 Needs | Below this, mental break risk |
| mood_recovery_rate | 0.1 | per hour | 0.01–1.0 | SYS-002 Needs | Passive mood recovery rate |

### Construction

| Parameter | Value | Unit | Range | System | Notes |
|-----------|-------|------|-------|--------|-------|
| base_build_speed | 1.0 | work/sec | 0.1–10.0 | SYS-001 Construction | Modified by skill level |
| deconstruct_material_return | 0.75 | ratio | 0.0–1.0 | SYS-001 Construction | Fraction of materials recovered |
| rain_build_penalty | 0.5 | multiplier | 0.0–1.0 | SYS-001 Construction | Speed multiplier in rain |

### Combat

| Parameter | Value | Unit | Range | System | Notes |
|-----------|-------|------|-------|--------|-------|
| bleed_rate_severe | 0.02 | hp/sec | 0.001–0.1 | SYS-003 Health | Severe wound bleed rate |
| down_threshold | 0 | hp | — | SYS-003 Health | HP at which colonist is downed |
| rescue_timeout | 300 | seconds | 60–600 | SYS-003 Health | Time before unrescued = death |

-->

## Template

Use this format for each group:

```markdown
### [Category / System Name]

| Parameter | Value | Unit | Range | System | Notes |
|-----------|-------|------|-------|--------|-------|
| ... | ... | ... | ... | ... | ... |
```

## Rules

1. **Every tunable number must be registered here.** No magic numbers in code that aren't traceable to this table.
2. **Ranges are design constraints.** The Range column defines what values are considered sane — values outside the range require an ADR.
3. **Units are explicit.** Never leave units ambiguous. "per second", "per tick", "ratio", "multiplier", "normalized 0–1" — be specific.
4. **Changes to values are cheap; changes to ranges are decisions.** Tweaking a number within its range is routine. Changing the range itself means the design assumption changed — document why.
