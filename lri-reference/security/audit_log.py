from datetime import datetime


class AuditLog:
    @staticmethod
    def record(event: str, subject_id: str | None = None, api_key: str | None = None):
        entry = {
            "ts": datetime.utcnow().isoformat(),
            "event": event,
            "subject_id": subject_id,
            "api_key": api_key,
        }
        # MVP: stdout / file
        print("[AUDIT]", entry)
