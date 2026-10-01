from .ast import BinaryOp, FunctionCall, Node, Number, UnaryOp, Variable
from .errors import ParserError
from .lexer import Token, tokenize

class Parser:
    def __init__(self, text: str):
        self.tokens = tokenize(text)
        self.index = 0

    @property
    def current(self) -> Token:
        return self.tokens[self.index]

    def advance(self) -> Token:
        token = self.current
        self.index += 1
        return token

    def expect(self, kind: str) -> Token:
        if self.current.kind != kind:
            raise ParserError(f"Expected {kind}, got {self.current.kind} at position {self.current.position}")
        return self.advance()

    def parse(self) -> Node:
        if self.current.kind == "EOF":
            raise ParserError("Expression is empty")
        node = self.expression()
        if self.current.kind != "EOF":
            raise ParserError(f"Unexpected token {self.current.value!r} at position {self.current.position}")
        return node

    def expression(self) -> Node:
        node = self.term()
        while self.current.kind == "OP" and self.current.value in {"+", "-"}:
            op = self.advance().value
            node = BinaryOp(op, node, self.term())
        return node

    def term(self) -> Node:
        node = self.unary()
        while self.current.kind == "OP" and self.current.value in {"*", "/", "%"}:
            op = self.advance().value
            node = BinaryOp(op, node, self.unary())
        return node

    def unary(self) -> Node:
        if self.current.kind == "OP" and self.current.value in {"+", "-"}:
            return UnaryOp(self.advance().value, self.unary())
        return self.power()

    def power(self) -> Node:
        node = self.primary()
        if self.current.kind == "OP" and self.current.value == "^":
            self.advance()
            node = BinaryOp("^", node, self.unary())
        return node

    def primary(self) -> Node:
        token = self.current
        if token.kind == "NUMBER":
            self.advance()
            return Number(float(token.value))
        if token.kind == "IDENT":
            name = self.advance().value
            if self.current.kind == "LPAREN":
                self.advance()
                args = []
                if self.current.kind != "RPAREN":
                    args.append(self.expression())
                    while self.current.kind == "COMMA":
                        self.advance()
                        args.append(self.expression())
                self.expect("RPAREN")
                return FunctionCall(name, tuple(args))
            return Variable(name)
        if token.kind == "LPAREN":
            self.advance()
            node = self.expression()
            self.expect("RPAREN")
            return node
        raise ParserError(f"Expected number, variable, or '(' at position {token.position}")

def parse(text: str) -> Node:
    return Parser(text).parse()
