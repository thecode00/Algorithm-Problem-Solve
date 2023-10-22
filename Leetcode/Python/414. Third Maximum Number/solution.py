# https://leetcode.com/problems/third-maximum-number/

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = sorted(set(nums), reverse=True)
        try:
            return nums[2]
        except:
            return nums[0]