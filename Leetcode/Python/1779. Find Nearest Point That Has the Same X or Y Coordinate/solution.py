# https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/
INF = float('inf')


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        index, manhattan = -1, INF
        for idx, (nx, ny) in enumerate(points):
            if (nx == x or ny == y) and abs(x - nx) + abs(y - ny) < manhattan:
                manhattan = abs(x - nx) + abs(y - ny)
                index = idx
        return index
