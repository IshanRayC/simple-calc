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


def test_trigonometry_in_degrees():
    assert math.isclose(evaluate("sin(30)"), 0.5, abs_tol=1e-12)
    assert math.isclose(evaluate("cos(60)"), 0.5, abs_tol=1e-12)
    assert math.isclose(evaluate("tan(45)"), 1.0, abs_tol=1e-12)


def test_inverse_trigonometry_in_degrees():
    assert math.isclose(evaluate("asin(0.5)"), 30.0, abs_tol=1e-12)
    assert math.isclose(evaluate("acos(0.5)"), 60.0, abs_tol=1e-12)
    assert math.isclose(evaluate("atan(1)"), 45.0, abs_tol=1e-12)


def test_nested_trigonometry():
    assert math.isclose(evaluate("sin(cos(60))"), math.sin(math.radians(0.5)), abs_tol=1e-12)
    assert math.isclose(evaluate("sin(asin(0.5))"), 0.5, abs_tol=1e-12)
    assert math.isclose(evaluate("cos(2 * asin(0.5))"), 0.5, abs_tol=1e-12)


def test_trig_inside_arithmetic():
    assert math.isclose(evaluate("2 * sin(30) + cos(60)"), 1.5, abs_tol=1e-12)


def test_invalid_trig_input():
    with pytest.raises(CalculatorError):
        evaluate("asin(2)")

    with pytest.raises(CalculatorError):
        evaluate("acos(-2)")


def test_unknown_functions_are_rejected():
    with pytest.raises(CalculatorError):
        evaluate("sqrt(25)")

    with pytest.raises(CalculatorError):
        evaluate("log(10)")


def test_invalid_expression():
    with pytest.raises(CalculatorError):
        evaluate("2 + unknown(3)")
