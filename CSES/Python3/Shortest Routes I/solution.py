# https://cses.fi/problemset/task/1671


import heapq
import sys

input = sys.stdin.readline

n, m = map(int, input().split())    # Number of cities, flights
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    # Start city, end city, length between a, b
    a, b, l = map(int, input().split())
    graph[a].append((l, b))

# distance[x] is shortest length between 1, x
distance = [float("inf") for _ in range(n + 1)]
distance[1] = 0  # Start point
heap = []
heapq.heappush(heap, (0, 1))

while heap:  # Dijkstra
    length, cur = heapq.heappop(heap)
    if distance[cur] < length:
        continue
    for l, n in graph[cur]:
        weight = length + l
        if (distance[n] > weight):
            distance[n] = weight
            heapq.heappush(heap, (weight, n))
print(" ".join(map(str, distance[1:])))
