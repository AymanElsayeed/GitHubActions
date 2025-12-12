"""

Unit tests for src module.

"""
#pylint: disable=W0621

import pytest
from ..src import src

@pytest.fixture
def a():
    """
    Fixture that returns the first number
    :return: 1 as int
    """
    return 1
@pytest.fixture
def b():
    """
    Fixture that returns the second number
    :return: 2 as int
    """
    return 2

def test_addition(a, b):
    """
    Test addition of two numbers.
    :param a: the first number
    :param b: the second number
    :return: none
    """
    assert src.sum_two_numbers(a,b) == 3
