# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
# import pathlib

import pytest

import kysy.kysy as ky


def test_main_empty():
    message = 'received wrong number of arguments'
    with pytest.raises(UserWarning) as ex:
        ky.main([]) == 2
    assert message in str(ex.value)
