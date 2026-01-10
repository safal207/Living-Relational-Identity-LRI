# LRI Read API (Read-Only)

**Access Level**: Public / Subscriber
**Philosophy**: Observation without Interference.

The Read API allows observers to query the state, history, and continuity of an LRI Identity. It is designed to be high-performance ("read-heavy") and cacheable.

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
