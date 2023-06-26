
# https://leetcode.com/problems/evaluate-division/


from collections import defaultdict
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        parent = dict()

        def find(string: str):
            if string != parent[string]:
                parent[string] = find(parent[string])
            return parent[string]

        def union(a: str, b: str):
            a, b = find(a), find(b)
            if a > b:
                parent[a] = b
            else:
                parent[b] = a

        # graph[a][b] = relation between a and b
        graph = defaultdict(dict)
        for idx, val in enumerate(equations):
            a, b = val[0], val[1]
            value = values[idx]
            graph[a][b] = value  # a is b * value
            graph[b][a] = 1 / value  # b is a * 1 / value
            if a not in parent:
                parent[a] = a
            if b not in parent:
                parent[b] = b
            union(a, b)

        result = []
        for c, d in queries:
            if find(c) != find(d):
                result.append(-1.0)
            else:
                stack = [(c, 1)]
                visited = set()
                visited.add(c)  # Start point
                while stack:
                    cur, total = stack.pop()
                    if cur == d:    # Found target
                        result.append(total)
                        break
                    for next, mul in graph[cur].items():
                        if next not in visited:
                            stack.append(next, total * mul)
                            visited.add(next)   # Check visit
        return result
