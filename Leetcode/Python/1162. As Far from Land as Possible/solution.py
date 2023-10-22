# https://leetcode.com/problems/as-far-from-land-as-possible/


from collections import deque


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        len_y, len_x = len(grid), len(grid[0])
        dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]
        max_distance = -1
        queue = deque()

        for y in range(len_y):
            for x in range(len_x):
                if grid[y][x] == 1:
                    # Make infinite negative to not be explored
                    grid[y][x] = -float("inf")
                    queue.append([y, x, 0])

        while queue:
            cur_y, cur_x, dist = queue.popleft()
            for idx in range(4):
                ny, nx = cur_y + dy[idx], cur_x + dx[idx]
                # If the element is 0, the part you didn't explore
                if 0 <= ny < len_y and 0 <= nx < len_x and grid[ny][nx] == 0:
                    queue.append([ny, nx, dist + 1])
                    grid[ny][nx] = dist + 1
                    max_distance = max(max_distance, dist + 1)
        return max_distance
