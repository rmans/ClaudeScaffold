---
name: scaffold-audio-sfx
description: Generate sound effects using ElevenLabs, informed by the project's style guide and design doc game feel.
argument-hint: [prompt or document-path]
allowed-tools: Read, Bash, Glob, Write
---

# /scaffold-audio-sfx

Generate sound effects using ElevenLabs, informed by the project's style guide and design doc game feel.

## Steps

### 1. Check API key

Check that `ELEVENLABS_API_KEY` is set (environment variable or `scaffold/.env`). If not found, explain how to set it:

```
export ELEVENLABS_API_KEY="..."
```

Or add to `scaffold/.env`:

```
ELEVENLABS_API_KEY=...
```

Stop here if the key is not available.

### 2. Read design context

Read these files for sound design context:

- `scaffold/design/style-guide.md` — visual tone, aesthetic pillars (translate to audio intensity and style)
- `scaffold/design/design-doc.md` — game feel, core loop, genre, setting

Summarize the game's feel into a compact sound design direction string (1-2 sentences covering intensity level, style, and audio character). If the files don't exist or are mostly TODOs, note this and proceed with a minimal context.

### 3. Determine mode

Check the argument passed to the skill:

- **Document-driven mode:** If the argument contains `/` or ends with `.md`, treat it as a document path. Read the document and extract sound-worthy elements — player actions, system events, impacts, feedback moments, and transitions.
- **Freeform mode:** Otherwise, treat the argument as a base prompt for SFX generation.

### 4. Build prompt

Combine the sound design direction from Step 2 with the user's prompt or document-extracted description into a single SFX generation prompt. Focus on:

- **Clarity** — the sound must be immediately recognizable
- **Impact** — appropriate weight and punch for the action
- **Timing** — short, snappy sounds for actions; longer for transitions
- **Game-appropriate intensity** — matches the project's visual and tonal style

**Show the composed prompt to the user and ask for confirmation or edits before generating.** Do not call the API until the user approves the prompt.

### 5. Generate audio

1. Ensure `scaffold/audio/sfx/` directory exists (create it if needed).

2. Generate a kebab-case filename from the prompt:
   - Take the first few meaningful words (max 40 characters)
   - Append a timestamp: `-YYYYMMDD-HHMMSS`
   - Add `.mp3` extension
   - Example: `sword-slash-impact-20260223-143022.mp3`

3. Run the generation command:

```bash
python scaffold/tools/audio-gen.py sfx \
    --prompt "<approved prompt>" \
    --output "scaffold/audio/sfx/<filename>.mp3"
```

   Add `--duration <seconds>` if the user specifies a desired length.
   Add `--prompt-influence <0.0-1.0>` to control how literally the prompt is interpreted.

4. Parse the JSON result from stdout. If `status` is `"error"`, report the error message and stop.

### 6. Update index

Append a row to `scaffold/audio/sfx/_index.md` in the Files table:

```markdown
| <filename>.mp3 | <short prompt summary, max 60 chars> | YYYY-MM-DD |
```

Create the index file from the template if it doesn't exist yet.

### 7. Report

Show the user:

- File path where the audio was saved
- Provider info from the result
- Ask if they want another variation, different duration, or adjusted prompt influence

## Rules

- **Always read style guide and design doc first** — even if the user provides a detailed prompt, the design context ensures the SFX matches the game's feel.
- **Show composed prompt before calling API** — the user must confirm or edit the prompt. Never generate without explicit approval.
- **If `ELEVENLABS_API_KEY` is not set, explain how to set it and stop** — do not attempt generation.
- **Kebab-case filenames with timestamps** — avoids collisions and keeps the directory scannable.
- **Do not modify any design documents** — this skill only creates audio files and updates the audio index.
