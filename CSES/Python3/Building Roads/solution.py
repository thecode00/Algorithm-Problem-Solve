# https://cses.fi/problemset/task/1666/

import sys

input = sys.stdin.readline

cities, roads = map(int, input().split())

parent = [i for i in range(cities + 1)]


def find(num):
    if parent[num] != num:
        parent[num] = find(parent[num])
    return parent[num]


def union(a, b):
    a, b = find(a), find(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


for _ in range(roads):
    a, b = map(int, input().split())
    union(a, b)

need_connect = set()
for idx in range(1, cities + 1):
    need_connect.add(find(parent[idx]))

need_connect = list(need_connect)
print(len(need_connect) - 1)

if len(need_connect) != 1:
    main = need_connect[0]
    for idx in range(1, len(need_connect)):
        print(main, need_connect[idx])
