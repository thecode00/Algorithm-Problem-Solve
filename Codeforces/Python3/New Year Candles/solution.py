# https://codeforces.com/problemset/problem/379/A

import sys

input = sys.stdin.readline

a, b = map(int, input().split())
used = 0
hour = 0
while a + used >= b:
    hour += a
    used += a
    a = used // b
    used %= b
else:  # Check remaining new candle
    hour += a
print(hour)
