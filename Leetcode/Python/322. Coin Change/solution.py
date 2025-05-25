# https://leetcode.com/problems/coin-change/description/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for idx in range(1, amount + 1):
            for coin in coins:
                if idx - coin >= 0:
                    dp[idx] = min(dp[idx], dp[idx - coin] + 1)

        return dp[-1] if dp[-1] != float("inf") else -1