# Tools — Index

> **Purpose:** Scripts and utilities that support the scaffold pipeline.

## Tools

| File | Description |
|------|-------------|
| `image-gen.py` | Image generator — DALL-E integration for the scaffold pipeline (shared by all 7 art skills) |
| `audio-gen.py` | Audio generator — multi-provider audio integration for the scaffold pipeline (shared by all 4 audio skills) |
| `audio_config.json` | Configuration for audio-gen.py (provider per audio type, model/voice defaults) |
| `doc-review.py` | Adversarial document reviewer — multi-provider (OpenAI / Anthropic) |
| `review_config.json` | Configuration for doc-review.py (provider, model, temperature) |
| `validate-refs.py` | Cross-reference validator — checks referential integrity across all scaffold docs |

## image-gen.py

Image generator that sends prompts to the DALL-E API and saves generated images locally. Shared by all 7 art skills: `/scaffold-art-concept`, `/scaffold-art-ui-mockup`, `/scaffold-art-character`, `/scaffold-art-environment`, `/scaffold-art-sprite`, `/scaffold-art-icon`, `/scaffold-art-promo`.

### Commands

| Command | Description |
|---------|-------------|
| `generate` | Generate an image from a text prompt via DALL-E |

### Usage

```
python scaffold/tools/image-gen.py generate \
    --prompt "a forest village at dusk" \
    --style-context "pixel art, warm palette" \
    --output scaffold/art/concept-art/forest-village.png \
    --size 1024x1024 \
    --model dall-e-3 \
    --quality standard
```

### Arguments

| Argument | Required | Default | Description |
|----------|----------|---------|-------------|
| `--prompt` | Yes | — | The image generation prompt |
| `--style-context` | No | — | Extra style/color context prepended to the prompt |
| `--output` | Yes | — | Output file path (.png) |
| `--size` | No | `1024x1024` | Image dimensions (`1024x1024`, `1792x1024`, `1024x1792`) |
| `--model` | No | `dall-e-3` | DALL-E model to use |
| `--quality` | No | `standard` | Image quality (`standard` or `hd`) |

### Output Format (JSON)

```json
{
  "status": "ok",
  "file": "scaffold/art/concept-art/forest-village.png",
  "revised_prompt": "A serene forest village at dusk...",
  "size": "1024x1024"
}
```

On error:

```json
{
  "status": "error",
  "message": "OPENAI_API_KEY not found..."
}
```

### Dependencies

None — uses Python standard library only (`urllib`, `json`, `argparse`, `base64`).

## audio-gen.py

Audio generator that sends requests to OpenAI TTS or ElevenLabs APIs and saves generated audio locally. Shared by all 4 audio skills: `/scaffold-audio-music`, `/scaffold-audio-sfx`, `/scaffold-audio-ambience`, `/scaffold-audio-voice`.

### Commands

| Command | Description |
|---------|-------------|
| `tts` | Generate speech audio (OpenAI TTS or ElevenLabs TTS) |
| `sfx` | Generate sound effects (ElevenLabs Sound Generation) |
| `music` | Generate music (ElevenLabs Music Generation) |
| `check-config` | Verify configuration and API keys |

### Usage

```
python scaffold/tools/audio-gen.py tts \
    --text "The ancient forest holds secrets." \
    --output scaffold/audio/voice/ancient-forest-line.mp3 \
    --voice alloy \
    --model tts-1

python scaffold/tools/audio-gen.py sfx \
    --prompt "sword slash impact, metallic ring" \
    --output scaffold/audio/sfx/sword-slash.mp3 \
    --duration 2.0 \
    --prompt-influence 0.3

python scaffold/tools/audio-gen.py music \
    --prompt "upbeat chiptune battle theme, 120 BPM" \
    --output scaffold/audio/music/battle-theme.mp3 \
    --duration 30 \
    --instrumental

python scaffold/tools/audio-gen.py check-config
```

### Arguments — tts

| Argument | Required | Default | Description |
|----------|----------|---------|-------------|
| `--text` | Yes | — | The text to speak |
| `--output` | Yes | — | Output file path (.mp3) |
| `--voice` | No | From config | Voice name/ID (OpenAI: alloy/echo/fable/onyx/nova/shimmer) |
| `--model` | No | From config | TTS model (e.g., `tts-1`, `gpt-4o-mini-tts`) |
| `--speed` | No | `1.0` | Speech speed 0.25–4.0 (OpenAI only) |
| `--instructions` | No | — | Voice instructions (`gpt-4o-mini-tts` only) |
| `--provider` | No | From config | Override provider (`openai` or `elevenlabs`) |

### Arguments — sfx

| Argument | Required | Default | Description |
|----------|----------|---------|-------------|
| `--prompt` | Yes | — | Description of the sound effect |
| `--output` | Yes | — | Output file path (.mp3) |
| `--duration` | No | — | Duration in seconds |
| `--prompt-influence` | No | From config | Prompt influence 0.0–1.0 |
| `--loop` | No | `false` | Mark as looping audio (metadata flag) |

### Arguments — music

| Argument | Required | Default | Description |
|----------|----------|---------|-------------|
| `--prompt` | Yes | — | Description of the music |
| `--output` | Yes | — | Output file path (.mp3) |
| `--duration` | No | — | Duration in seconds |
| `--instrumental` | No | `false` | Generate instrumental only (no vocals) |

### Output Format (JSON)

```json
{
  "status": "ok",
  "file": "scaffold/audio/music/battle-theme.mp3",
  "provider": "elevenlabs",
  "instrumental": true
}
```

On error:

```json
{
  "status": "error",
  "message": "ELEVENLABS_API_KEY not found..."
}
```

### Dependencies

None — uses Python standard library only (`urllib`, `json`, `argparse`).

## audio_config.json

Provider configuration for `audio-gen.py`. Specifies which provider to use for each audio type (tts, sfx, music), along with model/voice defaults and API key environment variable names.

### Structure

```json
{
  "tts": {
    "provider": "openai",
    "openai": { "model": "tts-1", "voice": "alloy", "api_key_env": "OPENAI_API_KEY" },
    "elevenlabs": { "model_id": "eleven_multilingual_v2", "voice_id": "...", "api_key_env": "ELEVENLABS_API_KEY" }
  },
  "sfx": {
    "provider": "elevenlabs",
    "elevenlabs": { "prompt_influence": 0.3, "api_key_env": "ELEVENLABS_API_KEY" }
  },
  "music": {
    "provider": "elevenlabs",
    "elevenlabs": { "api_key_env": "ELEVENLABS_API_KEY" }
  }
}
```

### Provider Selection

Each audio type (`tts`, `sfx`, `music`) has a `provider` field that selects which provider config to use. The `tts` subcommand also supports a `--provider` CLI flag to override at runtime.

## doc-review.py

Adversarial document reviewer that sends scaffold documents to an external LLM for review, then supports multi-turn back-and-forth conversations until consensus. Used by `/scaffold-iterate`.

### Commands

| Command | Description |
|---------|-------------|
| `review <path>` | Start a fresh review iteration — returns structured issues JSON |
| `respond <path>` | Continue conversation within an iteration (inner loop exchange) |
| `consensus <path>` | Request final consensus summary after discussion |
| `check-config` | Verify configuration and API key |

### Loop Structure

```
Outer Loop (iterations — fresh review of updated doc)
└── Inner Loop (exchanges — back-and-forth conversation)
    ├── Reviewer raises issues (structured JSON)
    ├── Claude evaluates, pushes back, or agrees
    ├── Reviewer counter-responds
    └── ... until consensus or max exchanges
```

### Usage

```
python scaffold/tools/doc-review.py review <path> --iteration 1 --context-files <file1> <file2>
python scaffold/tools/doc-review.py respond <path> --iteration 1 --message-file <file>
python scaffold/tools/doc-review.py consensus <path> --iteration 1
python scaffold/tools/doc-review.py check-config
```

### Doc Type Auto-Detection

The script detects document type from its path. Use `--type` to override. Supported types: design, style, system, reference, engine, input, roadmap, phase, slice, spec, task.

### Review Tiers

| Tier | Max Iter | Max Exchanges | Severity | Doc Types |
|------|----------|---------------|----------|-----------|
| Full | 5 | 5 | All | design, style, system, roadmap, phase, spec |
| Lite | 1 | 3 | HIGH only | engine, input, slice, task |
| Lint | 1 | 2 | HIGH only | reference |

### Configuration

Configured via `review_config.json` in the same directory. Supports OpenAI and Anthropic providers. API key is read from the environment variable specified in config, or from `scaffold/.env`.

### Dependencies

None — uses Python standard library only (`urllib`, `json`, `argparse`).

## validate-refs.py

Cross-reference validator that checks referential integrity across all scaffold documents. Detects broken references, missing registrations, glossary violations, and orphaned entries. Used by `/scaffold-validate`.

### Commands

```
python scaffold/tools/validate-refs.py [--format json|text]
```

### Checks Performed

| Check | What It Validates |
|-------|------------------|
| `system-ids` | Every SYS-### reference points to a registered system in systems/_index.md |
| `authority-entities` | Entity authorities match authority.md owners |
| `signals-systems` | Signal emitters/consumers are registered systems |
| `interfaces-systems` | Interface sources/targets are registered systems |
| `states-systems` | State machine authorities are registered systems |
| `glossary-not` | No non-theory doc uses a term from the glossary NOT column |
| `bidirectional-registration` | systems/_index.md and design-doc.md System Design Index match |
| `spec-slice` | Every spec appears in at least one slice |
| `task-spec` | Every task references a valid spec |

### Usage

```
python scaffold/tools/validate-refs.py                  # Human-readable text output
python scaffold/tools/validate-refs.py --format json     # JSON array of issues
python scaffold/tools/validate-refs.py --format text     # Human-readable text output
```

### Output Format (JSON)

```json
[
  {
    "check": "system-ids",
    "severity": "ERROR",
    "message": "SYS-005 referenced in authority.md but not registered in systems/_index.md",
    "file": "design/authority.md",
    "line": 12
  }
]
```

### Exit Codes

- `0` — All checks pass (no errors)
- `1` — One or more errors found

### Dependencies

None — uses Python standard library only (`pathlib`, `re`, `json`, `argparse`).
