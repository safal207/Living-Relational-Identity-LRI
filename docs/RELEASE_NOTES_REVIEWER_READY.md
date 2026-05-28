# LRI v0.2-engineering-hygiene — Release Notes

**Date:** 2026-05-28

**Repository:** https://github.com/safal207/Living-Relational-Identity-LRI

## Scope

LRI defines non-operational invariants for protecting living identity, revisability, relational context, and human authority in human-system relationships.

This release adds engineering-hygiene hardening atop the v0.1-reviewer-ready baseline: automated quality gating, consistent code formatting, and expanded test coverage.

## What is included

### Engineering hygiene (new in v0.2)
- **GitHub Actions CI** (`.github/workflows/ci.yml`): automated lint, format, validate, test, and snapshot on push/PR
- **Makefile** (`Makefile`): targets `validate`, `test`, `snapshot`, `lint`, `format`, `check`, `all`
- **pre-commit config** (`.pre-commit-config.yaml`): ruff, black, check-yaml, trailing-whitespace, end-of-file-fixer
- **pyproject.toml** (`lri-reference/pyproject.toml`): modern packaging config, replaces `sys.path.append`
- **sys.path.append removed** from 12 files — all imports resolved via `pip install -e .`
- **ruff + black** applied across all 48 Python files; CI gates on both (no `continue-on-error`)
- **English-only** sweep: all comments and code in English (9 files updated)
- **Docs**: GLOSSARY.md, identity_freezing_examples.md, consent_drift_scenario.md, silent_authorship.md, lri_vs_privacy_consent.md

### Test expansion
- **API smoke tests** (`test_api_smoke.py`): 15 tests covering subject CRUD, relations, authority policy, observer state, cycle simulation
- **Adapter smoke tests** (`test_adapters_smoke.py`): 5 tests covering CLI adapater, multi-agent CLI adapter, UI adapter
- Total: 36 tests (31 existing + 5 new)

### Protocol surface (unchanged from v0.1)
- Identity schema: `protocol/lri/schema/identity.yaml`
- Lifecycle schema: `protocol/lri/schema/lifecycle.yaml`
- Relations schema: `protocol/lri/schema/relations.yaml`
- Rules: coherence, lifecycle, relationships (`protocol/lri/schema/rules/`)
- Events: created, updated, reflected (`protocol/lri/events/`)
- Error codes: LRI_001–LRI_010 (`protocol/lri/error/`)
- Examples: Alice scenarios (`protocol/lri/examples/`)

### Reference implementation (unchanged from v0.1)
- FastAPI server (port 8000) with subject, relations, authority, observer, economic, and cycle simulation endpoints
- Services: cycle engine, authority policy, drift monitor, metrics engine, observer, multi-agent engine, DMP writer, trust boundary, artifact registry, security
- Models: identity state, metrics, audit snapshot, decision record, economic artifact
- Storage: DMP store (JSONL)
- Adapters: CLI, UI, multi-agent CLI, multi-agent UI

### Documentation (unchanged from v0.1)
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
- 36 reference implementation tests

### Playground (unchanged from v0.1)
- `playground/playground.py` — interactive scenario runner
- `playground/snapshots_manager.py` — thread-safe snapshot management
- 5 YAML scenarios (Alice emerging, relation, active, mentor-attention, mentorship-collapse)

### Trust infrastructure (unchanged from v0.1)
- `LICENSE` — MIT
- `SECURITY.md` — vulnerability reporting
- `CONTRIBUTING.md` — contribution guidelines

## What LRI is not

See `docs/NON_CLAIMS.md` for the full scope boundary.

## Known limitations

- In-memory storage: all state is lost on server restart
- Hardcoded secrets: JWT key and passwords are in code (not production-ready)
- No Dockerfile or container release
- PR #28 (snapshot_diff.py) triaged but not merged
- pre-commit requires manual installation (`pre-commit install`)
- `make` not available natively on Windows (use Git Bash, WSL, or direct pytest commands)

## Next steps

- Production hardening: persistence, secrets management
- Property-based testing (Hypothesis) for identity state invariants
- Docker build and compose for one-command demo
- Integration with LTP, CML, DMP, PythiaLabs
