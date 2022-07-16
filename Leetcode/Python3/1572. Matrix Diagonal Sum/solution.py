# https://leetcode.com/problems/matrix-diagonal-sum/

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        length = len(mat)
        end = length - 1
        answer = 0
        for idx in range(length):
            if idx != end:
                answer += mat[idx][idx] + mat[idx][end]
            else:
                answer += mat[idx][idx]
            end -= 1
        print(answer)
    # https://leetcode.com/problems/matrix-diagonal-sum/discuss/837795/Python-O(n)-by-iteration-w-Comment

    def diagonalSum(self, mat: List[List[int]]) -> int:
        length = len(mat)
        mid = length // 2
        answer = 0
        for idx in range(length):
            # Primary diagonal, secondary diagonal
            answer += mat[idx][idx] + mat[idx][length - idx - 1]
        if length % 2 == 1:
            answer -= mat[mid][mid]
        return answer
