import sys
import os
import json

# Ensure we can import from services sibling directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from api import subject
from services.cycle_engine import run_identity_cycle

def main():
    print("--- Hello, Alice! (LRI Quick Start) ---")

    subject_id = "alice-001"

    # 1. Create Identity
    print(f"\n1. Creating Identity for {subject_id}...")
    result = subject.create_subject(subject_id, {
        "id": subject_id,
        "name": "Alice",
        "role": "student",
        "trajectory": []
    })
    print(f"   Created: {result['subject']['name']} (Role: {result['subject']['role']})")

    # 2. Apply Action (Run Cycle)
    print("\n2. Applying Action: 'Complete Module 1'...")
    payload = {
        "subject_id": subject_id,
        "action": "complete_module_1",
        "intention": "learn_basics",
        "context": {"course": "LRI_101"}
    }

    # Run the LRI cycle
    snapshot = run_identity_cycle(payload)

    # 3. Print State
    print("\n3. Current State Snapshot:")
    print(json.dumps(snapshot, indent=2))

    # Check drift (simulated)
    drift = snapshot.get("metrics", {}).get("drift", 0.0)
    print(f"\n   Alice's Coherence Drift: {drift:.2f}")

    print("\n--- Done! Alice has evolved. ---")

if __name__ == "__main__":
    main()
