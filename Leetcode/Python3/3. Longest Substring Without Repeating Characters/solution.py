# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Ref: https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/1731/A-Python-solution-85ms-O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = maxLength = 0
        usedChar = {}
        for idx in range(len(s)):
            if s[idx] in usedChar:
                start = idx
            else:
                maxLength = max(maxLength, idx - start + 1)
        print(maxLength)