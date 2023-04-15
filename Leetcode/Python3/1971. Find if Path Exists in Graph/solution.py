# https://leetcode.com/problems/find-if-path-exists-in-graph/


class Solution:  # Union find
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        parent = [i for i in range(n)]

        def find(num: int):
            if parent[num] != num:
                parent[num] = find(parent[num])
            return parent[num]

        def union(num1: int, num2: int):
            num1, num2 = find(num1), find(num2)  # Find parent node
            if num1 > num2:
                parent[num1] = num2
            else:
                parent[num2] = num1

        for n1, n2 in edges:
            union(n1, n2)   # Union node
        print(parent)
        # If parent of source, destination is different there is no path
        return find(parent[source]) == find(parent[destination])
