---
name: scaffold-audio-voice
description: Generate voice audio using OpenAI TTS, informed by the project's style guide and design doc characters/narrative.
argument-hint: [prompt or document-path]
allowed-tools: Read, Bash, Glob, Write
---

# /scaffold-audio-voice

Generate voice audio using OpenAI TTS, informed by the project's style guide and design doc characters/narrative.

## Steps

### 1. Check API key

Check that `OPENAI_API_KEY` is set (environment variable or `scaffold/.env`). If not found, explain how to set it:

```
export OPENAI_API_KEY="sk-..."
```

Or add to `scaffold/.env`:

```
OPENAI_API_KEY=sk-...
```

Stop here if the key is not available.

### 2. Read design context

Read these files for character and narrative context:

- `scaffold/design/style-guide.md` — visual tone (translate to vocal energy and register)
- `scaffold/design/design-doc.md` — characters, narrative, dialogue style, world tone

Summarize the game's character voice direction into a compact context string (1-2 sentences covering vocal register, energy, pacing, and emotional range). If the files don't exist or are mostly TODOs, note this and proceed with a minimal context.

### 3. Determine mode

Check the argument passed to the skill:

- **Document-driven mode:** If the argument contains `/` or ends with `.md`, treat it as a document path. Read the document and extract character descriptions, dialogue lines, narrative text, or callout phrases.
- **Freeform mode:** Otherwise, treat the argument as the text to speak (or a description of what voice line to generate).

### 4. Build text and voice parameters

From the context in Step 2 and the user's input:

1. **Determine the text to speak** — exact dialogue line, narration, or callout.
2. **Choose a voice** — suggest one of the OpenAI TTS voices (`alloy`, `echo`, `fable`, `onyx`, `nova`, `shimmer`) based on character personality, or let the user pick.
3. **Set speed** — normal (1.0) by default; slower for gravitas, faster for urgency.
4. **Add instructions** — if using `gpt-4o-mini-tts` model, compose voice instructions for character personality, tone, and pacing.

**Show the text, voice selection, and any instructions to the user and ask for confirmation or edits before generating.** Do not call the API until the user approves.

### 5. Generate audio

1. Ensure `scaffold/audio/voice/` directory exists (create it if needed).

2. Generate a kebab-case filename from the text content:
   - Take the first few meaningful words (max 40 characters)
   - Append a timestamp: `-YYYYMMDD-HHMMSS`
   - Add `.mp3` extension
   - Example: `hero-battle-cry-20260223-143022.mp3`

3. Run the generation command:

```bash
python scaffold/tools/audio-gen.py tts \
    --text "<approved text>" \
    --output "scaffold/audio/voice/<filename>.mp3" \
    --voice <chosen-voice>
```

   Add `--speed <0.25-4.0>` if non-default speed is desired.
   Add `--model gpt-4o-mini-tts --instructions "<instructions>"` for character-directed voice.

4. Parse the JSON result from stdout. If `status` is `"error"`, report the error message and stop.

### 6. Update index

Append a row to `scaffold/audio/voice/_index.md` in the Files table:

```markdown
| <filename>.mp3 | <short text summary, max 60 chars> | YYYY-MM-DD |
```

Create the index file from the template if it doesn't exist yet.

### 7. Report

Show the user:

- File path where the audio was saved
- Voice and model used
- Ask if they want another take with a different voice, speed, or instructions

## Rules

- **Always read style guide and design doc first** — even if the user provides exact dialogue, the design context helps choose the right voice and tone.
- **Show text and voice parameters before calling API** — the user must confirm or edit. Never generate without explicit approval.
- **If `OPENAI_API_KEY` is not set, explain how to set it and stop** — do not attempt generation.
- **Kebab-case filenames with timestamps** — avoids collisions and keeps the directory scannable.
- **Do not modify any design documents** — this skill only creates audio files and updates the audio index.
