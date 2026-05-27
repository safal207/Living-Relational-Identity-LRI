# Consent Drift — Scenario

Status: reviewer-facing concept illustration.

See [NON_CLAIMS.md](NON_CLAIMS.md) for scope boundary. See [GLOSSARY.md](GLOSSARY.md) for term definitions.

LRI does not replace, implement, or certify consent mechanisms. It highlights a structural risk: consent given at one point can lose its meaning as context, relationship, risk, or use changes.

---

## Scenario: Long-term AI memory

A system offers a "memory" feature: it remembers user preferences, history, and goals to personalize interactions over time.

### Phase 1 — Initial consent

Alice opts in. She understands:

- the system will remember her name, goals, and preferences
- the memory is used to personalize her experience
- she can delete specific memories or reset at any time

Consent is clear, specific, and当下的.

### Phase 2 — Feature expansion

Six months later, the system adds:

- mood inference based on interaction patterns
- peer comparison based on goal progress
- predictive suggestions based on memory history

These features were not described at consent time. They are built on the same memory data. Alice was not re-consented.

### Phase 3 — Context shift

Alice's life circumstances change. Her goals, relationships, and priorities are different. The system continues to use her historical memory to predict her needs — but the predictions are based on a context she no longer inhabits.

The system has no way to know that her context has shifted. Consent was never contextualized.

### Phase 4 — Silent repurposing

The system's memory data is used to train a behavioral model. Alice is not informed. The model is used to rank users by "engagement reliability" — a score Alice never consented to.

The original consent ("improve my experience") has drifted so far from the actual use that it is no longer meaningful.

---

## What this scenario illustrates

Consent drift is not a failure of consent mechanisms. It is a structural property of long-term human-system relationships:

- consent is momentary; relationships are continuous
- context changes; consent does not automatically update
- data persists; its meaning and use evolve
- systems optimize; drift is operationally useful

## What LRI contributes

LRI does not solve consent drift. It makes drift visible by tracking:

- continuity boundaries (is this still the same identity context?)
- relational context (have relationships changed since consent?)
- authority (does the person still author their narrative?)

This visibility does not replace consent processes. It creates conditions under which drift can be surfaced.

## What this scenario is not

- not a legal analysis of consent law
- not a claim that any specific system exhibits this pattern
- not a consent management framework
- not a replacement for consent processes, human review, or legal advice
