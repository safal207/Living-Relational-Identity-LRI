from models.identity_state import IdentityState
import dmp
import ltp

def run_identity_cycle(payload: dict):
    subject_id = payload["subject_id"]

    # 1. Load identity
    identity = IdentityState.load(subject_id)

    # 2. Record decision (DMP)
    decision = dmp.record_decision(
        subject_id=subject_id,
        action=payload["action"],
        intention=payload.get("intention"),
        context=payload.get("context", {})
    )

    # 3. Update identity (LRI)
    # The evolve method expects a decision object/dict
    identity.evolve(decision)

    # 4. Save state (Persist before transmit to ensure consistency)
    identity.save()

    # 5. Transmit context (LTP)
    # Transmitting the snapshot of the *new* state
    snapshot = identity.snapshot()
    ltp.transmit_thread(snapshot)

    return snapshot
