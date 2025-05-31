# https://leetcode.com/problems/rotting-oranges/description/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rottens = deque()
        dy = [0, 0, 1, -1]
        dx = [1, -1, 0, 0]

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    rottens.append((row, col))

        time = -1
        while rottens:
            time += 1
            size = len(rottens)

            for _ in range(size):
                cur_row, cur_col = rottens.popleft()

                for idx in range(4):
                    new_row, new_col = cur_row + dy[idx], cur_col + dx[idx]

                    if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == 1:
                        rottens.append((new_row, new_col))
                        grid[new_row][new_col] = 2

        return max(time, 0) if all([all(o != 1 for o in n) for n in grid]) else -1
