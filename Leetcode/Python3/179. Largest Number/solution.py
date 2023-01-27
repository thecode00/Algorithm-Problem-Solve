# https://leetcode.com/problems/largest-number/


class Solution:  # Insertion sort
    def check_swap(self, num1: int, num2: int) -> bool:
        return str(num1) + str(num2) < str(num2) + str(num1)

    def largestNumber(self, nums: List[int]) -> str:
        idx = 1  # 0 ~ idx - 1 is sorted
        while idx < len(nums):
            temp = idx
            """
            ex. nums[temp - 1] = 9, nums[temp] = 10
            Check 910 < 109 
            It's better not to move the numbers than continue"""
            while temp > 0 and self.check_swap(nums[temp - 1], nums[temp]):
                nums[temp], nums[temp - 1] = nums[temp - 1], nums[temp]
                temp -= 1
            idx += 1
        # Convert to int to eliminate cases start with zero
        return str(int("".join(map(str, nums))))
