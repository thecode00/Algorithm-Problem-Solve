# https://leetcode.com/problems/diagonal-traverse/

from collections import defaultdict


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        num_dict = defaultdict(list)
        len_row, len_col = len(mat[0]), len(mat)
        for i in range(len_col):
            for j in range(len_row):
                num_dict[i + j].append(mat[i][j])
        answer = []
        for key in num_dict:
            if key % 2 == 0:
                answer += reversed(num_dict[key])
            else:
                answer += num_dict[key]
        return answer
