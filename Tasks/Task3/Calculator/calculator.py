from history import History
from memory import Memory
from parser import ParserError,evaluate
from scientific import CONSTANTS, get_functions
from utils import clean_number
class Calculator:
    """
    Ties together parsing, scientific functions,memory,and history
    to provide a complete calculator experience
    """
    def __init__(self):
        self.angle_mode = "DEG"
        self.memory = Memory()
        self.history = History()
        self.ans = 0.0

    def run(self, expression):
        functions = get_functions(self.angle_mode)
        names = dict(CONSTANTS)
        names["Ans"] = self.ans
        names["M"] = self.memory.recall()

        result = evaluate(expression, functions, names)

        formatted = clean_number(result)
        self.history.add(expression, formatted)
        self.ans = result
        return formatted

    def set_angle_mode(self, mode):
        self.angle_mode = mode

    def memory_add(self):
        return self.memory.add(self.ans)

    def memory_subtract(self):
        return self.memory.subtract(self.ans)

    def memory_store(self):
        return self.memory.store(self.ans)

    def memory_recall(self):
        return self.memory.recall()

    def memory_clear(self):
        self.memory.clear()

    def status(self):
        return{
            "mode": self.angle_mode,
            "memory": clean_number(self.memory.recall()),
            "ans": clean_number(self.ans),
        }
