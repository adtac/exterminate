import sys
import random
import math as actual_math


RANGE = (-0.01, 0.01)

class FakeMath:
    def __init__(self):
        self.custom_pi = actual_math.pi
        self.custom_e = actual_math.e

    @property
    def pi(self):
        self.custom_pi += random.uniform(*RANGE)
        return self.custom_pi

    @property
    def e(self):
        self.custom_e += random.uniform(*RANGE)
        return self.custom_e

    def __getattr__(self, name):
        """
        We don't want to break the entire math module. So if we get anything
        other than `e` or `pi`, let's give it to the original module.
        """
        return getattr(actual_math, name)

FakeMath.__doc__ = actual_math.__doc__
