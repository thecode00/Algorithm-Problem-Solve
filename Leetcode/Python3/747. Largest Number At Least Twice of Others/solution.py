# https://leetcode.com/problems/largest-number-at-least-twice-of-others/

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        temp = nums[:]  # Copy nums list
        temp.sort()
        return nums.index(temp[-1]) if temp[-1] >= temp[-2] * 2 else -1
