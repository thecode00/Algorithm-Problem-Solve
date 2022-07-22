# https://leetcode.com/problems/house-robber-ii/

# Ref: https://leetcode.com/problems/house-robber-ii/discuss/893957/Python-Just-use-House-Robber-twice
class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:
            return nums[0]
        dp1, dp2 = 0, 0
        for idx in range(length - 1):   # If rob first house we cant rob last house 
            dp1, dp2 = dp2, max(dp1 + nums[idx], dp2)
        dp3, dp4 = 0, 0
        for idx in range(1, length):    # If rob last house we cant rob first house
            dp3, dp4 = dp4, max(dp3 + nums[idx], dp4)
        # print(dp2, dp4)
        return max(dp2, dp4)