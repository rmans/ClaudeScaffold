# System Interfaces

> **Authority:** Rank 4
> **Layer:** Canon
> **Conforms to:** [design-doc.md](design-doc.md)

## Purpose

This document defines the contracts between game systems. Each interface specifies what data flows between systems and through which signals or methods — without specifying implementation details.

## Interface Contracts

<!-- Define each system-to-system interface. Format:

### [Source System] → [Target System]

**Signal/Method:** `signal_name` or `method_name`
**Data:** What is passed
**Contract:** What the caller can assume; what the receiver must guarantee

-->

*TODO: Define interface contracts as systems are designed.*

## Rules

1. Systems communicate only through interfaces defined here.
2. No system may reach into another system's internals.
3. Interface changes require an ADR (see [decisions/](../decisions/_index.md)).
