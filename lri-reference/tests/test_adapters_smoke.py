from adapters.cli_adapter import cli as cli_adapter
from adapters.cli_multi_agent import cli as cli_multi_agent
from click.testing import CliRunner
from fastapi.testclient import TestClient


class TestCLIAdapter:
    def test_cli_adapter_help(self):
        runner = CliRunner()
        result = runner.invoke(cli_adapter, ["--help"])
        assert result.exit_code == 0
        assert "simulate" in result.output

    def test_cli_adapter_simulate_help(self):
        runner = CliRunner()
        result = runner.invoke(cli_adapter, ["simulate", "--help"])
        assert result.exit_code == 0
        assert "subject" in result.output


class TestCLIMultiAgent:
    def test_cli_multi_agent_imports(self):
        from adapters import cli_multi_agent

        assert hasattr(cli_multi_agent, "cli")
        assert hasattr(cli_multi_agent, "repl")

    def test_cli_multi_agent_help(self):
        runner = CliRunner()
        result = runner.invoke(cli_multi_agent, ["--help"])
        assert result.exit_code == 0
        assert "Usage:" in result.output


class TestUIAdapter:
    def test_ui_adapter_index(self):
        from adapters.ui_adapter import app

        client = TestClient(app)
        response = client.get("/")
        assert response.status_code == 200
        assert "LPI UI Adapter" in response.text
