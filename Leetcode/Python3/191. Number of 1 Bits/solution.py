# https://leetcode.com/problems/number-of-1-bits/

class Solution:
    # def hammingWeight(self, n: int) -> int:
    #     if n < 2:
    #         return n
    #     answer = 0
    #     while n > 1:    # Binary number calculation
    #         q, r = divmod(n, 2)
    #         n = q
    #         if r != 0:
    #             answer += 1
    #         if n == 1:
    #             answer += 1
    #     return answer
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')
