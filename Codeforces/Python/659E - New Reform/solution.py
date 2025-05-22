# https://codeforces.com/problemset/problem/659/E

from collections import defaultdict


n, m = map(int, input().split())
graph = defaultdict(list)
visited = [False] * n

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1

    graph[a].append(b)
    graph[b].append(a)


def dfs(start: int):
    stack = []
    stack.append((start, -1))
    visited[start] = True

    while stack:
        city, prev_city = stack.pop()

        for next_city in graph[city]:
            if visited[next_city] and next_city != prev_city:
                return 0
            if not visited[next_city]:
                visited[next_city] = True
                stack.append((next_city, city))
    return 1


trees = 0

for city in range(n):
    if not visited[city]:
        trees += dfs(city)

print(trees)
