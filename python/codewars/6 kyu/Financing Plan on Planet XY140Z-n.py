def finance(n: int) -> int:
    return sum([sum([i for i in range(i, i + i + 1)]) for i in range(n, 0, -1)])

# or finance = lambda n: n * (n + 1) * (n + 2) / 2