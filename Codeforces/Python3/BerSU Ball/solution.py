# https://codeforces.com/problemset/problem/489/B

import sys

input = sys.stdin.readline

n = int(input())
boys = list(map(int, input().split()))
m = int(input())
girls = list(map(int, input().split()))
pair, last_idx = 0, -1

boys.sort()
girls.sort()

for b in boys:
    for idx in range(last_idx + 1, m):
        if abs(b - girls[idx]) <= 1:
            pair += 1
            last_idx = idx  # Store indexe to reduce search range
            break
print(pair)
