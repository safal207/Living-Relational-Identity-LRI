# LRI Protocol Versioning Policy

## Semantic Versioning

LRI Protocol follows [SemVer 2.0.0](https://semver.org/)

**Format:** MAJOR.MINOR.PATCH

- **MAJOR**: Breaking changes to schemas or semantics
- **MINOR**: Backward-compatible additions
- **PATCH**: Documentation or clarification

## Compatibility Promise

### Backward Compatibility
- v1.x will **always** work with v1.y (where y > x)
- Implementations MUST support at least previous MINOR version
- Deprecation warnings given **6 months** before removal

### Forward Compatibility
- New fields are **optional** by default
- Unknown fields MUST be **ignored** (not error)
- Events MUST **preserve** unknown fields when forwarding

## Version Negotiation

### Client Request
```http
GET /identity/123
X-LRI-Protocol-Version: 1.2.0
```

### Server Response
```http
200 OK
X-LRI-Protocol-Version: 1.2.0
X-LRI-Protocol-Supported: 1.0.0, 1.1.0, 1.2.0
```

### Version Mismatch
```http
400 Bad Request
{
  "error_code": "LRI_010",
  "error_type": "ProtocolVersionMismatch",
  "message": "Protocol version 2.0.0 not supported",
  "supported_versions": ["1.0.0", "1.1.0", "1.2.0"]
}
```

## Deprecation Process

1. **Announce** (v1.2.0): Mark as deprecated in docs
2. **Warn** (v1.3.0): Add deprecation warnings in responses
3. **Remove** (v2.0.0): Breaking change, major version bump

**Minimum Deprecation Period:** 6 months

## Schema Evolution Examples

### Adding Fields (MINOR version)
```yaml
# v1.0.0
Identity:
  subject_id: uuid

# v1.1.0 (backward compatible)
Identity:
  subject_id: uuid
  nickname: string?  # Optional new field
```

### Removing Fields (MAJOR version)
```yaml
# v1.5.0
Identity:
  subject_id: uuid
  legacy_field: string  # Deprecated

# v2.0.0
Identity:
  subject_id: uuid
  # legacy_field removed ← BREAKING
```

### Changing Semantics (MAJOR version)
```yaml
# v1.x: coherence_score range is 0-100
# v2.0: coherence_score range is 0.0-1.0 ← BREAKING
```

## Implementation Requirements

### MUST
- Support declared protocol version
- Reject incompatible versions with LRI_010 error
- Preserve unknown fields in events
- Document supported versions in README

### SHOULD
- Support previous MINOR version
- Warn on deprecated features
- Provide migration tools

### MAY
- Support multiple MAJOR versions simultaneously
- Auto-migrate between compatible versions
