# https://leetcode.com/problems/ipo/description/
# Ref: https://leetcode.com/problems/ipo/solutions/98216/python-priority-queue-with-explanation/?orderBy=most_votes


import heapq
from typing import List


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = sorted(zip(profits, capital), key=lambda x: x[1])    # x[0]: profit, x[1]: require capital
        heap = []
        idx = 0
        for _ in range(k):
            while idx < len(profits) and projects[idx][1] <= w: # Projects are sorted by require capital, so we dont need search past project
                heapq.heappush(heap, -projects[idx][0])
                idx += 1
            # for idx in range(len(projects)):
            #     if projects[idx][1] <= w:
            #         heapq.heappush(heap, projects[idx])
            if heap:
                w += -heapq.heappop(heap)
        return w
        
        