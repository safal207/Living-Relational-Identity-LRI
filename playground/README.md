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

To launch the interactive mode:
```bash
python playground.py --interactive
```

### Trajectory Snapshots

Snapshots in LRI are not saves.
They are moments of stabilization.

You don't store *who you are*.
You store *how you arrived here* — and choose where to continue.

#### Usage

```bash
> snapshot alpha          # Freeze current trajectory
> snapshots               # List all snapshots
> switch alpha            # Load snapshot (requires confirmation)
> continue                # Explicitly resume

# Branch exploration
> snapshot before_choice
> add_mentor alice dr-smith
> snapshot path_a
> switch before_choice
> add_peer alice bob
> snapshot path_b
```

Snapshots enable:
- **Exploration** without commitment
- **Branching** from stable points
- **Reproducibility** via checksums
- **Temporal agency** over identity evolution

Available commands:
- `add_mentor <subject> <mentor>`
- `add_peer <subject> <peer>`
- `transition <phase>`
- `snapshot <id>`
- `snapshots`
- `switch <id>`
- `continue`
- `show_trajectory`
- `show_state`
- `reset`
