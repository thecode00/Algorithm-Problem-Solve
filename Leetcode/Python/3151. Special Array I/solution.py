# https://leetcode.com/problems/special-array-i/description

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for idx in range(1, len(nums)):
            if nums[idx - 1] & 1 == nums[idx] & 1:
                return False

        return True
