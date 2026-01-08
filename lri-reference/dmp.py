from api import relations
import datetime
import uuid

def record_decision(subject_id, action, intention=None, context=None):
    """
    Simulates a DMP (Decision Memory Protocol) recording.
    """
    record_id = f"dmp-{uuid.uuid4().hex[:8]}"
    timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()

    decision_record = {
        "record_id": record_id,
        "subject_id": subject_id,
        "action": action,
        "intention": intention,
        "context": context,
        "timestamp": timestamp,
        "decision": "approved" # Simplified for simulation
    }

    # Link via LRI
    relations.link_subject(subject_id, record_id, "dmp_decision")

    return decision_record
