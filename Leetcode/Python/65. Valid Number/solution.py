# https://leetcode.com/problems/valid-number/

import re


class Solution:
    def isNumber(self, s: str) -> bool:
        p = re.compile("^([+-]?((\d+\.\d*)|(\.\d+)|(\d+))([eE][+-]?\d+)?)$")

        if p.match(s):
            return True
        else:
            return False
