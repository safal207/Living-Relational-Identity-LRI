# LRI vs. State Sourcing / Event Sourcing

While LRI shares similarities with Event Sourcing, it makes specific architectural choices that distinguish it as an Identity Protocol.

## 1. Event Sourcing (Generic)

*   **Focus**: Reconstruct state from history.
*   **Events**: Granular (e.g., `FieldUpdated`, `ItemAdded`).
*   **Truth**: The event log is the source of truth.

## 2. LRI (Identity Protocol)

*   **Focus**: Continuity and Authority.
*   **Events**: Semantic Steps (e.g., `LRI_UPDATED` with `Intent`).
*   **Truth**: The **Cryptographic Chain** is the source of truth.

### Key Differences

| Feature | Event Sourcing | LRI |
| :--- | :--- | :--- |
| **Atomicity** | Technical Transaction | Semantic Decision |
| **Verification** | App Logic | Cryptographic Proof |
| **Drift** | Not tracked | Core metric (Drift Monitoring) |
| **External View** | API Projection | Canonical Read API |
| **Delete** | Compensating Event | Termination State (No Erasure) |

## The "Skeleton" Concept

The `protocol/` directory defines the "Shape" of LRI.
- **Schema**: The Noun (Identity).
- **Events**: The Verbs (Created, Updated).
- **Diff**: The Adverb (How it changed).

This separation allows LRI to be "Infrastructure Agnostic". It can run on:
- SQL Database
- Blockchain / DLT
- Git Repo
- IPFS
