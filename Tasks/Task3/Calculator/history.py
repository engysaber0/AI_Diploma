from utils import shorten
class History:
    """to keeps a log of past calculations for the current session"""
    def __init__(self, limit=100):
        self.entries = []
        self.limit = limit

    def add(self, expression, result):
        self.entries.append((expression, result))
        if len(self.entries) > self.limit:
            self.entries.pop(0)

    def clear(self):
        self.entries.clear()

    def is_empty(self):
        return len(self.entries) == 0

    def as_lines(self):
        lines = []
        for i, (expression, result) in enumerate(self.entries, start=1):
            lines.append(f"  {i:>3}.  {shorten(expression)}  =  {result}")
        return lines
