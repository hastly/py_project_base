#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

"""Tests for future package."""

import pytest

from click.testing import CliRunner
from py_base.cli import main


# pytest.skip('skipping {} tests'.format(__name__), allow_module_level=True)


@pytest.fixture
def runner():
    return CliRunner()


def test_main(runner):
    result = runner.invoke(main)

    assert result.exit_code == 0
    assert 'Tabula rasa' in result.output

    help_result = runner.invoke(main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output
