# https://school.programmers.co.kr/learn/courses/30/lessons/86971

from collections import defaultdict


def solution(n, wires):
    graph = defaultdict(list)

    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)

    dp = [1 for _ in range(n + 1)]
    visited = [False for _ in range(n + 1)]

    def dfs(index):  # 서브트리들의 노드개수 구하기
        visited[index] = True
        if not graph[index]:    # 리프노드일 경우 그냥 넘어감
            return
        for node in graph[index]:
            if not visited[node]:
                dfs(node)
                dp[index] += dp[node]
    dfs(1)

    visited = [False for _ in range(n + 1)]

    def find(index):
        min_diff = float("inf")
        visited[index] = True
        if dp[index] == 1:
            return min_diff
        for node in graph[index]:
            if not visited[node]:
                # 현재 서브트리를 분리한 부모트리의 노드개수: dp[1] - dp[node], 현재 서브트리의 노드개수: dp[node]
                # 전봇대 노드 차이 = dp[1] - dp[node] - dp[node] = dp[1] - dp[node] * 2
                min_diff = min(find(node), min_diff, abs(dp[1] - dp[node] * 2))
                # print(node, index, min_diff, dp[index], dp[node])
        return min_diff

    return find(1)
