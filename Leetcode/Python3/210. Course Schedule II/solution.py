# https://leetcode.com/problems/course-schedule-ii/


from collections import deque
from typing import List


class Solution:  # Topological sort
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_degree = [0] * numCourses   # Initialize in-degree of nodes
        graph = [[] for _ in range(numCourses)]
        for n1, n2 in prerequisites:    # Make graph and set in-degree
            graph[n2].append(n1)
            in_degree[n1] += 1

        course = numCourses  # Number of nodes to explore
        result = []
        queue = deque()
        for idx, n in enumerate(in_degree):  # Search first 0 in-degree node
            if n == 0:
                queue.append(idx)
                course -= 1
                result.append(idx)

        while queue:
            cur = queue.popleft()
            for node in graph[cur]:
                in_degree[node] -= 1
                if in_degree[node] == 0:
                    result.append(node)
                    course -= 1
                    queue.append(node)
        # If queue is empty before exploring all nodes, then there is a cycle in graph
        return result if course == 0 else []


a = Solution()
a.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
