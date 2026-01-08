import sys
import os
import datetime

# Ensure we can import from sibling/parent directories
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from services.cycle_engine import run_identity_cycle

class MultiAgentEnvironment:
    def __init__(self):
        # In a real persistence layer, this would load from DB.
        # For this in-memory simulation, we rely on the state being managed
        # partly here and partly in the core LRI Subject store (via cycle_engine).
        # We'll use a local cache for the demo to show immediate state.
        self.agents = {}  # subject_id -> trajectory list

    def add_agent(self, subject_id):
        if subject_id not in self.agents:
            self.agents[subject_id] = []
        # In a real system, we'd ensure the Subject exists in LRI here.
        # cycle_engine.run_identity_cycle does auto-provisioning, so we are good.

    def interact(self, actor_id, target_id, action, intention):
        # 1. Actor performs an action (Identity Cycle)
        payload = {"subject_id": actor_id, "action": action, "intention": intention, "context": {"target": target_id}}
        result = run_identity_cycle(payload)

        # Update local cache for actor
        # In a real app, we'd refetch from LRI. Here we trust the return.
        # The result["trajectory"] is the full history.
        self.agents[actor_id] = result["trajectory"]

        # 2. Target receives effect (Simplified LTP reception)
        # We simulate the target's trajectory being influenced.
        if target_id not in self.agents:
             self.agents[target_id] = []

        influence_event = {
            "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "action": f"influenced_by_{actor_id}",
            "intention": f"reaction_to_{intention}",
            "context": {"source_action": action}
        }

        self.agents[target_id].append(influence_event)

        # Ideally, we would run an identity cycle for the target too,
        # creating a DMP record of their reaction.
        # For this step, we just update the in-memory trace to show the link.

        return result
