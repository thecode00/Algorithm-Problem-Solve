# https://leetcode.com/problems/is-graph-bipartite/


from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [-1] * len(graph)

        def dfs(start: int) -> bool:
            stack = [start]
            color[start] = 1
            while stack:
                cur = stack.pop()
                for next in graph[cur]:
                    # If adjacent node has same color return False
                    if color[next] == color[cur]:
                        return False
                    # Change color not visited node
                    if color[next] == -1:
                        if color[cur] == 1:
                            color[next] = 0
                        else:
                            color[next] = 1
                        stack.append(next)
            return True

        for idx in range(len(graph)):
            if color[idx] == -1:
                if not dfs(idx):
                    return False
        return True
