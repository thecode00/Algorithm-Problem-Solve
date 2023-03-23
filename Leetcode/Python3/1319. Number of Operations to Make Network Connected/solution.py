# https://leetcode.com/problems/number-of-operations-to-make-network-connected/


from typing import List


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        def find(num: int) -> int:
            if num != parent[num]:
                parent[num] = find(parent[num])
            return parent[num]

        def union(a: int, b: int) -> None:
            a, b = find(a), find(b)
            if a > b:
                parent[a] = b
            elif a < b:
                parent[b] = a
            else:
                self.cycles += 1

        parent = [i for i in range(n)]  # Initialize parent to self
        self.cycles = 0

        for a, b in connections:
            union(a, b)

        for num in range(n):    # Update all element
            find(num)
        not_connected = len(set(parent)) - 1    # Number of not connected network
        """
        If a cycle appears, one connection can be moved Therefore
        if the number of disconnected networks is greater than the number of cycles, it returns -1
        """
        return not_connected if not_connected <= self.cycles else -1
