# https://leetcode.com/problems/jewels-and-stones/

from collections import defaultdict

# Defaultdict
class Solution: 
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freq = defaultdict(int)
        count = 0

        for stone in stones:
            freq[stone] += 1
        
        for jewel in jewels:
            count += freq[jewel]
        return count

# Set
class Solution: 
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_set = set(jewels)
        count = 0
        for stone in stones:
            if stone in jewel_set:
                count += 1
        return count 

# Comprehension
class Solution: 
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(s in jewels for s in stones)