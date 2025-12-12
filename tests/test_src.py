"""

Unit tests for src module.

"""
import pytest
from ..src import src

@pytest.fixture
def a():
    return 1
@pytest.fixture
def b():
    return 2

def test_addition(a, b):
    assert src.sum_two_numbers(a,b) == 3
