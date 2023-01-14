# https://www.acmicpc.net/problem/1753


from collections import defaultdict
import heapq
import sys

input = sys.stdin.readline

v, e = map(int, input().split())    # 정점, 간선 개수
k = int(input())    # 시작 정점
graph = defaultdict(list)
dist = defaultdict(int)  # 최소거리를 담을 딕셔너리

for _ in range(e):
    s, e, w = map(int, input().split())  # 출발, 도착, 가중치
    graph[s].append((e, w))

heap = [(0, k)]
while heap:
    distance, node = heapq.heappop(heap)
    if node not in dist:
        dist[node] = distance
        for vtx, weight in graph[node]:
            heapq.heappush(heap, (distance + weight, vtx))

for node in range(1, v + 1):
    if node not in dist: # node까지 가는 경로가 없는경우
        print("INF")
    else:
        print(dist[node])
