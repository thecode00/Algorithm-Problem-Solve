# https://www.acmicpc.net/problem/11657

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
edges = []
distances = [float("inf")] * (n + 1)

for _ in range(m):
    edges.append(tuple(map(int, input().split())))


def bellman_ford() -> bool:
    """ 벨만포드 알고리즘을 실행하는 함수

    Returns:
        음수사이클의 존재여부를 알려주는 bool반환
    """
    distances[1] = 0
    for i in range(n):
        for a, b, c in edges:
            if distances[a] != float("inf") and distances[b] > distances[a] + c:
                if i == n - 1:  # 모든 노드를 다 삼펴본뒤에도 거리가 줄어들면 음수사이클이 존재하는것
                    return True
                distances[b] = distances[a] + c
    return False


is_cycle = bellman_ford()

if is_cycle:
    print(-1)
else:
    for dist in distances[2:]:
        print(dist if dist != float("inf") else -1)
