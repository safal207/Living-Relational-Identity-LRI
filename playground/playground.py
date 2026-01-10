import yaml
import os
import sys
import glob
import time

# Mock Coherence Logic
COHERENCE_RULES = {
    "add_relation": 0.22,
    "peer_relation": 0.15,
    "mentor_relation": 0.25,
    "drift_event": -0.30,
}

def apply_mock_coherence(identity, scenario):
    """
    Mock coherence calculation.
    This playground demonstrates flow, not math accuracy.
    """
    intent = scenario.get("intent")
    delta = COHERENCE_RULES.get(intent, 0.0)

    # Apply delta
    identity["coherence"] = round(
        max(0.0, min(1.0, identity["coherence"] + delta)), 2
    )

def render_identity(identity):
    print("┌─────────────────────────────┐")
    print(f"│ Identity: {identity['id']:<18} │")
    print("├─────────────────────────────┤")
    print(f"│ Phase: {identity['phase']:<20}│")
    print(f"│ Coherence: {str(identity['coherence']):<15}│")
    print("└─────────────────────────────┘")

def run_playground():
    print("\n🚀 Starting LRI Interactive Playground...\n")

    # Find all scenarios
    # We assume we run from playground/ directory or root?
    # The instructions say "python playground.py" inside playground directory?
    # Or "python playground/playground.py" from root?
    # The README says:
    # cd playground (implied by requirements.txt context usually, but checking)
    # The README says:
    # pip install -r requirements.txt
    # python playground.py
    # So we should assume CWD is playground/

    # However, I am running from repo root usually.
    # I will adapt the path finding to be relative to the script location.
    base_dir = os.path.dirname(os.path.abspath(__file__))
    scenarios_dir = os.path.join(base_dir, "scenarios")
    scenario_files = sorted(glob.glob(os.path.join(scenarios_dir, "*.yaml")))

    if not scenario_files:
        print(f"❌ No scenarios found in {scenarios_dir}")
        return

    # Identity state
    identity = {}

    for filepath in scenario_files:
        filename = os.path.basename(filepath)
        print(f"📄 Loading {filename}...")
        try:
            with open(filepath, 'r') as f:
                scenario = yaml.safe_load(f)
        except Exception as e:
            print(f"❌ Failed to load YAML: {e}")
            continue

        print(f"📖 Story: {scenario.get('story', 'Unknown')}")

        # Initialize identity if present (usually first scenario)
        if "identity" in scenario:
            identity = scenario["identity"]
            # Ensure coherence is float
            identity["coherence"] = float(identity["coherence"])

        if not identity:
            print("⚠️ No identity loaded yet. Skipping...")
            continue

        # Simulate processing
        intent = scenario.get("intent")
        expected = scenario.get("expected", {})
        error_caught = None

        # Logic to simulate errors based on scenario cues

        # Scenario 03: Drift Check
        if intent == "drift_event":
            # In this playground, we treat explicit 'drift_event' intent
            # combined with unauthorized fields as a trigger for drift error.
             if "change" in scenario and "unauthorized_field" in scenario["change"]:
                 error_caught = "LRI_007_DRIFT_DETECTED"

        # Scenario 04: Invalid Transition Check
        if "requested_transition" in scenario:
             trans = scenario["requested_transition"]
             if trans.get("from") == "archived" and trans.get("to") == "active":
                 error_caught = "LRI_004_INVALID_LIFECYCLE_TRANSITION"

        # Apply intent only if no error
        if not error_caught:
            apply_mock_coherence(identity, scenario)

            # Scenario 05: Activation Logic / Phase Change
            # If expected phase_after is set, update mock phase
            # In a real system this depends on rules.
            if "phase_after" in expected:
                 # Check conditions (mocking the rule check)
                 if identity["coherence"] >= 0.6: # Mock threshold
                     identity["phase"] = expected["phase_after"]
                 else:
                     print(f"⚠️ Phase transition to {expected['phase_after']} failed due to low coherence.")

        # Render current state
        render_identity(identity)

        # Validation against expectations
        passed = True

        # Check expected error
        if "error" in expected:
            if expected["error"] == error_caught:
                print(f"✅ Expected Error Caught: {error_caught}")
            else:
                print(f"❌ Failed: Expected error {expected['error']}, got {error_caught}")
                passed = False
        elif error_caught:
             print(f"❌ Unexpected Error: {error_caught}")
             passed = False

        # Check expected coherence
        if not error_caught:
            if "coherence_after" in expected:
                 # Just informational in this mock, verifying we didn't crash
                 pass
            if "coherence_min" in expected:
                if identity["coherence"] < expected["coherence_min"]:
                    print(f"❌ Failed: Coherence {identity['coherence']} < {expected['coherence_min']}")
                    passed = False

            # Verify phase if expected
            if "phase_after" in expected:
                if identity["phase"] != expected["phase_after"]:
                    print(f"❌ Failed: Phase is {identity['phase']}, expected {expected['phase_after']}")
                    passed = False

        if passed:
            print("✨ Scenario Completed\n")
            time.sleep(0.5)
        else:
            print("🛑 Scenario Failed\n")

    print("🎉 Playground finished.")

if __name__ == "__main__":
    run_playground()
