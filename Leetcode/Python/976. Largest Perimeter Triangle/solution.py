# https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        # https://www.khanacademy.org/math/cc-seventh-grade-math/cc-7th-geometry/cc-7th-constructing-geometric-shapes/v/triangle-inqequality-theorem
        for idx in range(len(nums) - 1, 1, -1):
            print(idx)
            if nums[idx - 1] + nums[idx - 2] > nums[idx]:
                return nums[idx - 1] + nums[idx - 2] + nums[idx]
        return 0
