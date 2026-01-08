from models.identity_state import IdentityState
from models.metrics import AgentMetrics
from services.metrics_engine import metrics_engine
from services.drift_monitor import drift_monitor
import dmp
import ltp

def run_identity_cycle(payload: dict):
    subject_id = payload["subject_id"]
    action = payload["action"]
    intention = payload.get("intention", "unknown")

    # 1. Load identity
    identity = IdentityState.load(subject_id)

    # 2. Record decision (DMP)
    decision = dmp.record_decision(
        subject_id=subject_id,
        action=action,
        intention=intention,
        context=payload.get("context", {})
    )

    # 3. Update identity (LRI)
    identity.evolve(decision)

    # 4. Save state (Persist before transmit to ensure consistency)
    identity.save()

    # --- Self-Observation (Core Metrics & Drift) ---
    # Record the event in the Metrics Engine
    metrics_engine.record(subject_id, action, intention)

    # Calculate Drift based on the accumulated history
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

    return snapshot
