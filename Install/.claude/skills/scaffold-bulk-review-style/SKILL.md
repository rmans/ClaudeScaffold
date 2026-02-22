---
name: scaffold-bulk-review-style
description: Review all Rank 2 style docs at once for completeness and cross-doc consistency. Use for a full audit of the style layer.
allowed-tools: Read, Grep, Glob
---

# Bulk Style Review

Review all Rank 2 documents for completeness, accuracy, and cross-doc consistency.

## Documents Audited

| Doc | File |
|-----|------|
| Style guide | `scaffold/design/style-guide.md` |
| Color system | `scaffold/design/color-system.md` |
| UI kit | `scaffold/design/ui-kit.md` |
| Glossary | `scaffold/design/glossary.md` |

## Steps

### 1. Read Everything

1. Read all 4 documents listed above.
2. Read the design doc at `scaffold/design/design-doc.md` for high-level cross-reference.

### 2. Per-Doc Completeness

For each document, assess:
- **Section count** — how many sections exist?
- **Filled sections** — how many have content beyond TODO markers?
- **Empty sections** — any sections still at template defaults?

Categorize each doc as: **Complete**, **Partial**, or **Empty**.

### 3. Cross-Doc Consistency

This is the main value of bulk review — checking relationships BETWEEN Rank 2 docs:

- **Style Guide ↔ Color System.** Visual Tone should inform the palette mood. If style-guide says "dark and gritty" but the palette is pastel — flag it. Environment Style should align with UI vs World Colors.
- **Style Guide ↔ UI Kit.** Art Direction should inform icon style and component visual language. Animation Style should align with UI Animation & Transitions. VFX style should be consistent with Component States feedback.
- **Color System ↔ UI Kit.** Color tokens should cover every color referenced in Component States. Usage Rules should account for every component state (hover, pressed, disabled, error). Accessibility contrast ratios should be achievable with the defined palette.
- **Glossary ↔ All Docs.** If the glossary has entries, check all style docs for NOT-column term violations. Check that game-specific terms used in style docs have glossary entries.
- **Design Doc ↔ All Docs.** Aesthetic Pillars should be reflected in Art Direction. Tone should align with Visual Tone and palette mood. Camera/Perspective should be consistent with Rendering Approach. Accessibility targets should match Color System accessibility section. Input Feel should align with Animation Style. Audio Identity should align with UI Sound Feedback.

### 4. Gap Analysis

Identify what's missing by reading the design doc and checking what style content should exist but doesn't:

- Design doc mentions visual themes but style-guide has no Art Direction
- Design doc mentions accessibility but color-system has no accessibility section
- Design doc describes UI-heavy gameplay but ui-kit has no components
- Player Verbs imply UI interactions that aren't covered in ui-kit Component Definitions
- Game-specific terms appear repeatedly but aren't in the glossary

### 5. Specificity Audit

For each filled section across all docs:
- Is the content specific enough to implement from?
- Flag vague entries: "make it look good", "standard colors", "nice animations"
- Flag implementation details that don't belong in design layer: node names, class names, engine API references

## Output Format

```
## Bulk Style Review — X docs audited

### Overview
| Doc | Status | Sections | Filled | Issues |
|-----|--------|----------|--------|--------|
| Style guide | Partial | 7 | 5 | 2 |
| Color system | Complete | 6 | 6 | 0 |
| ... | ... | ... | ... | ... |

### Cross-Doc Consistency
- **Style ↔ Colors:** [status — matches and mismatches]
- **Style ↔ UI Kit:** [status]
- **Colors ↔ UI Kit:** [status]
- **Glossary compliance:** [X violations found]
- **Design doc alignment:** [status]

### Gap Analysis
[List of content that should exist but doesn't, organized by source]

### Specificity Issues
[List of vague or implementation-leaking entries]

### Recommendations (prioritized)
1. [Highest-impact fix across all docs]
2. [Second priority]
3. ...
```

## Rules

- This skill is read-only. Do not modify any files.
- **Cross-doc consistency is the main value.** Individual completeness is what `/scaffold-review-style` does — bulk review focuses on relationships.
- Be specific. Name the exact sections and docs involved in every mismatch.
- If everything is consistent, say so. Don't manufacture issues.
- Prioritize by blast radius — issues affecting multiple docs rank higher.
