# https://leetcode.com/problems/search-insert-position/

from bisect import bisect_left

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect_left(nums, target) 


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start < end:
            mid = start + (end - start) // 2
            if nums[mid] > target:
                end = mid - 1
            else:
                start = mid
        return start
