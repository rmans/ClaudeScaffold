---
name: scaffold-review-audio
description: Review all generated audio assets for prompt consistency, index health, coverage gaps, and naming conventions.
allowed-tools: Read, Grep, Glob
---

# Audio Asset Review

Review all generated audio assets for prompt consistency with the design direction, index health, coverage gaps, and naming conventions.

> **Note:** Claude cannot listen to audio files. This review audits indexes, prompts, coverage, and metadata — not the audio content itself.

## Steps

### 1. Read Design Context

Read the tonal and mood direction documents:

1. **Read `scaffold/design/style-guide.md`** — tone, mood, aesthetic pillars that inform audio direction.
2. **Read `scaffold/design/color-system.md`** — mood associations and emotional palette that map to audio tone.
3. **Read `scaffold/design/design-doc.md`** — characters (voice needs), environments (ambience needs), systems (SFX needs), narrative (music needs), and overall game feel.

If none of these exist yet, note that design direction is undefined and review on general consistency only.

### 2. Scan Indexes

1. **Read `scaffold/audio/_index.md`** — top-level audio index.
2. **Read all 4 subdirectory indexes:**
   - `scaffold/audio/music/_index.md`
   - `scaffold/audio/sfx/_index.md`
   - `scaffold/audio/ambience/_index.md`
   - `scaffold/audio/voice/_index.md`
3. **Count assets per type** from the index entries.
4. **Glob each subdirectory** (`scaffold/audio/music/*`, etc.) to find actual audio files on disk.

### 3. Prompt Consistency

Review the prompts recorded in index entries for tonal consistency with the design direction:

- **Music** — Do prompts reference genres, tempos, moods, and instrumentation consistent with the style guide's tone and the design doc's emotional arc?
- **SFX** — Do prompts match the game feel described in the design doc (e.g., weighty vs snappy, realistic vs stylized)?
- **Ambience** — Do prompts capture the atmosphere of environments described in the design doc and the mood associations in the color system?
- **Voice** — Do voice parameters (voice selection, speed, tone) match character personalities described in the design doc?

Flag prompts that feel tonally inconsistent with the project direction (e.g., orchestral epic prompts for a cozy pixel game, or chiptune prompts for a realistic AAA title).

### 4. Coverage Analysis

Cross-reference the design doc against generated assets to identify gaps:

- **Music** — Does every major game state or area have music? Check for: main menu, gameplay themes per biome/area, boss encounters, victory/defeat stings, ambient exploration.
- **SFX** — Do key systems have sound effects? Check for: combat actions, UI interactions, item pickups, ability activations, environmental triggers, feedback sounds (success, failure, notification).
- **Ambience** — Does every distinct environment/area in the design doc have an ambient loop? Check for: outdoor areas, indoor areas, special locations, time-of-day variants if applicable.
- **Voice** — Do named characters with dialogue have voice assets? Check for: protagonist, key NPCs, narrator if applicable, UI voice prompts if designed.

List specific gaps as actionable items (e.g., "No SFX for the combat system described in SYS-001 — need hit impacts, ability sounds, defeat stings").

### 5. Index Health

Check for consistency between indexes and disk:

- **Missing entries** — Audio files on disk that are NOT listed in their subdirectory `_index.md`.
- **Stale entries** — Entries in `_index.md` that reference files NOT found on disk.
- **Naming conventions** — All audio files should use kebab-case with timestamp format: `description-YYYYMMDD-HHMMSS.ext`. Flag violations.
- **Metadata completeness** — Index entries should have name, summary, and date. Flag entries missing fields.

### 6. Report

## Output Format

```
## Audio Asset Review

### Asset Summary
| Category | Index Entries | Files on Disk | Issues |
|----------|--------------|---------------|--------|
| music | X | X | N |
| sfx | X | X | N |
| ambience | X | X | N |
| voice | X | X | N |
| **Total** | **X** | **X** | **N** |

### Prompt Consistency
- [Findings from prompt review — tonal alignment, style coherence]
- [Specific entries flagged with reasons]

### Coverage Gaps
- [Design doc elements with no corresponding audio]
- [Categories with no assets at all]

### Index Health
- [Missing entries, stale entries, naming violations]

### Recommendations (prioritized)
1. [Most impactful action]
2. ...
```

## Rules

- This skill is read-only. Do not modify any files.
- Be specific — name the exact file or index entry and quote the exact issue when flagging problems.
- Claude cannot listen to audio files. Do NOT attempt to evaluate audio quality, fidelity, or content by reading binary files. Focus on prompts, metadata, coverage, and index health.
- If the audio directory is empty, don't just say "empty" — list what SHOULD be there based on the design doc and suggest which audio skills to run first.
- If no style docs exist, review prompts for internal consistency and note that tonal alignment can't be checked yet.
- Prioritize recommendations by impact — coverage gaps and tonal inconsistencies rank higher than naming issues.
