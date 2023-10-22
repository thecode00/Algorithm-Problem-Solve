# https://leetcode.com/problems/length-of-last-word/


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        if not words:   # Filter blank word
            return 0
        return len(words[-1])