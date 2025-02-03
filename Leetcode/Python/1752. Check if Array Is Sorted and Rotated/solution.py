# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description

class Solution:  # Bruteforce
    def check(self, nums: List[int]) -> bool:
        double_nums = nums * 2

        for start in range(len(nums)):
            for idx in range(1, len(nums)):
                if double_nums[start + idx - 1] > double_nums[start + idx]:
                    break
            else:   # When for loop not break
                return True

        return False


class Solution:
    def check(self, nums: List[int]) -> bool:
        decrease_count = 0

        for idx in range(1, len(nums)):
            if nums[idx - 1] > nums[idx]:
                decrease_count += 1

        if nums[0] < nums[-1]:
            decrease_count += 1

        return decrease_count < 2
