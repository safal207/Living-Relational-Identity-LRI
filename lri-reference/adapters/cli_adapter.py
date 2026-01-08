import click
import sys
import os

# Ensure we can import from services sibling directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from services.cycle_engine import run_identity_cycle

@click.group()
def cli():
    """LPI CLI Adapter — органическое взаимодействие с LRI"""
    pass

@cli.command()
@click.option("--subject", prompt="Subject ID", help="ID субъекта")
@click.option("--action", prompt="Action", help="Действие пользователя")
@click.option("--intention", prompt="Intention", help="Намерение действия")
def simulate(subject, action, intention):
    """Симуляция полного цикла идентичности"""
    payload = {
        "subject_id": subject,
        "action": action,
        "intention": intention,
        "context": {}
    }
    try:
        result = run_identity_cycle(payload)
        click.echo("✅ Цикл завершён!")
        click.echo("Текущая траектория:")
        for step in result["trajectory"]:
            click.echo(f"- {step['timestamp']}: {step['action']} ({step['intention']})")
    except Exception as e:
        click.echo(f"Error: {e}", err=True)

if __name__ == "__main__":
    cli()
