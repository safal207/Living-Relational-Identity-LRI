from api import subject
import hashlib
import json

class IdentityState:
    def __init__(self, subject_id, trajectory=None, last_hash=None):
        self.subject_id = subject_id
        self.trajectory = trajectory or []
        self.last_hash = last_hash or "0" * 64  # Genesis hash

    def _calculate_hash(self, prev_hash, decision_data):
        """
        Calculates the cryptographic hash of the transition.
        Chain: prev_hash -> decision -> timestamp -> hash
        """
        payload = {
            "prev_hash": prev_hash,
            "action": decision_data.get("action"),
            "intention": decision_data.get("intention"),
            "timestamp": decision_data.get("timestamp"),
            # In a full impl, we would include relation hashes here
        }
        # Use a stable JSON serialization for hashing
        serialized = json.dumps(payload, sort_keys=True, default=str)
        return hashlib.sha256(serialized.encode("utf-8")).hexdigest()

    def evolve(self, decision):
        # decision is a dict from dmp.record_decision

        # Calculate new continuity hash
        new_hash = self._calculate_hash(self.last_hash, decision)

        # Update state
        self.last_hash = new_hash
        self.trajectory.append({
            "action": decision.get("action"),
            "intention": decision.get("intention"),
            "timestamp": decision.get("timestamp"),
            "continuity_hash": new_hash
        })

    def snapshot(self):
        return {
            "subject_id": self.subject_id,
            "trajectory": self.trajectory,
            "head_hash": self.last_hash
        }

    @classmethod
    def load(cls, subject_id):
        # Try to get subject from in-memory store
        subj_data = subject.get_subject(subject_id)
        if "error" in subj_data:
            return cls(subject_id)

        # Load trajectory if it exists in metadata, otherwise empty
        trajectory = subj_data.get("trajectory", [])
        last_hash = subj_data.get("head_hash")

        # If loading an old object without hash, try to find it in trajectory or init genesis
        if not last_hash:
            if trajectory:
                # If we have history but no head_hash, use the last item's hash or default
                last_hash = trajectory[-1].get("continuity_hash", "0" * 64)
            else:
                last_hash = "0" * 64

        return cls(subject_id, trajectory, last_hash)

    def save(self):
        # Update the subject's metadata with the new trajectory and hash
        update_data = {
            "trajectory": self.trajectory,
            "head_hash": self.last_hash
        }

        current = subject.get_subject(self.subject_id)
        if "error" in current:
            # Create if doesn't exist (auto-provisioning for simulation)
            subject.create_subject(self.subject_id, {
                "id": self.subject_id,
                "name": "Simulated Agent",
                "role": "simulated",
                **update_data
            })
        else:
            subject.update_subject(self.subject_id, update_data)
