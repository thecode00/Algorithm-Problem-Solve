# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        num_list = {i: 0 for i in range(1, len(nums) + 1)}
        for num in nums:
            if num in num_list:
                del num_list[num]
        return list(num_list.keys())