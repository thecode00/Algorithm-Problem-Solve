# https://leetcode.com/problems/course-schedule/


from collections import defaultdict, deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for s, e in prerequisites:
            graph[s].append(e)

        visit, trace = set(), set()

        def dfs(node):
            if node in trace:   # dfs has cycle
                return False

            if node in visit:   # Already searched node
                return True

            trace.add(node)

            for n in graph[node]:
                if not dfs(n):
                    return False

            visit.add(node)
            trace.remove(node)

            return True

        for g in list(graph):
            if not dfs(g):
                return False

        return True


class Solution:  # Topological sort
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses    # Initialize in-degree of nodes
        for n1, n2 in prerequisites:
            graph[n2].append(n1)
            in_degree[n1] += 1

        course = numCourses # Number of nodes to explore
        queue = deque()
        for c in range(numCourses): # Search first 0 in-degree node
            if in_degree[c] == 0:
                queue.append(c)
                course -= 1
        while queue:
            cur = queue.popleft()
            for c in graph[cur]:
                in_degree[c] -= 1
                if in_degree[c] == 0:
                    queue.append(c)
                    course -= 1
        # If queue is empty before exploring all nodes, then there is a cycle in graph
        return course == 0
