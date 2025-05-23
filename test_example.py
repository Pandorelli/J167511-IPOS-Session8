from example import add, subtract, multiply
from example import convert_fahrenheit_to_celsius as f2c
import pytest


def test_add():
    assert add(2, 3) == 5
    assert add('space', 'ship') == 'spaceship'


# uncomment the following test in step 5
def test_subtract():
    assert subtract(2, 3) == -1


def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(2, -1) == -2
    assert multiply(-1, -1) == 1
    assert multiply(0, -1) == 0


# uncomment the following test in step 11
def test_convert_fahrenheit_to_celsius():
    assert f2c(32) == 0
    assert f2c(122) == pytest.approx(50)
    with pytest.raises(AssertionError):
        f2c(-600)
