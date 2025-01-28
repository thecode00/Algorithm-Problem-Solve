# https://leetcode.com/problems/course-schedule-iv/description

class Solution:  # Topological sort
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        in_degree = [0] * numCourses
        graph = [[] for _ in range(numCourses)]
        # is_reachable[a][b] = b can reach a
        is_reachable = [[False] * numCourses for _ in range(numCourses)]

        for pre, to in prerequisites:
            in_degree[to] += 1
            graph[pre].append(to)

        queue = deque()
        for idx in range(numCourses):
            if in_degree[idx] == 0:
                queue.append(idx)
                is_reachable[idx][idx] = True

        while queue:
            cur = queue.popleft()

            for course in graph[cur]:
                in_degree[course] -= 1
                for idx in range(numCourses):
                    is_reachable[course][idx] |= is_reachable[cur][idx]
                is_reachable[course][course] = True

                if in_degree[course] == 0:
                    queue.append(course)

        result = []
        for query in queries:
            result.append(is_reachable[query[1]][query[0]])

        return result
