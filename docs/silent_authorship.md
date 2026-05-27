# Silent Authorship

Status: reviewer-facing concept definition.

See [NON_CLAIMS.md](NON_CLAIMS.md) for scope boundary. See [GLOSSARY.md](GLOSSARY.md) for term definitions.

LRI does not classify, score, diagnose, profile, or infer a person's true self.

---

## Definition

Silent authorship is the process by which a system silently becomes the author of a person's identity narrative — inferring, predicting, or filling in identity attributes, roles, or trajectories without the person's awareness, consent, or ability to revise.

## What it is not

- personalization or recommendation (though the boundary can be subtle)
- AI assistance where the person remains the author
- profile completion or data enrichment with explicit consent
- identity verification or authentication

## Core mechanism

Silent authorship typically follows this pattern:

1. The system observes behavior (clicks, choices, writing, timing)
2. It infers an attribute, label, or trajectory (persona, intent, capability, phase)
3. It acts on that inference (filtering, suggesting, routing, scoring)
4. The person is not informed that an inference was made
5. The person has no way to contest, revise, or opt out of the inference

At each step, the system moves from assistant to author.

## Example

A collaboration tool observes that Alice completes tasks reliably. It infers she is "executor-type." It begins routing execution tasks to her and filtering out strategic tasks. Alice never said she was an executor. She was not told she was classified as one. There is no interface to change this classification.

The system has silently authored a role for Alice in the collaboration narrative.

## Why it matters for LRI

Silent authorship violates three LRI invariants:

- **identity authority** — the person is no longer the author of their identity narrative
- **revisability** — the person cannot revise an inference they do not know exists
- **continuity** — the system-authored narrative can diverge from the person's living identity without detection

## What LRI does about it

LRI does not detect or prevent silent authorship. It defines invariants that make silent authorship visible and contestable:

- **authority checks** — are identity-relevant decisions attributable to the person or the system?
- **continuity tracking** — has the system's representation diverged from the person's self-representation?
- **observer endpoints** — can an external observer inspect the identity state chain for unexplained attributions?

These are protocol-level primitives, not production enforcement.

## Relationship to other concepts

| Concept | Relationship |
|---|---|
| identity freezing | Silent authorship is a mechanism that can cause freezing |
| consent drift | Silent authorship can occur without any consent violation at time of collection |
| optimization pressure | Systems optimize for smooth interaction, which favors silent authorship over explicit authoring |
