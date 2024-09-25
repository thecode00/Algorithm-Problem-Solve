# https://leetcode.com/problems/base-7/description/

class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return 0

        BASE = 7
        is_negative = False
        if (num < 0):
            is_negative = True
            num *= -1

        result = []

        while num > 0:
            q, r = divmod(num, BASE)
            result.append(str(r))
            num = q

        if is_negative:
            result.append("-")
        result.reverse()

        return "".join(result)
