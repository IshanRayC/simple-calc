# Simple Calc

A mathematical expression engine written in Python. It takes a string expression, tokenizes it, parses it into an AST, and evaluates the AST without using Python eval().

## Features

- Arithmetic: +, -, *, /
- Power: ^ and pow(a, b)
- Modulo: % and mod(a, b)
- Parentheses and operator precedence
- Constants: pi, e, tau
- Trigonometry: sin, cos, tan, asin, acos, atan (radians)
- Exponential/logarithmic functions: exp, ln, log
- Square root and absolute value
- Mean / average: mean(...), avg(...), average(...)
- Population standard deviation: std(...)
- Sample standard deviation: sample_std(...)
- Numerical derivative: derivative(expression, variable, point)
- Numerical definite integral: integral(expression, variable, lower, upper) using Simpson's rule
- Variables: 2*x + 1 with x supplied programmatically

## Examples

    2 + 3 * 4                 -> 14
    (2 + 3) * 4               -> 20
    2^3^2                     -> 512
    sin(pi / 2)               -> 1
    sqrt(25) + 2^3            -> 13
    mean(10, 20, 30, 40)      -> 25
    std(10, 20, 30, 40)       -> 11.180339887...
    derivative(x^2, x, 3)     -> approximately 6
    integral(x^2, x, 0, 3)    -> 9

## Architecture

    string
      |
    lexer / tokenizer
      |
    recursive-descent parser
      |
    AST
      |
    evaluator
      |
    number

The parser handles precedence and right-associative exponentiation. The evaluator never executes the input as Python code.

## Run

    python -m venv .venv
    # Windows: .venv\\Scripts\\activate
    # macOS/Linux: source .venv/bin/activate
    pip install -r requirements.txt
    python calc.py

## Test

    pytest

## Calculus note

The first calculus implementation is numerical, not symbolic: derivatives use a central finite difference and definite integrals use composite Simpson's rule. Symbolic differentiation/integration can be added later as a separate engine layer.
