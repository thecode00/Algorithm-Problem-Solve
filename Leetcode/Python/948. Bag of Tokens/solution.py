# https://leetcode.com/problems/bag-of-tokens/description/?envType=daily-question&envId=2024-03-04
from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        # For maximum charging power, sort tokens.
        tokens.sort()
        max_score = cur_score = 0
        # Use two pointer
        left, right = 0, len(tokens) - 1
        while left <= right:
            if power >= tokens[left]:
                cur_score += 1
                power -= tokens[left]
                left += 1
            elif cur_score > 0:
                power += tokens[right]
                cur_score -= 1
                right -= 1
            else:
                # Cant continue play game
                break
            max_score = max(max_score, cur_score)

        return max_score
