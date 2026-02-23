#!/usr/bin/env python3
"""Audio generator — multi-provider audio integration for the scaffold pipeline."""

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path


def get_api_key(env_var):
    """Resolve an API key from environment variable or .env file."""
    key = os.environ.get(env_var)

    if not key:
        env_file = Path(__file__).parent.parent / ".env"
        if env_file.exists():
            for line in env_file.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if line.startswith("#") or "=" not in line:
                    continue
                k, v = line.split("=", 1)
                k = k.strip()
                v = v.strip().strip("'").strip('"')
                if k == env_var:
                    key = v
                    break

    return key


def load_config():
    """Load audio_config.json from the same directory as this script."""
    config_path = Path(__file__).parent / "audio_config.json"
    if not config_path.exists():
        return None
    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)


def api_request(url, headers, body, timeout=120):
    """Make an API request and return raw response bytes."""
    req = urllib.request.Request(
        url,
        data=body,
        headers=headers,
        method="POST",
    )

    try:
        response = urllib.request.urlopen(req, timeout=timeout)
        return response.read(), response.headers.get("Content-Type", "")
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8") if e.fp else ""
        try:
            error_json = json.loads(error_body)
            msg = error_json.get("error", {}).get("message", "")
            if not msg:
                msg = error_json.get("detail", {}).get("message", error_body)
            if not msg:
                msg = error_body
        except (json.JSONDecodeError, AttributeError):
            msg = error_body
        return None, f"API error ({e.code}): {msg}"
    except urllib.error.URLError as e:
        return None, f"Connection error: {e.reason}"


# ---------------------------------------------------------------------------
# TTS subcommand
# ---------------------------------------------------------------------------

def cmd_tts(args):
    """Generate speech audio using OpenAI TTS or ElevenLabs TTS."""
    config = load_config()
    provider = args.provider
    if not provider and config:
        provider = config.get("tts", {}).get("provider", "openai")
    if not provider:
        provider = "openai"

    if provider == "openai":
        _tts_openai(args, config)
    elif provider == "elevenlabs":
        _tts_elevenlabs(args, config)
    else:
        _error(f"Unknown TTS provider: {provider}")


def _tts_openai(args, config):
    """Generate speech using OpenAI TTS API."""
    tts_config = (config or {}).get("tts", {}).get("openai", {})
    env_var = tts_config.get("api_key_env", "OPENAI_API_KEY")
    api_key = get_api_key(env_var)

    if not api_key:
        _error(f"{env_var} not found. Set it as an environment variable or in scaffold/.env")

    model = args.model or tts_config.get("model", "tts-1")
    voice = args.voice or tts_config.get("voice", "alloy")

    payload = {
        "model": model,
        "input": args.text,
        "voice": voice,
        "response_format": "mp3",
    }

    if args.speed and args.speed != 1.0:
        payload["speed"] = args.speed

    if args.instructions and model == "gpt-4o-mini-tts":
        payload["instructions"] = args.instructions

    body = json.dumps(payload).encode("utf-8")
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }

    data, content_type = api_request(
        "https://api.openai.com/v1/audio/speech", headers, body
    )

    if data is None:
        _error(f"OpenAI TTS: {content_type}")

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(data)

    result = {
        "status": "ok",
        "file": str(output_path),
        "provider": "openai",
        "model": model,
        "voice": voice,
    }
    print(json.dumps(result, indent=2))


def _tts_elevenlabs(args, config):
    """Generate speech using ElevenLabs TTS API."""
    tts_config = (config or {}).get("tts", {}).get("elevenlabs", {})
    env_var = tts_config.get("api_key_env", "ELEVENLABS_API_KEY")
    api_key = get_api_key(env_var)

    if not api_key:
        _error(f"{env_var} not found. Set it as an environment variable or in scaffold/.env")

    model_id = tts_config.get("model_id", "eleven_multilingual_v2")
    voice_id = args.voice or tts_config.get("voice_id", "21m00Tcm4TlvDq8ikWAM")

    payload = {
        "text": args.text,
        "model_id": model_id,
    }

    body = json.dumps(payload).encode("utf-8")
    headers = {
        "Content-Type": "application/json",
        "xi-api-key": api_key,
    }

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    data, content_type = api_request(url, headers, body)

    if data is None:
        _error(f"ElevenLabs TTS: {content_type}")

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(data)

    result = {
        "status": "ok",
        "file": str(output_path),
        "provider": "elevenlabs",
        "model_id": model_id,
        "voice_id": voice_id,
    }
    print(json.dumps(result, indent=2))


# ---------------------------------------------------------------------------
# SFX subcommand
# ---------------------------------------------------------------------------

def cmd_sfx(args):
    """Generate sound effects using ElevenLabs Sound Generation API."""
    config = load_config()
    sfx_config = (config or {}).get("sfx", {}).get("elevenlabs", {})
    env_var = sfx_config.get("api_key_env", "ELEVENLABS_API_KEY")
    api_key = get_api_key(env_var)

    if not api_key:
        _error(f"{env_var} not found. Set it as an environment variable or in scaffold/.env")

    payload = {
        "text": args.prompt,
    }

    if args.duration is not None:
        payload["duration_seconds"] = args.duration

    prompt_influence = args.prompt_influence
    if prompt_influence is None:
        prompt_influence = sfx_config.get("prompt_influence")
    if prompt_influence is not None:
        payload["prompt_influence"] = prompt_influence

    body = json.dumps(payload).encode("utf-8")
    headers = {
        "Content-Type": "application/json",
        "xi-api-key": api_key,
    }

    data, content_type = api_request(
        "https://api.elevenlabs.io/v1/sound-generation", headers, body
    )

    if data is None:
        _error(f"ElevenLabs SFX: {content_type}")

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(data)

    result = {
        "status": "ok",
        "file": str(output_path),
        "provider": "elevenlabs",
        "loop": args.loop,
    }
    print(json.dumps(result, indent=2))


# ---------------------------------------------------------------------------
# Music subcommand
# ---------------------------------------------------------------------------

def cmd_music(args):
    """Generate music using ElevenLabs Music Generation API."""
    config = load_config()
    music_config = (config or {}).get("music", {}).get("elevenlabs", {})
    env_var = music_config.get("api_key_env", "ELEVENLABS_API_KEY")
    api_key = get_api_key(env_var)

    if not api_key:
        _error(f"{env_var} not found. Set it as an environment variable or in scaffold/.env")

    payload = {
        "prompt": args.prompt,
    }

    if args.duration is not None:
        payload["duration_seconds"] = args.duration

    if args.instrumental:
        payload["instrumental"] = True

    body = json.dumps(payload).encode("utf-8")
    headers = {
        "Content-Type": "application/json",
        "xi-api-key": api_key,
    }

    data, content_type = api_request(
        "https://api.elevenlabs.io/v1/music", headers, body, timeout=180
    )

    if data is None:
        _error(f"ElevenLabs Music: {content_type}")

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(data)

    result = {
        "status": "ok",
        "file": str(output_path),
        "provider": "elevenlabs",
        "instrumental": args.instrumental,
    }
    print(json.dumps(result, indent=2))


# ---------------------------------------------------------------------------
# Check-config subcommand
# ---------------------------------------------------------------------------

def cmd_check_config(args):
    """Verify configuration and API keys."""
    config = load_config()
    if config is None:
        _error("audio_config.json not found in scaffold/tools/")

    results = []

    for audio_type in ("tts", "sfx", "music"):
        type_config = config.get(audio_type, {})
        provider = type_config.get("provider", "unknown")
        provider_config = type_config.get(provider, {})
        env_var = provider_config.get("api_key_env", "")

        has_key = bool(get_api_key(env_var)) if env_var else False

        results.append({
            "type": audio_type,
            "provider": provider,
            "api_key_env": env_var,
            "api_key_set": has_key,
        })

    all_ok = all(r["api_key_set"] for r in results)
    output = {
        "status": "ok" if all_ok else "warning",
        "config_file": str(Path(__file__).parent / "audio_config.json"),
        "checks": results,
    }

    if not all_ok:
        missing = [r["api_key_env"] for r in results if not r["api_key_set"]]
        output["message"] = f"Missing API key(s): {', '.join(set(missing))}"

    print(json.dumps(output, indent=2))


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _error(message):
    """Print error JSON and exit."""
    result = {"status": "error", "message": message}
    print(json.dumps(result, indent=2))
    sys.exit(1)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Audio generator — multi-provider audio integration for the scaffold pipeline."
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # --- tts ---
    p_tts = subparsers.add_parser("tts", help="Generate speech audio (OpenAI TTS or ElevenLabs)")
    p_tts.add_argument("--text", required=True, help="The text to speak")
    p_tts.add_argument("--output", required=True, help="Output file path (.mp3)")
    p_tts.add_argument("--voice", default=None, help="Voice name/ID (default: from config)")
    p_tts.add_argument("--model", default=None, help="TTS model (default: from config)")
    p_tts.add_argument("--speed", type=float, default=1.0, help="Speech speed 0.25-4.0 (OpenAI only, default: 1.0)")
    p_tts.add_argument("--instructions", default=None, help="Voice instructions (gpt-4o-mini-tts only)")
    p_tts.add_argument("--provider", default=None, choices=["openai", "elevenlabs"], help="Override provider (default: from config)")

    # --- sfx ---
    p_sfx = subparsers.add_parser("sfx", help="Generate sound effects (ElevenLabs)")
    p_sfx.add_argument("--prompt", required=True, help="Description of the sound effect")
    p_sfx.add_argument("--output", required=True, help="Output file path (.mp3)")
    p_sfx.add_argument("--duration", type=float, default=None, help="Duration in seconds")
    p_sfx.add_argument("--prompt-influence", type=float, default=None, help="Prompt influence 0.0-1.0 (default: from config)")
    p_sfx.add_argument("--loop", action="store_true", help="Mark as looping audio (metadata flag)")

    # --- music ---
    p_music = subparsers.add_parser("music", help="Generate music (ElevenLabs)")
    p_music.add_argument("--prompt", required=True, help="Description of the music")
    p_music.add_argument("--output", required=True, help="Output file path (.mp3)")
    p_music.add_argument("--duration", type=float, default=None, help="Duration in seconds")
    p_music.add_argument("--instrumental", action="store_true", help="Generate instrumental only (no vocals)")

    # --- check-config ---
    subparsers.add_parser("check-config", help="Verify configuration and API keys")

    args = parser.parse_args()

    if args.command == "tts":
        cmd_tts(args)
    elif args.command == "sfx":
        cmd_sfx(args)
    elif args.command == "music":
        cmd_music(args)
    elif args.command == "check-config":
        cmd_check_config(args)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
