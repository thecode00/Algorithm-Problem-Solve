# https://codeforces.com/problemset/problem/1697/B

import sys

input = sys.stdin.readline
print = sys.stdout.write

n, q = map(int, input().split())    # Number of items, query
items = list(map(int, input().split()))
items.sort(reverse=True)
for idx in range(1, n):
    items[idx] = items[idx] + items[idx - 1]
# print(items)
for _ in range(q):
    x, y = map(int, input().split())
    if x == y:
        print(str(items[x - 1]) + "\n")
    else:
        print(str(items[x - 1] - items[x - y - 1]) + "\n")
