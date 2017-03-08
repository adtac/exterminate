import random


RANGE = (-0.01, 0.01)


class AlternativeFloat(float):
    def __init__(self, number):
        self.number = number

    def __new__(self, number):
        return super(AlternativeFloat, self).__new__(self, number)

    def __add__(self, other):
        plus = random.uniform(*RANGE)

        if self.__class__ == other.__class__:
            return AlternativeFloat(self.number + float(other.number) + plus)
        else:
            return AlternativeFloat(self.number) + AlternativeFloat(other + plus)
