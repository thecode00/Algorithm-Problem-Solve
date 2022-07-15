# https://leetcode.com/problems/happy-number/

class Solution:
    def isHappy(self, n: int) -> bool:
        loop_check = []
        while n not in loop_check:
            loop_check.append(n)
            n = sum([int(s) ** 2 for s in list(str(n))])
            if n == 1:
                return True
        return False
