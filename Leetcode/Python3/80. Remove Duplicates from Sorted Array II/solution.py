# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index, non_duplicate = 0, 0
        while index < len(nums):
            cur_unique = nums[index]
            # Check unique element appear twice
            for num in nums[index: index + 2]:
                if num == cur_unique:
                    nums[non_duplicate] = num
                    non_duplicate += 1

            # Find next unique element index
            next_index = index
            while next_index < len(nums) and cur_unique == nums[next_index]:
                next_index += 1
            index = next_index

        return non_duplicate
