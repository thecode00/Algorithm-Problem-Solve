# https://leetcode.com/problems/rotate-array/

from collections import deque
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k %= length
        nums[:] = nums[length - k:] + nums[:length - k]


class Solution:  # Ref: https://leetcode.com/problems/rotate-array/solutions/54250/easy-to-read-java-solution/?envType=study-plan-v2&envId=top-interview-150

    def reverse(self, start: int, end: int, nums: List[int]) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        length = len(nums)
        k %= length

        self.reverse(0, length - 1, nums)
        self.reverse(0, k - 1, nums)
        self.reverse(k, length - 1, nums)
