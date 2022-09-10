# https://leetcode.com/problems/spiral-matrix/

# Ref: https://leetcode.com/problems/spiral-matrix/discuss/394774/python-3-solution-for-spiral-matrix-one-of-the-most-easiest-you-will-never-forget


class Solution:
    def spiralOrder(self, matrix):
        begin_x, begin_y = 0, 0
        end_x, end_y = len(matrix[0]), len(matrix)
        answer = []
        while begin_x < end_x and begin_y < end_y:
            for idx in range(begin_x, end_x):
                answer.append(matrix[begin_y][idx])
            begin_y += 1
            # print(begin_x, begin_y, end_x, end_y)
            for idx in range(begin_y, end_y):
                answer.append(matrix[idx][end_x - 1])
            end_x -= 1
            # print(begin_x, begin_y, end_x, end_y)
            if begin_y < end_y:
                for idx in range(end_x - 1, begin_x - 1, -1):
                    answer.append(matrix[end_y - 1][idx])
                end_y -= 1
            # print(begin_x, begin_y, end_x, end_y)
            if begin_x < end_x:
                for idx in range(end_y - 1, begin_y - 1, -1):
                    answer.append(matrix[idx][begin_x])
                begin_x += 1
            # print(begin_x, begin_y, end_x, end_y)
            # print(answer)
        return answer
