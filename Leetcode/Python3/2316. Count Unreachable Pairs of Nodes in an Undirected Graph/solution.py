# https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/


from collections import defaultdict


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        def find(num: int) -> int:
            if num != parent[num]:
                parent[num] = find(parent[num])
            return parent[num]

        def union(a: int, b: int) -> None:
            a, b = find(a), find(b)
            if a > b:
                parent[a] = b
            else:
                parent[b] = a

        parent = [i for i in range(n)]
        answer = 0
        for n1, n2 in edges:
            union(n1, n2)

        for num in range(n):    # TODO: Optimize
            find(num)

        connected = defaultdict(list)
        for idx, num in enumerate(parent):  # Group connected node
            connected[num].append(idx)

        for key in connected:
            # Connect unreachable node
            cur_network = connected[key]
            n -= len(cur_network)
            answer += len(cur_network) * n

        return answer
