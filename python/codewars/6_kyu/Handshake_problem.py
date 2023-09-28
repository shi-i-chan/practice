from math import ceil, sqrt

def get_participants(h: int) -> int:
    return ceil((1 + sqrt(8 * h + 1)) / 2) if h != 0 else 0
