---
name: scaffold-validate
description: Run cross-reference validation across all scaffold documents. Reports broken references, missing registrations, and glossary violations.
allowed-tools: Read, Bash, Grep, Glob
---

# Validate Cross-References

Run the cross-reference validation script and report issues.

## Steps

### 1. Run the Validator

1. **Run** `python scaffold/tools/validate-refs.py --format json` from the project root.
2. **Parse the JSON output** into a list of issues.

### 2. Categorize Results

Group issues by check type:

| Check | What It Validates |
|-------|------------------|
| `system-ids` | Every SYS-### reference points to a registered system |
| `authority-entities` | Entity authorities match authority.md owners |
| `signals-systems` | Signal emitters/consumers are registered systems |
| `interfaces-systems` | Interface sources/targets are registered systems |
| `states-systems` | State machine authorities are registered systems |
| `glossary-not-terms` | No non-theory doc uses a term from the glossary NOT column |
| `bidirectional-registration` | systems/_index.md and design-doc.md System Design Index match |
| `spec-slice` | Every spec appears in at least one slice |
| `task-spec` | Every task references a valid spec |

### 3. Report

Present results as a summary table:

| Check | Status | Issues |
|-------|--------|--------|
| System IDs | PASS/FAIL | count |
| ... | ... | ... |

Then list each failing issue with file, line, and message.

If all checks pass, report: **All cross-references validated. No issues found.**

### 4. Suggest Fixes

For each failing check, suggest the specific edit needed:
- Missing system registration → "Register SYS-### in systems/_index.md"
- Authority mismatch → "Update entity-components.md Authority column or authority.md Owning System"
- Glossary violation → "Replace [NOT term] with [canonical term] in [file]"
- Missing spec-slice link → "Add SPEC-### to a slice's Specs Included table"
- Missing task-spec link → "Verify TASK-### references a valid SPEC-### in its Implements field"

## Rules

- **Read-only analysis.** This skill reports issues but does not fix them. Use `/scaffold-update-doc` to apply fixes.
- **Run from project root.** The script expects `scaffold/` to be in the current directory.
- **If the script fails**, check that Python 3 is available and `scaffold/tools/validate-refs.py` exists.
- **Handle empty scaffold gracefully.** A fresh scaffold with no content should produce warnings, not errors.
