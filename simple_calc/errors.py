class CalculatorError(Exception):
    """Base class for calculator errors."""

class LexerError(CalculatorError):
    pass

class ParserError(CalculatorError):
    pass

class EvaluationError(CalculatorError):
    pass
