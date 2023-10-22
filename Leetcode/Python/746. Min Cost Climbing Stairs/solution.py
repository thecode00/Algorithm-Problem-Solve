# https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:  # Runtime: 142ms
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [cost[0], cost[1]]  # Initialize dp list
        for idx in range(2, len(cost)):
            # Recurrence relation
            dp.append(min(cost[idx] + dp[idx - 1], cost[idx] + dp[idx - 2]))
        # We can climb 1, 2 step so we need check dp[last 2steps]
        return min(dp[-1], dp[-2])
