---
name: scaffold-audio-ambience
description: Generate ambient audio loops using ElevenLabs, informed by the project's style guide, color system mood, and design doc world/setting.
argument-hint: [prompt or document-path]
allowed-tools: Read, Bash, Glob, Write
---

# /scaffold-audio-ambience

Generate ambient audio loops using ElevenLabs, informed by the project's style guide, color system mood, and design doc world/setting.

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

Read these files for atmospheric context:

- `scaffold/design/style-guide.md` — visual tone, aesthetic pillars (translate to ambient mood)
- `scaffold/design/color-system.md` — palette mood, emotional associations
- `scaffold/design/design-doc.md` — world, setting, environments, biomes

Summarize the game's atmosphere and world into a compact ambient direction string (1-2 sentences covering environment type, mood, depth, and spatial character). If the files don't exist or are mostly TODOs, note this and proceed with a minimal context.

### 3. Determine mode

Check the argument passed to the skill:

- **Document-driven mode:** If the argument contains `/` or ends with `.md`, treat it as a document path. Read the document and extract environment descriptions, world-building details, mood cues, and spatial settings.
- **Freeform mode:** Otherwise, treat the argument as a base prompt for ambience generation.

### 4. Build prompt

Combine the atmospheric direction from Step 2 with the user's prompt or document-extracted description into a single ambience generation prompt. Focus on:

- **Atmosphere** — the feeling of being in the space
- **Depth** — layers of near and far sounds
- **Layering** — multiple subtle elements that create a rich soundscape
- **Loop seamlessness** — the track must loop without noticeable cuts

**Show the composed prompt to the user and ask for confirmation or edits before generating.** Do not call the API until the user approves the prompt.

### 5. Generate audio

1. Ensure `scaffold/audio/ambience/` directory exists (create it if needed).

2. Generate a kebab-case filename from the prompt:
   - Take the first few meaningful words (max 40 characters)
   - Append a timestamp: `-YYYYMMDD-HHMMSS`
   - Add `.mp3` extension
   - Example: `misty-forest-clearing-20260223-143022.mp3`

3. Run the generation command:

```bash
python scaffold/tools/audio-gen.py sfx \
    --prompt "<approved prompt>" \
    --output "scaffold/audio/ambience/<filename>.mp3" \
    --loop
```

   Add `--duration <seconds>` if the user specifies a desired length.

4. Parse the JSON result from stdout. If `status` is `"error"`, report the error message and stop.

### 6. Update index

Append a row to `scaffold/audio/ambience/_index.md` in the Files table:

```markdown
| <filename>.mp3 | <short prompt summary, max 60 chars> | YYYY-MM-DD |
```

Create the index file from the template if it doesn't exist yet.

### 7. Report

Show the user:

- File path where the audio was saved
- Provider info from the result
- Note that `--loop` was used for seamless looping
- Ask if they want another variation, different duration, or a different environmental feel

## Rules

- **Always read style guide, color system, and design doc first** — even if the user provides a detailed prompt, the design context ensures atmospheric consistency with the game world.
- **Always use `--loop` flag** — ambience tracks are looping audio by nature.
- **Show composed prompt before calling API** — the user must confirm or edit the prompt. Never generate without explicit approval.
- **If `ELEVENLABS_API_KEY` is not set, explain how to set it and stop** — do not attempt generation.
- **Kebab-case filenames with timestamps** — avoids collisions and keeps the directory scannable.
- **Do not modify any design documents** — this skill only creates audio files and updates the audio index.
