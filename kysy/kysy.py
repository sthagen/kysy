# -*- coding: utf-8 -*-
# pylint: disable=expression-not-assigned,line-too-long
"""Ask or know (kysy tai tiedä). API."""
import os
import pathlib
import warnings
from typing import List, Union

DEBUG_VAR = 'KYSY_DEBUG'
DEBUG = os.getenv(DEBUG_VAR)

ENCODING = 'utf-8'
ENCODING_ERRORS_POLICY = 'ignore'


def main(argv: Union[List[str], None] = None) -> int:
    """Drive the analysis."""
    # [('diff'|'label'), repo_root, target, template]
    if not argv or len(argv) != 4:
        warnings.warn('received wrong number of arguments')
        return 2

    if argv[0] not in ('diff', 'label'):
        warnings.warn('received unknown command')
        return 2

    command, repo_root, target, template = argv

    if not pathlib.Path(str(repo_root)).is_dir():
        warnings.warn('repository root is no directory')
        return 1

    if template and target != 'STD_OUT':
        warnings.warn('templates not yet implemented')

    return 0
