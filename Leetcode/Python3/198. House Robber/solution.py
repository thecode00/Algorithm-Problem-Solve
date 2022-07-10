# https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        dp = [0] * length
        if length <= 1:
            return nums[0]
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for idx in range(2, length):
            # Recurrence relation
            dp[idx] = max(nums[idx] + dp[idx - 2], dp[idx - 1])
        return dp[-1]
