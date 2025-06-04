from typing import List


class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        connections.sort(key=lambda x: x[2])
        parents = [i for i in range(n + 1)]
        total_cost = 0
        connected = 0

        for a, b, cost in connections:
            if self.find_parent(a, parents) != self.find_parent(b, parents):
                total_cost += cost
                connected += 1

                self.union(a, b, parents)

        return total_cost if connected == n - 1 else -1

    def union(self, a: int, b: int, parent: List[int]):
        parent_a = self.find_parent(a, parent)
        parent_b = self.find_parent(b, parent)

        if parent_a > parent_b:
            parent[parent_a] = parent_b
        else:
            parent[parent_b] = parent_a

    def find_parent(self, num: int, parent: List[int]):
        if parent[num] != num:
            parent[num] = self.find_parent(parent[num], parent)

        return parent[num]
