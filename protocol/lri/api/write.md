# LRI Write API (Controlled)

**Access Level**: Owner / Authorized Agent
**Philosophy**: Write via Intent.

The Write API is not a direct database interface. It is an *Intent Processing System*. You do not "update a record"; you "propose a change" which is then verified, authorized, and committed to the chain.

## Endpoints

### 1. Submit Intent (Propose Update)
`POST /subject/{lri_id}/intent`

Submits a proposed change (Diff) or a high-level intent.
- **Body**:
  - `intent`: Description of desired outcome.
  - `diff`: (Optional) Proposed `LRIDiff` (see diff/lri.diff.yaml).
  - `proof`: Cryptographic signature of the requestor.

- **Process**:
  1. **Authority Check**: Does the requestor have the right to modify this scope?
  2. **Drift Check**: Does this change violate drift constraints?
  3. **Commit**: If valid, a new block is appended to the identity chain.

### 2. Establish Relation
`POST /subject/{lri_id}/relations`

Initiates a handshake to form a new relationship.
- **Body**: Target ID, Relation Type, Initial Context.

### 3. Trigger Reflection
`POST /subject/{lri_id}/reflect`

Forces an immediate self-audit cycle.
- **Use Case**: Before major architectural changes or critical decisions.
