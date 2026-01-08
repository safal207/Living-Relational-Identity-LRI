from api import subject

class IdentityState:
    def __init__(self, subject_id, trajectory=None):
        self.subject_id = subject_id
        self.trajectory = trajectory or []

    def evolve(self, decision):
        # decision is a dict from dmp.record_decision
        self.trajectory.append({
            "action": decision.get("action"),
            "intention": decision.get("intention"),
            "timestamp": decision.get("timestamp")
        })

    def snapshot(self):
        return {
            "subject_id": self.subject_id,
            "trajectory": self.trajectory
        }

    @classmethod
    def load(cls, subject_id):
        # Try to get subject from in-memory store
        subj_data = subject.get_subject(subject_id)
        if "error" in subj_data:
            # If not found, we treat it as a new identity for simulation purposes
            # or we could raise an error. For this simulation, let's create a transient one
            # if it doesn't exist, OR strictly require it exists.
            # The prompt implies "load", so let's assume it should exist or we initialize empty.
            # Let's initialize a fresh state if not found, but ideally we should create it first.
            return cls(subject_id)

        # Load trajectory if it exists in metadata, otherwise empty
        trajectory = subj_data.get("trajectory", [])
        return cls(subject_id, trajectory)

    def save(self):
        # Update the subject's metadata with the new trajectory
        current = subject.get_subject(self.subject_id)
        if "error" in current:
            # Create if doesn't exist (auto-provisioning for simulation)
            subject.create_subject(self.subject_id, {
                "id": self.subject_id,
                "name": "Simulated Agent",
                "role": "simulated",
                "trajectory": self.trajectory
            })
        else:
            subject.update_subject(self.subject_id, {"trajectory": self.trajectory})
