# https://school.programmers.co.kr/learn/courses/30/lessons/49189

import heapq
from collections import deque


def solution(n, edge):  # BFS
    graph = [[] for _ in range(n + 1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    distance = [-1] * (n + 1)
    # 시작지점 처리
    distance[1] = 0
    queue = deque([1])
    while queue:
        cur = queue.popleft()
        for next in graph[cur]:
            if distance[next] == -1:
                distance[next] = distance[cur] + 1
                queue.append(next)

    return distance.count(max(distance))


def solution(n, edge):  # 다익스트라
    graph = [[] for _ in range(n + 1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    distance = [float("inf")] * (n + 1)
    # 시작지점 처리
    distance[1] = 0
    heap = [(0, 1)]
    while heap:
        dist, cur = heapq.heappop(heap)
        if dist < distance[cur]:
            continue
        for next in graph[cur]:
            next_dist = dist + 1
            if distance[next] > next_dist:
                distance[next] = next_dist
                heapq.heappush(heap, (next_dist, next))
    return distance.count(max([d for d in distance if d != float("inf")]))
