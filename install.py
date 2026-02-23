#!/usr/bin/env python3
"""ClaudeScaffold installer — downloads from GitHub and installs into a target project."""

import argparse
import json
import os
import shutil
import sys
import tempfile
import zipfile
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import urlopen

GITHUB_ZIP_URL = "https://github.com/rmans/ClaudeScaffold/archive/refs/heads/{branch}.zip"
EXCLUDE_DIRS = {"__pycache__"}
SCAFFOLD_SKILL_PREFIX = "scaffold-"
EXPECTED_SKILLS = 45


def log(msg, verbose_only=False, *, verbose=False):
    if verbose_only and not verbose:
        return
    print(msg)


def is_excluded(path: Path) -> bool:
    for part in path.parts:
        if part in EXCLUDE_DIRS:
            return True
    if path.suffix == ".pyc":
        return True
    return False


def collect_files(src: Path, rel_base: Path = None) -> list:
    """Collect all files under src, returning (absolute, relative) pairs."""
    if rel_base is None:
        rel_base = src
    result = []
    for item in sorted(src.rglob("*")):
        if item.is_file() and not is_excluded(item.relative_to(rel_base)):
            result.append((item, item.relative_to(rel_base)))
    return result


def download_zip(branch: str, dest_path: Path):
    """Download the GitHub zip archive for the given branch."""
    url = GITHUB_ZIP_URL.format(branch=branch)
    print(f"  Downloading {url}")
    try:
        response = urlopen(url)
    except HTTPError as e:
        if e.code == 404:
            print(f"\nERROR: Branch or tag '{branch}' not found on GitHub.", file=sys.stderr)
            print(f"  URL: {url}", file=sys.stderr)
        else:
            print(f"\nERROR: HTTP {e.code} downloading from GitHub.", file=sys.stderr)
            print(f"  URL: {url}", file=sys.stderr)
        sys.exit(1)
    except URLError as e:
        print(f"\nERROR: Could not connect to GitHub.", file=sys.stderr)
        print(f"  {e.reason}", file=sys.stderr)
        print("  Check your internet connection and try again.", file=sys.stderr)
        sys.exit(1)

    total = response.headers.get("Content-Length")
    downloaded = 0
    chunk_size = 64 * 1024

    with open(dest_path, "wb") as f:
        while True:
            chunk = response.read(chunk_size)
            if not chunk:
                break
            f.write(chunk)
            downloaded += len(chunk)
            if total:
                pct = downloaded * 100 // int(total)
                print(f"\r  Downloaded {downloaded // 1024} KB ({pct}%)", end="", flush=True)
            else:
                print(f"\r  Downloaded {downloaded // 1024} KB", end="", flush=True)

    print()  # newline after progress


def merge_settings(existing_path: Path, new_path: Path, dry_run: bool, verbose: bool):
    """Merge settings.local.json: add scaffold entries, keep existing user entries."""
    try:
        with open(new_path, "r", encoding="utf-8") as f:
            new_settings = json.load(f)
    except (json.JSONDecodeError, OSError) as e:
        log(f"  WARNING: Could not read source settings: {e}")
        return

    try:
        with open(existing_path, "r", encoding="utf-8") as f:
            existing_settings = json.load(f)
    except (json.JSONDecodeError, OSError) as e:
        log(f"  WARNING: Could not read existing settings: {e}, will overwrite")
        existing_settings = {}

    # Merge permissions.allow lists (union, preserving order)
    existing_allow = existing_settings.get("permissions", {}).get("allow", [])
    new_allow = new_settings.get("permissions", {}).get("allow", [])
    merged_allow = list(existing_allow)
    for entry in new_allow:
        if entry not in merged_allow:
            merged_allow.append(entry)

    # Merge permissions.deny lists similarly
    existing_deny = existing_settings.get("permissions", {}).get("deny", [])
    new_deny = new_settings.get("permissions", {}).get("deny", [])
    merged_deny = list(existing_deny)
    for entry in new_deny:
        if entry not in merged_deny:
            merged_deny.append(entry)

    merged = dict(existing_settings)
    if "permissions" not in merged:
        merged["permissions"] = {}
    if merged_allow:
        merged["permissions"]["allow"] = merged_allow
    if merged_deny:
        merged["permissions"]["deny"] = merged_deny

    if dry_run:
        log(f"  Would merge settings.local.json ({len(existing_allow)} existing + {len(new_allow)} scaffold entries)")
        return

    existing_path.parent.mkdir(parents=True, exist_ok=True)
    with open(existing_path, "w", encoding="utf-8") as f:
        json.dump(merged, f, indent=2)
        f.write("\n")
    log(f"  Merged settings.local.json ({len(merged_allow)} allow entries)", verbose_only=True, verbose=verbose)


def copy_file(src: Path, dst: Path, dry_run: bool, verbose: bool):
    if dry_run:
        log(f"  Would copy: {dst}")
        return
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    log(f"  Copied: {dst}", verbose_only=True, verbose=verbose)


def main():
    parser = argparse.ArgumentParser(
        description="Install ClaudeScaffold into a target project.",
        epilog="Example: python install.py /path/to/your/project",
    )
    parser.add_argument("target", help="Path to the target project directory")
    parser.add_argument("--branch", default="main", help="GitHub branch or tag to download (default: main)")
    parser.add_argument("--force", action="store_true", help="Overwrite existing scaffold/ directory")
    parser.add_argument("--dry-run", action="store_true", help="Show what would happen without copying")
    parser.add_argument("--verbose", action="store_true", help="List every file as it is copied")
    args = parser.parse_args()

    target = Path(args.target).resolve()

    # Check target exists and is writable
    if not target.is_dir():
        print(f"ERROR: Target directory does not exist: {target}", file=sys.stderr)
        sys.exit(1)
    if not os.access(target, os.W_OK):
        print(f"ERROR: Target directory is not writable: {target}", file=sys.stderr)
        sys.exit(1)

    # --- Download from GitHub ---
    print(f"\n0. Downloading ClaudeScaffold ({args.branch})")
    tmp_dir = tempfile.mkdtemp(prefix="claudescaffold-")
    zip_path = Path(tmp_dir) / "repo.zip"

    try:
        download_zip(args.branch, zip_path)

        # Extract zip
        print("  Extracting...")
        with zipfile.ZipFile(zip_path, "r") as zf:
            zf.extractall(tmp_dir)

        # Locate the Install/ directory inside the extracted archive
        # GitHub zips contain a top-level directory like ClaudeScaffold-main/
        extracted_dirs = [d for d in Path(tmp_dir).iterdir() if d.is_dir()]
        install_dir = None
        for d in extracted_dirs:
            candidate = d / "Install"
            if candidate.is_dir():
                install_dir = candidate
                break

        if install_dir is None:
            print(f"ERROR: Could not find Install/ directory in downloaded archive.", file=sys.stderr)
            sys.exit(1)

        print(f"  Source: {install_dir}")

        # Source paths
        src_claude_md = install_dir / "CLAUDE.md"
        src_claude_dir = install_dir / ".claude"
        src_scaffold_dir = install_dir / "scaffold"
        src_settings = src_claude_dir / "settings.local.json"

        # Target paths
        dst_claude_md = target / "CLAUDE.md"
        dst_claude_dir = target / ".claude"
        dst_scaffold_dir = target / "scaffold"
        dst_settings = dst_claude_dir / "settings.local.json"
        dst_skills_dir = dst_claude_dir / "skills"

        mode = "[DRY RUN] " if args.dry_run else ""
        print(f"\n{mode}Installing ClaudeScaffold into {target}\n")

        backups_created = []
        files_copied = 0
        skills_installed = 0

        # --- CLAUDE.md ---
        print("1. CLAUDE.md")
        if dst_claude_md.exists():
            backup = target / "CLAUDE.md.bak"
            if args.dry_run:
                log(f"  Would back up existing CLAUDE.md to CLAUDE.md.bak")
            else:
                shutil.copy2(dst_claude_md, backup)
                log(f"  Backed up existing CLAUDE.md to CLAUDE.md.bak")
            backups_created.append("CLAUDE.md.bak")
        copy_file(src_claude_md, dst_claude_md, args.dry_run, args.verbose)
        files_copied += 1

        # --- .claude/ directory ---
        print("\n2. .claude/ (skills + settings)")

        # Settings merge
        if dst_settings.exists():
            log("  Existing settings.local.json found — merging")
            merge_settings(dst_settings, src_settings, args.dry_run, args.verbose)
        else:
            copy_file(src_settings, dst_settings, args.dry_run, args.verbose)
        files_copied += 1

        # Skills — copy all scaffold skill dirs, preserve non-scaffold user skills
        src_skills_dir = src_claude_dir / "skills"
        if src_skills_dir.is_dir():
            for skill_dir in sorted(src_skills_dir.iterdir()):
                if not skill_dir.is_dir():
                    continue
                if skill_dir.name in EXCLUDE_DIRS:
                    continue
                # Collect files in this skill dir
                for src_file in sorted(skill_dir.rglob("*")):
                    if src_file.is_file() and not is_excluded(src_file.relative_to(src_skills_dir)):
                        rel = src_file.relative_to(src_skills_dir)
                        copy_file(src_file, dst_skills_dir / rel, args.dry_run, args.verbose)
                        files_copied += 1
                skills_installed += 1

        # --- scaffold/ directory ---
        print(f"\n3. scaffold/")
        if dst_scaffold_dir.exists():
            if not args.force:
                print(f"\n  ERROR: scaffold/ already exists at {dst_scaffold_dir}")
                print("  This directory may contain project-specific design data.")
                print("  Use --force to overwrite, or remove it manually first.")
                sys.exit(1)
            else:
                if args.dry_run:
                    log("  Would remove and replace existing scaffold/")
                else:
                    shutil.rmtree(dst_scaffold_dir)
                    log("  Removed existing scaffold/ (--force)")

        scaffold_files = collect_files(src_scaffold_dir, src_scaffold_dir)
        for src_file, rel_path in scaffold_files:
            copy_file(src_file, dst_scaffold_dir / rel_path, args.dry_run, args.verbose)
            files_copied += 1

        # --- Post-install verification ---
        print(f"\n4. Verification")
        if not args.dry_run:
            # Count installed skill dirs
            if dst_skills_dir.is_dir():
                installed_skills = [
                    d for d in dst_skills_dir.iterdir()
                    if d.is_dir() and d.name.startswith(SCAFFOLD_SKILL_PREFIX)
                ]
                skill_count = len(installed_skills)
            else:
                skill_count = 0

            # Verify key files
            key_files = [
                dst_claude_md,
                dst_scaffold_dir / "_index.md",
                dst_scaffold_dir / "WORKFLOW.md",
            ]
            missing = [str(f.relative_to(target)) for f in key_files if not f.exists()]

            if skill_count == EXPECTED_SKILLS and not missing:
                log(f"  All checks passed: {skill_count} skills, key files present")
            else:
                if skill_count != EXPECTED_SKILLS:
                    log(f"  WARNING: Expected {EXPECTED_SKILLS} scaffold skills, found {skill_count}")
                if missing:
                    log(f"  WARNING: Missing key files: {', '.join(missing)}")
        else:
            log(f"  Skipped (dry run)")

        # --- Summary ---
        print(f"\n{'=' * 50}")
        print(f"{mode}Installation summary:")
        print(f"  Source:           github.com/rmans/ClaudeScaffold ({args.branch})")
        print(f"  Files copied:     {files_copied}")
        print(f"  Skills installed: {skills_installed}")
        if backups_created:
            print(f"  Backups created:  {', '.join(backups_created)}")
        print(f"  Target:           {target}")
        print(f"\nNext step: Run /scaffold-new-design to start the pipeline")
        print()

    finally:
        # Cleanup temp directory
        shutil.rmtree(tmp_dir, ignore_errors=True)


if __name__ == "__main__":
    main()
