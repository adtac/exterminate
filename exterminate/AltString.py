from exterminate.Utilities import builtins
import random


_str = builtins.str


class alt_str(_str):
    def __new__(cls, value, *args, **kwargs):
        value = _str(''.join(
            char
            for char in _str(value)
            if random.randint(1, 5) > 1
        ))
        return super().__new__(cls, value, *args, **kwargs)


builtins.str = alt_str
