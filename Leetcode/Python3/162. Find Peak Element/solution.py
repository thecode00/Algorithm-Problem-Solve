# https://leetcode.com/problems/find-peak-element/


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        while start < end:
            mid = start + (end - start) // 2
            print(mid)
            if nums[mid + 1] < nums[mid] and nums[mid] > nums[mid - 1]:
                return mid

            if nums[mid] < nums[mid + 1]:
                start = mid + 1
            else:
                end = mid - 1
        return start if nums[start] > nums[end] else end
