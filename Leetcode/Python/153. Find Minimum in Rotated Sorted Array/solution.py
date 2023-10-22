# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/?envType=study-plan&id=algorithm-ii

from xml.dom import minidom


class Solution:
    def findMin(self, nums: List[int]) -> int:  # Easy solution
        nums.sort()
        return nums[0]

    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        while start < end:
            mid = start + (end - start) // 2
            if nums[mid] > nums[end]:
                # If nums[mid] > nums[end] list is rotated
                start = mid + 1
            else:
                end = mid
        return nums[end]
