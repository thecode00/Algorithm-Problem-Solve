# https://leetcode.com/problems/count-servers-that-communicate/description

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        server_col, server_row = [0] * len(grid[0]), [0] * len(grid)

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x]:
                    server_row[y] += 1
                    server_col[x] += 1

        connected = 0

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] and (server_row[y] > 1 or server_col[x] > 1):
                    connected += 1

        return connected
