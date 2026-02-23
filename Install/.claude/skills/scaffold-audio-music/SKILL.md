---
name: scaffold-audio-music
description: Generate music tracks using ElevenLabs, informed by the project's style guide and design doc mood/tone.
argument-hint: [prompt or document-path]
allowed-tools: Read, Bash, Glob, Write
---

# /scaffold-audio-music

Generate music tracks using ElevenLabs, informed by the project's style guide and design doc mood/tone.

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

Read these files for musical direction context:

- `scaffold/design/style-guide.md` — visual tone, aesthetic pillars (translate to musical mood)
- `scaffold/design/design-doc.md` — overall mood, tone, setting, genre

Summarize the game's mood, tone, and setting into a compact musical direction string (1-2 sentences covering genre, tempo feel, instrumentation hints, and emotional tone). If the files don't exist or are mostly TODOs, note this and proceed with a minimal context.

### 3. Determine mode

Check the argument passed to the skill:

- **Document-driven mode:** If the argument contains `/` or ends with `.md`, treat it as a document path. Read the document and extract musical elements — mood, setting, tension level, pacing, and any described audio cues.
- **Freeform mode:** Otherwise, treat the argument as a base prompt for music generation.

### 4. Build prompt

Combine the musical direction from Step 2 with the user's prompt or document-extracted description into a single music generation prompt. Focus on:

- **Genre and tempo** — what style of music, approximate BPM feel
- **Mood and emotion** — the feeling the music should evoke
- **Instrumentation** — key instruments or sound textures
- **Loop-friendliness** — whether the track should loop seamlessly

**Show the composed prompt to the user and ask for confirmation or edits before generating.** Do not call the API until the user approves the prompt.

### 5. Generate audio

1. Ensure `scaffold/audio/music/` directory exists (create it if needed).

2. Generate a kebab-case filename from the prompt:
   - Take the first few meaningful words (max 40 characters)
   - Append a timestamp: `-YYYYMMDD-HHMMSS`
   - Add `.mp3` extension
   - Example: `forest-village-theme-20260223-143022.mp3`

3. Run the generation command:

```bash
python scaffold/tools/audio-gen.py music \
    --prompt "<approved prompt>" \
    --output "scaffold/audio/music/<filename>.mp3" \
    --instrumental
```

   Add `--duration <seconds>` if the user specifies a desired length.

4. Parse the JSON result from stdout. If `status` is `"error"`, report the error message and stop.

### 6. Update index

Append a row to `scaffold/audio/music/_index.md` in the Files table:

```markdown
| <filename>.mp3 | <short prompt summary, max 60 chars> | YYYY-MM-DD |
```

Create the index file from the template if it doesn't exist yet.

### 7. Report

Show the user:

- File path where the audio was saved
- Duration and provider info from the result
- Ask if they want another variation, different duration, or vocal vs instrumental

## Rules

- **Always read style guide and design doc first** — even if the user provides a detailed prompt, the design context ensures tonal consistency.
- **Show composed prompt before calling API** — the user must confirm or edit the prompt. Never generate without explicit approval.
- **If `ELEVENLABS_API_KEY` is not set, explain how to set it and stop** — do not attempt generation.
- **Kebab-case filenames with timestamps** — avoids collisions and keeps the directory scannable.
- **Do not modify any design documents** — this skill only creates audio files and updates the audio index.
