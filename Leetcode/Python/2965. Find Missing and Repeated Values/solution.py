# https://leetcode.com/problems/find-missing-and-repeated-values/description

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        exist = [False] * ((len(grid) ** 2) + 1)
        result = [0, 0]

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if exist[grid[y][x]]:
                    result[0] = grid[y][x]

                exist[grid[y][x]] = True

        for idx in range(1, len(exist)):
            if not exist[idx]:
                result[1] = idx
                return result

        return [-1, -1]
