# https://leetcode.com/problems/binary-search/

from bisect import bisect_left
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1   # When target dose not exist in nums


class Solution:  # Use built-in function
    def search(self, nums: List[int], target: int) -> int:
        index = bisect_left(nums, target)
        if index >= len(nums) or nums[index] != target:
            return -1
        return index
