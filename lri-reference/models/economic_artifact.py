from datetime import datetime
from typing import Any, Dict


class EconomicArtifact:
    """
    Read-only trust artifact / report for export.
    """

    def __init__(self, subject_id: str, artifact_type: str, payload: Dict[str, Any]):
        self.subject_id = subject_id
        self.artifact_type = artifact_type
        self.payload = payload
        self.created_at = datetime.utcnow()

    def export(self) -> Dict[str, Any]:
        """Returns a copy of the artifact for external use."""
        return {
            "subject_id": self.subject_id,
            "artifact_type": self.artifact_type,
            "payload": self.payload,
            "created_at": self.created_at.isoformat(),
        }
