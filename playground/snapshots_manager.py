import json
import hashlib
from datetime import datetime, timezone
from pathlib import Path
import os

SNAPSHOTS_DIR = Path(__file__).parent / "snapshots"

class SnapshotError(Exception):
    """Base exception for snapshot errors."""
    pass

class SnapshotExistsError(SnapshotError):
    """Raised when trying to overwrite an existing snapshot."""
    pass

class SnapshotNotFoundError(SnapshotError):
    """Raised when a requested snapshot does not exist."""
    pass

class ChecksumError(SnapshotError):
    """Raised when snapshot integrity verification fails."""
    pass

def compute_checksum(events: list) -> str:
    """Compute SHA256 checksum of trajectory events.

    Checksum is computed over ordered trajectory events,
    preserving causality. Uses compact separators to ensure
    deterministic serialization regardless of whitespace.
    """
    events_json = json.dumps(
        events,
        sort_keys=True,
        separators=(',', ':'),  # Compact, no whitespace variations
        default=str  # Handle datetime objects gracefully
    )
    return hashlib.sha256(events_json.encode()).hexdigest()[:16]

def create_snapshot(snapshot_id: str, trajectory_data: dict) -> dict:
    """Freeze current trajectory.

    Args:
        snapshot_id: Unique identifier for the snapshot.
        trajectory_data: Dictionary containing 'events' and 'current_state'.

    Returns:
        The created snapshot dictionary.

    Raises:
        ValueError: If snapshot ID is invalid.
        SnapshotExistsError: If snapshot already exists.
    """
    # Sanitize snapshot ID (security: prevent path traversal)
    safe_id = "".join([c for c in snapshot_id if c.isalnum() or c in ('-', '_')])
    if not safe_id:
        raise ValueError("Invalid snapshot ID: must contain alphanumeric characters")

    filepath = SNAPSHOTS_DIR / f"{safe_id}.json"

    SNAPSHOTS_DIR.mkdir(parents=True, exist_ok=True)
    events = trajectory_data.get("events", [])

    snapshot = {
        "id": safe_id,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "trajectory": trajectory_data,
        "checksum": compute_checksum(events)
    }

    # Atomic write: exclusive creation, prevents race condition
    try:
        with open(filepath, 'x') as f:
            json.dump(snapshot, f, indent=2, default=str)
    except FileExistsError:
        raise SnapshotExistsError(f"Snapshot '{safe_id}' already exists. Choose a different name.")

    return snapshot

def list_snapshots() -> list:
    """List all saved snapshots with metadata.

    Returns:
        List of snapshot metadata dictionaries.
    """
    snapshots = []
    # Ensure directory exists
    if not SNAPSHOTS_DIR.exists():
        return []

    for filepath in SNAPSHOTS_DIR.glob("*.json"):
        try:
            with open(filepath) as f:
                snapshot = json.load(f)

            trajectory = snapshot.get("trajectory", {})
            current_state = trajectory.get("current_state", {})
            events = trajectory.get("events", [])

            # Verify checksum implicitly to mark validity
            is_valid = False
            try:
                verify_checksum(snapshot)
                is_valid = True
            except ChecksumError:
                is_valid = False

            snapshots.append({
                "id": snapshot.get("id", filepath.stem),
                "created_at": snapshot.get("created_at"),
                "events_count": len(events),
                "phase": current_state.get("phase", "unknown"),
                "valid": is_valid
            })
        except Exception:
            # Skip corrupted files that aren't valid JSON
            continue

    # Sort by creation time (newest first)
    snapshots.sort(key=lambda x: x.get("created_at", ""), reverse=True)
    return snapshots

def load_snapshot(snapshot_id: str) -> dict:
    """Load snapshot by ID.

    Args:
        snapshot_id: The ID of the snapshot to load.

    Returns:
        The full snapshot dictionary.

    Raises:
        ValueError: If ID is invalid.
        SnapshotNotFoundError: If file doesn't exist.
        ChecksumError: If integrity check fails.
    """
    # Sanitize ID
    safe_id = "".join([c for c in snapshot_id if c.isalnum() or c in ('-', '_')])
    if not safe_id:
        raise ValueError("Invalid snapshot ID")

    filepath = SNAPSHOTS_DIR / f"{safe_id}.json"

    if not filepath.exists():
        raise SnapshotNotFoundError(f"Snapshot '{safe_id}' not found")

    with open(filepath) as f:
        snapshot = json.load(f)

    verify_checksum(snapshot)

    return snapshot

def verify_checksum(snapshot: dict):
    """Verify snapshot integrity.

    Raises:
        ChecksumError: If verification fails.
    """
    expected = snapshot.get("checksum")
    trajectory = snapshot.get("trajectory", {})
    events = trajectory.get("events", [])

    actual = compute_checksum(events)

    if expected != actual:
        raise ChecksumError(f"Snapshot integrity check failed. Expected {expected}, got {actual}")
