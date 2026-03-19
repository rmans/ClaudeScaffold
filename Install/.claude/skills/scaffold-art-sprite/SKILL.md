---
name: scaffold-art-sprite
description: Generate sprite art using OpenArt (default) or DALL-E, informed by the project's style guide and color system.
argument-hint: [prompt or document-path] [--model dalle|openart]
allowed-tools: Read, Bash, Glob, Write
---

# /scaffold-art-sprite

Generate sprite art using OpenArt (default) or DALL-E, informed by the project's style guide and color system.

## Steps

### 1. Check provider and API key

Parse the `--model` flag from the arguments. Supported values: `openart` (default), `dalle`.

- **If `--model dalle`:** Check that `OPENAI_API_KEY` is set (environment variable or `scaffold/.env`). If not found, explain how to set it and stop.
- **If `--model openart` (or no --model flag):** No API key needed. OpenArt is browser-based.

### 2. Read design context

Read these files for visual style context:

- `scaffold/design/style-guide.md` — art style, visual tone, aesthetic pillars
- `scaffold/design/color-system.md` — palette, color roles, mood

Summarize the art style, visual tone, and palette into a compact style context string (1-2 sentences). If the files don't exist or are mostly TODOs, note this and proceed with a minimal style context.

### 3. Determine mode

Check the argument passed to the skill:

- **Document-driven mode:** If the argument contains `/` or ends with `.md`, treat it as a document path. Read the document and extract visual elements, sprite subjects, or animation frame descriptions in it.
- **Freeform mode:** Otherwise, treat the argument as a base prompt for image generation.

### 4. Build prompt

Combine the style context from Step 2 with the user's prompt or document-extracted description into a single image generation prompt.

**Prompt focus:** Emphasize limited color palette, clean edges, small-size readability, and sprite-sheet clarity. Frame the image as a game sprite asset.

**Show the composed prompt to the user and ask for confirmation or edits before generating.** Do not call the API until the user approves the prompt.

### 5. Generate image

1. Ensure the output directory exists (create if needed). The directory is `scaffold/art/sprite-art/`.

2. Generate a kebab-case filename from the prompt:
   - Take the first few meaningful words (max 40 characters)
   - Append a timestamp: `-YYYYMMDD-HHMMSS`
   - Add `.png` extension

3. Determine the provider from the `--model` flag (default: `openart`).

4. Run the generation command:

```bash
python scaffold/tools/image-gen.py generate \
    --prompt "<approved prompt>" \
    --style-context "<style context from step 2>" \
    --output "scaffold/art/sprite-art/<filename>.png" \
    --provider <dalle|openart> \
    --size 1024x1024 \
    --model dall-e-3 \
    --quality standard
```

5. Parse the JSON result from stdout:
   - If `"status"` is `"error"`, report the error message and stop.
   - If `"status"` is `"ok"` (dalle), the image was saved automatically. Continue to step 6.
   - If `"status"` is `"manual"` (openart), show the user the composed prompt and instructions:
     1. Go to https://openart.ai/
     2. Paste the prompt into the generation field
     3. Generate and download the image
     4. Save to the output path shown
     Wait for the user to confirm the image is saved before continuing to step 6.

### 6. Update index

Append a row to `scaffold/art/sprite-art/_index.md` in the Files table:

```markdown
| <filename>.png | <short prompt summary, max 60 chars> | YYYY-MM-DD |
```

Create the index file from the template if it doesn't exist yet.

### 7. Report

Show the user:

- File path where the image was saved
- The provider's `revised_prompt` (dalle only — openart has no revised prompt)
- Ask if they want another variation or a different size/quality

## Rules

- **Always read style guide and color system first** — even if the user provides a detailed prompt, the style context ensures brand consistency.
- **Show composed prompt before calling API** — the user must confirm or edit the prompt. Never generate without explicit approval.
- **If using dalle and `OPENAI_API_KEY` is not set, explain how to set it and stop. OpenArt requires no API key.**
- **Kebab-case filenames with timestamps** — avoids collisions and keeps the directory scannable.
- **Do not modify any design documents** — this skill only creates images and updates the art index.
