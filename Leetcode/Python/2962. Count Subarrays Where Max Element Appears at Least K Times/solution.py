# https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/description

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_num = max(nums)

        count = 0
        max_indexs = []

        for idx, val in enumerate(nums):
            if val == max_num:
                max_indexs.append(idx)
            
            # For each index, add the number of subarrays ending at that index which have exactly k occurrences of the maximum element.
            if len(max_indexs) >= k:
                count += max_indexs[-k] + 1

        return count