# https://leetcode.com/problems/valid-perfect-square/

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return True if num ** .5 == int(num ** .5) else False
