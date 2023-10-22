# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

from typing import List


class Solution:  # Greedy
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        burst = 1
        end = points[0][1]
        for s, e in points:
            if s > end:
                burst += 1
                end = e
        return burst
