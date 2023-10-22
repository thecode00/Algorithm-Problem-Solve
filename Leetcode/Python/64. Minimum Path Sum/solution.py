# https://leetcode.com/problems/minimum-path-sum/description/
# Time complexity: O(N * M), N = grid.length, M = grid[0].length


from collections import deque
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        len_x, len_y = len(grid[0]), len(grid)
        dp = [[float("inf") for _ in range(len_x)] for _ in range(len_y)]
        # Can move only right, down
        dx = [0, 1]
        dy = [1, 0]

        dp[0][0] = grid[0][0]   # Starting point
        queue = deque([(0, 0)])
        while queue:    # BFS
            x, y = queue.popleft()
            for idx in range(2):
                nx, ny = x + dx[idx], y + dy[idx]
                if 0 <= nx < len_x and 0 <= ny < len_y and dp[ny][nx] > dp[y][x] + grid[ny][nx]:
                    dp[ny][nx] = dp[y][x] + grid[ny][nx]
                    queue.append((nx, ny))
        print(dp)
        return dp[-1][-1]
