# https://leetcode.com/problems/largest-number/


from typing import List


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
            If false not move numbers than continue
            """
            while temp > 0 and self.check_swap(nums[temp - 1], nums[temp]):
                nums[temp], nums[temp - 1] = nums[temp - 1], nums[temp]
                temp -= 1
            idx += 1
        # Convert to int to eliminate cases start with zero
        return str(int("".join(map(str, nums))))


class Solution:  # Optimize where delete zero
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        sort_index = 1
        while (sort_index < len(nums)):
            index = sort_index
            while index > 0 and self.compare(nums[index - 1], nums[index]):
                nums[index], nums[index - 1] = nums[index - 1], nums[index]
                index -= 1
            sort_index += 1
        result = "".join(nums)

        return result if result[0] != "0" else "0"

    def compare(self, num1: str, num2: str) -> bool:
        return num1 + num2 < num2 + num1
