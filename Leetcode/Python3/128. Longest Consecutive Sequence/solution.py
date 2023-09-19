# https://leetcode.com/problems/longest-consecutive-sequence/
# Ref: https://leetcode.com/problems/longest-consecutive-sequence/solutions/41057/simple-o-n-with-explanation-just-walk-each-streak/?envType=study-plan-v2&envId=top-interview-150


from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        num_set = set(nums)
        for num in nums:
            # Check num is start of consecutive sequence
            if num - 1 not in num_set:
                next = num + 1
                while next in num_set:
                    next += 1
                longest = max(longest, next - num)
        return longest
