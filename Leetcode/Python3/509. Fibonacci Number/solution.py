# https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        if n in [0, 1]:
            return n
        dp = [0] * (n + 1)
        dp[0], dp[1] = 0, 1
        for idx in range(2, n + 1):
            dp[idx] = dp[idx - 1] + dp[idx - 2]  # Recurrence relation
        return dp[n]
