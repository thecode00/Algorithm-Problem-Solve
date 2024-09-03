# https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        digits[-1] += 1
        for idx in range(len(digits) - 1, 0, -1):
            if digits[idx] < 10:
                break

            digits[idx] = 0
            digits[idx - 1] += 1

        # Add digit
        if digits[0] == 10:
            digits[0] = 1
            digits.append(0)

        return digits


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = int("".join(map(str, digits)))
        return list(map(int, str(number + 1)))
