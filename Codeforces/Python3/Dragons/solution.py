# https://codeforces.com/problemset/problem/230/A

import sys

input = sys.stdin.readline

s, n = map(int, input().split())
dragons = []
for _ in range(n):
    dragons.append(list(map(int, input().split())))
# In order to have as much power as possible in one battle, the larger the y, the more it is sent backwards.
dragons.sort(key=lambda x: (-x[0], x[1]))
while dragons:
    x, y = dragons.pop()
    if s <= x:
        print("NO")
        break
    s += y
else:
    print("YES")
