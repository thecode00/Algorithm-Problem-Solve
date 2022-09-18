# https://codeforces.com/problemset/problem/500/A

# This is Implemetion problem just follow problem

import sys

input = sys.stdin.readline

n, t = map(int, input().split())
portals = list(map(int, input().split()))
total, pos = 0, 0
while True:
    total += portals[pos]
    pos += portals[pos]
    if total + 1 > t:
        print("NO")
        break
    elif total + 1 == t:
        print("YES")
        break
