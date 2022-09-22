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
