import sys
import random
if sys.version_info >= (3,):
    import builtins
else:
    import __builtin__ as builtins


from destruction.FakeFloat import FakeFloat
builtins.float = FakeFloat

from destruction.FakeMath import FakeMath
sys.modules['math'] = FakeMath()
