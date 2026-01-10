# Migration Guide: v0.x → v1.0.0

## Overview

This guide helps migrate from pre-release versions (v0.x) to production-ready v1.0.0.

**Estimated migration time:** 30-60 minutes for typical installation

---

## Breaking Changes

### 1. Coherence Score Format
**Before (v0.x):** Integer 0-100
**After (v1.0):** Float 0.0-1.0

### 2. Event Structure
**Before (v0.x):** Only `event_id` and `timestamp`
**After (v1.0):** Added `correlation_id` (required), `causation_id`, `idempotency_key`

### 3. Error Codes
**Before (v0.x):** Text messages like "Invalid intent"
**After (v1.0):** Structured codes like "LRI_001"

---

## Step-by-Step Migration

### Step 1: Backup Data
```bash
# Export all identities
lri-export --output ./backup-$(date +%Y%m%d).json

# Verify backup
lri-verify-backup ./backup-*.json
```

### Step 2: Update Coherence Scores

**Python:**
```python
# Before (v0.x)
coherence = 85  # 0-100

# After (v1.0)
coherence = 0.85  # 0.0-1.0

# Migration function
def migrate_coherence(old_score: int) -> float:
    if not (0 <= old_score <= 100):
        raise ValueError(f"Invalid old score: {old_score}")
    return old_score / 100.0
```

**JavaScript:**
```javascript
// Before (v0.x)
const coherence = 85;

// After (v1.0)
const coherence = 0.85;

// Migration
function migrateCoherence(oldScore) {
  if (oldScore < 0 || oldScore > 100) {
    throw new Error(`Invalid old score: ${oldScore}`);
  }
  return oldScore / 100;
}
```

### Step 3: Add Event Metadata

**Before (v0.x):**
```yaml
event_id: "550e8400-e29b-41d4-a716-446655440000"
timestamp: "2026-01-10T14:30:00Z"
```

**After (v1.0):**
```yaml
event_id: "550e8400-e29b-41d4-a716-446655440000"
correlation_id: "660e8400-e29b-41d4-a716-446655440000"  # NEW
causation_id: null  # Optional for first event
timestamp: "2026-01-10T14:30:00Z"
actor: "system:migration"  # NEW
idempotency_key: "migration-2026-01-10-001"  # NEW
ttl: 2592000  # NEW (30 days)
retry_count: 0  # NEW
```

**Migration script:**
```python
import uuid
from datetime import datetime

def add_event_metadata(old_event: dict) -> dict:
    return {
        **old_event,
        "correlation_id": str(uuid.uuid4()),
        "causation_id": None,
        "actor": "system:migration",
        "idempotency_key": f"migration-{datetime.now().isoformat()}-{old_event['event_id'][:8]}",
        "ttl": 2592000,  # 30 days
        "retry_count": 0
    }
```

### Step 4: Update Error Handling

**Before (v0.x):**
```python
if error == "Invalid intent":
    handle_invalid_intent()
elif error == "Coherence too low":
    handle_coherence_error()
```

**After (v1.0):**
```python
if error["error_code"] == "LRI_001":
    handle_invalid_intent(error)
elif error["error_code"] == "LRI_002":
    handle_coherence_error(error)

# Access structured fields
print(error["error_type"])     # "InvalidIntent"
print(error["remediation"])    # "Check intent format"
print(error["http_status"])    # 400
```

### Step 5: Validate Migration

```bash
# Run protocol validator
lri-validate --data ./migrated/ --strict

# Expected output:
# ✓ Coherence scores: all in [0.0, 1.0]
# ✓ Events: all have correlation_id
# ✓ Error handling: using LRI_XXX codes
# ✓ Relationships: valid types and strengths
#
# Migration successful!
```

---

## Automated Migration

### Using CLI Tool

```bash
# Full automatic migration
lri-migrate \
  --from v0.5.0 \
  --to v1.0.0 \
  --data ./identities/ \
  --backup ./backup/ \
  --dry-run  # Test first

# After verifying dry-run:
lri-migrate \
  --from v0.5.0 \
  --to v1.0.0 \
  --data ./identities/ \
  --backup ./backup/
```

### Using Python API

```python
from lri_protocol import Migrator

migrator = Migrator(
    source_version="0.5.0",
    target_version="1.0.0",
    data_path="./identities/",
    backup_path="./backup/"
)

# Dry run
report = migrator.plan()
print(report.summary())

# Execute
if report.is_safe():
    migrator.execute()
    print("Migration complete!")
else:
    print("Migration unsafe:", report.issues)
```

---

## Rollback Plan

If migration fails:

```bash
# Restore from backup
lri-restore --from ./backup-20260110.json

# Verify restoration
lri-validate --data ./identities/

# Downgrade protocol version
echo "0.5.0" > protocol/VERSION
```

---

## Common Issues

### Issue 1: Coherence Scores Out of Range

**Error:**
```
ValueError: Coherence score 150 exceeds maximum 1.0
```

**Solution:**
```python
# Data corruption - cap to valid range
coherence = min(1.0, old_score / 100.0)
```

### Issue 2: Missing Event Fields

**Error:**
```
ValidationError: 'correlation_id' is required
```

**Solution:**
```python
# Generate missing correlation_id
event["correlation_id"] = str(uuid.uuid4())
```

### Issue 3: Invalid Lifecycle Phase

**Error:**
```
ValueError: Unknown phase 'beta' not in [emerging, active, dormant, archived]
```

**Solution:**
```python
# Map old phases to new
phase_mapping = {
    "beta": "emerging",
    "stable": "active",
    "inactive": "dormant"
}
new_phase = phase_mapping.get(old_phase, "emerging")
```

---

## Timeline

| Action | Duration |
|--------|----------|
| Backup data | 5 min |
| Run migration | 10-30 min |
| Validate results | 5 min |
| Test application | 15-30 min |
| **Total** | **35-70 min** |

---

## Support

If migration fails:
1. Check logs: `lri-migrate --logs`
2. Join Discord: [discord.gg/lri-protocol]
3. Open issue: [github.com/safal207/LRI/issues]
4. Email: support@lri-protocol.org

---

## Post-Migration Checklist

- [ ] All identities migrated successfully
- [ ] Coherence scores in [0.0, 1.0] range
- [ ] Events have correlation_id
- [ ] Error codes use LRI_XXX format
- [ ] Application tests passing
- [ ] Documentation updated
- [ ] Team trained on v1.0 changes

**Migration complete!** 🎉
