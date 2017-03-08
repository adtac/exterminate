import sys
import random
if sys.version_info >= (3,):
    import builtins
else:
    import __builtin__ as builtins


from destruction.AlternativeFloat import AlternativeFloat
builtins.float = AlternativeFloat


from destruction.AlternativeMath import AlternativeMath
sys.modules['math'] = AlternativeMath()


from destruction.AlternativeRange import alternative_range
builtins.range = alternative_range
