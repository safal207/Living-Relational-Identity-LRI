# LRI v0.3-evidence-expansion — Release Notes

**Date:** 2026-05-28

**Repository:** https://github.com/safal207/Living-Relational-Identity-LRI

## Scope

LRI defines non-operational invariants for protecting living identity, revisability, relational context, and human authority in human-system relationships.

This release adds identity-boundary enforcement: structured fixtures and automated tests that prevent profiling/classification/diagnosis framing drift.

## What is included

### Identity boundary enforcement (new in v0.3)
- **Fixtures** (`docs/fixtures/identity_boundary/`):
  - `prohibited_patterns.yaml` — 30 prohibited terms, 20 prohibited phrases, 12 prohibited schema fields, 10 prohibited API endpoints
  - `identity_boundary_rules.yaml` — boundary principle, 8 required invariants, 15 prohibited behaviors, 3 required disclaimers, 10 allowed capabilities
  - `boundary_scenarios.yaml` — 7 deterministic scenarios (identity freezing, consent drift, silent authorship, revisability preservation, profiling rejection, diagnostic rejection, automated decisioning rejection)
- **Boundary tests** (`test_identity_boundary.py`): 19 tests enforcing:
  - No prohibited fields in protocol schemas
  - No prohibited endpoints in reference implementation
  - No prohibited phrases in docs (outside allowlist)
  - No prohibited terms in code comments
  - NON_CLAIMS.md structure and required entries
  - Required disclaimers present
  - Allowed capabilities are protective
  - Prohibited behaviors absent from reference
  - Identity authority preserved (subject endpoints, authority check, observer read-only)
  - Boundary scenarios structurally valid and enforceable

### Engineering hygiene (carried from v0.2)
- GitHub Actions CI with hard-gated lint/format
- Makefile targets: validate, test, snapshot, lint, format, check, all
- pre-commit: ruff, black, check-yaml, trailing-whitespace, end-of-file-fixer
- pyproject.toml packaging, sys.path.append removed
- ruff + black across all 50 Python files
- English-only code and comments

### Test expansion (v0.2 + v0.3)
- API smoke tests: 15 tests
- Adapter smoke tests: 5 tests
- Identity boundary tests: 19 tests
- Legacy tests: 15 tests
- Total: **54 tests**

### Protocol surface (unchanged from v0.1)
- Identity, lifecycle, relations schemas
- Rules: coherence, lifecycle, relationships
- Events: created, updated, reflected
- Error codes: LRI_001–LRI_010
- Alice scenario examples

### Reference implementation (unchanged from v0.1)
- FastAPI server with subject, relations, authority, observer, economic, cycle endpoints
- Services, models, storage, adapters

### Documentation (v0.2 + v0.3)
- GLOSSARY.md, NON_CLAIMS.md, REVIEWER_PATH.md
- identity_freezing_examples.md, consent_drift_scenario.md, silent_authorship.md
- lri_vs_privacy_consent.md, SECURITY_MODEL.md
- Identity boundary fixtures as structured boundary contracts

### Validation
- `scripts/validate_project.py` — project-level validation
- `VALIDATION_RESULTS.md` — 54 tests, validation PASS

### Trust infrastructure (unchanged from v0.1)
- LICENSE — MIT
- SECURITY.md, CONTRIBUTING.md

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
