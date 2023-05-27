# https://leetcode.com/problems/3sum/


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()
        for idx in range(len(nums) - 2):
            # Skip duplicate triplets
            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue
            left, right = idx + 1, len(nums) - 1
            while left < right:
                total = nums[idx] + nums[left] + nums[right]
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:   # Found sum
                    answer.append([nums[idx], nums[left], nums[right]])
                    # Skip duplicate number
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return answer
