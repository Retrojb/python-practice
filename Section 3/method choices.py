class FixedFloat:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f'<FixedFloat {self.amount: .2f}>'

    @staticmethod
    def from_sum(value1, value2):
        return FixedFloat(value1 + value2)

    @classmethod
    def from_another_sum(cls, num1, num2):
        return cls(num1 * num2)

number = FixedFloat.from_sum(19.578, 0.789)
print(number)

class Euro(FixedFloat):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol = '&'

    def __repr__(self):
        return f'<Euro {self.symbol}{self.amount:.2f}>'

money = Euro(18.786)
print(money)

new_money = Euro.from_another_sum(13.768, 4.55543)
print(new_money)

## cls stands for class