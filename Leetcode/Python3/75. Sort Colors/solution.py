# https://leetcode.com/problems/sort-colors/


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        nums.sort()


class Solution:  # Insertion sort
    def sortColors(self, nums: List[int]) -> None:
        idx = 1
        while idx < len(nums):
            temp = idx
            while temp > 0 and nums[temp] < nums[temp - 1]:
                nums[temp], nums[temp - 1] = nums[temp - 1], nums[temp]
                temp -= 1
            idx += 1
