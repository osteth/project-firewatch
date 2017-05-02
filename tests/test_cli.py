from click.testing import CliRunner

from projectfirewatch.scripts.cli import cli


def test_cli_update():
    runner = CliRunner()
    result = runner.invoke(cli, ['update'])
    assert result.output == "MODIS satelite data updated."
    print(result.output)

def test_cli_start():
    runner = CliRunner()
    result = runner.invoke(cli, ['start'])
    assert result.output == "* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)"
