# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
import pytest
from typer.testing import CliRunner

import kysy
import kysy.cli as cli
from kysy.cli import app
from kysy.render import Template

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
    message = 'ignoring template: ignored'
    with pytest.raises(UserWarning) as ex:
        cli.main(['diff', '.', 'kysy.txt', 'ignored']) == 0
        assert message in str(ex.value)


def test_cli_diff_path():
    message = 'ignoring template: ignored'
    with pytest.raises(UserWarning) as ex:
        cli.diff_repo(source=cli.CWD, output='foran-eller-bagved.txt') == 0
        assert message in str(ex.value)
