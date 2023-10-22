# https://leetcode.com/problems/removing-stars-from-a-string/description/


class Solution:
    def removeStars(self, s: str) -> str:
        result = []
        for char in s:
            if char == "*" and result:
                result.pop()
                continue
            result.append(char)
        return "".join(result)
