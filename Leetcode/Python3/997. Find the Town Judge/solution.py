# https://leetcode.com/problems/find-the-town-judge/


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = [[] for _ in range(n + 1)]
        trust_people = [False for _ in range(n + 1)]

        for a, b in trust:
            graph[b].append(a)  # a trust b
            trust_people[a] = True
        for idx in range(1, n + 1):
            if len(graph[idx]) == n - 1 and not trust_people[idx]:  # Everybody trust judge
                return idx
        return -1   # There is no town judge
