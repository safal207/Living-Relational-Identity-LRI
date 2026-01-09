from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class AuditSnapshot(BaseModel):
    subject_id: str
    timestamp: datetime
    continuity_hash: str
    drift_score: float
    authority_claims: List[str]
    trajectory_length: int
