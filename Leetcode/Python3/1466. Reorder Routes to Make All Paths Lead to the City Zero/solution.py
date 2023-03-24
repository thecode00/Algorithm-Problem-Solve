# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/
# Ref: https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/solutions/661774/python3-easy-short-dfs/?orderBy=most_votes

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        visited = set()
        visited.add(0)  # Starting point
        count = 0

        path = [[] for _ in range(n)]
        for start, end in connections:
            # 1 = cost for reverse original path, 0 = reversed path
            path[start].append((end, 1))
            path[end].append((start, 0))

        stack = [0]
        while stack:
            cur = stack.pop()
            for next, cost in path[cur]:
                if next not in visited:
                    visited.add(next)
                    # If the original road is the same as the current direction, it cant reach 0
                    # So add reverse cost
                    count += cost
                    stack.append(next)
        return count
