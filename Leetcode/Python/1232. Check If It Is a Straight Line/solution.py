# https://leetcode.com/problems/check-if-it-is-a-straight-line/

# TODO: Solve later
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        first_x, first_y = coordinates[0][0], coordinates[0][1]
        coordinates.sort(key=lambda x: (x[0], x[1]))
        diff = abs(first_x - coordinates[1][0]) + \
            abs(first_y - coordinates[1][1])
        for idx in range(len(coordinates) - 1):
            cur_diff = abs(coordinates[idx][0] - coordinates[idx + 1][0]) + \
                abs(coordinates[idx][1] - coordinates[idx + 1][1])
            if cur_diff != diff and coordinates[idx][0] != first_x and coordinates[idx][1]:
                return False
        return True
