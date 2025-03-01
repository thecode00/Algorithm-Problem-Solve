# https://leetcode.com/problems/apply-operations-to-an-array/description

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        insert_idx = 0

        for idx in range(len(nums) - 1):
            if nums[idx] == nums[idx + 1]:
                nums[idx] *= 2
                nums[idx + 1] = 0

        for idx in range(len(nums)):
            if nums[idx] != 0:
                nums[idx], nums[insert_idx] = nums[insert_idx], nums[idx]
                insert_idx += 1

        return nums
