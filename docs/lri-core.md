# LRI Core Scope & Invariants

## 1. Core Definition (LRI)

Living-Relational-Identity (LRI) is a foundational protocol for establishing and maintaining persistent, verifiable identity continuity for autonomous agents and digital entities within dynamic environments. It decouples identity from specific temporal instantiations, anchoring it instead in a verifiable history of decisions, relationships, and authorized contexts. LRI provides a mechanism to cryptographically assert authority to act based on this historical continuity, rather than ephemeral session tokens or static keys alone. It formalizes the relational context of an identity, ensuring that an entity is defined not just by what it is, but by its established web of trust and interactions over time. This enables long-term traceability and accountability for autonomous systems operating across disparate platforms and timescales.

## 2. Problems LRI Solves

LRI addresses critical gaps in existing identity and autonomous systems:

1.  **Identity Fragmentation in Autonomous Operations**: Current systems treat agent instances as ephemeral processes. When an AI agent restarts or migrates, it often loses its "selfhood" and contextual authority, requiring costly re-verification and loss of operational continuity.
2.  **Lack of Accountable Agency**: In complex automated workflows, it is difficult to trace back a specific action to the precise authoritative state of an agent at the moment of decision. This creates liability gaps in enterprise environments where audit trails are mandatory.
3.  **Contextual Amnesia**: Agents often fail to carry the memory of their relational standing (trust levels, permissions granted by others) across sessions, leading to redundant negotiation phases and inefficient collaboration in multi-agent systems.

## 3. LRI Invariants

These invariants must remain true regardless of the underlying implementation language or environment:

*   **Identity Persists Beyond Instantiation**: An LRI identity remains valid and addressable regardless of the lifecycle state (running, paused, stopped) of the underlying computational process.
*   **Authority is Derived from Continuity**: The right to act is cryptographically proven by linking the current state to a valid chain of previous states and authorized transitions.
*   **Relationships are Intrinsic**: The identity definition includes the set of active relationships and contracts; an entity cannot be fully resolved without its relational context.
*   **Decisions are Non-Repudiable Attributes**: Significant state changes and decisions become part of the identity's immutable record, serving as the basis for future trust.

## 4. Explicit Non-Goals

To prevent scope creep and architectural confusion, LRI explicitly defines the following non-goals:

*   **Not a General Purpose Database**: LRI is not designed to store bulk application data or model arbitrary business logic unrelated to identity and authority.
*   **Not a Replacement for OAuth/OIDC**: LRI does not replace standard authentication protocols for human users or simple service access; it provides a deeper layer of agentic identity that may utilize these protocols as transport.
*   **Not a Consensus Mechanism**: LRI does not attempt to solve distributed consensus (like Proof-of-Work); it relies on underlying ledgers or trusted storage for ordering if strict global consensus is required.
*   **No "God Mode"**: LRI does not grant universal access; it strictly scopes authority to what has been explicitly granted and maintained through continuity.

## 5. Position in the Ecosystem

LRI serves as the foundational identity layer for the broader protocol ecosystem:

*   **LRI vs. LTP (Liminal Thread Protocol)**: LRI defines *who* is acting. LTP defines *how* they communicate and synchronize state. LRI provides the stable identity that LTP threads attach to.
*   **LRI vs. DMP (Decision Memory Protocol)**: LRI establishes the *agent* responsible for a decision. DMP provides the *storage and retrieval* mechanics for those decisions. LRI relies on DMP patterns to prove identity continuity through decision history.
