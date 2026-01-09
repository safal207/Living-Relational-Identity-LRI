from fastapi import APIRouter, HTTPException
from services.observer import observer_service
from models.audit_snapshot import AuditSnapshot

router = APIRouter(prefix="/observer", tags=["Observer"])

@router.get("/subject/{subject_id}/snapshot", response_model=AuditSnapshot)
def get_snapshot(subject_id: str):
    """
    Get a full audit snapshot of the identity.
    """
    return observer_service.get_identity_snapshot(subject_id)

@router.get("/subject/{subject_id}/continuity")
def get_continuity(subject_id: str):
    """
    Verify and retrieve continuity proofs.
    """
    return observer_service.verify_continuity(subject_id)

@router.get("/subject/{subject_id}/drift")
def get_drift(subject_id: str):
    """
    Get drift metrics for the identity.
    """
    return observer_service.read_drift_metrics(subject_id)
