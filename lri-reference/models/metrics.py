from dataclasses import dataclass

@dataclass
class AgentMetrics:
    actions: int
    drift: float
