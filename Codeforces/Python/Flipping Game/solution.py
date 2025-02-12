# https://codeforces.com/problemset/problem/327/A

import sys

input = sys.stdin.readline


def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    original_one = sum(arr)
    max_score = 1 if arr[0] == 0 else -1
    flip_advantage = 0

    # Kadane's Algorithm
    for idx in range(len(arr)):
        flip_score = -1 if arr[idx] == 1 else 1
        flip_advantage += flip_score

        max_score = max(max_score, flip_advantage)

        flip_advantage = max(flip_advantage, 0)

    print(max_score + original_one)


solve()
