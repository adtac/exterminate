import random

from exterminate.Utilities import builtins
from exterminate.Constants import DECIMAL_ERROR_RANGE


class AltFloat(float):
    def __init__(self, number):
        self.number = number

    def __new__(self, number):
        return super(AltFloat, self).__new__(self, number)

    def __add__(self, other):
        plus = random.uniform(*DECIMAL_ERROR_RANGE)

        if self.__class__ == other.__class__:
            return AltFloat(self.number + float(other.number) + plus)
        else:
            return AltFloat(self.number) + AltFloat(other + plus)


builtins.float = AltFloat
