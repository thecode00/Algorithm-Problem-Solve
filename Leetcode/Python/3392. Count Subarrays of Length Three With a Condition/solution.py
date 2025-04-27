# https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition/description

class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        count = 0

        max_search = len(nums) - 2

        for idx in range(max_search):
            if (nums[idx] + nums[idx + 2]) * 2 == nums[idx + 1]:
                count += 1
        
        return count