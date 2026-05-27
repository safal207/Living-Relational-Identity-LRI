# LRI v0.1-reviewer-ready — Release Notes

**Date:** 2026-05-27

**Repository:** https://github.com/safal207/Living-Relational-Identity-LRI

## Scope

LRI defines non-operational invariants for protecting living identity, revisability, relational context, and human authority in human-system relationships.

This release marks the reviewer-ready baseline for external evaluation.

## What is included

### Protocol surface
- Identity schema: `protocol/lri/schema/identity.yaml`
- Lifecycle schema: `protocol/lri/schema/lifecycle.yaml`
- Relations schema: `protocol/lri/schema/relations.yaml`
- Rules: coherence, lifecycle, relationships (`protocol/lri/schema/rules/`)
- Events: created, updated, reflected (`protocol/lri/events/`)
- Error codes: LRI_001–LRI_010 (`protocol/lri/error/`)
- Examples: Alice scenarios (`protocol/lri/examples/`)

### Reference implementation
- FastAPI server (port 8000) with subject, relations, authority, observer, economic, and cycle simulation endpoints
- Services: cycle engine, authority policy, drift monitor, metrics engine, observer, multi-agent engine, DMP writer, trust boundary, artifact registry, security
- Models: identity state, metrics, audit snapshot, decision record, economic artifact
- Storage: DMP store (JSONL)
- Adapters: CLI, UI, multi-agent CLI, multi-agent UI

### Documentation
- `README.md` — problem framing, quick start, validation commands
- `docs/NON_CLAIMS.md` — explicit scope boundaries
- `docs/REVIEWER_PATH.md` — recommended reading sequence
- `docs/PORTFOLIO_RELATIONSHIP.md` — LRI in broader ecosystem
- `docs/SECURITY_MODEL.md` — security and trust principles
- `docs/safety/identity_governance_threat_model.md` — identity governance threat model
- `docs/architecture/` — trust model, observer model, drift metrics flow, DMP-lite adapter

### Validation
- `scripts/validate_project.py` — project-level validation
- `scripts/generate_validation_results.py` — validation snapshot generator
- `VALIDATION_RESULTS.md` — current validation snapshot
- 16 reference implementation tests (continuity, authority, observer, metrics, DMP-lite, security)

### Playground
- `playground/playground.py` — interactive scenario runner
- `playground/snapshots_manager.py` — thread-safe snapshot management
- 5 YAML scenarios (Alice emerging, relation, active, mentor-attention, mentorship-collapse)

### Trust infrastructure
- `LICENSE` — MIT
- `SECURITY.md` — vulnerability reporting
- `CONTRIBUTING.md` — contribution guidelines

## What LRI is not

See `docs/NON_CLAIMS.md` for the full scope boundary. In brief, LRI is not:

- an identity classifier
- a profiling system
- personality scoring
- diagnosis
- therapy
- mental-health assessment
- social credit
- risk scoring of people
- automated decisioning about humans
- prediction of a person's true self

## Known limitations

- In-memory storage: all state is lost on server restart
- Hardcoded secrets: JWT key and passwords are in code (not production-ready)
- `sys.path.append()` in multiple files — module structure pending refactor
- Limited test coverage: 16 tests, no API route tests, no adapter tests
- No CI/CD, Docker, or pre-commit automation
- PR #28 (snapshot_diff.py) triaged but not merged

## Next steps

- Production hardening: persistence, secrets management, proper import structure
- Expanded test coverage: API routes, adapters, property-based testing
- CI/CD pipeline: GitHub Actions, pre-commit, Docker
- Integration with LTP, CML, DMP, PythiaLabs
