# https://leetcode.com/problems/course-schedule/


from collections import defaultdict


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
        