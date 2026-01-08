from fastapi import APIRouter, HTTPException
from services.cycle_engine import run_identity_cycle
from pydantic import BaseModel
from typing import Optional, Dict, Any

router = APIRouter()

class SimulationPayload(BaseModel):
    subject_id: str
    action: str
    intention: Optional[str] = None
    context: Optional[Dict[str, Any]] = {}

@router.post("/simulate/cycle")
def simulate_cycle(payload: SimulationPayload):
    """
    Runs full LPI -> DMP -> LRI -> LTP identity cycle.
    """
    try:
        # Convert Pydantic model to dict for the engine
        result = run_identity_cycle(payload.dict())
        return {
            "status": "cycle_completed",
            "identity_state": result
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
