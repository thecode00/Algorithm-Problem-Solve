"""
https://leetcode.com/problems/k-th-symbol-in-grammar/
Ref: https://leetcode.com/problems/k-th-symbol-in-grammar/discuss/113710/Python-simple-solution-to-understand-with-explanations
Time Complexity: O(log N)
"""


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        half = 2 ** (n - 2)  # Total number = 2 ^ (n - 1) so half == 2 ^ (n - 2)
        if k <= half:
            return self.kthGrammar(n - 1, k)
        else:
            """
             0 1 1 0, n = 3, k = 3, half = 2
             ^   ^
            num  k
             find num and flip value
            """
            num = self.kthGrammar(n - 1, k - half)
            if num:
                return 0
            else:
                return 1
