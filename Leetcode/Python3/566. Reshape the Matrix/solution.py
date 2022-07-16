# https://leetcode.com/problems/reshape-the-matrix/

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        # If the number of elements is not the same it cant be reshape
        if m * n != r * c:
            return mat
        temp = []
        answer = []
        for l in mat:   # Convert 2D Array to 1D Array
            temp += l
        for idx in range(0, len(temp), c):  # Slice a 1D array by c to make a 2D array
            answer.append(temp[idx: idx + c])
        return answer
