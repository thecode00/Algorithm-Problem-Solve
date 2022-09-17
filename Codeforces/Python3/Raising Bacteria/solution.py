# https://codeforces.com/problemset/problem/579/A

import sys

input = sys.stdin.readline

target = int(input())
answer = 0
# Bacteria increase in multiples of 2, so divide the target by 2 and add the minimum number of bacteria for each remainder.
while target >= 1:
    if target % 2 != 0:
        answer += 1
    target //= 2
print(answer)
