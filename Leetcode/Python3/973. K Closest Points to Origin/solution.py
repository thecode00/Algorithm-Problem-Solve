# https://leetcode.com/problems/k-closest-points-to-origin/


import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = sorted(points, key=lambda x: x[0]**2 + x[1]**2)
        return points[:k]


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            heapq.heappush(heap, (x**2 + y**2, x, y))

        result = []
        for _ in range(k):
            _, x, y = heapq.heappop(heap)
            result.append([x, y])
        return result
