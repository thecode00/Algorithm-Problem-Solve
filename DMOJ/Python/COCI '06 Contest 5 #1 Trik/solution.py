# https://dmoj.ca/problem/coci06c5p1

import sys

input = sys.stdin.readline

triks = list(input().strip())
ball_position = 1   # Ball under the leftmost cup


def swap_ball(left: int, right: int, ball: int) -> int:
    # If ball in trik range move ball
    if ball == right:
        return left

    if ball == left:
        return right
    # Ball not in trik range
    return ball


for t in triks:
    if t == "A":
        ball_position = swap_ball(1, 2, ball_position)
    elif t == "B":
        ball_position = swap_ball(2, 3, ball_position)
    elif t == "C":
        ball_position = swap_ball(1, 3, ball_position)

print(ball_position)
