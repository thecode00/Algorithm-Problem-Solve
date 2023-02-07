# https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        
        dp = [-1 for _ in range(len(nums))]
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for idx in range(2, len(nums)):
            # Not robbed current house and robbed current house
            dp[idx] = max(dp[idx - 1], dp[idx - 2] + nums[idx]) 
        return dp[-1]
        

