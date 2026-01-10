# LRI Reference Implementation Skeleton

This is a minimal reference skeleton for the Living-Relational-Identity (LRI) protocol.

## Structure

*   `api/`: Python modules for Subject CRUD, Relations, Authority checks, and Simulation.
*   `adapters/`: CLI and UI adapters for interactive simulation.
*   `models/`: Data models for Identity State (for simulation).
*   `services/`: Logic for the Identity Cycle Engine and Multi-Agent Environment.
*   `examples/`: JSON reference payloads for Subjects, LTP events, and DMP records.
*   `main.py`: A FastAPI service demonstrating LRI integration.

## Installation

1.  Navigate to the `lri-reference` directory.
2.  Install requirements:
    ```bash
    pip install -r requirements.txt
    ```

## Quick Start (Alice's Journey)

To see LRI in action in under 1 minute:

### 1. Simple Script
See Alice create an identity, apply an action, and evolve.

```bash
python examples/hello_alice.py
```

### 2. Interactive Demo ("Alice in Action")
Run a visual web interface to guide Alice from Student → Apprentice → Mentor.

```bash
python examples/alice_demo_server.py
```
Open `http://localhost:8005` in your browser.

---

## How to run

### 1. PoC Integration Script (CLI)

To see a full demonstration of LRI integrating with LTP (Liminal Thread Protocol) events and DMP (Decision Memory Protocol) records via CLI:

```bash
python examples/poc_integration.py
```

### 2. Live API Service (FastAPI)

To run the LRI Integration Service:

```bash
python main.py
```

The service will start on `http://0.0.0.0:8000`. You can access the auto-generated documentation at `http://0.0.0.0:8000/docs`.

### 3. LPI Adapters (PR #8)

#### CLI Adapter
Interact with the system organically from the command line:

```bash
python adapters/cli_adapter.py simulate --subject "user-cli-001" --action "login" --intention "access_cli"
```

#### UI Adapter
Run a minimal web interface for testing identity cycles:

```bash
python adapters/ui_adapter.py
```
Open `http://0.0.0.0:8001` in your browser.

### 4. Multi-Agent Simulation (PR #9 & PR #10)

#### CLI Shell
Run the interactive multi-agent shell to simulate interactions between multiple entities via command line:

```bash
python adapters/cli_multi_agent.py
```

#### Multi-Agent UI Adapter (PR #10 & PR #12)
Run a web interface to visualize and manage multiple agents with **security controls**:

```bash
python adapters/ui_multi_agent.py
```
Open `http://0.0.0.0:8002` in your browser.

*   **Login**: Use the built-in login form to generate a JWT token.
    *   Default credentials: `agent_user` / `agentpass`
*   **Add Agent**: Requires a valid token with `agent` role.
*   **Interact**: Requires a valid token with `agent` role.
*   **Visualize**: See real-time trajectory updates.

### Core Features

#### PR #14: Drift & Metrics Engine (Self-Observation)

LRI now tracks its own behavior patterns:
- **Metrics Engine**: Records all actions and intentions in a central registry.
- **Drift Monitor**: Calculates the divergence of an agent's intentions (`drift score`).
- **Core Integration**: Every identity cycle now automatically updates metrics and calculates drift, which is returned in the simulation snapshot.

---

#### Identity Cycle Simulation (PR #7)

You can now simulate a full **LPI → DMP → LRI → LTP** identity cycle with a single endpoint.

**POST** `/simulate/cycle`

```bash
curl -X POST "http://localhost:8000/simulate/cycle" \
     -H "Content-Type: application/json" \
     -d '{
           "subject_id": "user-001",
           "action": "launch_poc_api",
           "intention": "validate architecture idea",
           "context": {
             "risk_level": "medium",
             "time_horizon": "2_weeks"
           }
         }'
```
