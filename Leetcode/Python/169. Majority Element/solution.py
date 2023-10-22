# https://leetcode.com/problems/majority-element/


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Center of sorted list is always majority element
        # [2, 2, 1, 1, 1, 2, 2].sort() -> [1, 1, 1, 2, 2, 2, 2] center = 2
        nums.sort()
        return nums[len(nums) // 2]


class Solution:  # Divide and conquer
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        left = self.majorityElement(nums[:len(nums) // 2])
        right = self.majorityElement(nums[len(nums) // 2:])
        return [left, right][nums.count(right) > len(nums) // 2]
