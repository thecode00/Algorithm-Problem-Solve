# https://leetcode.com/problems/string-to-integer-atoi/description/

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()   # Delete whitespace
        num = []
        isSign = False
        sign = 1

        for char in s:
            if char.isdigit():
                num.append(char)

            elif not num and char in ["+", "-"] and not isSign:
                if char == "-":
                    sign = -1
                isSign = True

            else:
                break

        if num: # Rounding
            return max(min(int("".join(num)) * sign, 2 ** 31 - 1), -2 ** 31)

        return 0
