# -*- coding: utf-8 -*-
# pylint: disable=import-outside-toplevel
# pylint: disable=missing-function-docstring
"""Testing of module autoset_pwd."""
import os
import pathlib as pl


def test_autoset_pwd(bin_dir: pl.Path) -> None:

    assert os.getcwd() == os.getenv("PWD_DIR")