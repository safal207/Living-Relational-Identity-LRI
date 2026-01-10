import sys
import os
import uvicorn
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

# Ensure we can import from services sibling directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from api import subject
from services.cycle_engine import run_identity_cycle
from models.identity_state import IdentityState

app = FastAPI(title="Alice in Action Demo")

# Initialize Alice if not exists
subject_id = "alice-demo-001"
if "error" in subject.get_subject(subject_id):
    subject.create_subject(subject_id, {
        "id": subject_id,
        "name": "Alice",
        "role": "student",
        "trajectory": []
    })

@app.get("/", response_class=HTMLResponse)
def index():
    # Fetch current state
    subj = subject.get_subject(subject_id)
    identity = IdentityState.load(subject_id)
    trajectory = identity.trajectory

    # Calculate drift/coherence
    drift = 0.0
    if hasattr(identity, 'metrics') and identity.metrics: # Usually computed in cycle
         pass
         # In cycle_engine it returns snapshot with metrics, but IdentityState in memory might not have it attached directly unless saved

    # For demo visualization, let's just grab the last snapshot or re-calculate if needed.
    # But since cycle_engine updates metrics engine, we can query metrics engine?
    # Simpler: just use trajectory length for now or last known drift.

    # Let's simple format the trajectory HTML
    traj_html = ""
    for step in reversed(trajectory):
        traj_html += f"""
        <div class="step">
            <span class="timestamp">{step.get('timestamp', '')}</span>
            <span class="action">Action: {step.get('action')}</span>
            <span class="intention">Intention: {step.get('intention')}</span>
            <span class="hash" title="{step.get('continuity_hash')}">Hash: {step.get('continuity_hash')[:8]}...</span>
        </div>
        """

    current_role = subj.get("role", "student")
    role_color = "gray"
    if current_role == "student": role_color = "#3498db"
    elif current_role == "apprentice": role_color = "#f1c40f"
    elif current_role == "mentor": role_color = "#2ecc71"

    # Simulate Coherence Score visualization
    # In a real app, this comes from `identity.metrics.drift`
    # We'll calculate a "Coherence" (1.0 - drift) based on trajectory length or simulated errors
    # For demo: randomly fluctuate or decay slightly with actions unless maintained

    # Check if last action was an error
    last_action = trajectory[-1].get("action") if trajectory else ""
    is_error_state = "error" in last_action or "break" in last_action

    coherence = 1.0
    if is_error_state:
        coherence = 0.45 # Low coherence due to error
    elif len(trajectory) > 0:
        # Simulate organic fluctuation
        coherence = max(0.7, 1.0 - (len(trajectory) * 0.05))
        if current_role == "mentor": coherence = 0.98 # High coherence for mentors

    coherence_color = "#2ecc71" if coherence > 0.8 else "#f1c40f" if coherence > 0.5 else "#e74c3c"
    coherence_percent = int(coherence * 100)

    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Alice in Action - LRI Demo</title>
        <style>
            body {{ font-family: sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; background-color: #f4f4f9; }}
            h1 {{ color: #333; }}
            .card {{ background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); margin-bottom: 20px; }}
            .status-badge {{ background-color: {role_color}; color: white; padding: 5px 10px; border-radius: 15px; font-weight: bold; text-transform: uppercase; }}
            .coherence-badge {{ background-color: {coherence_color}; color: white; padding: 5px 10px; border-radius: 15px; font-weight: bold; }}
            .step {{ border-left: 4px solid #3498db; padding-left: 10px; margin-bottom: 10px; background: #fafafa; padding: 10px; }}
            .step:first-child {{ border-left-color: {coherence_color}; background: #e8f8f5; }}
            .controls button {{ padding: 10px 15px; margin-right: 10px; cursor: pointer; border: none; border-radius: 5px; font-size: 14px; transition: background 0.3s; }}
            .btn-action {{ background-color: #3498db; color: white; }}
            .btn-promote {{ background-color: #9b59b6; color: white; }}
            .btn-error {{ background-color: #e74c3c; color: white; }}
            .btn-reset {{ background-color: #95a5a6; color: white; float: right; }}
            .btn-action:hover {{ background-color: #2980b9; }}
            .timestamp {{ color: #7f8c8d; font-size: 0.8em; display: block; }}
            .hash {{ font-family: monospace; color: #95a5a6; font-size: 0.8em; }}
            .meter-container {{ background-color: #ecf0f1; border-radius: 10px; height: 20px; width: 200px; display: inline-block; vertical-align: middle; margin-left: 10px; }}
            .meter-fill {{ background-color: {coherence_color}; height: 100%; border-radius: 10px; width: {coherence_percent}%; transition: width 0.5s; }}
        </style>
        <script>
            function showError(msg) {{
                alert("LRI Protocol Error:\\n" + msg);
            }}
        </script>
    </head>
    <body onload="{ "showError('LRI_DRIFT_DETECTED: Identity Coherence critical (< 0.5)')" if is_error_state else "" }">
        <h1>👩‍🎓 Alice in Action <span style="font-size:0.5em; color:#7f8c8d;">LRI v1.0.0 Demo</span></h1>

        <div class="card">
            <h2>
                State: <span class="status-badge">{current_role}</span>
            </h2>
            <p>
                <strong>Coherence Score:</strong>
                <span class="meter-container"><div class="meter-fill"></div></span>
                <span class="coherence-badge">{coherence_percent}%</span>
            </p>
            <p><strong>Subject ID:</strong> {subject_id}</p>
            <p><strong>Head Hash:</strong> <code style="word-break: break-all;">{identity.last_hash}</code></p>

            <div class="controls">
                <form action="/act" method="post" style="display:inline;">
                    <input type="hidden" name="action_type" value="study">
                    <button type="submit" class="btn-action">📚 Study (Add Action)</button>
                </form>

                <form action="/promote" method="post" style="display:inline;">
                     <button type="submit" class="btn-promote">🌟 Promote Alice</button>
                </form>

                <form action="/error" method="post" style="display:inline;">
                     <button type="submit" class="btn-error">⚠️ Simulate Error</button>
                </form>

                <form action="/reset" method="post" style="display:inline;">
                     <button type="submit" class="btn-reset">Reset</button>
                </form>
            </div>
        </div>

        <div class="card">
            <h3>Evolution Trajectory (Chain of Custody)</h3>
            {traj_html if trajectory else "<p>No history yet. Start Alice's journey!</p>"}
        </div>

        <p style="text-align:center; color:#bdc3c7; font-size:0.8em;">LRI Reference Implementation</p>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

@app.post("/act", response_class=HTMLResponse)
def act(action_type: str = Form(...)):
    # Simulate a study action
    payload = {
        "subject_id": subject_id,
        "action": "study_session",
        "intention": "increase_competence",
        "context": {"module": "advanced_lri"}
    }
    run_identity_cycle(payload)
    return index()

@app.post("/promote", response_class=HTMLResponse)
def promote():
    # Logic to promote based on current role
    subj = subject.get_subject(subject_id)
    current_role = subj.get("role", "student")

    new_role = current_role
    action = "promote_attempt"

    if current_role == "student":
        new_role = "apprentice"
        action = "promote_to_apprentice"
    elif current_role == "apprentice":
        new_role = "mentor"
        action = "promote_to_mentor"

    # 1. Run cycle to record the promotion event
    payload = {
        "subject_id": subject_id,
        "action": action,
        "intention": "career_growth",
        "context": {"old_role": current_role, "new_role": new_role}
    }
    run_identity_cycle(payload)

    # 2. Actually update the role in the subject registry (simulating external system update reacting to LRI)
    subject.update_subject(subject_id, {"role": new_role})

    return index()

@app.post("/error", response_class=HTMLResponse)
def trigger_error():
    # Simulate an error (Unauthorized or Validation)
    # We can try to run an unauthorized action or just flash a message
    # For this demo, let's try to pass an empty action which might fail validation if we had strict validation
    # Or we can just simulate a "drift" error visualization

    # Let's record a "mistake" that increases drift?
    payload = {
        "subject_id": subject_id,
        "action": "break_production",
        "intention": "unknown_chaos",
        "context": {"severity": "high"}
    }
    run_identity_cycle(payload)
    return index()

@app.post("/reset", response_class=HTMLResponse)
def reset():
    # Reset Alice
    subject.delete_subject(subject_id)
    subject.create_subject(subject_id, {
        "id": subject_id,
        "name": "Alice",
        "role": "student",
        "trajectory": []
    })
    return index()

if __name__ == "__main__":
    print("Starting Alice Demo on http://0.0.0.0:8005")
    uvicorn.run(app, host="0.0.0.0", port=8005)
