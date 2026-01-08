from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass(frozen=True)
class DecisionRecord:
    agent_id: str
    intention: str
    decision: str
    context: Optional[str]
    timestamp: datetime
