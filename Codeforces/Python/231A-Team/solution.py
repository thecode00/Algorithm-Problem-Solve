# https://codeforces.com/problemset/problem/231/A

import sys

input = sys.stdin.readline

n = int(input())
solved = 0

for _ in range(n):
    if sum(map(int, input().split())) >= 2:
        solved += 1

print(solved)
