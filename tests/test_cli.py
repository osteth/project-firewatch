from click.testing import CliRunner
from projectfirewatch.scripts.cli import cli


def test_cli_update():
    runner = CliRunner()
    result = runner.invoke(cli, ['update'])           
    assert result.output is not None
