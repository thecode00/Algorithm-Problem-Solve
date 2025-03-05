# https://leetcode.com/problems/count-total-number-of-colored-cells/description

class Solution:
    def coloredCells(self, n: int) -> int:
        blank_corner = (n - 1) * n // 2
        return (n * 2 - 1) ** 2 - 4 * (blank_corner)
