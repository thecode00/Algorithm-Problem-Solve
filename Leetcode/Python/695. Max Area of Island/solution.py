# https://leetcode.com/problems/max-area-of-island/

from collections import deque
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def bfs(x, y):
            area = 1
            q = deque()
            q.append((x, y))
            grid[x][y] = 0
            while q:
                x, y = q.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        q.append((nx, ny))
                        grid[nx][ny] = 0
                        area += 1
            return area
        m, n = len(grid), len(grid[0])
        island = 0
        for idx_x in range(m):
            for idx_y in range(n):
                if grid[idx_x][idx_y] == 1:
                    island = max(bfs(idx_x, idx_y), island) # Compare current max area with bfs area
        return island

