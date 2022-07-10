# https://leetcode.com/problems/rotate-array/

from collections import deque


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k %= length
        nums[:] = nums[length - k:] + nums[:length - k]
