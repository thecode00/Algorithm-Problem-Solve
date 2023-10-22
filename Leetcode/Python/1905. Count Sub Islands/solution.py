# https://leetcode.com/problems/count-sub-islands/

from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def bfs(x, y):
            sub = True
            q = deque()
            q.append((x, y))
            grid2[x][y] = 0
            while q:
                x, y = q.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < m and 0 <= ny < n and grid2[nx][ny] == 1:
                        if grid1[nx][ny] == 0:
                            sub = False
                        q.append((nx, ny))
                        grid2[nx][ny] = 0
            return sub
        m, n = len(grid1), len(grid1[0])
        answer = 0
        for idx_x in range(m):
            for idx_y in range(n):
                if grid1[idx_x][idx_y] and grid2[idx_x][idx_y]:
                    answer += bfs(idx_x, idx_y) # If sub True answer += 1, False answer += 0
        return answer
        
