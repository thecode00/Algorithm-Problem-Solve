# https://codeforces.com/problemset/problem/1800/C1

import heapq
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    deck = list(map(int, input().split()))

    bonus = []
    power = 0

    for card in deck:
        if card == 0 and bonus:
            power += -heapq.heappop(bonus)
        elif card != 0:
            heapq.heappush(bonus, -card)

    print(power)
