# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/


from bisect import bisect_right
from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for li in grid:
            li.sort()
            idx = bisect_right(li, -1)
            count += idx
        return count
