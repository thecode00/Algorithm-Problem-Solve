# https://leetcode.com/problems/reverse-string/

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        length = len(s)
        for idx in range(length // 2):
            s[idx], s[length - idx - 1] = s[length - idx - 1], s[idx]


class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()


class Solution:
    def reverseString(self, s: List[str]) -> None:
        s[:] = s[::-1]
