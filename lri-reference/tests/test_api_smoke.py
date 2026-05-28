from fastapi.testclient import TestClient
from main import app, key_store
from security.access_control import APIKey, AccessScope
from api.subject import subjects

client = TestClient(app)

def setup_module():
    subjects.clear()
    key_store.register_key(APIKey("test-key-continuity", [AccessScope.READ_CONTINUITY]))


class TestSubjectAPI:
    def test_create_subject(self):
        response = client.post("/subject/", json={"id": "smoke-1", "name": "Smoke", "role": "tester"})
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "created"

    def test_create_duplicate_subject(self):
        response = client.post("/subject/", json={"id": "smoke-1", "name": "Smoke", "role": "tester"})
        assert response.status_code == 200
        data = response.json()
        assert data.get("error") == "Subject already exists"

    def test_get_subject(self):
        response = client.get("/subject/smoke-1")
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == "smoke-1"

    def test_get_nonexistent_subject(self):
        response = client.get("/subject/nonexistent")
        assert response.status_code == 200
        data = response.json()
        assert "error" in data


class TestRelationsAPI:
    def test_list_relations_empty(self):
        response = client.get("/subject/smoke-1/relations")
        assert response.status_code == 200
        data = response.json()
        assert data["relations"] == []

    def test_ltp_event_creates_relation(self):
        response = client.post("/ltp_event/", json={"event_id": "evt-1", "subject_id": "smoke-1", "action": "test"})
        assert response.status_code == 200

    def test_dmp_record_creates_relation(self):
        response = client.post("/dmp_record/", json={"record_id": "rec-1", "subject_id": "smoke-1", "decision": "approve"})
        assert response.status_code == 200

    def test_list_relations_after_events(self):
        response = client.get("/subject/smoke-1/relations")
        assert response.status_code == 200
        data = response.json()
        assert len(data["relations"]) == 2


class TestAuthorityAPI:
    def test_check_authority(self):
        response = client.get("/subject/smoke-1/authority", params={"action": "test_action"})
        assert response.status_code == 200
        data = response.json()
        assert data["authorized"] is True

    def test_check_continuity_authorized(self):
        response = client.get("/subject/smoke-1/continuity", params={"api_key": "test-key-continuity"})
        assert response.status_code == 200
        data = response.json()
        assert data["continuous"] is True

    def test_check_continuity_unauthorized(self):
        response = client.get("/subject/smoke-1/continuity", params={"api_key": "invalid-key"})
        assert response.status_code == 403


class TestObserverAPI:
    def test_observer_snapshot(self):
        response = client.get("/observer/subject/smoke-1/snapshot")
        assert response.status_code == 200
        data = response.json()
        assert data["subject_id"] == "smoke-1"

    def test_observer_continuity(self):
        response = client.get("/observer/subject/smoke-1/continuity")
        assert response.status_code == 200
        data = response.json()
        assert "status" in data

    def test_observer_drift(self):
        response = client.get("/observer/subject/smoke-1/drift")
        assert response.status_code == 200
        data = response.json()
        assert "drift_score" in data


class TestSimulateCycleAPI:
    def test_simulate_cycle(self):
        response = client.post("/simulate/cycle", json={
            "subject_id": "smoke-1",
            "action": "login",
            "intention": "access"
        })
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "cycle_completed"
