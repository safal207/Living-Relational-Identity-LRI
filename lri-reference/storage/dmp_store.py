import json
from pathlib import Path
from models.decision_record import DecisionRecord

class DMPStore:
    def __init__(self, path: str = "dmp_log.jsonl"):
        self.path = Path(path)

    def append(self, record: DecisionRecord):
        # Ensure parent directory exists if path has parents
        if self.path.parent != Path('.'):
           self.path.parent.mkdir(parents=True, exist_ok=True)

        with self.path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(record.__dict__, default=str) + "\n")
