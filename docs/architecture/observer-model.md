# Observer Model & Audit Interface

## 1. Overview

The Observer is a core architectural component of LRI designed to provide **Identity Observability without Control**. It enables external parties (auditors, regulators, users) to verify the state, continuity, and behavior of an autonomous agent without having the authority to mutate that state or intervene in real-time execution.

> "To observe is not to control."

## 2. Role of the Observer

The Observer is:
*   **Read-Only**: It cannot change state, approve transactions, or block actions.
*   **Verifiable**: It provides cryptographic proofs (continuity hashes) that the observed state is authentic.
*   **Non-Invasive**: Observation does not pause or alter the agent's cognitive cycle.

## 3. Audit Snapshot

The primary artifact of the Observer is the `AuditSnapshot`. It is a timestamped, cryptographically anchored report of an identity at a specific moment in time.

### Structure
*   **Subject ID**: Who is being observed.
*   **Timestamp**: When the observation occurred.
*   **Continuity Hash**: The cryptographic tail of the identity's decision chain.
*   **Drift Score**: Quantitative measure of deviation from original intent.
*   **Authority Claims**: What the agent is currently authorized to do.

## 4. Trust & Ethics

The Observer model implements the principle of **Transparent Autonomy**.

*   **For the Agent**: It guarantees that being audited does not mean being commandeered.
*   **For the Operator**: It provides a "Check Engine Light" (Drift Score) and a "Black Box" (Continuity Chain).
*   **For the Public**: It offers proof that the agent is operating within defined boundaries (Authority Policy).

## 5. Interface

The Observer exposes a standardized API:
*   `GET /observer/subject/{id}/snapshot`: Full state report.
*   `GET /observer/subject/{id}/continuity`: Chain verification.
*   `GET /observer/subject/{id}/drift`: Behavioral analysis.
