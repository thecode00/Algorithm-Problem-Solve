# https://leetcode.com/problems/minimum-height-trees/


from collections import defaultdict


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 1:  # Check except
            return [0]

        graph = defaultdict(list)
        for a, b in edges:  # a to b edge
            graph[a].append(b)
            graph[b].append(a)

        leaves = []
        for idx in range(n):
            if len(graph[idx]) == 1:
                leaves.append(idx)
        while n > 2:    # Maximum answer is 2
            n -= len(leaves)
            print(leaves)
            temp = []   # Save next leaf nodes list
            for leaf in leaves:
                parent = graph[leaf].pop()  # graph[leaf] has only parent node
                graph[parent].remove(leaf)
                # If parent node become leaf node append to temp list
                if len(graph[parent]) == 1:
                    temp.append(parent)

            leaves = temp

        return leaves
