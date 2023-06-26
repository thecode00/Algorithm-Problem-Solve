# https://leetcode.com/problems/shortest-path-in-binary-matrix/


from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # Except no clear path
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1
        # 8-direction
        dx = [0, 0, 1, 1, 1, -1, -1, -1]
        dy = [1, -1, 0, -1, 1, 0, -1, 1]

        def bfs(start_x: int, start_y: int) -> None:
            grid[start_y][start_x] = 1
            queue = deque()
            queue.append((start_y, start_x))
            while queue:
                cur_y, cur_x = queue.popleft()
                for idx in range(8):
                    new_y, new_x = cur_y + dy[idx], cur_x + dx[idx]
                    if (0 <= new_y < len(grid) and 0 <= new_x < len(grid[0]) and grid[new_y][new_x] == 0):
                        grid[new_y][new_x] = grid[cur_y][cur_x] + 1
                        queue.append((new_y, new_x))

        bfs(0, 0)
        # If the bottom-right cannot be reached after BFS, return -1
        return grid[-1][-1] if grid[-1][-1] != 0 else -1
