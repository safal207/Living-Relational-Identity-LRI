from datetime import datetime
from typing import List

from pydantic import BaseModel


class AuditSnapshot(BaseModel):
    subject_id: str
    timestamp: datetime
    continuity_hash: str
    drift_score: float
    authority_claims: List[str]
    trajectory_length: int
