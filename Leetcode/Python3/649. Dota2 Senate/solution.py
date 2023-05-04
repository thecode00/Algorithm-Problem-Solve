# https://leetcode.com/problems/dota2-senate/description/


from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r = d = 0
        queue = deque()
        for team in senate:  # Append to queue and count each team
            queue.append(team)
            if team == "R":
                r += 1
            else:
                d += 1

        ban_r = ban_d = 0
        while r != 0 and d != 0:
            cur = queue.popleft()
            if cur == "R":
                if ban_r == 0:  # If no ban Radiant, Radiant play next round and ban Dire
                    queue.append(cur)
                    ban_d += 1
                else:   # Dire ban Radiant so cant exercise
                    ban_r -= 1
                    r -= 1
            elif cur == "D":
                if ban_d == 0:  # If no ban Dire, Dire play next round and ban Radiant
                    queue.append(cur)
                    ban_r += 1
                else:  # Radiant ban Dire so cant exercise
                    ban_d -= 1
                    d -= 1
        return "Radiant" if d == 0 else "Dire"
