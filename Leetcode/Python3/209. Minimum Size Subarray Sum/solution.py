# https://leetcode.com/problems/minimum-size-subarray-sum/


from typing import List


class Solution: # Sliding window
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