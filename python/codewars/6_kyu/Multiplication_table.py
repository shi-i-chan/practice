from typing import List

def multiplication_table(size: int) -> List:
    return [[x * y for x in range(1, size + 1)] for y in range(1, size + 1)]
