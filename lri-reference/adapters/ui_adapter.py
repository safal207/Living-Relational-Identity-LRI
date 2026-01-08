from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import sys
import os
import uvicorn

# Ensure we can import from services sibling directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from services.cycle_engine import run_identity_cycle

app = FastAPI(title="LPI UI Adapter")

@app.get("/", response_class=HTMLResponse)
def index():
    return """
    <html>
        <body>
            <h2>LPI UI Adapter</h2>
            <form action="/simulate" method="post">
                Subject ID: <input name="subject" value="user-001"><br>
                Action: <input name="action" value="login"><br>
                Intention: <input name="intention" value="access_dashboard"><br>
                <button type="submit">Run Cycle</button>
            </form>
        </body>
    </html>
    """

@app.post("/simulate", response_class=HTMLResponse)
def simulate(subject: str = Form(...), action: str = Form(...), intention: str = Form(...)):
    payload = {"subject_id": subject, "action": action, "intention": intention, "context": {}}
    result = run_identity_cycle(payload)
    traj_html = "<ul>"
    for step in result["trajectory"]:
        traj_html += f"<li>{step['timestamp']}: {step['action']} ({step['intention']})</li>"
    traj_html += "</ul>"
    return f"<h3>Цикл завершён ✅</h3>{traj_html}<a href='/'>Назад</a>"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
