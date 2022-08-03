# https://leetcode.com/problems/remove-element/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # When you delete an element from the list, you have to pull all the elements after it one space, so delete the element from the back.
        for idx in range(len(nums) - 1, -1, -1):
            if nums[idx] == val:
                del nums[idx]