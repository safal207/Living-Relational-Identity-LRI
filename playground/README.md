# LRI Interactive Playground

This playground demonstrates how a Living Relational Identity
evolves over time using story-driven scenarios.

The goal is not correctness of math,
but clarity of protocol behavior.

## How it works
- Each YAML file represents a **story moment**
- The playground applies it sequentially
- Identity state, coherence and lifecycle are validated

⚠️ Coherence changes are intentionally mocked.

## Run
```bash
pip install -r requirements.txt
python playground.py
```
