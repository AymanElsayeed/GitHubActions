import pytest


@pytest.fixture
def a():
    return 1
@pytest.fixture
def b():
    return 2

def test_addition(a, b):
    assert a + b == 3
