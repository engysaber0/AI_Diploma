import re

TOKEN_RE = re.compile(
    r"""
    (?P<NUMBER>\d+(\.\d+)?)   |
    (?P<NAME>[A-Za-z_][A-Za-z_0-9]*) |
    (?P<POW>\^)               |
    (?P<FLOORDIV>//)          |
    (?P<OP>[+\-*/%(),!])
    """,
    re.VERBOSE,
)


class ParserError(ValueError):
    pass
def tokenize(text):
    tokens = []
    pos = 0
    while pos < len(text):
        char = text[pos]
        if char.isspace():
            pos += 1
            continue
        match = TOKEN_RE.match(text, pos)
        if not match:
            raise ParserError(f"Unrecognized character: '{char}'")
        tokens.append(match.group(0))
        pos = match.end()
    return tokens


class Parser:
    def __init__(self, tokens, functions, names):
        self.tokens = tokens
        self.pos = 0
        self.functions = functions
        self.names = names

    def peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def next(self):
        token = self.peek()
        self.pos += 1
        return token

    def expect(self, expected):
        token = self.next()
        if token != expected:
            raise ParserError(f"Expected '{expected}' but got '{token}'")
        return token

    def run(self):
        value = self.expr()
        if self.peek() is not None:
            raise ParserError(f"Unexpected token: '{self.peek()}'")
        return value

    def expr(self):
        value = self.term()
        while self.peek() in ("+", "-"):
            op = self.next()
            rhs = self.term()
            value = value + rhs if op == "+" else value - rhs
        return value

    def term(self):
        value = self.power()
        while self.peek() in ("*", "/", "%", "//"):
            op = self.next()
            rhs = self.power()
            if op == "*":
                value *= rhs
            elif op == "/":
                if rhs == 0:
                    raise ParserError("Division by zero")
                value /= rhs
            elif op == "//":
                if rhs == 0:
                    raise ParserError("Division by zero")
                value //= rhs
            elif op == "%":
                if rhs == 0:
                    raise ParserError("Division by zero")
                value %= rhs
        return value

    def power(self):
        base = self.unary()
        if self.peek() == "^":
            self.next()
            return base ** self.power()
        return base

    def unary(self):
        if self.peek() == "-":
            self.next()
            return -self.unary()
        if self.peek() == "+":
            self.next()
            return self.unary()
        return self.postfix()

    def postfix(self):
        value = self.atom()
        while self.peek() == "!":
            self.next()
            if value < 0 or value != int(value):
                raise ParserError("Factorial needs a non-negative whole number")
            total = 1
            for i in range(2, int(value) + 1):
                total *= i
            value = total
        return value

    def atom(self):
        token = self.peek()
        if token is None:
            raise ParserError("Unexpected end of expression")

        if re.fullmatch(r"\d+(\.\d+)?", token):
            self.next()
            return float(token)

        if token == "(":
            self.next()
            value = self.expr()
            self.expect(")")
            return value

        if re.fullmatch(r"[A-Za-z_][A-Za-z_0-9]*", token):
            self.next()
            if self.peek() == "(":
                return self.call(token)
            return self.lookup(token)

        raise ParserError(f"Unexpected token: '{token}'")

    def call(self, name):
        if name not in self.functions:
            raise ParserError(f"Unknown function: '{name}'")

        self.expect("(")
        args = []
        if self.peek() != ")":
            args.append(self.expr())
            while self.peek() == ",":
                self.next()
                args.append(self.expr())
        self.expect(")")

        try:
            return self.functions[name](*args)
        except ParserError:
            raise
        except ValueError as exc:
            raise ParserError(str(exc)) from exc
        except TypeError as exc:
            raise ParserError(f"Wrong number of arguments for '{name}'") from exc

    def lookup(self, name):
        if name in self.names:
            return self.names[name]
        raise ParserError(f"Unknown name: '{name}'")


def evaluate(text, functions, names):
    if not text.strip():
        raise ParserError("Empty")

    tokens = tokenize(text)
    if not tokens:
        raise ParserError("Empty")

    return Parser(tokens, functions, names).run()
