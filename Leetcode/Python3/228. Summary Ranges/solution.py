# https://leetcode.com/problems/summary-ranges/

from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        start = 0
        for idx in range(len(nums)):
            if idx == len(nums) - 1 or nums[idx + 1] != nums[idx] + 1:
                if start == idx:
                    result.append(f"{nums[start]}")
                else:
                    result.append(f"{nums[start]}->{nums[idx]}")
                start = idx + 1
        return result
