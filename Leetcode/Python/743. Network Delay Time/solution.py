# https://leetcode.com/problems/network-delay-time/


from collections import defaultdict
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        dist = [float("inf") for _ in range(n + 1)]
        dist[k] = 0  # Set start point distance 0

        for s, e, w in times:
            graph[s].append((e, w))

        heap = [(0, k)]  # Insert start point in the heap
        while heap:
            distance, node = heapq.heappop(heap)
            for v, w in graph[node]:
                if distance + w < dist[v]:
                    dist[v] = distance + w
                    heapq.heappush(heap, (dist[v], v))

        max_dist = max(dist[1:])
        # If dist has INF there is not reach node
        return max_dist if max_dist != float("inf") else -1


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        dist = defaultdict(int)

        for s, e, w in times:
            graph[s].append((e, w))

        heap = [(0, k)]
        while heap:
            distance, node = heapq.heappop(heap)
            if node not in dist:    # First search node
                dist[node] = distance
                for v, w in graph[node]:
                    alt = distance + w
                    heapq.heappush(heap, (alt, v))
        # dist has node number as a key and contain distance from k to node number in value
        # So len(dist) != n there is cant reach node
        if len(dist) != n:
            return -1
        else:
            return max(dist.values())
