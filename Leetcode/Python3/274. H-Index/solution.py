# https://leetcode.com/problems/h-index/
# Time complexity: O(N log N)

from bisect import bisect_left
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h_index = 0
        citations.sort()

        for i in range(citations[-1] + 1):
            idx = bisect_left(citations, i)
            if len(citations) - idx >= i:
                h_index = i

        return h_index
