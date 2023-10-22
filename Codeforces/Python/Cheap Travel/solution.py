# https://codeforces.com/problemset/problem/466/A

import sys

input = sys.stdin.readline

n, m, a, b = map(int, input().split())
if m * a <= b:
    print(n * a)
else:
    total = n // m * b
    total += min(n % m * a, b)
    print(total)
