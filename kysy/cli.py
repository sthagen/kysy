#! /usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=line-too-long
"""Commandline API gateway for kysy."""
import pathlib
import sys
from typing import List, Union

import typer

import kysy
import kysy.kysy as ky
from kysy.render import Template

CWD = '.'
APP_NAME = 'Ask or know (kysy tai tiedä).'
APP_ALIAS = 'kysy'
app = typer.Typer(
    add_completion=False,
    context_settings={'help_option_names': ['-h', '--help']},
    no_args_is_help=True,
)


@app.callback(invoke_without_command=True)
def callback(
    version: bool = typer.Option(
        False,
        '-V',
        '--version',
        help='Display the kysy version and exit',
        is_eager=True,
    )
) -> None:
    """
    Ask or know (kysy tai tiedä).
    Relating answers to files and folders (Finnish: Vastaukset tiedostoihin ja kansioihin).
    """
    if version:
        typer.echo(f'{APP_NAME} version {foran.__version__}')
        raise typer.Exit()


def classify_template(template: str) -> Template:
    """
    Process the received template and return the classification
    """
    if not template:
        return Template.NONE

    if '{{' in str(template):
        return Template.JINJA_STRING

    if '{' in str(template):
        return Template.F_STRING

    if pathlib.Path(str(template)).is_file():
        return Template.JINJA_PATH

    return Template.STRING


@app.command('diff')
def diff_repo(
    source: str = typer.Argument(CWD),
    input: str = typer.Option('', '-i', '--input'),
    output: str = typer.Option('', '-o', '--output'),
    template: str = typer.Option('', '-t', '--template'),
) -> int:
    """
    Match the local data to the remote information  (no template handling yet)
    """
    repo_root = input if input else source
    target = 'STD_OUT' if not str(output) else str(output)
    return ky.main(['diff', repo_root, target, template])


@app.command('label')
def label_repo(
    source: str = typer.Argument(CWD),
    input: str = typer.Option('', '-i', '--input'),
    output: str = typer.Option('', '-o', '--output'),
    template: str = typer.Option('', '-t', '--template'),
) -> int:
    """
    Labels the local data (no template handling yet)
    """
    repo_root = input if input else source
    target = 'STD_OUT' if not str(output) else str(output)
    return ky.main(['label', repo_root, target, template])


@app.command('template')
def app_template(output: str = typer.Option('', '-o', '--output')) -> None:
    """
    Output an example jinja template representing the defaults
    """
    target = 'STD_OUT' if not output else output
    typer.echo(f'Example template generated per {target}')


@app.command('version')
def app_version() -> None:
    """
    Display the kysy version and exit
    """
    callback(True)


# pylint: disable=expression-not-assigned
# @app.command()
def main(argv: Union[List[str], None] = None) -> int:
    """Delegate processing to functional module."""
    argv = sys.argv[1:] if argv is None else argv
    return ky.main(argv)
