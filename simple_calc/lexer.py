from dataclasses import dataclass
import re

from .errors import LexerError


@dataclass(frozen=True)
class Token:
    kind: str
    value: str
    position: int


_TOKEN_RE = re.compile(
    r"(?P<NUMBER>(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?)"
    r"|(?P<OP>[+\-*/%^!])"
    r"|(?P<LPAREN>\()|(?P<RPAREN>\))|(?P<WS>\s+)"
)


def tokenize(text: str) -> list[Token]:
    tokens = []
    pos = 0

    while pos < len(text):
        match = _TOKEN_RE.match(text, pos)
        if not match:
            raise LexerError(
                f"Unexpected character {text[pos]!r} at position {pos}"
            )

        kind = match.lastgroup
        value = match.group()

        if kind != "WS":
            tokens.append(Token(kind, value, pos))

        pos = match.end()

    tokens.append(Token("EOF", "", len(text)))
    return tokens
