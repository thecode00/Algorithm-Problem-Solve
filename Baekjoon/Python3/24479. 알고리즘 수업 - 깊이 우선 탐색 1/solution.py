# https://www.acmicpc.net/problem/24479

import sys

input = sys.stdin.readline


N, M, R = map(int, input().split())  # 정점개수, 간선개수, 시작점

edge, node = [[] for _ in range(N + 1)], [0] * (N + 1)
for _ in range(M):
    start, end = map(int, input().split())
    edge[start].append(end)  # 양방향 노선
    edge[end].append(start)

for l in edge:  # 정점 번호를 오름차순으로 방문하기위해 각 간선을 정렬
    l.sort(key=lambda x: -x)

node[R] = 1
stack, visit = edge[R], 2

while stack:
    n = stack.pop()
    if node[n] != 0:  # 이미 방문했던 노드는 무시
        continue
    node[n] = visit
    visit += 1
    for end in edge[n]:
        stack.append(end)
for idx in range(1, N + 1):
    print(node[idx])
