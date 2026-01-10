from typing import Dict
from .access_control import APIKey


class APIKeyStore:
    """
    Minimal in-memory key store.
    Replaceable by DB / Vault later.
    """

    def __init__(self):
        self._keys: Dict[str, APIKey] = {}

    def register_key(self, api_key: APIKey):
        self._keys[api_key.key_id] = api_key

    def get_key(self, key_id: str) -> APIKey | None:
        return self._keys.get(key_id)
