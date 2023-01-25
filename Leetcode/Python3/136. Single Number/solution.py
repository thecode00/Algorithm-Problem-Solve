# https://leetcode.com/problems/single-number/


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            # ^: XOR if both number same result is 0 else result = none zero num
            # Ex. 5 ^ 5 = 0, 5 ^ 0 = 5
            result ^= num
        return result
