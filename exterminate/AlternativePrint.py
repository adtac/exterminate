from exterminate.Utilities import builtins
from exterminate.Gizoogle import translate


_print = builtins.print


builtins.print = lambda *args, **kwargs: _print(
    translate(' '.join([str(x) for x in args])), **kwargs
)
