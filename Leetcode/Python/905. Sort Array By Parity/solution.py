# https://leetcode.com/problems/sort-array-by-parity/

class Solution:  # Runtime: 171 ms
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        position = 0
        for idx in range(len(nums)):
            if nums[idx] % 2 == 0:
                nums[idx], nums[position] = nums[position], nums[idx]
                position += 1
        return nums


class Solution:  # Runtime: 78 ms
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        nums.sort(key=lambda x: x % 2)
        return nums


class Solution:  # Space complexity: O(1)
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even, odd = 0, len(nums) - 1

        while even < odd:
            if nums[even] % 2 == 0:
                even += 1
            else:
                nums[even], nums[odd] = nums[odd], nums[even]
                odd -= 1

        return nums
