# Tools — Index

> **Purpose:** Scripts and utilities that support the scaffold pipeline.

## Tools

| File | Description |
|------|-------------|
| `doc-review.py` | Adversarial document reviewer — multi-provider (OpenAI / Anthropic) |
| `review_config.json` | Configuration for doc-review.py (provider, model, temperature) |
| `validate-refs.py` | Cross-reference validator — checks referential integrity across all scaffold docs |

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
