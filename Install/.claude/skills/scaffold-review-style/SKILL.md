---
name: scaffold-review-style
description: Review a single Rank 2 style doc for completeness, quality, and consistency with the design doc. Pick which doc to audit.
argument-hint: [style-guide|color-system|ui-kit|glossary]
allowed-tools: Read, Grep, Glob
---

# Style Document Review

Review a single Rank 2 document: **$ARGUMENTS**

## Supported Documents

| Argument | File |
|----------|------|
| `style-guide` | `scaffold/design/style-guide.md` |
| `color-system` | `scaffold/design/color-system.md` |
| `ui-kit` | `scaffold/design/ui-kit.md` |
| `glossary` | `scaffold/design/glossary.md` |

## Steps

### 1. Identify Target

1. Match the argument to a supported document above.
2. If no argument or unrecognized argument, list the options and ask the user which doc to review.

### 2. Read the Target Doc

Read the target doc and assess its overall state — empty, partially filled, or populated.

### 3. Read Advisory Context

Read theory doc for advisory context (informs observations but never causes hard failures):
- `scaffold/theory/ux-heuristics.md` — UX principles to check style decisions against
- `scaffold/theory/audio-design.md` — audio principles for reviewing sound feedback

### 4. Read the Design Doc for Cross-Reference

Read `scaffold/design/design-doc.md` — especially the sections relevant to the target:

- **style-guide** ← Tone, Aesthetic Pillars, Camera/Perspective, Audio Identity
- **color-system** ← Tone, Aesthetic Pillars, Accessibility Philosophy, Accessibility Targets
- **ui-kit** ← Core Loop, Player Verbs, Camera/Perspective, Target Platforms, Input Feel, Audio Identity
- **glossary** ← All sections (check for terms that should be canonicalized)

### 5. Completeness Check

**style-guide** —
- Every section should have content beyond the TODO marker.
- Art Direction should reference or align with the design doc's Aesthetic Pillars.
- Rendering Approach should be consistent with Camera/Perspective.
- Animation Style should align with Input Feel.
- Flag sections that are empty or say "TBD" without detail.

**color-system** —
- Palette should have named colors with hex values or clear descriptions.
- Color Tokens should map to palette colors with semantic names.
- Usage Rules should define when each token is used — not just list colors.
- UI vs World Colors should have a clear boundary statement.
- Accessibility should reference specific contrast ratios or colorblind strategies.
- Theme Variants should either define variants or explicitly state there are none.

**ui-kit** —
- Component Definitions should list every UI component the game needs based on the Core Loop and Player Verbs.
- Layout Rules should define spacing scale, safe zones, and HUD placement.
- Typography should define a clear hierarchy with specific sizes/weights.
- Component States should cover at minimum: default, hover, pressed, focused, disabled.
- Animation & Transitions should define timing and feel, not just "we'll animate it."
- Sound Feedback should describe feel, not filenames.
- Responsive & Resolution Scaling should state minimum resolution and scaling approach.

**glossary** —
- Every game-specific term that appears more than once in the design doc should have a glossary entry.
- Every entry should have a Definition and a NOT column (forbidden synonyms).
- Entries should be in alphabetical order.
- Flag terms used in the design doc that don't have glossary entries yet.

### 6. Quality Check

For all docs:
- **Consistency with design doc.** Does the content align with the vision, tone, and pillars in the design doc? Flag contradictions.
- **Specificity.** Vague content ("make it look nice") is flagged. Content should be concrete enough to implement from.
- **No implementation details.** Style docs describe WHAT, not HOW. Flag any engine-specific references (node names, class names, API calls).
- **Internal consistency.** Within the doc, do sections agree with each other? E.g., if visual tone says "dark and gritty" but VFX says "bright neon explosions" — flag it.

## Output Format

```
## Style Review: [Doc Name]

### Completeness: X/Y sections filled
[List each section with status: Complete, Partial, or Empty]

### Quality Issues
- [Specific issues with quotes]

### Design Doc Alignment
- [Matches and contradictions between this doc and the design doc]

### Advisory Observations
[Patterns from UX heuristics worth considering. Clearly labeled as advisory, not hard failures.]

### Recommendations
1. [Most important fix]
2. ...
```

## Rules

- This skill is read-only. Do not modify any files.
- Be specific — quote the exact text when flagging issues.
- If the doc is empty, don't just say "empty" — list what SHOULD be in it based on the design doc.
- If the design doc itself is empty, report that and suggest filling it first.
- **Theory observations are advisory only.** Present them as "worth considering" — never as errors or required fixes. Theory docs carry no authority.
