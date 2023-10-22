
from typing import List


def bellman_ford(graph: List[int], start: int, n: int):
    # n = Number of nodes, m = number of edges
    m = len(graph)
    distance = [float("inf") for _ in range(n + 1)]
    distance[start] = 0

    for _ in range(n):
        for idx in range(m):
            a, b, w = graph[idx]
            if distance[a] != float("inf") and distance[a] + w < distance[b]:
                distance[b] = distance[a] + w

    for idx in range(m):    # Find negative cycle
        a, b, w = graph[idx]
        if distance[a] != float("inf") and distance[a] + w < distance[b]:
            return None  # Exist negative cycle

    return distance
