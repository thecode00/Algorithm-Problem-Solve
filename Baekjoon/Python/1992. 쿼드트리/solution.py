# https://www.acmicpc.net/problem/1992

import sys
from typing import List

input = sys.stdin.readline
n = int(input())
board = [list(input()) for _ in range(n)]


def zip(x: int, y: int, board: List[List[int]], length: int) -> int:
    if length == 1:
        return board[y][x]
    letter = board[y][x]
    for i in range(y, y + length):
        for j in range(x, x + length):
            if letter != board[i][j]:
                return ("(" + str(zip(x, y, board, length // 2))    # 1사분면
                        + str(zip(x + length // 2, y, board, length // 2))  # 2사분면
                        + str(zip(x, y + length // 2, board, length // 2))  # 3사분면
                        + str(zip(x + length // 2, y + length // 2, board, length // 2)) + ")")  # 4사분면
    return letter


print(f"{zip(0, 0, board, n)}")
