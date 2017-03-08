import builtins
import random


_str = builtins.str


class alt_str(_str):
    def __new__(cls, value, *args, **kwargs):
        value = _str(''.join(
            char
            for char in _str(value)
            if random.randint(0, 10) < 8
        ))
        return super().__new__(cls, value, *args, **kwargs)
