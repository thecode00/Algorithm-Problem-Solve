# https://www.acmicpc.net/problem/1389


from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n)]
for _ in range(m):
    # 입력이 1-index로 들어오므로 0-index로 만듬
    a, b = map(lambda x: x - 1, map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)


def search(start: int) -> int:
    dist = [-1] * n
    queue = deque()
    queue.append(start)
    dist[start] = 0
    while queue:
        cur = queue.popleft()
        next_dist = dist[cur] + 1
        for next in graph[cur]:
            if dist[next] == -1:
                dist[next] = next_dist
                queue.append(next)
    return sum(dist)


distances = [0] * n
# 사람들의 케빈베이컨수를 구함
for i in range(n):
    distances[i] = search(i)

min_kevin = 10000
min_people = 0
for idx, val in enumerate(distances):
    if val < min_kevin:
        min_people = idx
        min_kevin = val

print(min_people + 1)  # 0-index로 계산을 했으므로 1-index로 변환
