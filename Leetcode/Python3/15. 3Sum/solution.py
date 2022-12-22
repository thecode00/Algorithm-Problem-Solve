# https://leetcode.com/problems/3sum/


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()
        for idx in range(len(nums) - 2):
            left, right = idx + 1, len(nums) - 1
            while left < right:
                total = nums[idx] + nums[left] + nums[right]
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:  # Find answer
                    answer.append([idx, left, right])
