import pytest
from models.identity_state import IdentityState
from services.authority_policy import AuthorityPolicy

def test_continuity_hashing():
    # 1. Initialize
    agent_id = "test_agent_continuity"
    identity = IdentityState(agent_id)
    assert identity.last_hash == "0" * 64

    # 2. Evolve (First Step)
    decision1 = {
        "action": "step1",
        "intention": "init",
        "timestamp": "2023-01-01T10:00:00Z"
    }
    identity.evolve(decision1)
    hash1 = identity.last_hash
    assert hash1 != "0" * 64
    assert identity.trajectory[-1]["continuity_hash"] == hash1

    # 3. Evolve (Second Step)
    decision2 = {
        "action": "step2",
        "intention": "follow_up",
        "timestamp": "2023-01-01T10:01:00Z"
    }
    identity.evolve(decision2)
    hash2 = identity.last_hash
    assert hash2 != hash1

    # 4. Verify Determinism (Manually recalc)
    # We create a new instance with the state at step 1
    recalc_identity = IdentityState(agent_id, trajectory=[], last_hash=hash1)

    # Calculate what hash2 should be manually
    calculated_hash = recalc_identity._calculate_hash(hash1, decision2)
    assert calculated_hash == hash2

def test_authority_policy_drift():
    policy = AuthorityPolicy(drift_threshold=0.5)
    identity = IdentityState("test_agent_auth")

    # Case 1: Low drift, any action ok
    assert policy.is_authorized(identity, "normal_action", {}, drift_score=0.1) == True
    assert policy.is_authorized(identity, "critical_action", {}, drift_score=0.1) == True

    # Case 2: High drift, critical action rejected
    assert policy.is_authorized(identity, "normal_action", {}, drift_score=0.9) == True
    assert policy.is_authorized(identity, "critical_action", {}, drift_score=0.9) == False
