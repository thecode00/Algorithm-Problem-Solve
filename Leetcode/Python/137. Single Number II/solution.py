# https://leetcode.com/problems/single-number-ii/description/

from collections import Counter
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = Counter(nums)
        return count.most_common(len(nums))[-1][0]
