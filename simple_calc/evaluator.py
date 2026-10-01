import math

from .ast import BinaryOp, Node, Number, UnaryOp
from .errors import EvaluationError
from .parser import parse


def _number(value: float) -> float:
    if not math.isfinite(value):
        raise EvaluationError("Result is not finite")
    return value


def evaluate_node(node: Node) -> float:
    if isinstance(node, Number):
        return node.value

    if isinstance(node, UnaryOp):
        value = evaluate_node(node.operand)

        if node.operator == "+":
            return _number(value)
        if node.operator == "-":
            return _number(-value)
        if node.operator == "!":
            if value < 0 or not value.is_integer():
                raise EvaluationError("Factorial is only defined here for non-negative integers")
            try:
                return _number(float(math.factorial(int(value))))
            except (OverflowError, ValueError) as exc:
                raise EvaluationError(str(exc)) from exc

        raise EvaluationError(f"Unsupported unary operator: {node.operator}")

    if isinstance(node, BinaryOp):
        left = evaluate_node(node.left)
        right = evaluate_node(node.right)

        try:
            if node.operator == "+":
                return _number(left + right)
            if node.operator == "-":
                return _number(left - right)
            if node.operator == "*":
                return _number(left * right)
            if node.operator == "/":
                return _number(left / right)
            if node.operator == "%":
                return _number(left % right)
            if node.operator == "^":
                return _number(left ** right)
        except (ArithmeticError, ValueError, OverflowError) as exc:
            raise EvaluationError(str(exc)) from exc

        raise EvaluationError(f"Unsupported binary operator: {node.operator}")

    raise EvaluationError(f"Unsupported AST node: {type(node).__name__}")


def evaluate(expression: str) -> float:
    return evaluate_node(parse(expression))
