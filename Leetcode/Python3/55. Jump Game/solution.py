# https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp, length = 0, len(nums)   # dp = max index where we can reach
        for idx in range(length):
            if dp < idx:    # When we cant reach current index return False    
                return False
            dp = max(dp, nums[idx] + idx)
        return True