# https://leetcode.com/problems/guess-number-higher-or-lower/

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        start, end = 1, n + 1
        answer = 0
        while start <= end:
            mid = start + (end - start) // 2
            guess_result = guess(mid)
            if guess_result == 0:
                return mid
            elif guess_result == -1:
                end = mid - 1
            else:
                start = mid + 1
