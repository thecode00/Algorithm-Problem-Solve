# https://leetcode.com/problems/redundant-connection/description

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [n for n in range(len(edges) + 1)]
        tree_size = [0] * (len(edges) + 1)

        for a, b in edges:
            if self.find_parent(a, parent) == self.find_parent(b, parent):
                return [a, b]
            else:
                self.union(a, b, parent)
        # Handle except
        return [-1, -1]

    def union(self, a: int, b: int, parent: List[int]) -> None:
        parent_a, parent_b = self.find_parent(
            a, parent), self.find_parent(b, parent)

        if parent_a > parent_b:
            parent[parent_a] = parent_b
        else:
            parent[parent_b] = parent_a

    def find_parent(self, target: int, parent: List[int]) -> int:
        if parent[target] != target:
            parent[target] = self.find_parent(parent[target], parent)
        return parent[target]
