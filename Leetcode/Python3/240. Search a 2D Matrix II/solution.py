# https://leetcode.com/problems/search-a-2d-matrix-ii/


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for m in matrix:
            start, end = 0, len(matrix[0]) - 1
            while start <= end:
                mid = start + (end - start) // 2
                if m[mid] == target:
                    return True
                elif m[mid] > target:
                    end = mid - 1
                else:
                    start = mid + 1
        return False


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = 0, len(matrix[0]) - 1
        while col >= 0 and row < len(matrix):
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        return False
