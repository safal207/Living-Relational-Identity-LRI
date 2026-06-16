import json
import sys
from datetime import datetime
from itertools import zip_longest
from typing import Dict, List, Any, Tuple, Optional, TypedDict, Union

# ==========================================
#  PR #28: Semantic Snapshot Diff Engine
#  Features: Caching, Strict Typing, Weights
# ==========================================

# -----------------------------
# 0. Configuration & Types
# -----------------------------

DIVERGENCE_WEIGHTS = {
    'identity': 0.4,
    'graph': 0.4,
    'narrative': 0.2
}

class Snapshot(TypedDict, total=False):
    id: str
    timestamp: str
    peers: List[str]
    peers_status: Dict[str, str]
    coherence: float
    autonomy: float
    critical_choice: Optional[str]
    events: List[str]

class ConflictDetail(TypedDict):
    type: str
    field: str
    severity: str
    detail: str

# -----------------------------
# 1. I/O Boundary (Cached)
# -----------------------------

_snapshot_cache: Dict[str, Snapshot] = {}

def load_snapshot(snapshot_id: str) -> Snapshot:
    """
    Загружает снапшот с кэшированием и валидацией.
    """
    if snapshot_id in _snapshot_cache:
        return _snapshot_cache[snapshot_id]

    path = f"snapshots/{snapshot_id}.json"
    try:
        with open(path, "r", encoding='utf-8') as f:
            data = json.load(f)

        # Validation
        required_keys = {'id', 'timestamp'}
        if not required_keys.issubset(data.keys()):
            missing = required_keys - set(data.keys())
            print(f"[WARNING] Snapshot {snapshot_id} incomplete. Missing: {missing}")
            return {} # type: ignore

        _snapshot_cache[snapshot_id] = data
        return data # type: ignore

    except FileNotFoundError:
        print(f"[ERROR] Snapshot file '{path}' not found.")
        return {} # type: ignore
    except json.JSONDecodeError:
        print(f"[ERROR] Snapshot '{snapshot_id}' contains invalid JSON.")
        return {} # type: ignore

# -----------------------------
# 2. Core Logic (Pure Functions)
# -----------------------------

def calculate_set_diff(list_a: list, list_b: list) -> Tuple[set, set]:
    set_a, set_b = set(list_a), set(list_b)
    return (set_b - set_a), (set_a - set_b)

def diff_structure(snap1: Snapshot, snap2: Snapshot) -> dict:
    keys1, keys2 = set(snap1.keys()), set(snap2.keys())

    added_keys = {k: snap2[k] for k in keys2 - keys1} # type: ignore
    removed_keys = {k: snap1[k] for k in keys1 - keys2} # type: ignore

    common_keys = keys1 & keys2
    changed_values = {}

    for k in common_keys:
        if k == 'peers': continue
        if snap1[k] != snap2[k]: # type: ignore
            changed_values[k] = (snap1[k], snap2[k]) # type: ignore

    peers_added, peers_lost = calculate_set_diff(
        snap1.get('peers', []),
        snap2.get('peers', [])
    )

    return {
        'snapshot_a': snap1.get('id'),
        'snapshot_b': snap2.get('id'),
        'added_keys': added_keys,
        'removed_keys': removed_keys,
        'changed_values': changed_values,
        'topology': {
            'peers_added': list(peers_added),
            'peers_lost': list(peers_lost)
        }
    }

# -----------------------------
# 3. Semantic Analysis
# -----------------------------

def interpret_coherence(old: float, new: float) -> str:
    delta = new - old
    if delta > 0.05:
        return f"coherence +{delta:.2f} (Stronger integration)"
    elif delta < -0.05:
        return f"coherence {delta:.2f} (Fragmentation risk)"
    return f"stable ({delta:+.2f})"

def detect_conflicts(snap1: Snapshot, snap2: Snapshot, changed: dict) -> List[ConflictDetail]:
    conflicts: List[ConflictDetail] = []

    # 1. Critical Choice
    if 'critical_choice' in changed:
        conflicts.append({
            'type': 'CRITICAL_VALUE_CLASH',
            'field': 'critical_choice',
            'severity': 'HIGH',
            'detail': f"Manual resolution required: {changed['critical_choice']}"
        })

    # 2. Peer Paradox
    peers1 = set(snap1.get('peers', []))
    peers2 = set(snap2.get('peers', []))
    common_peers = peers1 & peers2

    status1 = snap1.get('peers_status', {})
    status2 = snap2.get('peers_status', {})

    for peer in common_peers:
        s1 = status1.get(peer, 'unknown')
        s2 = status2.get(peer, 'unknown')
        if s1 != s2:
            conflicts.append({
                'type': 'RELATIONSHIP_PARADOX',
                'field': 'peers_status',
                'severity': 'MEDIUM',
                'detail': f"Peer '{peer}': '{s1}' vs '{s2}'"
            })

    return conflicts

def analyze_semantics(snap1: Snapshot, snap2: Snapshot) -> dict:
    diff = diff_structure(snap1, snap2)

    # Coherence
    coherence_msg = "no data"
    if 'coherence' in diff['changed_values']:
        old, new = diff['changed_values']['coherence']
        coherence_msg = interpret_coherence(float(old), float(new))

    # Graph
    added = diff['topology']['peers_added']
    lost = diff['topology']['peers_lost']
    graph_msg = "stable"
    if added or lost:
        parts = []
        if added: parts.append(f"New: {', '.join(added)}")
        if lost: parts.append(f"Lost: {', '.join(lost)}")
        graph_msg = " | ".join(parts)

    return {
        'structural': diff,
        'meaning': {
            'coherence_shift': coherence_msg,
            'autonomy_delta': snap2.get('autonomy', 0.0) - snap1.get('autonomy', 0.0),
            'social_graph': graph_msg
        },
        'conflicts': detect_conflicts(snap1, snap2, diff['changed_values'])
    }

# -----------------------------
# 4. Divergence Metrics
# -----------------------------

def calculate_divergence_score(snap1: Snapshot, snap2: Snapshot) -> float:
    # A. Identity
    keys = set(snap1.keys()) | set(snap2.keys())
    if not keys: return 0.0
    identity_diff = sum(1 for k in keys if snap1.get(k) != snap2.get(k)) / len(keys) # type: ignore

    # B. Graph
    peers1 = set(snap1.get('peers', []))
    peers2 = set(snap2.get('peers', []))
    union = len(peers1 | peers2)
    graph_diff = (len(peers1 ^ peers2) / union) if union > 0 else 0.0

    # C. Narrative
    seq1 = snap1.get('events', [])
    seq2 = snap2.get('events', [])
    seq_len = max(len(seq1), len(seq2), 1)
    narrative_diff = sum(1 for a, b in zip_longest(seq1, seq2) if a != b) / seq_len

    # Weighted Calculation
    w = DIVERGENCE_WEIGHTS
    return (
        identity_diff * w['identity'] +
        graph_diff * w['graph'] +
        narrative_diff * w['narrative']
    )

# -----------------------------
# 5. CLI Presentation
# -----------------------------

def show_diff(id1: str, id2: str):
    print(f"Loading snapshots: {id1}, {id2}...")

    s1 = load_snapshot(id1)
    s2 = load_snapshot(id2)

    if not s1 or not s2:
        print("[ABORT] Cannot compare incomplete or missing snapshots.")
        return

    analysis = analyze_semantics(s1, s2)
    score = calculate_divergence_score(s1, s2)

    print("-" * 50)
    print(f"TRAJECTORY DIFF: {id1} -> {id2}")
    print("-" * 50)

    # Time
    try:
        t1 = datetime.fromisoformat(s1.get('timestamp', ''))
        t2 = datetime.fromisoformat(s2.get('timestamp', ''))
        dt = t2 - t1
        print(f"Elapsed Time:     {dt}")
    except ValueError:
        print(f"Elapsed Time:     Unknown")

    print(f"Divergence Score: {score:.4f}")
    print("-" * 50)

    mean = analysis['meaning']
    print(f"Coherence:        {mean['coherence_shift']}")
    print(f"Autonomy Shift:   {mean['autonomy_delta']:+.2f}")
    print(f"Graph Dynamics:   {mean['social_graph']}")

    print("-" * 50)
    conflicts = analysis['conflicts']
    if conflicts:
        print(f"[!] CONFLICTS DETECTED: {len(conflicts)}")
        for c in conflicts:
            print(f"    - [{c['severity']}] {c['type']}")
            print(f"      {c.get('detail', '')}")
        print("")
        print("[BLOCK] AUTO-MERGE BLOCKED")
    else:
        print("[OK] NO CONFLICTS - READY TO MERGE")
    print("-" * 50 + "\n")

if __name__ == "__main__":
    if len(sys.argv) > 2:
        show_diff(sys.argv[1], sys.argv[2])
    else:
        # Default test
        show_diff("alpha", "beta")
