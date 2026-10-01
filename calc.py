#!/usr/bin/env python3
"""Interactive command-line interface for Simple Calc."""

from simple_calc import evaluate
from simple_calc.errors import CalculatorError


def main() -> None:
    print("Simple Calc — arithmetic expression engine")
    print("Supported: +  -  *  /  %  ^  !")
    print("Type an expression or 'quit' to exit.")
    print("Examples: 2 + 3*4 | 2^8 | 10%3 | 5! | (2+3)*4")

    while True:
        try:
            expression = input("calc> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break

        if expression.lower() in {"quit", "exit"}:
            break
        if not expression:
            continue

        try:
            print(evaluate(expression))
        except CalculatorError as exc:
            print(f"Error: {exc}")


if __name__ == "__main__":
    main()
