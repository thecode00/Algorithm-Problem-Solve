# https://leetcode.com/problems/ransom-note/\

from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = Counter(ransomNote) - Counter(magazine)
        if bool(count):  # When magazine cant construct ransomNote
            return False
        else:
            return True


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count_ransom, count_magazine = Counter(ransomNote), Counter(magazine)
        return len(count_ransom - count_magazine) == 0
