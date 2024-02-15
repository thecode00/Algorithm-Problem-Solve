# https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/

from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()

        loegest_perimeter = -1

        nums_sum = sum(nums)

        while len(nums) > 2:
            # Pick longest side
            cur_longest_side = nums.pop()
            nums_sum -= cur_longest_side
            # Check is valid polygon
            if cur_longest_side < nums_sum:
                loegest_perimeter = max(
                    loegest_perimeter, cur_longest_side + nums_sum)

        return loegest_perimeter
