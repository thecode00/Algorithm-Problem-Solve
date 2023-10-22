# https://leetcode.com/problems/sign-of-the-product-of-an-array/

from ast import operator
from functools import reduce


class Solution:
    # My solution Runtime: 102 ms
    def arraySign(self, nums: List[int]) -> int:
        num = reduce(operator.mul, nums)
        if num > 0:
            return 1
        elif num < 0:
            return -1
        else:
            return 0
    # https://leetcode.com/problems/sign-of-the-product-of-an-array/discuss/1152412/Python3-line-sweep
    # Runime: 64 ms

    def arraySign(self, nums: List[int]) -> int:
        ans = 1
        for x in nums:
            if x == 0:
                return 0
            if x < 0:
                ans *= -1
        return ans
