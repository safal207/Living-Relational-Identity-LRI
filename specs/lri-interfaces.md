# LRI Core Interfaces

This document defines the formal interfaces for Living-Relational-Identity (LRI). These interfaces allow external protocols and systems to interact with the LRI core, ensuring identity continuity, relational context management, and authority verification.

## 1. Subject Management (CRUD)

These methods manage the lifecycle of an LRI Subject. A "Subject" is an autonomous agent or digital entity.

### `createSubject`
Initializes a new LRI identity anchor.
*   **Invariant Enforced**: *Identity Persists Beyond Instantiation*. Creates the genesis state of the identity chain.
*   **Input**: `CreateSubjectRequest` (Initial public keys, genesis metadata)
*   **Output**: `Subject` (The created identity object with a unique LRI ID)

### `getSubject`
Retrieves the current state and metadata of a subject.
*   **Input**: `subjectId` (UUID or DID)
*   **Output**: `Subject`

### `updateSubject`
Updates subject state (e.g., key rotation, metadata update).
*   **Invariant Enforced**: *Decisions are Non-Repudiable Attributes*. Every update appends to the immutable history.
*   **Input**: `UpdateSubjectRequest` (Must include cryptographic proof signed by the current key)
*   **Output**: `Subject` (Updated state)

### `deleteSubject`
Marks a subject as terminal or archived.
*   **Invariant Enforced**: *Identity Continuity*. The record is not erased; the identity is transitioned to a "Terminated" state, preserving its history for auditability.
*   **Input**: `subjectId`, `proof` (Authorization signature)
*   **Output**: `boolean` (Success status)

---

## 2. Relationship Management

These methods define the "Relational" aspect of LRI, managing the web of trust and context.

### `linkSubject`
Establishes a directed relationship between the acting subject and a target.
*   **Invariant Enforced**: *Relationships are Intrinsic*. The identity's context is modified by this link.
*   **Input**:
    *   `sourceId`: The LRI ID of the actor.
    *   `targetId`: The LRI ID of the entity being linked to.
    *   `relationType`: (e.g., "OWNER", "PEER", "CHILD", "AUDITOR")
    *   `proof`: Signature from `sourceId`.
*   **Output**: `Relationship`

### `unlinkSubject`
Removes or archives an active relationship.
*   **Input**: `sourceId`, `targetId`, `relationType`, `proof`
*   **Output**: `boolean` (Success status)

### `listRelations`
Retrieves the active relational context for a subject.
*   **Input**: `subjectId`, `filter` (optional type filter)
*   **Output**: `Relationship[]`

---

## 3. Authority & Continuity

These methods are the primary integration points for external systems (LTP, DMP) to verify an agent.

### `checkAuthority`
Verifies if a subject is authorized to perform a specific action within a given context.
*   **Invariant Enforced**: *Authority is Derived from Continuity*. Authority is not static; it is calculated based on current state, active relationships, and history.
*   **Input**:
    *   `subjectId`: The agent attempting the action.
    *   `action`: The operation being attempted (e.g., "COMMIT_CODE", "APPROVE_BUDGET").
    *   `context`: The target resource or environment.
*   **Output**: `AuthorityResult` (Allowed/Denied + Reason)

### `validateContinuity`
Verifies the cryptographic integrity of a subject's history chain.
*   **Invariant Enforced**: *Identity Continuity across system changes*. Ensures the current instance is a valid successor of the previous instance.
*   **Input**:
    *   `subjectId`: The identity to verify.
    *   `presentedStateHash`: The hash of the state the agent claims to hold.
*   **Output**: `ValidationResult` (Valid/Invalid, LastKnownBlockHeight)
