# LRI Trust Model

## 1. Overview
The LRI (Living Relational Identity) Trust Model defines the security and reliability guarantees provided by the protocol. It shifts the trust anchor from "admin privileges" to "cryptographic continuity".

## 2. Threat Model

### 2.1. In Scope (Mitigated Threats)
*   **Identity Spoofing**: An actor claiming to be an agent without the correct state chain history.
    *   *Mitigation*: Continuity Proofs (Hash Chain).
*   **History Revisionism**: Altering past decisions to change current context.
    *   *Mitigation*: Immutable DMP (Decision Memory Protocol) & Hash Chaining.
*   **Drift/Rogue Agents**: Agents deviating significantly from their intended trajectory.
    *   *Mitigation*: Authority Policy Engine (Drift Thresholds).

### 2.2. Out of Scope (Accepted Risks)
*   **Endpoint Compromise**: If the agent's private keys or runtime environment is fully compromised, LRI cannot prevent authorized actions initiated by the attacker (until drift is detected).
*   **Oracle Problem**: LRI trusts the input data (decisions/intentions) provided by the agent's integration layer. It verifies *consistency*, not *truth*.

## 3. Assumptions

1.  **Storage Integrity**: The underlying storage for DMP and Identity State is reliable. LRI ensures tamper-evidence, but not tamper-proof storage (unless on blockchain).
2.  **Clock Synchronization**: Timestamps are reasonably accurate (though logical ordering via hash chains takes precedence).
3.  **Single Writer**: For a given identity, operations are serialized (LRI Cycle is sequential per identity).

## 4. Trust Boundary

LRI operates strictly as a **Governance & Identity Layer**, not an **Execution Layer**.

*   **LRI DOES**: Sign off on state changes, verify authority, track drift.
*   **LRI DOES NOT**: Execute code, make API calls to external systems, or interpret natural language.

> "LRI is the passport control, not the traveler."
