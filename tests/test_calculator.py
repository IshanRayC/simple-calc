import math

import pytest

from simple_calc import evaluate
from simple_calc.errors import CalculatorError


def test_basic_arithmetic():
    assert evaluate("2 + 3") == 5
    assert evaluate("10 - 4") == 6
    assert evaluate("6 * 7") == 42
    assert evaluate("20 / 5") == 4
    assert evaluate("17 % 5") == 2


def test_operator_precedence():
    assert evaluate("2 + 3 * 4") == 14
    assert evaluate("(2 + 3) * 4") == 20
    assert evaluate("2^3^2") == 512
    assert evaluate("-2^2") == -4


def test_power_and_factorial():
    assert evaluate("2^8") == 256
    assert evaluate("5!") == 120
    assert evaluate("3!^2") == 36
    assert evaluate("(3 + 2)!") == 120


def test_decimal_numbers():
    assert math.isclose(evaluate("2.5 * 4"), 10.0)
    assert math.isclose(evaluate("1e2 / 4"), 25.0)


def test_invalid_factorial():
    with pytest.raises(CalculatorError):
        evaluate("(-1)!")

    with pytest.raises(CalculatorError):
        evaluate("2.5!")


def test_unsupported_features_are_rejected():
    with pytest.raises(CalculatorError):
        evaluate("sin(1)")

    with pytest.raises(CalculatorError):
        evaluate("x + 1")


def test_invalid_expression():
    with pytest.raises(CalculatorError):
        evaluate("2 + unknown(3)")
