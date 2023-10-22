# https://leetcode.com/problems/sort-array-by-parity/

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]: # Runtime: 171 ms
        position = 0
        for idx in range(len(nums)):
            if nums[idx] % 2 == 0:
                nums[idx], nums[position] = nums[position], nums[idx]
                position += 1
        return nums
    def sortArrayByParity(self, nums: List[int]) -> List[int]: # Runtime: 78 ms
        nums.sort(key= lambda x: x % 2)
        return nums