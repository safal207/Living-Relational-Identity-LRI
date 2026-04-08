# Living Relational Identity (LRI)

LRI defines non-operational invariants for protecting living identity in human-system relationships from optimization, capture, silent substitution, and continuity loss.

The central idea is that identity should not be treated as a fixed profile, a static score, or a target for optimization. Identity remains living only if systems preserve revisability, relational context, and the human's authority to continue becoming over time.

## Problem

Many systems model humans as stable, optimizable objects. That creates recurring risks such as:

- identity freezing through static labeling
- silent transition from assistance to authorship
- memory persistence beyond consented scope
- optimization against hesitation, refusal, or ambiguity
- profiling that becomes destiny
- relational drift that is operationally useful but existentially harmful

These are not only product-design issues. They are failures of identity governance.

## What LRI Does

LRI provides a protocol and reference implementation for reasoning about identity continuity, authority, drift, and relational change without collapsing a living person into a fixed machine-readable essence.

The project currently includes:

- protocol-level identity and lifecycle schemas
- trust and security model docs
- a reference implementation with observer, drift, authority, security, and metrics services
- API and adapter skeletons
- playground scenarios and snapshots
- tests for continuity, metrics, observer behavior, DMP-lite integration, and security

## Why This Matters for Safety

A system can be operationally useful while still being identity-damaging.

Examples:

- a system infers who a person "really is" from past behavior
- a profile starts deciding treatment or opportunity
- a memory layer outlives consent boundaries
- an assistant becomes an author without an explicit boundary crossing
- drift is measured only for operational control, not for relational harm

LRI is useful because it treats these as governance and protocol problems, not only product bugs.

## Current Artifact

This repository already contains a concrete artifact, not only philosophical framing:

- protocol definitions in `protocol/`
- security and trust model documentation in `docs/`
- a Python reference implementation in `lri-reference/`
- playground scenarios and trajectory snapshots in `playground/`
- validation-facing assets and tests

Key files:

- `docs/SECURITY_MODEL.md`
- `docs/architecture/lri-trust-model.md`
- `protocol/lri/schema/identity.yaml`
- `protocol/lri/schema/lifecycle.yaml`
- `lri-reference/services/authority_policy.py`
- `lri-reference/services/drift_monitor.py`
- `lri-reference/services/observer.py`
- `lri-reference/tests/`
- `VALIDATION_RESULTS.md`

## Threat Model Fit

LRI is most relevant for failures such as:

- identity spoofing without continuity grounding
- history revisionism and loss of causal identity memory
- drift beyond declared trust boundaries
- optimization against agency, refusal, or revisability
- substitution of self-creation by automated system narratives

For broader framing, see [docs/safety/identity_governance_threat_model.md](docs/safety/identity_governance_threat_model.md).

## Validation Surface

The repository now exposes a simple root-level validation path:

- reference implementation tests
- deterministic project validation snapshot
- tracked validation results in [VALIDATION_RESULTS.md](VALIDATION_RESULTS.md)

Run:

```bash
python scripts/validate_project.py
python scripts/generate_validation_results.py
```

## Quick Start

Reference implementation tests:

```bash
cd lri-reference
python -m pytest -q
```

Explore the playground:

```bash
cd playground
python playground.py
```

## Bottom Line

LRI is not trying to optimize identity.

It is trying to define what must remain protected if a human identity is to stay living, revisable, and relational in the presence of systems that would otherwise compress it.