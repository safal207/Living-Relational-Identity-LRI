# LRI Reviewer Path

Status: reviewer-facing navigation path.

This document gives a short reading path for OpenAI, grant, and external reviewers.

## One-sentence summary

LRI defines non-operational invariants for protecting living identity in human-system relationships from optimization, capture, silent substitution, and continuity loss.

## Core thesis

```text
Human identity should not be collapsed into a fixed profile, score, prediction target, or system-owned narrative.
```

LRI exists to protect revisability, relational context, and the human's authority to continue becoming over time.

## If you only have 5 minutes

Read:

1. `README.md`
2. `docs/NON_CLAIMS.md`
3. `docs/PORTFOLIO_RELATIONSHIP.md`
4. `docs/safety/identity_governance_threat_model.md`
5. `VALIDATION_RESULTS.md`

Then answer:

```text
Does LRI clearly protect human revisability and relational identity boundaries without becoming profiling, classification, therapy, or automated decisioning about humans?
```

## Recommended reviewer sequence

1. Start with `README.md` for problem framing and validation commands.
2. Read `docs/NON_CLAIMS.md` to confirm scope boundaries.
3. Read `docs/PORTFOLIO_RELATIONSHIP.md` to understand how LRI relates to PythiaLabs, LTP, CML, and DMP.
4. Read `docs/safety/identity_governance_threat_model.md` for identity-governance risks.
5. Read `docs/SECURITY_MODEL.md` and `docs/architecture/lri-trust-model.md` for security and trust framing.
6. Inspect `protocol/lri/schema/identity.yaml` and `protocol/lri/schema/lifecycle.yaml` for protocol surface.
7. Inspect `lri-reference/tests/` and `VALIDATION_RESULTS.md` for current validation evidence.

## What LRI evaluates

LRI focuses on identity-boundary risks in human-system relationships.

It asks:

```text
Is the system preserving the human's revisability?
Is relational context being respected?
Is the system silently becoming the author of the person's identity narrative?
Is memory persistence still aligned with consented meaning?
Is the person being compressed into a fixed profile or optimization target?
```

## What LRI is distinct from

| System type | Usually asks | LRI asks |
|---|---|---|
| Profiling | What stable traits can be inferred? | Is the human being reduced to a fixed representation? |
| Personalization | What should the system optimize for this user? | Is optimization preserving revisability and refusal? |
| Consent records | Was consent given at collection time? | Has meaning, context, risk, or relationship changed? |
| Identity verification | Is this person who they claim to be? | Is living identity being protected from capture and substitution? |
| Therapy/diagnosis | What is the person's condition? | Not in scope. LRI must not diagnose or treat. |
| Social scoring | How should a person be ranked or treated? | Not in scope. LRI must not score people. |

## Fast validation

From the repository root:

```bash
python scripts/validate_project.py
python scripts/generate_validation_results.py
```

Reference implementation tests:

```bash
cd lri-reference
python -m pytest -q
```

Expected current result:

```text
validation passes
tests pass
tracked validation snapshot is current
```

## Current evidence anchors

- README: `README.md`
- Non-claims: `docs/NON_CLAIMS.md`
- Portfolio relationship: `docs/PORTFOLIO_RELATIONSHIP.md`
- Security model: `docs/SECURITY_MODEL.md`
- Trust model: `docs/architecture/lri-trust-model.md`
- Threat model: `docs/safety/identity_governance_threat_model.md`
- Identity schema: `protocol/lri/schema/identity.yaml`
- Lifecycle schema: `protocol/lri/schema/lifecycle.yaml`
- Reference implementation: `lri-reference/`
- Validation snapshot: `VALIDATION_RESULTS.md`

## Reviewer questions

A useful review should answer:

1. Is LRI clearly scoped as protective boundary reasoning rather than profiling?
2. Are non-claims explicit enough?
3. Does the repository contain concrete protocol and reference artifacts?
4. Are validation commands clear?
5. How does LRI relate to the rest of the portfolio?
6. What evidence would make LRI more fundable?

## Portfolio relationship

LRI is one layer in a broader trustworthy-agent evidence architecture:

```text
PythiaLabs — pre-execution evidence gates
LTP — path-level trace/replay/admissibility
CML — causal permission and responsibility lineage
DMP — decision memory and irreversibility governance
LRI — living identity and relational invariants
```

LRI's specific role:

```text
Protect human revisability, identity authority, relational context, and continuity boundaries.
```

## Funding interpretation

LRI is most fundable as a narrow human-boundary governance primitive:

```text
non-operational invariants for protecting living identity and revisability in human-system relationships
```

It should not be presented as an identity classifier, profiling system, diagnostic tool, therapy system, or automated decisioning system.
