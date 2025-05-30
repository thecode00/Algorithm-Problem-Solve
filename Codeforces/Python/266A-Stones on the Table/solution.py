# https://codeforces.com/problemset/problem/266/A

import sys

input = sys.stdin.readline

n = int(input())

table = list(input().rstrip())

taken = 0

idx = 0
while idx < n:
    cur_color = table[idx]

    idx += 1
    while idx < n and cur_color == table[idx]:
        idx += 1
        taken += 1

print(taken)

# Pythonic
n = int(input())
s = input().strip()
print(sum(s[i] == s[i-1] for i in range(1, len(s))))
