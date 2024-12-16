# https://leetcode.com/problems/find-champion-ii/description

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        in_degree = [0] * n

        for strong, weak in edges:
            in_degree[weak] += 1

        champ_count = 0
        champ_team = -1

        for team in range(n):
            if in_degree[team] == 0:
                champ_team = team
                champ_count += 1

        return champ_team if champ_count == 1 else -1
