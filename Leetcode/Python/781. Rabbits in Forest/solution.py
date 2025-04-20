# https://leetcode.com/problems/rabbits-in-forest/description

from collections import defaultdict
from math import ceil


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counter = defaultdict(int)

        for num in answers:
            # Since the answer 'n' means there are n other rabbits of the same color, we add 1 for this rabbit itself.
            counter[num + 1] += 1
        
        rabbits = 0

        for color, count in counter.items():
            rabbits += color * ceil(count / (color))
        
        return rabbits