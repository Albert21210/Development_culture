class Calculator:
    def __init__(self, initial_value=0):
        self._value = initial_value

    def add(self, amount):
        self._value += amount
        return self

    def subtract(self, amount):
        self._value -= amount
        return self

    def multiply(self, amount):
        self._value *= amount
        return self

    def divide(self, amount):
        if amount == 0:
            raise ValueError("Деление на ноль невозможно.")
        self._value /= amount
        return self

    def result(self):
        return self._value

    def __repr__(self):
        return f"Calculator(value={self._value})"