# Simple Calc

A beginner-friendly arithmetic expression engine written in Python.

Simple Calc takes an expression, tokenizes it, parses it into an Abstract Syntax Tree (AST), and evaluates the AST without using Python's eval().

## Current scope

Simple Calc supports arithmetic plus trigonometric functions.

### Arithmetic operators

| Operator | Meaning | Example |
|---|---|---|
| + | Addition | 2 + 3 |
| - | Subtraction | 7 - 4 |
| * | Multiplication | 6 * 5 |
| / | Division | 20 / 4 |
| % | Modulo | 17 % 5 |
| ^ | Power | 2 ^ 8 |
| ! | Factorial | 5! |

Parentheses are supported for grouping.

### Trigonometric functions

Normal trig functions take an angle in degrees and return a decimal value.

| Function | Meaning | Example |
|---|---|---|
| sin(x) | Sine | sin(30) -> 0.5 |
| cos(x) | Cosine | cos(60) -> 0.5 |
| tan(x) | Tangent | tan(45) -> 1 |

Inverse trig functions take a ratio/value and return an angle in degrees.

| Function | Meaning | Example |
|---|---|---|
| asin(x) | Inverse sine | asin(0.5) -> 30 |
| acos(x) | Inverse cosine | acos(0.5) -> 60 |
| atan(x) | Inverse tangent | atan(1) -> 45 |

### Nested functions

Function calls can be nested:

    sin(cos(60))
    sin(asin(0.5))
    cos(2 * asin(0.5))

Functions can also be combined with normal arithmetic:

    2 * sin(30) + cos(60)

## Important angle convention

Simple Calc uses degrees for trigonometry.

sin(30) means sine of 30 degrees, not 30 radians.

Inverse functions also return degrees:

asin(0.5) returns 30 degrees.

## Invalid trig input

- asin(x) and acos(x) require -1 <= x <= 1.
- atan(x) accepts any finite real number.
- tan(x) follows Python's floating-point behavior near undefined angles.

## How to use it

### 1. Clone the repository

    git clone https://github.com/IshanRayC/simple-calc.git
    cd simple-calc

### 2. Create and activate a virtual environment

Windows:

    python -m venv .venv
    .venv\Scripts\activate

macOS/Linux:

    python3 -m venv .venv
    source .venv/bin/activate

### 3. Install dependencies

    python -m pip install -r requirements.txt

### 4. Run Simple Calc

    python calc.py

Example session:

    calc> sin(30)
    0.5
    calc> asin(0.5)
    30.0
    calc> sin(asin(0.5))
    0.5
    calc> quit

### 5. Run the tests

    python -m pytest

## Architecture

    Expression
        |
        v
    Lexer / Tokenizer
        |
        v
    Parser
        |
        v
    AST
        |
        v
    Evaluator
        |
        v
    Number / Result

The parser recognizes the approved function names and supports nested function calls. The evaluator converts degrees to radians for normal trig functions and converts inverse-trig results back to degrees.

## Project structure

    simple-calc/
    ├── simple_calc/
    │   ├── __init__.py
    │   ├── __main__.py
    │   ├── ast.py
    │   ├── errors.py
    │   ├── lexer.py
    │   ├── parser.py
    │   └── evaluator.py
    ├── tests/
    │   └── test_calculator.py
    ├── .github/
    │   └── workflows/
    │       └── test.yml
    ├── calc.py
    ├── requirements.txt
    ├── README.md
    └── LICENSE
