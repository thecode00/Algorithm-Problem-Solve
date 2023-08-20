# https://leetcode.com/problems/minimum-size-subarray-sum/


from bisect import bisect_right
from typing import List


class Solution:  # Sliding window
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float("inf")
        total = left = 0
        for idx in range(len(nums)):
            total += nums[idx]
            while total >= target:
                min_length = min(min_length, idx - left + 1)
                total -= nums[left]
                left += 1
        return min_length if min_length != float("inf") else 0


class Solution:  # Prefix sum and binary search
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        # Make prefix sum, nums[i] = sum nums 0 ~ i
        for idx in range(1, len(nums)):
            nums[idx] += nums[idx - 1]
        min_length = float("inf")
        for right, num in enumerate(nums):
            if num >= target:
                # Find upper_bound index of maximum value that can be subtracted from the sum of elements in nums from index 0 to idx to make it equal to the target.
                left = bisect_right(nums, num - target)
                min_length = min(min_length, right - left + 1)

        return min_length if min_length != float("inf") else 0
