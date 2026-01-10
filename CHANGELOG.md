# Changelog

All notable changes to the LRI Protocol will be documented in this file.

## [1.0.0] - 2026-01-10

### Added
- Protocol version tracking (VERSION, VERSION.json)
- Complete versioning policy (VERSIONING.md)
- Migration guide from v0.x (MIGRATION.md)
- 10 standardized error schemas (LRI_001-LRI_010)
- Relationship validation rules
- Enhanced event metadata (correlation_id, causation_id, idempotency_key)
- Coherence thresholds for operations
- Lifecycle transition rules with conditions
- Story-driven examples (Alice's journey)

### Changed
- Coherence score format: 0-100 → 0.0-1.0 (BREAKING)
- Event structure: added required correlation_id (BREAKING)
- Error codes: text → structured LRI_XXX format (BREAKING)

### Fixed
- Missing relationships validation
- Unclear lifecycle transitions
- Incomplete error handling

### Security
- Added rate limiting specifications
- Idempotency keys for duplicate prevention
- TTL for event cleanup

## [Unreleased] - PR #20

### Protocol Definition
- **Added**: `protocol/` directory structure to formalize LRI interfaces.
- **Added**: `protocol/lri/schema/` containing `identity.yaml`, `relations.yaml`, and `lifecycle.yaml`.
- **Added**: `protocol/lri/events/` defining `lri.created`, `lri.updated`, and `lri.reflected`.
- **Added**: `protocol/lri/diff/` defining the semantic `lri.diff.yaml`.
- **Added**: `protocol/lri/api/` documenting Read and Write interfaces.

### Documentation
- **Added**: `docs/lri-philosophy.md` explaining the shift from CRUD to Identity Continuity.
- **Added**: `docs/lri-vs-state.md` differentiating LRI from generic Event Sourcing.
