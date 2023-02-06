# https://leetcode.com/problems/climbing-stairs/


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return n
        dp = [1, 1]
        for idx in range(2, n + 1):
            dp.append(dp[idx - 1] + dp[idx - 2])
        return dp[n]
