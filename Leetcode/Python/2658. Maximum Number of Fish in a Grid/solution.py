# https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/description

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        dy = [0, 0, 1, -1]
        dx = [1, -1, 0, 0]
        max_fish = 0

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] != 0:
                    total_fish = 0
                    stack = [(x, y)]

                    while stack:
                        cur_x, cur_y = stack.pop()

                        total_fish += grid[cur_y][cur_x]
                        grid[cur_y][cur_x] = 0

                        for idx in range(4):
                            next_x, next_y = cur_x + dx[idx], cur_y + dy[idx]

                            if 0 <= next_x < len(grid[0]) and 0 <= next_y < len(grid) and grid[next_y][next_x] != 0:
                                stack.append((next_x, next_y))

                    max_fish = max(max_fish, total_fish)

        return max_fish
