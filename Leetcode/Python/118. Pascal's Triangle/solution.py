# https://leetcode.com/problems/pascals-triangle/


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = [[1] * (i + 1) for i in range(numRows)]
        for idx in range(numRows):
            for i in range(1, idx):  # first, last element is 1
                pascal[idx][i] = pascal[idx - 1][i - 1] + pascal[idx - 1][i]
        return pascal
