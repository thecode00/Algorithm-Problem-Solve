# https://leetcode.com/problems/best-team-with-no-conflicts/

# TODO: solve
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        players = []
        for score, age in zip(scores, ages):
            players.append([score, age])

        players = sorted(players, key=lambda x: (-x[1], -x[0]))
        print(players)

        max_score = -float("inf")
        max_age = float("inf")
        team_score, cur_score = 0, 0
        select = set()

        for score, age in players:
            if score > max_score and age < max_age:
                team_score = max(team_score, cur_score)
                cur_score = 0
                continue
            cur_score += score
            max_score = max(max_score, score)
        team_score = max(team_score, cur_score)
        return team_score
