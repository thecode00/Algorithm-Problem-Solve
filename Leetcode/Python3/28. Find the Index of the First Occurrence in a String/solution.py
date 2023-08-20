# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for left in range(len(haystack) - len(needle) + 1):
            for idx in range(len(needle)):
                if haystack[left + idx] != needle[idx]:
                    break
            else:
                return left
        return -1


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
