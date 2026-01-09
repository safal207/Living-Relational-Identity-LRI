from models.identity_state import IdentityState
from models.metrics import AgentMetrics
from services.metrics_engine import metrics_engine
from services.drift_monitor import drift_monitor
from services.dmp_writer import dmp_writer
from services.authority_policy import authority_policy
from models.economic_artifact import EconomicArtifact
from services.artifact_registry import artifact_registry
from fastapi import HTTPException
import dmp
import ltp

def run_identity_cycle(payload: dict):
    subject_id = payload["subject_id"]
    action = payload["action"]
    intention = payload.get("intention", "unknown")

    # 1. Load identity
    identity = IdentityState.load(subject_id)

    # --- Pre-computation for Authority Check ---
    # We need current drift to check authority.
    # In a real system, this might be cached or computed from identity state.
    # Here we peek at metrics engine.
    raw_metrics = metrics_engine.snapshot(subject_id)
    current_drift = drift_monitor.calculate(raw_metrics.get("intentions", []))

    # 2. Authority Check
    if not authority_policy.is_authorized(identity, action, payload.get("context", {}), current_drift):
        # In a real system, we might record a "Rejected" decision in DMP and return error
        # For now, we raise 403
        raise HTTPException(status_code=403, detail="Action unauthorized by LRI Authority Policy")

    # 3. Record decision (DMP)
    decision = dmp.record_decision(
        subject_id=subject_id,
        action=action,
        intention=intention,
        context=payload.get("context", {})
    )

    # 4. Update identity (LRI)
    identity.evolve(decision)

    # 5. Save state (Persist before transmit to ensure consistency)
    identity.save()

    # --- Self-Observation (Core Metrics & Drift) ---
    # Record the event in the Metrics Engine
    metrics_engine.record(subject_id, action, intention)

    # DMP-lite: Record the decision immutably (memory, not brain)
    dmp_writer.record(
        agent_id=subject_id,
        intention=intention,
        decision=action,
        context="interaction"
    )

    # Calculate Drift based on the accumulated history (post-action)
    raw_metrics = metrics_engine.snapshot(subject_id)
    drift_score = drift_monitor.calculate(raw_metrics.get("intentions", []))

    # Create the formal metrics contract
    core_metrics = AgentMetrics(
        actions=raw_metrics.get("actions", 0),
        drift=drift_score
    )
    # -----------------------------------------------

    # 5. Transmit context (LTP)
    # The snapshot now implicitly carries the context of this "living" cycle.
    # In a future PR, we might attach `core_metrics` to the LTP payload or LRI state.
    snapshot = identity.snapshot()

    # Inject metrics into the return value for immediate observability in adapters
    snapshot["metrics"] = {
        "actions": core_metrics.actions,
        "drift": core_metrics.drift
    }

    ltp.transmit_thread(snapshot)

    # === Economic Hooks: создаём артефакт для экспорта ===
    artifact_payload = {
        "identity_state": identity.snapshot(),
        "drift_score": drift_score,
        "decisions_count": len(identity.trajectory)
    }
    economic_artifact = EconomicArtifact(subject_id, artifact_type="cycle_snapshot", payload=artifact_payload)
    artifact_registry.register_artifact(economic_artifact)

    return snapshot
