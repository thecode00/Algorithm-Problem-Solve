# https://leetcode.com/problems/first-unique-character-in-a-string/description/

from collections import defaultdict


class Solution:
    def firstUniqChar(self, s: str) -> int:
        used = defaultdict(int)
        for char in s:
            used[char] += 1
        
        for idx, char in enumerate(s):
            if used[char] <= 1:
                return idx 
        return -1