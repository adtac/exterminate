import random
import builtins

_shuffle = random.shuffle
_sorted = builtins.sorted


def alternative_shuffle(a: list, *args, **kwargs):
    a.sort()  # Shuffle returns None and shuffles in place


def alternative_sorted(a, *args, **kwargs):
    shuffled = list(a)
    _shuffle(shuffled)
    return shuffled
