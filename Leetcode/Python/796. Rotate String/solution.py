# https://leetcode.com/problems/rotate-string/description

import re


class Solution:  # First solution
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        p = re.compile(goal)

        s = s * 2
        return True if p.search(s) else False


class Solution:  # Second solution, remove unnecessary regexp
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        # If goal is rotated string s, goal in double s
        return goal in (s * 2)
