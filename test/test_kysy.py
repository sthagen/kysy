# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
# import pathlib

import pytest

import kysy.kysy as ky


def test_main_empty():
    with pytest.warns(UserWarning):
        ky.main([]) == 2
