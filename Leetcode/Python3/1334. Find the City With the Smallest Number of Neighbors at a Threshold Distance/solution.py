# https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/description/

"""
Floyd-Warshall algorithm
Time complexity: O(N ^ 3)
"""
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        distance = [[float("inf")] * n for _ in range(n)]
        for n1, n2, wei in edges:
            distance[n1][n2] = wei
            distance[n2][n1] = wei

        for i in range(n):
            distance[i][i] = 0
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
        
        min_reach_city = n
        index = 0
        for i in range(n):
            reached = 0
            for j in range(n):
                if distance[i][j] <= distanceThreshold:
                    reached += 1
            if min_reach_city >= reached:
                min_reach_city = reached
                index = i
        
        return index
        