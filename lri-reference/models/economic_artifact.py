from datetime import datetime
from typing import Dict, Any

class EconomicArtifact:
    """
    Read-only артефакт доверия / отчёт для экспортирования.
    """
    def __init__(self, subject_id: str, artifact_type: str, payload: Dict[str, Any]):
        self.subject_id = subject_id
        self.artifact_type = artifact_type
        self.payload = payload
        self.created_at = datetime.utcnow()

    def export(self) -> Dict[str, Any]:
        """Возвращает копию артефакта для внешнего использования."""
        return {
            "subject_id": self.subject_id,
            "artifact_type": self.artifact_type,
            "payload": self.payload,
            "created_at": self.created_at.isoformat()
        }
