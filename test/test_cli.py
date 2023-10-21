from typer.testing import CliRunner

import kysy
import kysy.cli as cli
from kysy.cli import app

# from kysy.render import Template

runner = CliRunner()


def test_app_version():
    result = runner.invoke(app, ['version'])
    assert result.exit_code == 0
    assert cli.APP_NAME in result.stdout
    assert kysy.__version__ in result.stdout


def test_app_template():
    result = runner.invoke(app, ['template'])
    assert result.exit_code == 0
    assert 'Example template generated per ' in result.stdout


def test_cli_main():
    cli.main(['diff', '.', 'kysy.txt', 'ignored']) == 0


def test_cli_diff_path():
    cli.diff_repo(source=cli.CWD, output='kysy-ysyk.txt') == 0
