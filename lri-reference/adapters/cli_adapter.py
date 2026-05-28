import click
from services.cycle_engine import run_identity_cycle


@click.group()
def cli():
    """LPI CLI Adapter — organic interaction with LRI"""
    pass


@cli.command()
@click.option("--subject", prompt="Subject ID", help="Subject identifier")
@click.option("--action", prompt="Action", help="User action")
@click.option("--intention", prompt="Intention", help="Intention of the action")
def simulate(subject, action, intention):
    """Simulate a full identity cycle"""
    payload = {"subject_id": subject, "action": action, "intention": intention, "context": {}}
    try:
        result = run_identity_cycle(payload)
        click.echo("✅ Cycle completed!")
        click.echo("Current trajectory:")
        for step in result["trajectory"]:
            click.echo(f"- {step['timestamp']}: {step['action']} ({step['intention']})")
    except Exception as e:
        click.echo(f"Error: {e}", err=True)


if __name__ == "__main__":
    cli()
