from datetime import datetime, timezone
from models.decision_record import DecisionRecord
from storage.dmp_store import DMPStore

class DMPWriter:
    def __init__(self, store: DMPStore):
        self.store = store

    def record(self, agent_id, intention, decision, context=None):
        record = DecisionRecord(
            agent_id=agent_id,
            intention=intention,
            decision=decision,
            context=context,
            timestamp=datetime.now(timezone.utc)
        )
        self.store.append(record)

# Global instance for reference implementation
dmp_writer = DMPWriter(DMPStore())
