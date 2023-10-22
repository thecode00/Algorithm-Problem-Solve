# https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza/

# TODO: solve
class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        rows, cols = len(pizza), len(pizza[0])
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]
        for y in range()
