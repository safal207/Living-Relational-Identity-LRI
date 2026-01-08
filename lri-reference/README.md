# LRI Reference Implementation Skeleton

This is a minimal reference skeleton for the Living-Relational-Identity (LRI) protocol.

## Structure

*   `api/`: Python modules for Subject CRUD, Relations, Authority checks, and Simulation.
*   `adapters/`: CLI and UI adapters for interactive simulation.
*   `models/`: Data models for Identity State (for simulation).
*   `services/`: Logic for the Identity Cycle Engine.
*   `examples/`: JSON reference payloads for Subjects, LTP events, and DMP records.
*   `main.py`: A FastAPI service demonstrating LRI integration.

## Installation

1.  Navigate to the `lri-reference` directory.
2.  Install requirements:
    ```bash
    pip install -r requirements.txt
    ```

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

Or interactively:
```bash
python adapters/cli_adapter.py simulate
```

#### UI Adapter
Run a minimal web interface for testing identity cycles:

```bash
python adapters/ui_adapter.py
```
Open `http://0.0.0.0:8001` in your browser.

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

This will:
1.  **Load** the identity (creating it if necessary).
2.  **Record** a decision in DMP (mock).
3.  **Evolve** the LRI identity state based on the decision.
4.  **Transmit** the new context via LTP (mock).
5.  Return the updated **Identity Snapshot**.
