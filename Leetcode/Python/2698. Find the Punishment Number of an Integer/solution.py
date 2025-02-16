# https://leetcode.com/problems/find-the-punishment-number-of-an-integer/description

class Solution:
    def punishmentNumber(self, n: int) -> int:
        answer = 0

        for num in range(1, n + 1):
            sqr_num = num ** 2
            if self.isPunishment(sqr_num, num):
                answer += sqr_num

        return answer

    def isPunishment(self, num: int, target: int) -> bool:
        if num < target or target < 0:
            return False

        if num == target:
            return True

        # Search recursivly split number and check 1, 2, 3 digits, 1 <= n <= 1000 so dont need check 4 digits
        # Optimized string convert
        return self.isPunishment(num // 10, target - num % 10) or self.isPunishment(num // 100, target - num % 100) or self.isPunishment(num // 1000, target - num % 1000)


class Solution:
    def punishmentNumber(self, n: int) -> int:
        answer = 0

        for num in range(1, n + 1):
            sqr_num = num ** 2
            if self.isPunishment(str(sqr_num), num):
                answer += sqr_num

        return answer

    def isPunishment(self, num: str, target: int) -> bool:
        if not num and target == 0:
            return True

        # Search recursivly split number and check target
        for idx in range(len(num)):
            left = num[:idx + 1]
            right = num[idx + 1:]

            if self.isPunishment(right, target - int(left)):
                return True

        return False
