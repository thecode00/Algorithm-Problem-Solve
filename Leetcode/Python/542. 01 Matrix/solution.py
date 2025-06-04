# https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        queue = deque()

        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col] == 0:
                    queue.append((row, col, 0))
                else:
                    mat[row][col] = -1

        while queue:
            cur_row, cur_col, cur_dist = queue.popleft()
            for idx in range(4):
                new_row, new_col = cur_row + dy[idx], cur_col + dx[idx]
                new_dist = cur_dist + 1
                if 0 <= new_row < len(mat) and 0 <= new_col < len(mat[0]) and mat[new_row][new_col] == -1:
                    mat[new_row][new_col] = new_dist
                    queue.append((new_row, new_col, new_dist))

        return mat
