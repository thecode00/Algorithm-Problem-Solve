# https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:  # Runtime: 254 ms
        nums = [num ** 2 for num in nums]
        return sorted(nums)
    def sortedSquares(self, nums: List[int]) -> List[int]:  # Runtime: 208 ms
        for i in range(len(nums)):
            nums[i] *= nums[i]
        nums.sort()
        return nums
            
