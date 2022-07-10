# https://leetcode.com/problems/peak-index-in-a-mountain-array/

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        start, end = 0, len(arr) - 1
        while start <= end:
            mid = (start + end) >> 1
            if arr[mid] <= arr[mid + 1]:
                start = mid
            else:
                end = mid - 1
        return start
