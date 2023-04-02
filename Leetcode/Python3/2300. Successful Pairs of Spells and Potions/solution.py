# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/description/


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        pairs = {}
        temp = sorted(spells)  # [1, 3, 5]
        potions = sorted(potions, reverse=True)  # [5, 4, 3, 2, 1]
        length = len(potions)
        cur = 0
        for s in temp:  # Find pair
            while cur < length:
                if potions[cur] * s < success:
                    break
                cur += 1
            pairs[s] = cur
        answer = []
        for s in spells:
            answer.append(pairs[s])
        return answer
