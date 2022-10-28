# https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index = 0
        len_s = len(s)
        if len_s == 0:
            return True
        for string in t:
            if string == s[index]:
                index += 1
            if index >= len_s:
                return True
        return False