# LRI Reference Implementation Skeleton

This is a minimal reference skeleton for the Living-Relational-Identity (LRI) protocol.

## Structure

*   `api/`: Python modules for Subject CRUD, Relations, and Authority checks.
*   `examples/`: JSON reference payloads for Subjects, LTP events, and DMP records.

## How to run

1.  Ensure you have Python 3.10+ installed.
2.  Navigate to the `lri-reference` directory.
3.  Import modules from `api/` into your Python script or console.

### Example Usage

Run this from inside the `lri-reference/` directory:

```python
from api.subject import create_subject, get_subject
from api.relations import link_subject

# Create a subject
alice = create_subject("subj-001", {"name": "Alice", "role": "agent"})
print(alice)

# Link subjects
link_subject("subj-001", "subj-002", "PEER")
```

### PoC Integration (LTP & DMP)

To see a full demonstration of LRI integrating with LTP (Liminal Thread Protocol) events and DMP (Decision Memory Protocol) records, run the PoC script:

```bash
python examples/poc_integration.py
```

This script demonstrates:
1.  **Subject Creation**: Initializing an LRI identity.
2.  **LTP Integration**: Linking a communication event to the identity.
3.  **DMP Integration**: Linking a decision record to the identity.
4.  **Verification**: Checking authority and continuity invariants.
5.  **Traceability**: Listing all relational contexts for the subject.

## Requirements

No external dependencies are required for this skeleton.
