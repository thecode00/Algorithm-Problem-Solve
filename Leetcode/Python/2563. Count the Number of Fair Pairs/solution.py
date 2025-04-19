# https://leetcode.com/problems/count-the-number-of-fair-pairs/description/

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()

        pairs = 0

        for idx in range(len(nums)):
            upperIdx = self.upperBound(nums, upper - nums[idx], idx + 1)
            lowerIdx = self.lowerBound(nums, lower - nums[idx], idx + 1)

            pairs += upperIdx - lowerIdx

        return pairs

    def lowerBound(self, nums: List[int], target: int, start: int) -> int :
        left = start
        right = len(nums)

        while (left < right):
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        
        return left
    
    def upperBound(self, nums: List[int], target: int, start: int) -> int :
        left = start
        right = len(nums)

        while (left < right):
            mid = (left + right) // 2

            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid
        
        return left
        