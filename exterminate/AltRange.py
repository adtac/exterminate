from exterminate.Utilities import builtins


_range = range


def alt_range(start, stop, step=1):
    return _range(start-2, stop+2, max(1, int(step/2)))


builtins.range = alt_range
