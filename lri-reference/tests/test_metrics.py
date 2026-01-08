import sys
import os
import pytest
from collections import defaultdict

# Ensure imports work
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from services.metrics_engine import MetricsEngine
from services.drift_monitor import DriftMonitor

def test_metrics_engine_record():
    engine = MetricsEngine()
    engine.record("agent_1", "run", "speed")
    engine.record("agent_1", "jump", "height")

    snapshot = engine.snapshot("agent_1")
    assert snapshot["actions"] == 2
    assert snapshot["intentions"] == ["speed", "height"]

    snapshot_empty = engine.snapshot("agent_2")
    assert snapshot_empty == {}

def test_drift_monitor_calculate():
    monitor = DriftMonitor()

    # Empty
    assert monitor.calculate([]) == 0.0

    # Low drift (consistent)
    # 2 unique out of 4 total = 0.5
    assert monitor.calculate(["a", "a", "b", "b"]) == 0.5

    # High drift (divergent)
    # 4 unique out of 4 total = 1.0
    assert monitor.calculate(["a", "b", "c", "d"]) == 1.0

    # Single item
    assert monitor.calculate(["a"]) == 1.0
