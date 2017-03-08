_range = range


def alternative_range(start, stop, step=1):
    return _range(start-2, stop+2, max(1, int(step/2)))
