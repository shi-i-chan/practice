def count(string: str) -> dict:
    return {value: string.count(value) for value in string}
