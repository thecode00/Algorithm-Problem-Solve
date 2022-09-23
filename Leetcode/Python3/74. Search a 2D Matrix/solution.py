# https://leetcode.com/problems/search-a-2d-matrix/?envType=study-plan&id=algorithm-ii


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        length = len(matrix[0])
        for row in matrix:
            if row[0] > target:
                break
            start, end = 0, length - 1
            while start <= end:
                mid = (start + end) >> 1
                if row[mid] == target:
                    return True
                if row[mid] > target:
                    end = mid - 1
                else:
                    start = mid + 1
        return False

    # Stretch 2d matrix
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        len_row = len(matrix[0])
        start, end = 0, len_row * len(matrix) - 1
        while start <= end:
            mid = (start + end) >> 1
            """
            If matrix == [[1, 2], [3, 4]] we can think like this [1, 2, 3, 4]
            When mid == 2 we find 3 in 2d matrix cause [1, 2, 3, 4][2] == 3
            We find row mid // len_row -> 2 // 2 == 1, and find column mid % len_row -> 2 % 2 == 0
            Then find mid element: matrix[1][0] == 3
            """
            num = matrix[mid // len_row][mid % len_row]
            if num == target:
                return True

            if num > target:
                end = mid - 1
            else:
                start = mid + 1
        return False
