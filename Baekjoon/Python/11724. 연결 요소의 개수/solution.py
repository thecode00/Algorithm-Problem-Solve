# https://www.acmicpc.net/problem/11724

# 인접리스트 방식
import sys

input = sys.stdin.readline

n, m = map(int, input().split())    # 노드, 간선 개수
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
component = 0

for _ in range(m):
    u, v = map(int, input().split())
    # 무방향 그래프이므로 양쪽에 노드 추가
    graph[u].append(v)
    graph[v].append(u)


def dfs(start: int):
    stack = [start]
    visited[start] = True
    while stack:
        cur = stack.pop()
        for next in graph[cur]:
            if not visited[next]:
                stack.append(next)
                visited[next] = True    # 백트래킹을 위해 스택에 추가할때 방문처리


for node in range(1, n + 1):
    if not visited[node]:   # 아직 방문하지않은 연결요소 방문처리
        component += 1
        dfs(node)

print(component)

# 인접행렬 방식

input = sys.stdin.readline

n, m = map(int, input().split())    # 노드, 간선 개수
vec = [[0] * (n + 1) for _ in range(n + 1)]
visited = [False] * (n + 1)
component = 0

for _ in range(m):
    u, v = map(int, input().split())
    # 무방향 그래프이므로 양쪽에 노드 추가, vec[u][v]가 1이면 u, v노드가 연결돼있다는 뜻
    vec[u][v] = vec[v][u] = 1


def dfs(start: int):
    visited[start] = True
    stack = [start]
    while stack:
        cur = stack.pop()
        for next in range(1, n + 1):
            if vec[cur][next] and not visited[next]:
                visited[next] = True
                stack.append(next)


for node in range(1, n + 1):
    if not visited[node]:
        component += 1
        dfs(node)

print(component)
