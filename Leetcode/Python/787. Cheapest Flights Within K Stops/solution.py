# https://leetcode.com/problems/cheapest-flights-within-k-stops/
# Ref: https://leetcode.com/problems/cheapest-flights-within-k-stops/solutions/115541/java-c-python-priority-queue-solution-tle-now/


from collections import defaultdict
import heapq


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        dist = [-float("inf") for _ in range(n + 1)]

        for f, t, p in flights:     # from, to, price
            graph[f].append((t, p))

        heap = [(0, k, src)]    # (price, distance, node)
        while heap:
            price, distance, node = heapq.heappop(heap)
            if node == dst:
                return price
            if distance < 0:
                continue
            # The larger distance, coming out of heapq first, so if it is lower than dist[node], skip it.
            if distance <= dist[node]:
                continue
            dist[node] = distance
            for v, w in graph[node]:
                heapq.heappush(heap, (price + w, distance - 1, v))

        return -1
