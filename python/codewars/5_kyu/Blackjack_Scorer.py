from typing import List

def score_hand(cards: List[str]) -> int:
    counter = sum([11 if value == 'A' else 10 if value in 'JQK' else int(value) for value in cards])
    for _ in range(cards.count('A')):
        if counter > 21:
            counter -= 10
    return counter
