# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        num_dict = {}
        # When you delete an element from the list, you have to pull all the elements after it one space, so delete the element from the back.
        for idx in range(len(nums) - 1, -1, -1):
            if nums[idx] in num_dict:
                del nums[idx]
            num_dict[nums[idx]] = 1
    
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for idx in range(len(nums) - 1):
            if nums[idx] != nums[idx + 1]:
                nums[k] = nums[idx + 1]
                k += 1
        return k