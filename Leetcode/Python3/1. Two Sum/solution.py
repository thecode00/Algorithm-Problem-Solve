# https://leetcode.com/problems/two-sum/description/


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for idx in range(len(nums)):
            if nums[idx] not in num_dict:
                num_dict[target - nums[idx]] = idx
            else:
                return [num_dict[nums[idx]], idx]
        