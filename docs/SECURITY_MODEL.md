# LRI Security Model

## Principles

- Explicit trust boundaries
- Scope-based access
- All sensitive operations are auditable

## API Access

Each API consumer is identified by an API key.

Each key is associated with scopes:

- read:artifact
- read:continuity
- write:decision

## Auditability

Every access to identity artifacts or authority checks
is recorded in an immutable audit stream.

This audit log can be linked to DMP for non-repudiation.
