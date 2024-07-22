# https://codeforces.com/problemset/problem/791/A

import sys
input = sys.stdin.readline

a, b = map(int, input().split())
year = 0

while a <= b:
    a *= 3
    b *= 2
    year += 1

print(year)
