import math
from statistics import fmean, pstdev, stdev
from .ast import BinaryOp, FunctionCall, Node, Number, UnaryOp, Variable
from .errors import EvaluationError
from .parser import parse

CONSTANTS = {"pi": math.pi, "e": math.e, "tau": math.tau}

def _number(value: float) -> float:
    if not math.isfinite(value):
        raise EvaluationError("Result is not finite")
    return value

def _values(args, variables):
    return [evaluate_node(arg, variables) for arg in args]

def _require_count(name, args, count):
    if len(args) != count:
        raise EvaluationError(f"{name}() expects {count} argument(s), got {len(args)}")

def _derivative(expr, variable, point, variables):
    h = max(1e-5, math.sqrt(math.ulp(max(1.0, abs(point)))))
    a = dict(variables, **{variable: point + h})
    b = dict(variables, **{variable: point - h})
    return _number((evaluate_node(expr, a) - evaluate_node(expr, b)) / (2 * h))

def _integral(expr, variable, lower, upper, variables):
    if lower == upper:
        return 0.0
    sign = 1.0
    if lower > upper:
        lower, upper = upper, lower
        sign = -1.0
    n = 1000
    h = (upper - lower) / n
    total = 0.0
    for i in range(n + 1):
        x = lower + i * h
        y = evaluate_node(expr, dict(variables, **{variable: x}))
        weight = 1 if i in (0, n) else (4 if i % 2 else 2)
        total += weight * y
    return _number(sign * total * h / 3)

def evaluate_node(node: Node, variables=None) -> float:
    variables = {} if variables is None else variables
    if isinstance(node, Number): return node.value
    if isinstance(node, Variable):
        if node.name in variables: return variables[node.name]
        if node.name in CONSTANTS: return CONSTANTS[node.name]
        raise EvaluationError(f"Unknown variable or constant: {node.name}")
    if isinstance(node, UnaryOp):
        value = evaluate_node(node.operand, variables)
        return _number(value if node.operator == "+" else -value)
    if isinstance(node, BinaryOp):
        left, right = evaluate_node(node.left, variables), evaluate_node(node.right, variables)
        try:
            if node.operator == "+": return _number(left + right)
            if node.operator == "-": return _number(left - right)
            if node.operator == "*": return _number(left * right)
            if node.operator == "/": return _number(left / right)
            if node.operator == "%": return _number(left % right)
            if node.operator == "^": return _number(left ** right)
        except (ArithmeticError, ValueError, OverflowError) as exc:
            raise EvaluationError(str(exc)) from exc
    if isinstance(node, FunctionCall):
        name = node.name.lower()
        funcs = {"sin": math.sin, "cos": math.cos, "tan": math.tan, "asin": math.asin, "acos": math.acos, "atan": math.atan, "sqrt": math.sqrt, "exp": math.exp, "ln": math.log, "log": math.log10, "abs": abs}
        if name in funcs:
            _require_count(name, node.arguments, 1)
            try: return _number(funcs[name](evaluate_node(node.arguments[0], variables)))
            except (ArithmeticError, ValueError, OverflowError) as exc: raise EvaluationError(str(exc)) from exc
        if name in {"mean", "avg", "average", "fmean"}:
            if not node.arguments: raise EvaluationError("mean() needs at least one value")
            return _number(fmean(_values(node.arguments, variables)))
        if name in {"std", "stdev", "standard_deviation"}:
            if len(node.arguments) < 2: raise EvaluationError("std() needs at least two values")
            return _number(pstdev(_values(node.arguments, variables)))
        if name in {"sample_std", "sstd"}:
            if len(node.arguments) < 2: raise EvaluationError("sample_std() needs at least two values")
            return _number(stdev(_values(node.arguments, variables)))
        if name in {"derivative", "diff"}:
            if len(node.arguments) != 3 or not isinstance(node.arguments[1], Variable): raise EvaluationError("derivative(expr, variable, point) is required")
            return _derivative(node.arguments[0], node.arguments[1].name, evaluate_node(node.arguments[2], variables), variables)
        if name in {"integral", "integrate"}:
            if len(node.arguments) != 4 or not isinstance(node.arguments[1], Variable): raise EvaluationError("integral(expr, variable, lower, upper) is required")
            return _integral(node.arguments[0], node.arguments[1].name, evaluate_node(node.arguments[2], variables), evaluate_node(node.arguments[3], variables), variables)
        if name == "pow":
            _require_count(name, node.arguments, 2)
            return _number(evaluate_node(node.arguments[0], variables) ** evaluate_node(node.arguments[1], variables))
        if name == "mod":
            _require_count(name, node.arguments, 2)
            return _number(evaluate_node(node.arguments[0], variables) % evaluate_node(node.arguments[1], variables))
        raise EvaluationError(f"Unknown function: {node.name}")
    raise EvaluationError(f"Unsupported AST node: {type(node).__name__}")

def evaluate(expression: str, variables=None) -> float:
    return evaluate_node(parse(expression), variables)
