# https://leetcode.com/problems/add-digits/


class Solution:
    def addDigits(self, num: int) -> int:
        while num > 10:
            temp = 0
            while num > 10:
                temp += num % 10
                num //= 10
            num += temp
        return num


class Solution:  # O(1)
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        result = num % 9
        return 9 if result == 0 else result
