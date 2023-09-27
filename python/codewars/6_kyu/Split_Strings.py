from typing import List

def solution(string: str) -> List:
    def splt(string: str) -> List:
        return [string[i: i + 2] for i in range(0, len(string), 2)]
    return splt(string) if len(string) % 2 == 0 else splt(string + '_')
