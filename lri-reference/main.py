from fastapi import FastAPI
from api import subject, relations, authority, simulate_cycle
from pydantic import BaseModel
import uvicorn
import os
import sys

# Ensure we can import from api sibling directory if running directly
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

app = FastAPI(title="LRI Integration Service")

# Include the simulation router
app.include_router(simulate_cycle.router)

# -------------------------------
# Models
# -------------------------------
class SubjectModel(BaseModel):
    id: str
    name: str
    role: str

class EventModel(BaseModel):
    event_id: str
    subject_id: str
    action: str

class DMPModel(BaseModel):
    record_id: str
    subject_id: str
    decision: str

# -------------------------------
# Endpoints
# -------------------------------
@app.post("/subject/")
def create_subject_api(s: SubjectModel):
    return subject.create_subject(s.id, s.dict())

@app.get("/subject/{subject_id}")
def get_subject_api(subject_id: str):
    return subject.get_subject(subject_id)

@app.post("/ltp_event/")
def create_ltp_event(event: EventModel):
    # In a real app, we would store the event itself.
    # Here we just link it to the subject in LRI.
    relations.link_subject(event.subject_id, event.event_id, "ltp_event")
    return {"status": "linked", "event": event.dict()}

@app.post("/dmp_record/")
def create_dmp_record(record: DMPModel):
    # In a real app, we would store the record itself.
    # Here we just link it to the subject in LRI.
    relations.link_subject(record.subject_id, record.record_id, "dmp_record")
    return {"status": "linked", "record": record.dict()}

@app.get("/subject/{subject_id}/relations")
def list_relations_api(subject_id: str):
    return {"relations": relations.list_relations(subject_id)}

@app.get("/subject/{subject_id}/authority")
def check_authority_api(subject_id: str, action: str):
    return authority.check_authority(subject_id, action)

@app.get("/subject/{subject_id}/continuity")
def check_continuity_api(subject_id: str):
    return authority.validate_continuity(subject_id)

# -------------------------------
# Run service
# -------------------------------
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
