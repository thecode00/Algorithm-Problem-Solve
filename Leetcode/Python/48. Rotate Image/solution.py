# https://leetcode.com/problems/rotate-image/description/

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rotate_count = len(matrix) // 2

        for layer in range(rotate_count):
            first = layer 
            last = len(matrix) - layer - 1

            for idx in range(first, last):
                offset = idx - first
                top = matrix[first][idx]

                matrix[first][idx] = matrix[last - offset][first]

                matrix[last - offset][first] = matrix[last][last - offset]

                matrix[last][last - offset] = matrix[idx][last]

                matrix[idx][last] = top

    
