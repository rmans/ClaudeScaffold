---
name: scaffold-review-art
description: Review all generated art assets for visual consistency, index health, coverage gaps, and naming conventions.
allowed-tools: Read, Grep, Glob
---

# Art Asset Review

Review all generated art assets for visual consistency with the style guide, index health, coverage gaps, and naming conventions.

## Steps

### 1. Read Design Context

Read the visual identity documents that define what the art should look like:

1. **Read `scaffold/design/style-guide.md`** — art style, aesthetic pillars, visual tone.
2. **Read `scaffold/design/color-system.md`** — color palette, tokens, mood associations.
3. **Read `scaffold/design/design-doc.md`** — characters, environments, systems, UI elements, and world/setting that should have visual representation.

If none of these exist yet, note that visual identity is undefined and review on general quality only.

### 2. Scan Indexes

1. **Read `scaffold/art/_index.md`** — top-level art index.
2. **Read all 7 subdirectory indexes:**
   - `scaffold/art/concept-art/_index.md`
   - `scaffold/art/ui-mockups/_index.md`
   - `scaffold/art/character-art/_index.md`
   - `scaffold/art/environment-art/_index.md`
   - `scaffold/art/sprite-art/_index.md`
   - `scaffold/art/icon-art/_index.md`
   - `scaffold/art/promo-art/_index.md`
3. **Count assets per type** from the index entries.
4. **Glob each subdirectory** (`scaffold/art/concept-art/*`, etc.) to find actual image files on disk.

### 3. Visual Inspection

For each image file found on disk:

1. **Read the image** (Claude is multimodal — read the file directly to view it).
2. **Evaluate against the style guide:**
   - Does the art style match the aesthetic pillars (e.g., pixel art, painterly, flat)?
   - Does the color palette adhere to the color system tokens?
   - Is the quality level consistent with other assets in the same category?
   - Does the mood/tone match the project's visual identity?
3. **Flag inconsistencies** — note the specific file, what's off, and what it should match.

If no style guide or color system exists, evaluate for internal consistency across assets (do they look like they belong to the same project?).

### 4. Coverage Analysis

Cross-reference the design doc against generated assets to identify gaps:

- **Characters** — Does every named character in the design doc have character art? Are there characters with concept art but no sprite?
- **Environments** — Does every distinct environment/biome/area in the design doc have environment art?
- **Systems** — Do key systems (combat, inventory, crafting, etc.) have concept art visualizing their mechanics?
- **UI** — Does every major screen or HUD element described in the design doc or UI kit have a mockup?
- **Icons** — Do key items, abilities, or status effects have icon art?
- **Promo** — Is there at least one promotional piece representing the game's identity?

List specific gaps as actionable items (e.g., "No environment art for the Sunken Caves area described in design-doc.md § World Design").

### 5. Index Health

Check for consistency between indexes and disk:

- **Missing entries** — Image files on disk that are NOT listed in their subdirectory `_index.md`.
- **Stale entries** — Entries in `_index.md` that reference files NOT found on disk.
- **Naming conventions** — All art files should use kebab-case with timestamp format: `description-YYYYMMDD-HHMMSS.ext`. Flag violations.
- **Metadata completeness** — Index entries should have name, summary, and date. Flag entries missing fields.

### 6. Report

## Output Format

```
## Art Asset Review

### Asset Summary
| Category | Index Entries | Files on Disk | Issues |
|----------|--------------|---------------|--------|
| concept-art | X | X | N |
| ui-mockups | X | X | N |
| character-art | X | X | N |
| environment-art | X | X | N |
| sprite-art | X | X | N |
| icon-art | X | X | N |
| promo-art | X | X | N |
| **Total** | **X** | **X** | **N** |

### Visual Consistency
- [Findings from visual inspection — palette adherence, style match, quality]
- [Specific files flagged with reasons]

### Coverage Gaps
- [Design doc elements with no corresponding art]
- [Categories with no assets at all]

### Index Health
- [Missing entries, stale entries, naming violations]

### Recommendations (prioritized)
1. [Most impactful action]
2. ...
```

## Rules

- This skill is read-only. Do not modify any files.
- Be specific — name the exact file and quote the exact issue when flagging problems.
- Visual inspection is the core value of this review. Spend time looking at each image and comparing against the style guide.
- If the art directory is empty, don't just say "empty" — list what SHOULD be there based on the design doc and suggest which art skills to run first.
- If no style docs exist, review for internal consistency across assets and note that style alignment can't be checked yet.
- Prioritize recommendations by impact — coverage gaps and style inconsistencies rank higher than naming issues.
