# https://codeforces.com/problemset/problem/20/C

from collections import defaultdict
import heapq


n, m = map(int, input().split())

graph = defaultdict(list)

for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append((w, b))
    graph[b].append((w, a))

path = [(0, 1)]
parent = [0] * (n + 1)
distance = [float("inf")] * (n + 1)
distance[1] = 0

while path:
    dist, cur = heapq.heappop(path)

    for node in graph[cur]:
        cost, next_node = node
        new_cost = dist + cost
        if distance[next_node] > new_cost:
            distance[next_node] = new_cost
            parent[next_node] = cur
            heapq.heappush(path, (new_cost, next_node))

if distance[n] == float("inf"):
    print(-1)
else:
    path = []
    cur = n

    while cur:
        path.append(cur)
        cur = parent[cur]

    print(*reversed(path))
