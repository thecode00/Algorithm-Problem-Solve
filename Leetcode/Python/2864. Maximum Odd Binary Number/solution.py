# https://leetcode.com/problems/maximum-odd-binary-number/description/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count_1 = 0
        # Convert to integer and count of 1-bits
        int_num = int(s, 2)
        # print(int_num)
        while int_num > 0:
            count_1 += int_num & 1
            int_num >>= 1
        # s has least one 1-bit so remove it before make binary number
        count_1 -= 1
        length = len(s) - 1

        return f"{'1' * count_1}{'0' * (length - count_1)}1"
