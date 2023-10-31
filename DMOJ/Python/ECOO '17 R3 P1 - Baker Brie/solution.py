# https://dmoj.ca/problem/ecoo17r3p1

import sys

input = sys.stdin.readline

for _ in range(10):
    f, d = map(int, input().split())
    franchises_amounts = [0] * f
    bonus = 0
    amounts = [list(map(int, input().split())) for _ in range(d)]
    # Get each day sales all franchises
    for y in range(d):
        total_all_franchises = 0
        for x, val in enumerate(amounts[y]):
            franchises_amounts[x] += val
            total_all_franchises += val
        if total_all_franchises % 13 == 0:
            bonus += total_all_franchises // 13
    # Get each franchises all sales
    for a in franchises_amounts:
        if a % 13 == 0:
            bonus += a // 13

    print(bonus)
