import random

from exterminate.Utilities import builtins


_shuffle = random.shuffle
_sorted = builtins.sorted


def alt_shuffle(a: list, *args, **kwargs):
    a.sort()  # Shuffle returns None and shuffles in place


def alt_sorted(a, *args, **kwargs):
    shuffled = list(a)
    _shuffle(shuffled)
    return shuffled


builtins.sorted = alt_sorted
builtins.shuffle = alt_shuffle
