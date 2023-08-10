# https://leetcode.com/problems/remove-element/

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # When you delete an element from the list, you have to pull all the elements after it one space, so delete the element from the back.
        for idx in range(len(nums) - 1, -1, -1):
            if nums[idx] == val:
                del nums[idx]


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        not_target_index = 0
        for idx, num in enumerate(nums):
            if num != val:
                nums[idx], nums[not_target_index] = nums[not_target_index], nums[idx]
                not_target_index += 1
        return not_target_index
