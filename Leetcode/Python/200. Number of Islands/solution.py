# https://leetcode.com/problems/number-of-islands/

from collections import deque

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


class Solution:  # Runtime: 456 ms
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        island = 0  # Number of island
        q = deque()
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == "1":
                    island += 1
                    # Bfs
                    q.append((y, x))
                    grid[y][x] = 0
                    while q:
                        pop_y, pop_x = q.popleft()
                        for i in range(4):
                            ny, nx = pop_y + dy[i], pop_x + dx[i]
                            if 0 <= ny and ny < m and 0 <= nx and nx < n and grid[ny][nx] == "1":
                                q.append((ny, nx))
                                grid[ny][nx] = 0
        return island
