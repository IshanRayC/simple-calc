#!/usr/bin/env python3
"""Interactive command-line interface for Simple Calc."""
from simple_calc import evaluate
from simple_calc.errors import CalculatorError

def main() -> None:
    print("Simple Calc — expression engine")
    print("Type an expression or 'quit' to exit.")
    print("Examples: 2 + 3*4 | sin(pi/2) | mean(1,2,3) | derivative(x^2,x,3)")
    while True:
        try: expression = input("calc> ").strip()
        except (EOFError, KeyboardInterrupt):
            print(); break
        if expression.lower() in {"quit", "exit"}: break
        if not expression: continue
        try: print(evaluate(expression))
        except CalculatorError as exc: print(f"Error: {exc}")

if __name__ == "__main__": main()
