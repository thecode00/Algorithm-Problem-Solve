# https://leetcode.com/problems/number-of-ways-to-split-array/description

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0
        valid = 0

        for idx in range(len(nums) - 1):
            left_sum += nums[idx]

            if left_sum >= total - left_sum:
                valid += 1

        return valid
