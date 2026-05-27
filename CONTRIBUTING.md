# Contributing to LRI

## Scope

LRI defines non-operational invariants for protecting living identity in human-system relationships. Contributions should align with this narrow scope.

LRI is not:
- an identity classifier, profiling system, personality scoring, diagnosis, therapy, mental-health assessment, social credit, risk scoring of people, automated decisioning about humans, or prediction of a person's true self.

See [docs/NON_CLAIMS.md](docs/NON_CLAIMS.md) for the full scope boundary.

## How to Contribute

1. Open an issue to discuss proposed changes before submitting a PR.
2. Fork the repository and create a feature branch.
3. Ensure validation passes:
   ```bash
   python scripts/validate_project.py
   cd lri-reference && python -m pytest -q
   ```
4. Open a pull request with a clear description of the change and its motivation.

## Code Style

- Python 3.11+ with type annotations where practical.
- YAML for protocol schemas and scenarios.
- Markdown for documentation.
- English for all code, comments, and documentation.

## What Needs Review

All changes to:
- `protocol/` — protocol schemas and rules
- `lri-reference/` — reference implementation
- `docs/` — documentation and scope boundaries

## Questions

Open an issue at https://github.com/safal207/Living-Relational-Identity-LRI/issues
