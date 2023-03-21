# https://leetcode.com/problems/number-of-zero-filled-subarrays/


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = 0   # Number of zero-fill subarray
        index = 0
        while index < len(nums):
            if nums[index] == 0:
                right = index
                while right < len(nums) and nums[right] == 0:
                    right += 1
                length = right - index
                count += length * (1 + length) // 2     # Sum of arithmetic sequences formula
                index = right   # Send index to not searched index
            else:
                index += 1
        return count
