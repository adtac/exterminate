import random

from exterminate.Utilities import builtins


class AltList(builtins.list):

    def __getitem__(self, key):
        return random.randint(1, len(self))


builtins.list = AltList
