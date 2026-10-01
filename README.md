# Simple Calc

A beginner-friendly mathematical expression engine written in Python. It takes a string expression, tokenizes it, parses it into an AST, and evaluates the AST **without using Python `eval()`**.

## What can it calculate?

- **Arithmetic:** `+`, `-`, `*`, `/`
- **Power:** `^` and `pow(a, b)`
- **Modulo:** `%` and `mod(a, b)`
- **Parentheses and operator precedence**
- **Constants:** `pi`, `e`, `tau`
- **Trigonometry:** `sin`, `cos`, `tan`, `asin`, `acos`, `atan` (radians)
- **Exponential/logarithmic functions:** `exp`, `ln`, `log`
- **Square root and absolute value:** `sqrt`, `abs`
- **Statistics:** `mean`, `avg`, `average`, `std`, `sample_std`
- **Numerical calculus:** `derivative(...)` and `integral(...)`
- **Variables:** for example, `2*x + 1` with `x` supplied programmatically

## Quick examples

```text
2 + 3 * 4                 -> 14
(2 + 3) * 4               -> 20
2^3^2                     -> 512
17 % 5                    -> 2
sin(pi / 2)               -> 1
sqrt(25) + 2^3            -> 13
mean(10, 20, 30, 40)      -> 25
std(10, 20, 30, 40)       -> 11.180339887...
derivative(x^2, x, 3)     -> approximately 6
integral(x^2, x, 0, 3)    -> 9
```

# How to use it

## 1. Get the project from GitHub

If you are new to GitHub, the easiest method is:

1. Open the repository on GitHub.
2. Click the green **Code** button.
3. Choose **Download ZIP**.
4. Extract the ZIP somewhere easy, such as your Desktop.
5. Open the extracted `simple-calc` folder in VS Code.

If you already know Git, you can clone it instead:

```bash
git clone https://github.com/IshanRayC/simple-calc.git
cd simple-calc
```

## 2. Check that Python is installed

Open a terminal in the project folder and run:

```bash
python --version
```

You should see Python 3.x.

On some Windows installations, use:

```bash
py --version
```

## 3. Create a virtual environment

### Windows

```bash
python -m venv .venv
.venv\\Scripts\\activate
```

If `python` does not work, try:

```bash
py -m venv .venv
.venv\\Scripts\\activate
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

After activation, your terminal should show something like `(.venv)`.

## 4. Install the test dependency

```bash
python -m pip install -r requirements.txt
```

## 5. Start the calculator

You can run:

```bash
python calc.py
```

or:

```bash
python -m simple_calc
```

You will see:

```text
Simple Calc — expression engine
Type an expression or 'quit' to exit.
calc>
```

Now type expressions such as:

```text
calc> 2 + 3 * 4
14

calc> sin(pi / 2)
1.0

calc> mean(10, 20, 30, 40)
25.0

calc> derivative(x^2, x, 3)
6.0

calc> integral(x^2, x, 0, 3)
9.0
```

Type `quit` to stop.

## 6. Run the automated tests

From the project folder, run:

```bash
python -m pytest
```

Pytest will run the tests in `tests/` and report which tests passed or failed.

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
User input string
      |
      v
Lexer / Tokenizer
      |
      v
Recursive-descent Parser
      |
      v
AST (Abstract Syntax Tree)
      |
      v
Evaluator
      |
      v
Number / Result
```

The parser handles operator precedence and right-associative exponentiation. The evaluator never executes the input as Python code.

## Calculus note

The current calculus implementation is **numerical, not symbolic**:

- derivatives use a central finite difference
- definite integrals use composite Simpson's rule

Symbolic differentiation and integration can be added later as a separate engine layer.
