# https://leetcode.com/problems/jump-game-ii/

# Ref: https://leetcode.com/problems/jump-game-ii/discuss/170518/8-Lines-in-Python!-Easiest-Solution!
class Solution:
    def jump(self, nums: List[int]) -> int:
        length = len(nums)
        if length <= 1:
            return 0
        left, right = 0, nums[0]
        times = 1
        while right < length - 1:
            times += 1
            left, right = right, max(i + nums[i] for i in range(left, right + 1))
        return times

                
            