# https://leetcode.com/problems/range-sum-query-2d-immutable/description/


from typing import List

# TODO: optimize code


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix_sum = [[] for _ in range(len(matrix))]
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                if x == 0:
                    self.prefix_sum[y].append(matrix[y][x])
                elif y == 0:
                    self.prefix_sum[y].append(self.prefix_sum[y][x - 1] + matrix[y][x])
                else:
                    self.prefix_sum[y].append(matrix[y][x] + matrix[y - 1][x] + matrix[y]
                                              [x - 1] + self.prefix_sum[y-1][x-1])

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = self.prefix_sum[row2][col2]
        if row1 != 0:
            total -= self.prefix_sum[row1 - 1][col2]
        if col1 != 0:
            total -= self.prefix_sum[row2][col1 - 1]
        return total


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
