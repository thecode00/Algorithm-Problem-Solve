# https://leetcode.com/problems/number-of-enclaves/
from collections import deque
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def bfs(x, y):
            close, move = True, 1
            q = deque()
            q.append((x, y))
            grid[x][y] = 0
            while q:
                x, y = q.popleft()
                # If the land is connected to the wall of the grid, it is not close.
                if x == 0 or x == m - 1 or y == 0 or y == n - 1:    
                            close = False
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        q.append((nx, ny))
                        grid[nx][ny] = 0
                        move += 1
            return move if close else 0
        m, n = len(grid), len(grid[0])
        moves = 0
        for idx_x in range(m):
            for idx_y in range(n):
                if grid[idx_x][idx_y] == 1:
                    moves += bfs(idx_x, idx_y)
        return moves