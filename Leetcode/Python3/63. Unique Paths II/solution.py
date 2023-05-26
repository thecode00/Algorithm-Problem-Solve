# https://leetcode.com/problems/unique-paths-ii/


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = [[0] * len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
        for y in range(len(obstacleGrid)):
            for x in range(len(obstacleGrid[0])):
                if obstacleGrid[y][x] == 1:
                    continue
                if y == 0 and x == 0:   # Start point
                    dp[y][x] = 1
                elif y == 0:
                    dp[y][x] = dp[y][x - 1]
                elif x == 0:
                    dp[y][x] = dp[y - 1][x]
                else:
                    dp[y][x] = dp[y - 1][x] + dp[y][x - 1]
        return dp[-1][-1]