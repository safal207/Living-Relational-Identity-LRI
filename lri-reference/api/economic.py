from fastapi import APIRouter, HTTPException
from services.artifact_registry import artifact_registry

router = APIRouter()

@router.get("/artifact/{artifact_type}")
def export_artifact(artifact_type: str, subject_id: str):
    artifact = artifact_registry.get_artifact(subject_id, artifact_type)
    if artifact is None:
        raise HTTPException(status_code=404, detail="Artifact not found")
    return artifact.export()

@router.get("/artifacts")
def list_artifacts(subject_id: str):
    return [a.export() for a in artifact_registry.list_exportable_artifacts(subject_id)]

# TODO: добавить регистрацию артефактов из цикла identity
