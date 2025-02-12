# https://codeforces.com/problemset/problem/1989/A

import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    if y >= -1:
        print("YES")
    else:
        print("NO")
