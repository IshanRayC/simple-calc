from dataclasses import dataclass

class Node: pass

@dataclass(frozen=True)
class Number(Node):
    value: float

@dataclass(frozen=True)
class Variable(Node):
    name: str

@dataclass(frozen=True)
class UnaryOp(Node):
    operator: str
    operand: Node

@dataclass(frozen=True)
class BinaryOp(Node):
    operator: str
    left: Node
    right: Node

@dataclass(frozen=True)
class FunctionCall(Node):
    name: str
    arguments: tuple[Node, ...]
