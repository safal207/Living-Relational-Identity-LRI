# LRI Read API (Read-Only)

**Access Level**: Public / Subscriber
**Philosophy**: Observation without Interference.

The Read API allows observers to query the state, history, and continuity of an LRI Identity. It is designed to be high-performance ("read-heavy") and cacheable.

## Rate Limiting

### Response Headers

Every API response includes rate limit information:

```http
X-RateLimit-Limit: 1000          # Total allowed per window
X-RateLimit-Remaining: 847       # Remaining in current window
X-RateLimit-Reset: 1704902400    # Unix timestamp when resets
X-RateLimit-Window: 60           # Window duration in seconds
```

### When Rate Limited

```http
HTTP/1.1 429 Too Many Requests
Retry-After: 45
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 0
X-RateLimit-Reset: 1704902445

{
  "error_code": "LRI_006",
  "error_type": "RateLimitExceeded",
  "message": "Rate limit exceeded. Retry after 45 seconds.",
  "retry_after": 45
}
```

## Endpoints

### 1. Get Subject State
`GET /subject/{lri_id}`

Retrieves the current canonical state of an identity.
- **Returns**: `LRIIdentity` (see schema/identity.yaml)
- **Headers**: `Last-Modified`, `ETag` (State Hash)

### 2. Verify Continuity
`GET /subject/{lri_id}/continuity`

Verifies the cryptographic chain of the identity.
- **Params**: `since_hash` (optional)
- **Returns**: Proof of validity from `since_hash` to `current_head`.

### 3. Get Relations
`GET /subject/{lri_id}/relations`

Returns the active web of trust/context.
- **Params**: `type` (filter by relation type)

### 4. Get Reflection/Metrics
`GET /subject/{lri_id}/reflection`

Returns the latest reflection metrics (Drift, Coherence).
- **Access**: May require specific `OBSERVER` permissions.
