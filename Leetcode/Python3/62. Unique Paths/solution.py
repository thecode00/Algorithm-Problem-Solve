# https://leetcode.com/problems/unique-paths/


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        for y in range(m):
            for x in range(n):
                # Robot can only move right, down so border of top and left unique path is 1
                if y == 0 or x == 0:
                    dp[y][x] == 1
                else:
                    # Path from top and left
                    dp[y][x] = dp[y - 1][x] + dp[y][x - 1]
        return dp[-1][-1]
                