# Simple Calc

A beginner-friendly arithmetic expression engine written in Python.

Simple Calc takes an expression, tokenizes it, parses it into an **Abstract Syntax Tree (AST)**, and evaluates the AST without using Python's `eval()`.

## Current scope

For now, the calculator supports only these arithmetic operators:

| Operator | Meaning | Example |
|---|---|---|
| `+` | Addition | `2 + 3` |
| `-` | Subtraction | `7 - 4` |
| `*` | Multiplication | `6 * 5` |
| `/` | Division | `20 / 4` |
| `%` | Modulo | `17 % 5` |
| `^` | Power | `2 ^ 8` |
| `!` | Factorial | `5!` |

Parentheses are also supported for grouping, and the parser respects operator precedence.

### Examples

```text
2 + 3 * 4       -> 14
(2 + 3) * 4     -> 20
20 / 5          -> 4
17 % 5          -> 2
2^3^2           -> 512
5!              -> 120
3!^2            -> 36
(3 + 2)!        -> 120
```

Factorial is currently limited to **non-negative integers**.

## What is intentionally not supported yet?

The project previously contained extra functionality such as trigonometry, statistics, variables, and numerical calculus. Those features have been removed from the current version so that the parsing and calculation core stays small and easy to understand.

They can be added back later as separate features once the core arithmetic engine is solid.

## How to use it

### 1. Clone the repository

```bash
git clone https://github.com/IshanRayC/simple-calc.git
cd simple-calc
```

### 2. Check Python

Windows:

```powershell
python --version
```

If `python` is unavailable, try:

```powershell
py --version
```

### 3. Create a virtual environment

Windows:

```powershell
python -m venv .venv
.venv\\Scripts\\activate
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install test dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Run Simple Calc

```bash
python calc.py
```

You can also run:

```bash
python -m simple_calc
```

Example session:

```text
Simple Calc — arithmetic expression engine
Supported: +  -  *  /  %  ^  !
Type an expression or 'quit' to exit.
Examples: 2 + 3*4 | 2^8 | 10%3 | 5! | (2+3)*4
calc> 5!
120.0
calc> 2 + 3 * 4
14.0
calc> quit
```

### 6. Run the tests

```bash
python -m pytest
```

## Project structure

```text
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
```

## Architecture

```text
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
```

The parser handles precedence and right-associative exponentiation. The evaluator performs the arithmetic directly on the AST and never executes the input as Python code.

## Roadmap

The immediate goal is to make the core arithmetic engine reliable and easy to understand. More advanced mathematical features can be added later without making the initial parser unnecessarily complicated.
