# https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:  # Runtime: 302 ms
        """
        Do not return anything, modify nums in-place instead.
        """
        position = 0
        for idx in range(len(nums)):
            if nums[idx] != 0:
                nums[position], nums[idx] = nums[idx], nums[position]
                position += 1
    def moveZeroes(self, nums: List[int]) -> None:  # Runtime: 261 ms
        point = 0
        length = len(nums)
        for idx in range(length):
            if nums[idx]:
                nums[point] = nums[idx]
                point += 1
        for idx in range(point, length):
            nums[idx] = 0