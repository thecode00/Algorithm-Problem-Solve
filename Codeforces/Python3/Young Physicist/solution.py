# https://codeforces.com/problemset/problem/69/A

import sys

input = sys.stdin.readline
print = sys.stdout.write

x, y, z = 0, 0, 0
for _ in range(int(input())):
    x1, y1, z1 = map(int, input().split())
    x -= x1
    y -= y1
    z -= z1
if x == 0 and y == 0 and z == 0:
    print("YES")
else:
    print("NO")
