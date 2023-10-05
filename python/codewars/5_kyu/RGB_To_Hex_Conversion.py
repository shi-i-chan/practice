def rgb(r: int, g: int, b: int) -> str:
    round = lambda x: max(0, min(x, 255))
    return ''.join('%02X' % i for i in [round(value) for value in (r, g, b)])
