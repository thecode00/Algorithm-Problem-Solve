# https://leetcode.com/problems/queue-reconstruction-by-height/


import heapq


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        result = []
        heap = []
        for height, idx in people:
            # For make max_heap convert to negative number
            heapq.heappush(heap, (-height, idx))

        while heap:
            p = heapq.heappop(heap)
            result.insert(p[1], [-p[0], p[1]])

        return result
