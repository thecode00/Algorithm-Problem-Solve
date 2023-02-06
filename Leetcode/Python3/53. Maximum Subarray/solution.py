"""
https://leetcode.com/problems/maximum-subarray/
Time complexity: O(N)
"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for idx in range(1, len(nums)):
            # Add to the current value only when the previous sums are positive.
            if nums[idx - 1] > 0:
                nums[idx] += nums[idx - 1]
        return max(nums)


class Solution: # Kadane`s algorithm
    def maxSubArray(self, nums: List[int]) -> int:
        best_sum = -float("inf")
        current_sum = 0
        for num in nums:
            current_sum = max(num, current_sum + num)
            best_sum = max(best_sum, current_sum)
        
        return best_sum