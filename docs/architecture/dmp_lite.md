# DMP-lite (Decision Memory Protocol integration)

## Overview
DMP-lite provides an append-only memory for decisions made by the LRI system.
It is designed to be immutable, non-optimizing, and strictly factual.

> DMP-lite records what was decided, not why it was right.

## Principles

1. **Append-only**: Decisions are never modified or deleted.
2. **Observation only**: It does not influence the agent's behavior or decision-making process.
3. **No Interpretation**: It stores raw facts (intention, decision, context).

## Architecture

### Components

*   `DecisionRecord`: Immutable data class representing a single decision.
*   `DMPStore`: Handles append-only storage (JSONL format).
*   `DMPWriter`: Service to record decisions into the store.

### Integration

The `DMPWriter` is integrated into the LRI cycle after a decision is made and before the cycle completes. It serves as an independent observer.

```python
# In cycle_engine.py
dmp_writer.record(
    agent_id=agent_id,
    intention=intention,
    decision=action,
    context="interaction"
)
```

## Data Format

Storage is in JSONL (JSON Lines) format, where each line is a valid JSON object representing a `DecisionRecord`.

```json
{"agent_id": "A1", "intention": "explore", "decision": "move_forward", "context": "interaction", "timestamp": "2023-10-27T10:00:00Z"}
```
