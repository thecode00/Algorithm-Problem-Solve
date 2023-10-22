# https://codeforces.com/problemset/problem/231/A

import sys

input = sys.stdin.readline

total = 0
for _ in range(int(input())):
    answer = list(map(int, input().split()))
    if sum(answer) >= 2:
        total += 1
print(total)
