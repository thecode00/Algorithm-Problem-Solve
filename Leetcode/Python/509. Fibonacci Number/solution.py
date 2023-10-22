# https://leetcode.com/problems/fibonacci-number/

class Solution: # Tabulation(bottom-up)
    def fib(self, n: int) -> int:
        if n <= 1:
            return 1
        
        dp = [0, 1]
        for idx in range(2, n + 1):
            dp.append(dp[idx - 1] + dp[idx - 2])
        return dp[n]
    

class Solution:  # Use only two variable
    def fib(self, n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a
