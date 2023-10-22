"""
https://leetcode.com/problems/product-of-array-except-self/
Time complexity: O(N)
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        mul = 1  # Multiply of left side
        for idx in range(len(nums)):
            answer.append(mul)
            mul *= nums[idx]
        mul = 1  # Multiply of right side
        for idx in range(len(nums) - 1, -1, -1):
            answer[idx] *= mul
            mul *= nums[idx]
        return answer
