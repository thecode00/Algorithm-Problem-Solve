# https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        """
        The test cases are generated such that there is at least one path between 1 and n.
        So you just need to check the distance between all the cities connected to 1
        """
        graph = [[] for _ in range(n + 1)]
        min_score = float("inf")
        for a, b, dist in roads:    # Add path
            graph[a].append((dist, b))
            graph[b].append((dist, a))
        stack = [1]
        visited = set()
        visited.add(1)  # Starting point
        while stack:
            cur = stack.pop()
            for dist, next in graph[cur]:
                min_score = min(min_score, dist)
                if next not in visited:
                    stack.append(next)
                    visited.add(next)   # Check visited city

        return min_score
