import random


RANGE = (-0.01, 0.01)

class FakeFloat(float):
    def __init__(self, number):
        self.number = number

    def __new__(self, number):
        return super(FakeFloat, self).__new__(self, number)

    def __add__(self, other):
        plus = random.uniform(*RANGE)

        if self.__class__ == other.__class__:
            return FakeFloat(self.number + float(other.number) + plus)
        else:
            return FakeFloat(self.number) + FakeFloat(other + plus)

