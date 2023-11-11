# https://leetcode.com/problems/reverse-integer/description/

class Solution:
    def reverse(self, x: int) -> int:
        # signed 32-bit integer range
        min_num = -2 ** 31
        max_num = 2 ** 31 - 1

        minus_flag = x < 0

        if minus_flag:
            str_num = list(str(x)[1:])
        else:
            str_num = list(str(x))
        str_num.reverse()

        if minus_flag:
            str_num.insert(0, "-")
        # Check reversed number is in signed 32-bit integer range
        result = int("".join(str_num))
        return result if min_num <= result <= max_num else 0
