# https://leetcode.com/problems/string-to-integer-atoi/description/

class Solution:
    def myAtoi(self, s: str) -> int:
        # Delete space
        s = s.strip()

        if len(s) == 0:
            return 0

        idx = 0
        isNegative = False
        if s[0] in ["-", "+"]:
            if s[0] == "-":
                isNegative = True
            idx += 1

        # Read number from left
        number = 0
        while idx < len(s):
            if idx == len(s) or not s[idx].isdigit():
                break

            number *= 10
            number += int(s[idx])
            idx += 1

        if isNegative:
            number *= -1

        # Round number
        number = max(min(number, 2 ** 31 - 1), -2 ** 31)
        return number


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

        if num:  # Rounding
            return max(min(int("".join(num)) * sign, 2 ** 31 - 1), -2 ** 31)

        return 0
