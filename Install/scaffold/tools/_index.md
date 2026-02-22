# Tools — Index

> **Purpose:** Scripts and utilities that support the scaffold pipeline.

## Tools

| File | Description |
|------|-------------|
| `doc-review.py` | Two-loop AI document review and refinement process |

## doc-review.py

Runs an iterative review process where Claude and OpenAI discuss a document, reach agreement on changes, and apply them.

### Loop Structure

```
Outer Loop (N iterations, default 1)
└── Inner Loop
    ├── Claude reviews the document
    ├── OpenAI reviews the document
    ├── Claude and OpenAI discuss until agreement
    └── Agreed changes are applied to the document
```

### Usage

```
python doc-review.py <document-path>
python doc-review.py <document-path> --iterations 3
```

### Arguments

| Argument | Required | Default | Description |
|----------|----------|---------|-------------|
| `document-path` | Yes | — | Path to the markdown document to review |
| `--iterations`, `-n` | No | `1` | Number of outer loop iterations to run |

### Status

**Not yet implemented.** This index describes the intended behavior.
