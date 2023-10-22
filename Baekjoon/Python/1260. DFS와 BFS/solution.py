# https://www.acmicpc.net/problem/1260

from collections import deque
import sys


input = sys.stdin.readline

n, m, v = map(int, input().split())  # 노드 개수, 간선 개수, 시작 노드
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)
for idx in range(1, n + 1):
    graph[idx].sort()

# DFS
visited = {}
stack = [v]
while stack:
    node = stack.pop()
    if node in visited:
        continue
    visited[node] = 1
    print(node, end=" ")
    for n in graph[node][::-1]:
        if n not in visited:
            stack.append(n)
print()

# BFS
visited = {}
queue = deque()
queue.append(v)
while queue:
    node = queue.popleft()
    if node in visited:
        continue
    print(node, end=" ")
    visited[node] = 1
    for n in graph[node]:
        if n not in visited:
            queue.append(n)
