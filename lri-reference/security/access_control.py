from typing import List


class AccessScope:
    READ_ARTIFACT = "read:artifact"
    READ_CONTINUITY = "read:continuity"
    WRITE_DECISION = "write:decision"


class APIKey:
    def __init__(self, key_id: str, scopes: List[str]):
        self.key_id = key_id
        self.scopes = scopes

    def allows(self, scope: str) -> bool:
        return scope in self.scopes
