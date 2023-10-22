# https://leetcode.com/problems/assign-cookies/


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        result = 0
        size_index = 0
        # Explore small greed children by giving them small cookies.
        for greed in g:
            if size_index == len(s):
                break
            for idx in range(size_index, len(s)):
                if greed <= s[idx]:
                    result += 1
                    size_index = idx + 1
                    break
        return result
