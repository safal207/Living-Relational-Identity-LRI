# Reference Payloads

This document provides skeleton JSON payloads for the core LRI data structures. These serve as the reference implementation format for integration.

## 1. LRI Subject (with Relations)

A standard Subject object representing an identity state.

```json
{
  "subject": {
    "lri_id": "did:lri:b34c-89df-22a1",
    "version": 12,
    "state_hash": "sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "created_at": "2023-10-27T14:00:00Z",
    "last_updated_at": "2023-11-05T09:30:00Z",
    "status": "ACTIVE",
    "keys": {
      "primary_sign_key": "ed25519:MCOWBQYDK2VwAyE...",
      "recovery_key": "ed25519:KBxK7..."
    },
    "relations": [
      {
        "target_id": "did:lri:system-root-01",
        "type": "PARENT",
        "established_at": "2023-10-27T14:00:00Z",
        "metadata": {
          "permissions": ["audit", "shutdown"]
        }
      },
      {
        "target_id": "did:lri:agent-colleague-55",
        "type": "PEER",
        "established_at": "2023-11-01T10:15:00Z"
      }
    ]
  }
}
```

## 2. LTP Stream Event (Linked to LRI)

An example of a message in the Liminal Thread Protocol (LTP) that is cryptographically anchored to an LRI identity.

```json
{
  "ltp_event": {
    "event_id": "evt_99887766",
    "thread_id": "th_112233",
    "timestamp": "2023-11-05T09:35:12Z",
    "type": "MESSAGE",
    "payload": {
      "content": "Deploying update to staging environment.",
      "content_type": "text/plain"
    },
    "sender_context": {
      "lri_id": "did:lri:b34c-89df-22a1",
      "lri_state_hash_at_sending": "sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    },
    "signature": "sig_ed25519:77665544..." // Signs (event_id + timestamp + payload + sender_context) using LRI primary key
  }
}
```

## 3. DMP Decision Record (Linked to LRI)

An example of a Decision Memory Protocol (DMP) record, showing how a decision is attributed to an LRI subject for accountability.

```json
{
  "dmp_record": {
    "decision_id": "dec_55443322",
    "timestamp": "2023-11-05T09:40:00Z",
    "context_hash": "sha256:aabbcc...",
    "outcome": {
      "action": "APPROVE_DEPLOY",
      "target": "staging-cluster-01"
    },
    "reasoning_snapshot": "Metrics within nominal range. Tests passed.",
    "authority_proof": {
      "author_lri_id": "did:lri:b34c-89df-22a1",
      "checked_at": "2023-11-05T09:39:55Z",
      "authority_token": "tok_signed_by_lri_core..." // Proof that 'checkAuthority' returned true
    },
    "signature": "sig_ed25519:112233..." // Signs the entire record using LRI primary key
  }
}
```
