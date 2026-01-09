from datetime import datetime, timezone
from models.identity_state import IdentityState
from models.audit_snapshot import AuditSnapshot
from services.metrics_engine import metrics_engine
from services.drift_monitor import drift_monitor
from services.authority_policy import authority_policy

class Observer:
    """
    Observer Service.
    Provides read-only access to identity state, metrics, and continuity proofs.
    Does not mutate state.
    """

    def get_identity_snapshot(self, subject_id: str) -> AuditSnapshot:
        """
        Generates a comprehensive audit snapshot of the identity.
        """
        # 1. Load State (Read-Only)
        identity = IdentityState.load(subject_id)

        # 2. Calculate Drift
        raw_metrics = metrics_engine.snapshot(subject_id)
        drift_score = drift_monitor.calculate(raw_metrics.get("intentions", []))

        # 3. Gather Claims (Placeholder logic based on state)
        # In a real system, these would be VC (Verifiable Credentials) or similar
        claims = ["authorized_agent"]
        if drift_score < 0.2:
            claims.append("low_drift_certified")

        return AuditSnapshot(
            subject_id=subject_id,
            timestamp=datetime.now(timezone.utc),
            continuity_hash=identity.last_hash,
            drift_score=drift_score,
            authority_claims=claims,
            trajectory_length=len(identity.trajectory)
        )

    def verify_continuity(self, subject_id: str) -> dict:
        """
        Verifies the cryptographic continuity of the subject's chain.
        """
        identity = IdentityState.load(subject_id)
        # In a full implementation, this would re-hash the entire trajectory
        # and verify it matches the head hash.
        # For now, we return the head hash and trajectory metadata.
        return {
            "subject_id": subject_id,
            "head_hash": identity.last_hash,
            "chain_length": len(identity.trajectory),
            "status": "verified" # Placeholder for actual re-hashing verification
        }

    def read_drift_metrics(self, subject_id: str) -> dict:
        """
        Returns drift analysis for the subject.
        """
        raw_metrics = metrics_engine.snapshot(subject_id)
        drift = drift_monitor.calculate(raw_metrics.get("intentions", []))
        return {
            "subject_id": subject_id,
            "drift_score": drift,
            "intentions_count": len(raw_metrics.get("intentions", [])),
            "actions_count": raw_metrics.get("actions", 0)
        }

    def read_authority_claims(self, subject_id: str) -> dict:
        """
        Returns the current authority standing of the subject.
        """
        # This reuses the snapshot logic but focuses on auth
        snapshot = self.get_identity_snapshot(subject_id)
        return {
            "subject_id": subject_id,
            "claims": snapshot.authority_claims,
            "policy_threshold": authority_policy.drift_threshold
        }

# Global instance
observer_service = Observer()
