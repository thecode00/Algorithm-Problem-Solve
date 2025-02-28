# https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/description

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        total = 0
        negative_total = 0
        positive_total = 0

        # Get biggest diff from zero and remove smallest diff total for maximize abs
        for num in nums:
            total += num

            negative_total = min(negative_total, total)
            positive_total = max(positive_total, total)

        return positive_total - negative_total
