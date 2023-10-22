"""
https://codeforces.com/problemset/problem/339/B
"""

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
tasks = list(map(int, input().split()))
now, time = 1, 0
for task in tasks:
    if now > task:  # Need rotate to house 1
        time += n - now + task
    else:
        time += task - now
    now = task
print(time)
