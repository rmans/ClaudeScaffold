#!/usr/bin/env python3
"""
Shared utility functions for scaffold orchestrators.

Provides mechanical operations that don't need Claude's judgment:
- complete: mark a document as Complete (status, rename, index)
- build_and_test: run build commands and test suites
- reorder_tasks: topological sort by dependencies
- These can be called as standalone commands or imported by orchestrators.

Commands:
    complete     Mark a scaffold doc as Complete.
    build-test   Run build and test commands.
    reorder      Topological sort tasks by dependency.
"""

import json
import os
import sys
import argparse
import re
import subprocess
from pathlib import Path
from datetime import datetime


TOOLS_DIR = Path(__file__).parent
SCAFFOLD_DIR = TOOLS_DIR.parent
PROJECT_ROOT = SCAFFOLD_DIR.parent


# ---------------------------------------------------------------------------
# Complete — Mark doc as Complete
# ---------------------------------------------------------------------------

def complete_doc(doc_path, scaffold_dir=None):
    """Mark a scaffold document as Complete. Updates status, renames file, updates index."""
    sd = Path(scaffold_dir) if scaffold_dir else SCAFFOLD_DIR
    abs_path = sd / doc_path if not Path(doc_path).is_absolute() else Path(doc_path)

    if not abs_path.exists():
        return {"status": "error", "message": f"File not found: {doc_path}"}

    content = abs_path.read_text(encoding="utf-8")

    # Update status field
    content = re.sub(
        r"(>\s*\*\*Status:\*\*)\s*\w+",
        r"\1 Complete",
        content
    )

    # Update Last Updated
    today = datetime.now().strftime("%Y-%m-%d")
    content = re.sub(
        r"(>\s*\*\*Last Updated:\*\*)\s*[\d-]+",
        rf"\1 {today}",
        content
    )

    # Add changelog entry
    changelog_match = re.search(r"(>\s*\*\*Changelog:\*\*)", content)
    if changelog_match:
        insert_pos = content.find("\n", changelog_match.end())
        if insert_pos != -1:
            entry = f"\n> - {today}: Status → Complete."
            content = content[:insert_pos] + entry + content[insert_pos:]

    abs_path.write_text(content, encoding="utf-8")

    # Rename file — change status suffix
    old_name = abs_path.name
    new_name = re.sub(r"_(draft|review|approved)", "_complete", old_name)
    if new_name != old_name:
        new_path = abs_path.parent / new_name
        abs_path.rename(new_path)
        abs_path = new_path

    # Update index
    index_files = list(abs_path.parent.glob("_index.md"))
    if index_files:
        index_path = index_files[0]
        index_content = index_path.read_text(encoding="utf-8")
        # Replace old filename with new
        index_content = index_content.replace(old_name, new_name)
        # Update status in index table if present
        index_content = re.sub(
            rf"(\|\s*\[?{re.escape(old_name.split('_')[0])}[^\|]*\|[^\|]*\|)\s*\w+\s*\|",
            rf"\1 Complete |",
            index_content
        )
        index_path.write_text(index_content, encoding="utf-8")

    return {
        "status": "ok",
        "file": str(abs_path.relative_to(sd)),
        "old_name": old_name,
        "new_name": new_name,
    }


# ---------------------------------------------------------------------------
# Build and Test — Run build commands
# ---------------------------------------------------------------------------

def build_and_test(files=None, skip_unit=False, skip_lint=False, project_root=None):
    """Run build and test commands. Returns pass/fail with details."""
    root = Path(project_root) if project_root else PROJECT_ROOT
    results = {"passed": True, "steps": [], "error": ""}

    # Detect build system
    if (root / "SConstruct").exists():
        # Godot/SCons build
        build_cmd = ["scons", "-j4"]
        result = _run_cmd(build_cmd, root)
        results["steps"].append({"name": "scons build", "passed": result["passed"], "output": result["output"][:500]})
        if not result["passed"]:
            results["passed"] = False
            results["error"] = result["output"][:1000]
            return results

    elif (root / "Cargo.toml").exists():
        result = _run_cmd(["cargo", "build"], root)
        results["steps"].append({"name": "cargo build", "passed": result["passed"], "output": result["output"][:500]})
        if not result["passed"]:
            results["passed"] = False
            results["error"] = result["output"][:1000]
            return results

    # Lint
    if not skip_lint:
        if (root / ".gdlintrc").exists() or (root / "game" / ".gdlintrc").exists():
            lint_files = files or []
            gd_files = [f for f in lint_files if f.endswith(".gd")]
            if gd_files:
                for gd_file in gd_files:
                    result = _run_cmd(["gdlint", gd_file], root)
                    results["steps"].append({"name": f"gdlint {gd_file}", "passed": result["passed"]})
                    if not result["passed"]:
                        results["passed"] = False
                        results["error"] += f"\ngdlint {gd_file}: {result['output'][:200]}"

    # Tests
    if not skip_unit:
        # GUT tests
        gut_dirs = list(root.glob("**/addons/gut")) + list(root.glob("**/addons/GUT"))
        if gut_dirs:
            result = _run_cmd(["godot", "--headless", "--script", "addons/gut/gut_cmdln.gd"], root)
            results["steps"].append({"name": "GUT tests", "passed": result["passed"], "output": result["output"][:500]})
            if not result["passed"]:
                results["passed"] = False
                results["error"] += f"\nGUT: {result['output'][:500]}"

        # Cargo tests
        if (root / "Cargo.toml").exists():
            result = _run_cmd(["cargo", "test"], root)
            results["steps"].append({"name": "cargo test", "passed": result["passed"]})
            if not result["passed"]:
                results["passed"] = False
                results["error"] += f"\ncargo test: {result['output'][:500]}"

    return results


def _run_cmd(cmd, cwd):
    """Run a shell command and return result."""
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=300, cwd=str(cwd))
        return {
            "passed": result.returncode == 0,
            "output": result.stdout + result.stderr,
        }
    except FileNotFoundError:
        return {"passed": False, "output": f"Command not found: {cmd[0]}"}
    except subprocess.TimeoutExpired:
        return {"passed": False, "output": f"Timeout after 300s: {' '.join(cmd)}"}


# ---------------------------------------------------------------------------
# Reorder Tasks — Topological sort by dependency
# ---------------------------------------------------------------------------

def reorder_tasks(task_dir=None, scaffold_dir=None):
    """Topological sort tasks by Depends on field. Returns ordered list."""
    sd = Path(scaffold_dir) if scaffold_dir else SCAFFOLD_DIR
    tdir = sd / (task_dir or "tasks")

    tasks = {}
    for task_file in sorted(tdir.glob("TASK-*-*.md")):
        content = task_file.read_text(encoding="utf-8")
        task_id_match = re.search(r"TASK-\d+", task_file.name)
        if not task_id_match:
            continue
        task_id = task_id_match.group()

        deps = []
        dep_match = re.search(r">\s*\*\*Depends on:\*\*\s*(.+)", content)
        if dep_match:
            dep_text = dep_match.group(1).strip()
            if dep_text != "—" and dep_text != "None":
                deps = re.findall(r"TASK-\d+", dep_text)

        tasks[task_id] = {
            "id": task_id,
            "file": str(task_file.relative_to(sd)),
            "depends_on": deps,
        }

    # Kahn's algorithm
    in_degree = {tid: 0 for tid in tasks}
    graph = {tid: [] for tid in tasks}

    for tid, task in tasks.items():
        for dep in task["depends_on"]:
            if dep in graph:
                graph[dep].append(tid)
                in_degree[tid] += 1

    queue = sorted([tid for tid, deg in in_degree.items() if deg == 0])
    ordered = []

    while queue:
        node = queue.pop(0)
        ordered.append(tasks[node])
        for neighbor in sorted(graph.get(node, [])):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Cycle detection
    remaining = [tasks[tid] for tid in tasks if tid not in [t["id"] for t in ordered]]
    for r in remaining:
        r["_cycle"] = True
        ordered.append(r)

    return ordered


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Scaffold utility functions")
    subparsers = parser.add_subparsers(dest="command")

    # complete
    p_comp = subparsers.add_parser("complete", help="Mark a doc as Complete")
    p_comp.add_argument("doc", help="Document path relative to scaffold/")

    # build-test
    p_build = subparsers.add_parser("build-test", help="Run build and tests")
    p_build.add_argument("--files", nargs="*", default=[], help="Files to lint")
    p_build.add_argument("--skip-unit", action="store_true")
    p_build.add_argument("--skip-lint", action="store_true")

    # reorder
    p_reorder = subparsers.add_parser("reorder", help="Topological sort tasks")
    p_reorder.add_argument("--task-dir", default="tasks")

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(1)

    if args.command == "complete":
        result = complete_doc(args.doc)
        print(json.dumps(result, indent=2))
    elif args.command == "build-test":
        result = build_and_test(args.files, args.skip_unit, args.skip_lint)
        print(json.dumps(result, indent=2))
    elif args.command == "reorder":
        result = reorder_tasks(args.task_dir)
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
