from collections import defaultdict

class MetricsEngine:
    def __init__(self):
        # Stores raw event data for each agent
        self._data = defaultdict(lambda: {
            "actions": 0,
            "intentions": []
        })

    def record(self, agent_id: str, action: str, intention: str):
        """
        Records a single action/intention event for an agent.
        """
        m = self._data[agent_id]
        m["actions"] += 1
        # In a real system, we might limit the history size for drift calculation
        m["intentions"].append(intention)

    def snapshot(self, agent_id: str) -> dict:
        """
        Returns a snapshot of the raw metrics for an agent.
        """
        return dict(self._data.get(agent_id, {}))

# Global instance for the reference implementation
metrics_engine = MetricsEngine()
