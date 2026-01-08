from fastapi import FastAPI, Form, HTTPException, Response
from fastapi.responses import HTMLResponse, JSONResponse
import sys
import os
import uvicorn

# Ensure we can import from services sibling directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from services.multi_agent_engine import MultiAgentEnvironment
from services.security import authenticate_user, get_current_user, require_role

app = FastAPI(title="Multi-Agent LRI UI")
env = MultiAgentEnvironment()

@app.get("/", response_class=HTMLResponse)
def index():
    agents_list = "".join(f"<li>{agent}</li>" for agent in env.agents)
    return f"""
    <html>
    <body>
        <h2>Multi-Agent LRI UI (Secured)</h2>

        <div style="border: 1px solid #ccc; padding: 10px; margin-bottom: 20px;">
            <h3>Login (Get Token)</h3>
            <form action="/login" method="post" target="_blank">
                Username: <input name="username" value="agent_user"><br>
                Password: <input name="password" type="password" value="agentpass"><br>
                <button type="submit">Get Token</button>
            </form>
            <p><small>Roles: admin/adminpass, agent_user/agentpass, observer/observerpass</small></p>
        </div>

        <h3>Агенты:</h3>
        <ul>{agents_list}</ul>

        <h3>Добавить агента (Role: agent):</h3>
        <form action="/add" method="post">
            Token: <input name="token" placeholder="Paste Token Here" required><br>
            Subject ID: <input name="subject"><br>
            <button type="submit">Add</button>
        </form>

        <h3>Симуляция взаимодействия (Role: agent):</h3>
        <form action="/interact" method="post">
            Token: <input name="token" placeholder="Paste Token Here" required><br>
            Actor ID: <input name="actor"><br>
            Target ID: <input name="target"><br>
            Action: <input name="action"><br>
            Intention: <input name="intention"><br>
            <button type="submit">Interact</button>
        </form>
    </body>
    </html>
    """

@app.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    token = authenticate_user(username, password)
    if not token:
        return {"error": "Invalid credentials"}
    return {"token": token, "info": "Copy this token and paste it into the forms"}

@app.post("/add", response_class=HTMLResponse)
def add_agent(response: Response, subject: str = Form(...), token: str = Form(...)):
    try:
        user = get_current_user(token)
        require_role(user, "agent")
        env.add_agent(subject)
        return f"<h3>Агент {subject} добавлен ✅</h3><a href='/'>Назад</a>"
    except HTTPException as e:
        response.status_code = e.status_code
        return f"<h3>Error: {e.detail}</h3><a href='/'>Назад</a>"
    except Exception as e:
        response.status_code = 500
        return f"<h3>Error: {e}</h3><a href='/'>Назад</a>"

@app.post("/interact", response_class=HTMLResponse)
def interact(response: Response, actor: str = Form(...), target: str = Form(...), action: str = Form(...), intention: str = Form(...), token: str = Form(...)):
    try:
        user = get_current_user(token)
        require_role(user, "agent")
        env.interact(actor, target, action, intention)
        traj_html = "<ul>"
        for step in env.agents[actor]:
            traj_html += f"<li>{step['timestamp']}: {step['action']} ({step['intention']})</li>"
        traj_html += "</ul>"
        return f"<h3>Взаимодействие завершено ✅</h3><p>Траектория ({actor}):</p>{traj_html}<a href='/'>Назад</a>"
    except HTTPException as e:
        response.status_code = e.status_code
        return f"<h3>Error: {e.detail}</h3><a href='/'>Назад</a>"
    except Exception as e:
        response.status_code = 500
        return f"<h3>Error: {e}</h3><a href='/'>Назад</a>"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8002)
