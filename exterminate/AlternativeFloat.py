import random

from exterminate.Utilities import builtins
from exterminate.Constants import DECIMAL_ERROR_RANGE


class AlternativeFloat(float):
    def __init__(self, number):
        self.number = number

    def __new__(self, number):
        return super(AlternativeFloat, self).__new__(self, number)

    def __add__(self, other):
        plus = random.uniform(*DECIMAL_ERROR_RANGE)

        if self.__class__ == other.__class__:
            return AlternativeFloat(self.number + float(other.number) + plus)
        else:
            return AlternativeFloat(self.number) + AlternativeFloat(other + plus)


builtins.float = AlternativeFloat
