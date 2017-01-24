import sys
import random
if sys.version_info >= (3,):
    import builtins
else:
    import __builtin__ as builtins


from FakeFloat import FakeFloat
builtins.float = FakeFloat

from FakeMath import FakeMath
sys.modules['math'] = FakeMath()
