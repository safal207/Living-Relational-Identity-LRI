from typing import List, Optional
from models.economic_artifact import EconomicArtifact

class ArtifactRegistry:
    """Хранилище экспортируемых артефактов, read-only."""
    def __init__(self):
        self._registry: List[EconomicArtifact] = []

    def register_artifact(self, artifact: EconomicArtifact):
        self._registry.append(artifact)

    def list_exportable_artifacts(self, subject_id: str) -> List[EconomicArtifact]:
        return [a for a in self._registry if a.subject_id == subject_id]

    def get_artifact(self, subject_id: str, artifact_type: str) -> Optional[EconomicArtifact]:
        for a in self._registry:
            if a.subject_id == subject_id and a.artifact_type == artifact_type:
                return a
        return None

# Singleton instance to be shared across services and API
artifact_registry = ArtifactRegistry()
