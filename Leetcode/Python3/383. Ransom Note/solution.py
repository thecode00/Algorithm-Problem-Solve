# https://leetcode.com/problems/ransom-note/\

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = Counter(ransomNote) - Counter(magazine)
        if bool(count):  # When magazine cant construct ransomNote
            return False
        else:
            return True
