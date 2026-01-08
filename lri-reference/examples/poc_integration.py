import sys
import os
import json

# Ensure we can import from api sibling directory if running directly
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from api import subject, relations, authority

def run_poc():
    print("=== LRI PoC Integration: LRI ↔ LTP / DMP ===\n")

    # -------------------------------
    # 1. Create Subject
    # -------------------------------
    subject_data = {
        "id": "subj-001",
        "name": "Alice",
        "role": "agent",
        "created_at": "2026-01-08T00:00:00Z"
    }

    res_create = subject.create_subject(subject_data["id"], subject_data)
    print(f"[1] Created Subject:\n{json.dumps(res_create, indent=2)}\n")

    # -------------------------------
    # 2. Create LTP Event
    # -------------------------------
    ltp_event = {
        "event_id": "ltp-001",
        "subject_id": "subj-001",
        "action": "trade",
        "timestamp": "2026-01-08T00:01:00Z"
    }

    # Link event to subject
    relations.link_subject(subject_data["id"], ltp_event["event_id"], "LTP_EVENT")
    print(f"[2] Linked LTP Event:\n{json.dumps(ltp_event, indent=2)}\n")

    # -------------------------------
    # 3. Create DMP Record
    # -------------------------------
    dmp_record = {
        "record_id": "dmp-001",
        "subject_id": "subj-001",
        "decision": "approved",
        "timestamp": "2026-01-08T00:02:00Z"
    }

    # Link record to subject
    relations.link_subject(subject_data["id"], dmp_record["record_id"], "DMP_RECORD")
    print(f"[3] Linked DMP Record:\n{json.dumps(dmp_record, indent=2)}\n")

    # -------------------------------
    # 4. Check Authority and Continuity
    # -------------------------------
    auth_check = authority.check_authority(subject_data["id"], "trade")
    continuity_check = authority.validate_continuity(subject_data["id"])
    print(f"[4] Authority Check:\n{json.dumps(auth_check, indent=2)}")
    print(f"    Continuity Check:\n{json.dumps(continuity_check, indent=2)}\n")

    # -------------------------------
    # 5. List All Relations
    # -------------------------------
    all_relations = relations.list_relations(subject_data["id"])
    print(f"[5] All Relations for Subject {subject_data['id']}:\n{json.dumps(all_relations, indent=2)}\n")

    print("=== PoC Integration Completed Successfully ===")

if __name__ == "__main__":
    run_poc()
