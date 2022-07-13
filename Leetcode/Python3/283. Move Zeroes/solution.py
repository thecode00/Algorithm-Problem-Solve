# https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        position = 0
        for idx in range(len(nums)):
            if nums[idx] != 0:
                nums[position], nums[idx] = nums[idx], nums[position]
                position += 1
