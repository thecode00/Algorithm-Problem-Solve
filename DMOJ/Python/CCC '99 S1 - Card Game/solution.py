# https://dmoj.ca/problem/ccc99s1

import sys

input = sys.stdin.readline

high_card = {"jack": 1, "queen": 2, "king": 3, "ace": 4}
score_a = score_b = 0
turn = 0    # 0 = Player A turn, 1 = player B turn
remain_card = 52

deck = [input().rstrip() for _ in range(remain_card)]


def check_score(remain: int, need: int, start: int) -> int:
    """
    Check high card score
    """
    if remain < need:
        return 0

    for i in range(need):
        if deck[start + i] in high_card:
            return 0

    return need


for idx in range(52):
    remain_card -= 1
    card = deck[idx]

    if card in high_card:
        score = check_score(remain_card, high_card[card], idx + 1)
        if score != 0:
            if turn == 0:
                print(f"Player A scores {score} point(s).")
                score_a += score
            else:
                print(f"Player B scores {score} point(s).")
                score_b += score
    # Pass turn
    turn ^= 1

print(f"Player A: {score_a} point(s).")
print(f"Player B: {score_b} point(s).")
