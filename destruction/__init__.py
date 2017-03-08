import sys

if sys.version_info >= (3,):
    import builtins
else:
    import __builtin__ as builtins


from destruction.AlternativeFloat import AlternativeFloat
builtins.float = AlternativeFloat


from destruction.AlternativeMath import AlternativeMath
sys.modules['math'] = AlternativeMath()


from destruction.AlternativeSorting import alternative_shuffle, alternative_sorted
import random
builtins.sorted = alternative_sorted
random.shuffle = alternative_shuffle
