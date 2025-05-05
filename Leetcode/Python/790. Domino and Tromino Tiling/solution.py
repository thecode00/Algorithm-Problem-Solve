# https://leetcode.com/problems/domino-and-tromino-tiling/description

class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7

        if n == 0:
            return 1
        elif n == 1:
            return 1
        elif n == 2:
            return 2

        dp = [0] * (n + 1)
        dp[0], dp[1], dp[2] = 1, 1, 2

        # dp[n] = dp[n - 1] + dp[n - 2] + (dp[n - 3] + dp[n - 4] + ... + dp[0]) * 2
        # = dp[n - 1] + dp[n - 2] + dp[n - 3] + dp[n - 3] + (dp[n - 4] + dp[n - 5] + ... + dp[0]) * 2
        # = dp[n - 1] + dp[n - 3] + (dp[n - 2] + dp[n - 3] + (dp[n - 4] + dp[n - 5] + ... + dp[0]) * 2)
        # = dp[n - 1] + dp[n - 3] + dp[n - 1]
        # = dp[n - 1] * 2 + dp[n - 3]
        # dp[n - 1] = dp[n - 2] + dp[n - 3] + (dp[n - 4] + ... + dp[0]) * 2
        for i in range(3, n + 1):
            dp[i] = (2 * dp[i - 1] + dp[i - 3]) % MOD

        return dp[n]
