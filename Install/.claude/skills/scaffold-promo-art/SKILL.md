---
name: scaffold-promo-art
description: Generate promotional art using DALL-E, informed by the project's style guide and color system.
argument-hint: [prompt or document-path]
allowed-tools: Read, Bash, Glob, Write
---

# /scaffold-promo-art

Generate promotional art using DALL-E, informed by the project's style guide and color system.

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

Read these files for visual style and brand identity context:

- `scaffold/design/style-guide.md` — art style, visual tone, aesthetic pillars
- `scaffold/design/color-system.md` — palette, color roles, mood

Also check for identity and vision context in the design doc:

- `scaffold/design/design-doc.md` — look for Core Fantasy, Identity, Vision, and Aesthetic Pillars sections

Summarize the art style, visual tone, brand identity, and palette into a compact style context string (1-2 sentences). If the files don't exist or are mostly TODOs, note this and proceed with a minimal style context.

### 3. Determine mode

Check the argument passed to the skill:

- **Document-driven mode:** If the argument contains `/` or ends with `.md`, treat it as a document path. Read the document and extract key visual themes, dramatic moments, or brand identity elements described in it.
- **Freeform mode:** Otherwise, treat the argument as a base prompt for image generation.

### 4. Build prompt

Combine the style context from Step 2 with the user's prompt or document-extracted description into a single DALL-E prompt.

**Prompt focus:** Emphasize dramatic composition, marketing appeal, text-safe space (leave room for title/logo overlay), landscape orientation, eye-catching focal point, and emotional impact. Frame the image as a game promotional banner, key art, or store page hero image.

**Show the composed prompt to the user and ask for confirmation or edits before generating.** Do not call the API until the user approves the prompt.

### 5. Generate image

1. Ensure `scaffold/art/promo-art/` directory exists (create it if needed).

2. Generate a kebab-case filename from the prompt:
   - Take the first few meaningful words (max 40 characters)
   - Append a timestamp: `-YYYYMMDD-HHMMSS`
   - Add `.png` extension
   - Example: `hero-banner-dark-forest-20260223-143022.png`

3. Run the generation command:

```bash
python scaffold/tools/image-gen.py generate \
    --prompt "<approved prompt>" \
    --style-context "<style context from step 2>" \
    --output "scaffold/art/promo-art/<filename>.png" \
    --size 1792x1024 \
    --model dall-e-3 \
    --quality standard
```

4. Parse the JSON result from stdout. If `status` is `"error"`, report the error message and stop.

### 6. Update index

Append a row to `scaffold/art/promo-art/_index.md` in the Files table:

```markdown
| <filename>.png | <short prompt summary, max 60 chars> | YYYY-MM-DD |
```

Create the index file from the template if it doesn't exist yet.

### 7. Report

Show the user:

- File path where the image was saved
- DALL-E's `revised_prompt` (how DALL-E interpreted the prompt)
- Ask if they want another variation or a different size/quality

## Rules

- **Always read style guide and color system first** — even if the user provides a detailed prompt, the style context ensures brand consistency.
- **Show composed prompt before calling API** — the user must confirm or edit the prompt. Never generate without explicit approval.
- **If `OPENAI_API_KEY` is not set, explain how to set it and stop** — do not attempt generation.
- **Kebab-case filenames with timestamps** — avoids collisions and keeps the directory scannable.
- **Do not modify any design documents** — this skill only creates images and updates the art index.
