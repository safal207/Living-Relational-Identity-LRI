import sys
import os
import pytest
from fastapi.testclient import TestClient

# Ensure imports work by adding parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from adapters.ui_multi_agent import app
from services.security import authenticate_user, encrypt_data, decrypt_data

client = TestClient(app)

# Generate tokens for testing
# Note: In a real test setup, we might mock the DB or auth function,
# but here we use the actual implementation as it relies on a static in-memory DB.
admin_token = authenticate_user("admin", "adminpass")
observer_token = authenticate_user("observer", "observerpass")
agent_token = authenticate_user("agent_user", "agentpass")

def test_authenticate_user_valid():
    assert agent_token is not None
    assert observer_token is not None

def test_authenticate_user_invalid():
    token = authenticate_user("agent_user", "wrongpass")
    assert token is None

def test_add_agent_role_agent():
    # Agent role is allowed to add agents
    response = client.post("/add", data={"subject": "A_test_valid", "token": agent_token})
    assert response.status_code == 200
    assert "Агент A_test_valid добавлен" in response.text

def test_add_agent_role_observer_forbidden():
    # Observer role is forbidden from adding agents
    response = client.post("/add", data={"subject": "A_test_fail", "token": observer_token})
    assert response.status_code == 403

def test_add_agent_invalid_token():
    response = client.post("/add", data={"subject": "A_test_invalid", "token": "invalidtoken123"})
    assert response.status_code == 401

def test_agent_interact_allowed():
    # Setup agents first
    client.post("/add", data={"subject": "Actor1", "token": agent_token})
    client.post("/add", data={"subject": "Target1", "token": agent_token})

    # Agent role allowed to interact
    response = client.post("/interact", data={
        "actor": "Actor1",
        "target": "Target1",
        "action": "ping",
        "intention": "test_conn",
        "token": agent_token
    })
    assert response.status_code == 200
    assert "Взаимодействие завершено" in response.text

def test_agent_interact_observer_forbidden():
    response = client.post("/interact", data={
        "actor": "Actor1",
        "target": "Target1",
        "action": "spy",
        "intention": "observe",
        "token": observer_token
    })
    assert response.status_code == 403

def test_encrypt_decrypt():
    secret = "secret_data"
    enc = encrypt_data(secret)
    dec = decrypt_data(enc)
    assert dec == secret
