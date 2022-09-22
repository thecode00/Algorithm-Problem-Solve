# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/?envType=study-plan&id=algorithm-ii


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        start, end = 0, length - 1
        left, right = 0, 0
        while start <= end:
            mid = (start + end) >> 1
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        left = start
        start, end = 0, length - 1
        while start <= end:
            mid = (start + end) >> 1
            if nums[mid] <= target:
                start = mid + 1
            else:
                end = mid - 1
        right = end
        return [left, right] if left <= right else [-1, -1]
