# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/description

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0

        for num in nums:
            if self.getNumberOfDigit(num) % 2 == 0:
                count += 1
        
        return count

    def getNumberOfDigit(self, num: int) -> int:
        digit_count = 1

        while 10 <= num:
            digit_count += 1
            num //= 10
        
        return digit_count