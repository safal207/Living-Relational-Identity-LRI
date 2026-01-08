import click
import sys
import os
import json

# Ensure we can import from sibling/parent directories
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from services.multi_agent_engine import MultiAgentEnvironment

# Note: Since this CLI runs as a script, the environment is re-initialized on every command.
# To make state persist between commands for the DEMO, we need to serialize the environment
# or use a persistent store. The LRI core (subjects map in memory) resets if the process exits.
#
# HOWEVER, for a CLI "interact" command that just triggers the engine, we can rely on
# the fact that `run_identity_cycle` interacts with the `api.subject` module.
#
# BUT: `api.subject` uses a global `subjects = {}`.
# If we run `python cli_multi_agent.py add` then exit, the memory is lost.
#
# SOLUTION FOR DEMO:
# We will create an interactive shell mode (REPL) within this CLI so the process stays alive.
# Or we just accept that for this PoC skeleton, we run the "interact" sequence in one go.
# Let's implement an interactive REPL mode using click.

env = MultiAgentEnvironment()

@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    """CLI для Multi-Agent LRI"""
    if ctx.invoked_subcommand is None:
        repl()

def repl():
    click.echo("--- Multi-Agent LRI Shell (Type 'exit' to quit) ---")
    while True:
        command = click.prompt("lri-multi-agent >", type=str)
        if command == "exit":
            break

        parts = command.split()
        if not parts:
            continue

        cmd = parts[0]

        try:
            if cmd == "add":
                if len(parts) < 2:
                    click.echo("Usage: add <subject_id>")
                    continue
                subject = parts[1]
                env.add_agent(subject)
                click.echo(f"✅ Агент {subject} добавлен")

            elif cmd == "interact":
                if len(parts) < 5:
                    click.echo("Usage: interact <actor> <target> <action> <intention>")
                    continue
                actor = parts[1]
                target = parts[2]
                action = parts[3]
                intention = parts[4]

                result = env.interact(actor, target, action, intention)
                click.echo("✅ Взаимодействие завершено")
                click.echo(f"Траектория Actor ({actor}):")
                click.echo(json.dumps(env.agents[actor], indent=2))
                click.echo(f"Траектория Target ({target}):")
                click.echo(json.dumps(env.agents[target], indent=2))

            elif cmd == "status":
                 click.echo(json.dumps(env.agents, indent=2))

            else:
                click.echo("Unknown command. Available: add, interact, status, exit")

        except Exception as e:
            click.echo(f"Error: {e}")

if __name__ == "__main__":
    cli()
