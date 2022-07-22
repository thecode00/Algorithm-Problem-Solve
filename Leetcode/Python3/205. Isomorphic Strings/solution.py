# https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # If s = "abc", t = "cde" len(set(s)) == len(set(t)) == True so we need check len(set(zip(s, t)))
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))
