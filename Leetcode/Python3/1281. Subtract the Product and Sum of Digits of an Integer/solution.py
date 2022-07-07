# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

from functools import reduce
import operator


class Solution:
    # def subtractProductAndSum(self, n: int) -> int:
    #     number = list(map(int, str(n)))
    #     answer = 1
    #     for num in number:
    #         answer *= num
    #     return answer - sum(answer)
    def subtractProductAndSum(self, n: int) -> int:
        A = list(map(int, str(n)))
        return reduce(operator.mul, A) - sum(A)
