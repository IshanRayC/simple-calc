import math
import pytest
from simple_calc import evaluate
from simple_calc.errors import CalculatorError

def test_arithmetic_precedence():
    assert evaluate("2 + 3 * 4") == 14
    assert evaluate("(2 + 3) * 4") == 20
    assert evaluate("2^3^2") == 512
    assert evaluate("-2^2") == -4

def test_math_functions():
    assert math.isclose(evaluate("sin(pi / 2)"), 1.0, abs_tol=1e-12)
    assert evaluate("sqrt(25) + 2^3") == 13
    assert evaluate("mod(17, 5)") == 2

def test_statistics():
    assert evaluate("mean(10, 20, 30, 40)") == 25
    assert math.isclose(evaluate("std(10, 20, 30, 40)"), 11.1803398875, rel_tol=1e-10)

def test_calculus_numeric():
    assert math.isclose(evaluate("derivative(x^2, x, 3)"), 6.0, rel_tol=1e-5)
    assert math.isclose(evaluate("integral(x^2, x, 0, 3)"), 9.0, rel_tol=1e-8)

def test_variables():
    assert evaluate("2*x + 1", {"x": 4}) == 9

def test_invalid_expression():
    with pytest.raises(CalculatorError):
        evaluate("2 + unknown(3)")
