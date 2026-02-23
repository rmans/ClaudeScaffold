#!/usr/bin/env python3
"""Concept art generator — DALL-E integration for the scaffold pipeline."""

import argparse
import base64
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path


def get_api_key():
    """Resolve OpenAI API key from environment variable or .env file."""
    env_var = "OPENAI_API_KEY"

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


def generate_image(args):
    """Generate an image using the DALL-E API."""
    api_key = get_api_key()
    if not api_key:
        result = {
            "status": "error",
            "message": "OPENAI_API_KEY not found. Set it as an environment variable or in scaffold/.env",
        }
        print(json.dumps(result, indent=2))
        sys.exit(1)

    # Build the full prompt with optional style context
    full_prompt = args.prompt
    if args.style_context:
        full_prompt = f"{args.style_context}. {args.prompt}"

    # Prepare the request payload
    payload = {
        "model": args.model,
        "prompt": full_prompt,
        "n": 1,
        "size": args.size,
        "quality": args.quality,
        "response_format": "b64_json",
    }

    body = json.dumps(payload).encode("utf-8")

    req = urllib.request.Request(
        "https://api.openai.com/v1/images/generations",
        data=body,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        },
        method="POST",
    )

    try:
        response = urllib.request.urlopen(req, timeout=120)
        response_data = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8") if e.fp else ""
        try:
            error_json = json.loads(error_body)
            msg = error_json.get("error", {}).get("message", error_body)
        except json.JSONDecodeError:
            msg = error_body
        result = {"status": "error", "message": f"OpenAI API error ({e.code}): {msg}"}
        print(json.dumps(result, indent=2))
        sys.exit(1)
    except urllib.error.URLError as e:
        result = {"status": "error", "message": f"Connection error: {e.reason}"}
        print(json.dumps(result, indent=2))
        sys.exit(1)

    # Extract image data
    image_data = response_data["data"][0]
    b64_image = image_data["b64_json"]
    revised_prompt = image_data.get("revised_prompt", "")

    # Decode and save
    image_bytes = base64.b64decode(b64_image)
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(image_bytes)

    result = {
        "status": "ok",
        "file": str(output_path),
        "revised_prompt": revised_prompt,
        "size": args.size,
    }
    print(json.dumps(result, indent=2))


def main():
    parser = argparse.ArgumentParser(
        description="Concept art generator — DALL-E integration for the scaffold pipeline."
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    p_generate = subparsers.add_parser("generate", help="Generate concept art via DALL-E")
    p_generate.add_argument("--prompt", required=True, help="The image generation prompt")
    p_generate.add_argument(
        "--style-context",
        default=None,
        help="Extra style/color context prepended to the prompt",
    )
    p_generate.add_argument("--output", required=True, help="Output file path (.png)")
    p_generate.add_argument(
        "--size",
        default="1024x1024",
        choices=["1024x1024", "1792x1024", "1024x1792"],
        help="Image dimensions (default: 1024x1024)",
    )
    p_generate.add_argument(
        "--model",
        default="dall-e-3",
        help="DALL-E model to use (default: dall-e-3)",
    )
    p_generate.add_argument(
        "--quality",
        default="standard",
        choices=["standard", "hd"],
        help="Image quality (default: standard)",
    )

    args = parser.parse_args()

    if args.command == "generate":
        generate_image(args)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
