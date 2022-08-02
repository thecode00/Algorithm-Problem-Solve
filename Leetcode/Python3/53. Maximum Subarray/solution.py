# https://leetcode.com/problems/maximum-subarray/

from itertools import combinations

# TODO: Solve
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        length = len(nums)
        answer = 0
        for i in range(length):
            for idx in range(length - i):
                answer = max(answer, sum(nums[idx: idx + i + 1]))
                print(answer)