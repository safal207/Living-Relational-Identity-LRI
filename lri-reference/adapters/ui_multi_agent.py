from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import sys
import os
import uvicorn

# Ensure we can import from services sibling directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from services.multi_agent_engine import MultiAgentEnvironment

app = FastAPI(title="Multi-Agent LRI UI")
env = MultiAgentEnvironment()

@app.get("/", response_class=HTMLResponse)
def index():
    agents_list = "".join(f"<li>{agent}</li>" for agent in env.agents)
    return f"""
    <html>
    <body>
        <h2>Multi-Agent LRI UI</h2>
        <h3>Агенты:</h3>
        <ul>{agents_list}</ul>
        <h3>Добавить агента:</h3>
        <form action="/add" method="post">
            Subject ID: <input name="subject">
            <button type="submit">Add</button>
        </form>
        <h3>Симуляция взаимодействия:</h3>
        <form action="/interact" method="post">
            Actor ID: <input name="actor"><br>
            Target ID: <input name="target"><br>
            Action: <input name="action"><br>
            Intention: <input name="intention"><br>
            <button type="submit">Interact</button>
        </form>
    </body>
    </html>
    """

@app.post("/add", response_class=HTMLResponse)
def add_agent(subject: str = Form(...)):
    env.add_agent(subject)
    return f"<h3>Агент {subject} добавлен ✅</h3><a href='/'>Назад</a>"

@app.post("/interact", response_class=HTMLResponse)
def interact(actor: str = Form(...), target: str = Form(...), action: str = Form(...), intention: str = Form(...)):
    try:
        env.interact(actor, target, action, intention)
        traj_html = "<ul>"
        for step in env.agents[actor]:
            traj_html += f"<li>{step['timestamp']}: {step['action']} ({step['intention']})</li>"
        traj_html += "</ul>"
        return f"<h3>Взаимодействие завершено ✅</h3><p>Траектория ({actor}):</p>{traj_html}<a href='/'>Назад</a>"
    except Exception as e:
        return f"<h3>Error: {e}</h3><a href='/'>Назад</a>"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8002)
