# LRI Reference Implementation Skeleton

This is a minimal reference skeleton for the Living-Relational-Identity (LRI) protocol.

## Structure

*   `api/`: Python modules for Subject CRUD, Relations, and Authority checks.
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

#### Live Demo Workflow

1.  **Create Subject:**
    ```bash
    curl -X POST "http://localhost:8000/subject/" \
         -H "Content-Type: application/json" \
         -d '{"id": "subj-001", "name": "Alice", "role": "agent"}'
    ```

2.  **Link LTP Event:**
    ```bash
    curl -X POST "http://localhost:8000/ltp_event/" \
         -H "Content-Type: application/json" \
         -d '{"event_id": "ltp-100", "subject_id": "subj-001", "action": "trade"}'
    ```

3.  **Link DMP Record:**
    ```bash
    curl -X POST "http://localhost:8000/dmp_record/" \
         -H "Content-Type: application/json" \
         -d '{"record_id": "dmp-500", "subject_id": "subj-001", "decision": "approved"}'
    ```

4.  **Check Relations:**
    ```bash
    curl "http://localhost:8000/subject/subj-001/relations"
    ```

5.  **Check Authority:**
    ```bash
    curl "http://localhost:8000/subject/subj-001/authority?action=trade"
    ```
