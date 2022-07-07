# https://leetcode.com/problems/climbing-stairs/


class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2
        for idx in range(3, n + 1):
            dp[idx] = dp[idx - 1] + dp[idx - 2]
        return dp[n]
