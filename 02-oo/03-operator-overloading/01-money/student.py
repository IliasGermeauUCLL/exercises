class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __add__(self, other):
        if self.currency != other.currency:
            raise RuntimeError("Andere currency")
        return Money(self.amount + other.amount, self.currency)

    def __sub__(self, other):
        if self.currency != other.currency:
            raise RuntimeError("Andere currency")
        return Money(self.amount - other.amount, self.currency)

    def __mul__(self, factor):
        return Money(self.amount * factor, self.currency)
