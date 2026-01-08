from api import relations
import datetime
import uuid

def transmit_thread(payload):
    """
    Simulates an LTP (Liminal Thread Protocol) transmission.
    """
    event_id = f"ltp-{uuid.uuid4().hex[:8]}"
    timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
    subject_id = payload.get("subject_id")

    ltp_event = {
        "event_id": event_id,
        "subject_id": subject_id,
        "type": "IDENTITY_SNAPSHOT",
        "payload": payload,
        "timestamp": timestamp
    }

    # Link via LRI if subject exists in payload
    if subject_id:
        relations.link_subject(subject_id, event_id, "ltp_transmission")

    return ltp_event
