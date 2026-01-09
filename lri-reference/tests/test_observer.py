from fastapi.testclient import TestClient
from main import app
from models.identity_state import IdentityState
from services.metrics_engine import metrics_engine
from services.observer import observer_service

client = TestClient(app)

def test_observer_snapshot_api():
    subject_id = "test_observer_agent"

    # Pre-populate state
    identity = IdentityState(subject_id)
    decision = {
        "action": "test_action",
        "intention": "test_intent",
        "timestamp": "2023-10-27T10:00:00Z"
    }
    identity.evolve(decision)
    identity.save()

    metrics_engine.record(subject_id, "test_action", "test_intent")

    # Call API
    response = client.get(f"/observer/subject/{subject_id}/snapshot")
    assert response.status_code == 200
    data = response.json()

    assert data["subject_id"] == subject_id
    assert data["continuity_hash"] == identity.last_hash
    assert data["drift_score"] == 1.0 # 1 unique intention / 1 total = 1.0
    # Actually, let's just check the field exists for now.
    assert "drift_score" in data
    assert "authority_claims" in data

def test_observer_continuity_api():
    subject_id = "test_continuity_agent"
    identity = IdentityState(subject_id)
    identity.save()

    response = client.get(f"/observer/subject/{subject_id}/continuity")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "verified"
    assert "head_hash" in data

def test_observer_drift_api():
    subject_id = "test_drift_agent"
    # Populate some metrics
    metrics_engine.record(subject_id, "a1", "i1")
    metrics_engine.record(subject_id, "a2", "i1")

    response = client.get(f"/observer/subject/{subject_id}/drift")
    assert response.status_code == 200
    data = response.json()
    assert data["intentions_count"] == 2
    assert "drift_score" in data
