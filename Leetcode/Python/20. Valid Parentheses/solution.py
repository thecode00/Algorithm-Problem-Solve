# https://leetcode.com/problems/valid-parentheses/


class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis = {")": "(", "}": "{", "]": "["}
        stack = []
        for p in s:
            if p not in parenthesis:  # (, {, [
                stack.append(p)
            elif not stack or stack.pop() != parenthesis[p]:
                return False
        return len(stack) == 0  # If stack not empty there is single open parenthesis
