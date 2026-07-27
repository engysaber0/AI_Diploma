class Memory:
    #single numeric memory slot, like the M key on a physical calculator
    def __init__(self):
        self.value = 0.0

    def add(self, amount):
        self.value += amount
        return self.value

    def subtract(self, amount):
        self.value -= amount
        return self.value


    def store(self, amount):
        self.value = amount
        return self.value


    def recall(self):
        return self.value

    def clear(self):
        self.value = 0.0

    def has_value(self):
        return self.value != 0.0
