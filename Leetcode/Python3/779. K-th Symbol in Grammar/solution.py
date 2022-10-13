# https://leetcode.com/problems/k-th-symbol-in-grammar/

pattern = [0, 1, 1]


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        return pattern[(k - 1) % 3]
