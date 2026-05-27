# LRI Glossary

Status: reviewer-facing terminology reference.

See [NON_CLAIMS.md](NON_CLAIMS.md) for the full scope boundary.

LRI is a **human-boundary protocol**. It does not classify, score, diagnose, profile, or infer a person's true self.

---

### living relational identity

**Definition:** Identity that is not fixed — it continues to become through relationships, context, and self-revision over time.

**What it is not:** A stable profile, a static trait set, a system-owned representation of who a person really is.

**Example:** Alice's identity in the system is defined by her current relational context (peers, mentor, phase), not by a permanent label. She can enter a new phase, change relations, and revise her narrative without losing continuity.

---

### identity freezing

**Definition:** The process by which a system reduces a living person to a fixed representation — a label, score, category, or profile that resists revision.

**What it is not:** Accurate modeling, personalization, user profiling, diagnosis, or identity verification.

**Example:** A system assigns Alice a "collaborator" persona based on early behavior and continues to filter her options through that lens even after her role changes.

---

### revisability

**Definition:** The ability of a person to revise their identity narrative, role, relationships, or self-understanding without losing continuity or being treated as inconsistent.

**What it is not:** Profile editing, data correction, account settings, or identity reset.

**Example:** Alice transitions from "emerging" to "active" phase. The system does not flag this as an anomaly or treat her as a different user.

---

### relational context

**Definition:** The set of relationships, roles, and social positions that shape a person's current identity state.

**What it is not:** A social graph, a friend list, a network map for ranking or targeting.

**Example:** Alice's identity includes her mentor relation, peer connections, and group membership. These are part of who she is in the system, not just metadata.

---

### identity authority

**Definition:** A person's right to define, revise, and assert their own identity without the system silently overriding or substituting its own representation.

**What it is not:** Authentication, access control, identity verification, or proof of who someone really is.

**Example:** When the system detects a coherence shift in Alice's trajectory, it records the change but does not automatically rewrite her identity without her authority.

---

### silent authorship

**Definition:** The system silently becoming the author of a person's identity narrative — inferring, predicting, or filling in identity attributes without the person's awareness or consent.

**What it is not:** Personalization, recommendation, AI assistance, or profile completion.

**Example:** The system infers that Alice is "ready for leadership" based on her metrics and begins routing leadership opportunities to her before she has expressed any such intent.

---

### consent drift

**Definition:** The phenomenon where consent given at one point in time loses its meaning as context, relationship, risk, or use changes.

**What it is not:** Consent revocation, data deletion, privacy policy violation, or clinical concept of capacity.

**Example:** Alice agreed to share her trajectory data for "improving collaboration." Later, the system uses that same data to rank her against peers. The original consent has drifted.

---

### memory persistence beyond consent

**Definition:** Data, inferences, or identity artifacts that remain in the system after their originally consented meaning or purpose has expired.

**What it is not:** Data retention, backup policy, GDPR compliance, or storage management.

**Example:** Alice's early-phase trajectory data is still used to evaluate her even after she has explicitly moved to a different context and role.

---

### identity capture

**Definition:** When a system's representation of a person becomes the authoritative version — overriding, constraining, or replacing the person's own living identity.

**What it is not:** Identity theft, account takeover, impersonation, or fraud.

**Example:** The system's profile of Alice is used by downstream services to make decisions about her. She has no way to contest or revise that profile without breaking continuity.

---

### optimization pressure

**Definition:** System incentives that push a person toward behaviors, roles, or narratives that maximize a system metric rather than preserving the person's own trajectory.

**What it is not:** Manipulation, nudging, coercion, or addictive design (though it may correlate).

**Example:** The system rewards coherence by making Alice's interactions smoother when she repeats established patterns — discouraging exploration or self-revision.

---

### self-creation

**Definition:** A person's ongoing capacity to shape their own identity narrative through choices, relations, and revision — not merely as a response to system feedback.

**What it is not:** Profile customization, avatar creation, preference setting, or personalization.

**Example:** Alice chooses to seek a mentor and enter a new phase. This is her self-creation, not a system-suggested optimization.

---

### continuity boundary

**Definition:** The invariant that identity persists across time, context shifts, and state changes — each new state links cryptographically to the previous one, preserving a non-rewritable chain.

**What it is not:** A session token, a user ID, a login session, or a database primary key.

**Example:** Every change to Alice's identity produces a new state linked to the previous one by a SHA-256 hash. The chain cannot be broken or rewritten without detection.

---

### human-boundary protocol

**Definition:** A protocol designed to protect human autonomy, revisability, relational context, and identity authority from being compressed, captured, or optimized by a system.

**What it is not:** An identity platform, a user model, a profiling system, a consent management tool, or a compliance framework.

**Example:** LRI is a human-boundary protocol. It does not claim to know who Alice is — it only preserves the conditions under which she can continue to become who she is.
