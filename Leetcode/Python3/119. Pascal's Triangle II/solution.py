# https://leetcode.com/problems/pascals-triangle-ii/


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pascal = [[1] * (i + 1) for i in range(rowIndex + 1)]
        for row_idx in range(1, rowIndex + 1):
            for idx in range(1, row_idx):
                pascal[row_idx][idx] = pascal[row_idx - 1][idx - 1] + pascal[row_idx - 1][idx]
        return pascal[-1]
