from typing import List

class DriftMonitor:
    def calculate(self, intentions: List[str]) -> float:
        """
        Calculates the 'Identity Drift' based on the diversity/divergence of intentions.

        Formula: Density of unique intentions / Total intentions.
        0.0 = No intentions yet.
        Low value = High consistency (repeating same intentions).
        High value = High divergence (doing many different things).
        """
        if not intentions:
            return 0.0
        return len(set(intentions)) / len(intentions)

# Global instance
drift_monitor = DriftMonitor()
