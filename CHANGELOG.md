# Changelog

All notable changes to the LRI Protocol will be documented in this file.

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
