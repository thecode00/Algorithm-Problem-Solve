# https://leetcode.com/problems/n-th-tribonacci-number/

class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 2:
            return n
        elif n == 2:
            return 1
        dp = [0] * (n + 1)
        dp[0], dp[1], dp[2] = 0, 1, 1
        for idx in range(3, n + 1):
            # Recurrence relation
            dp[idx] = dp[idx - 1] + dp[idx - 2] + dp[idx - 3]
        return dp[n]
