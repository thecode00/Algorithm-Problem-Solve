# https://leetcode.com/problems/sort-an-array/


class Solution:  # Tim sort
    def sortArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        return nums


class Solution:  # Bubble sort(TLE), Time complexity: O(N ^ 2)
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            for idx in range(len(nums) - 1 - i):
                if nums[idx] > nums[idx + 1]:
                    nums[idx], nums[idx + 1] = nums[idx + 1], nums[idx]
        return nums


class Solution:  # Selection sort(TLE), Time complexity: O(N ^ 2)
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            min_value = nums[i]
            swap_index = i
            for idx in range(i + 1, len(nums)):
                if nums[idx] < min_value:
                    min_value = nums[idx]
                    swap_index = idx
            nums[swap_index], nums[i] = nums[i], nums[swap_index]  # Swap
        return nums


class Solution:  # Insertion sort(TLE), Time complexity: O(N ^ 2)
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            while i > 0 and nums[i] < nums[i - 1]:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
                i -= 1
        return nums


class Solution:  # Quick sort(TLE), Time complexity: O(N ^ 2)
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        pivot = nums[0]
        small, big = [], []
        for idx in range(1, len(nums)):
            if nums[idx] <= pivot:
                small.append(nums[idx])
            else:
                big.append(nums[idx])
        return self.sortArray(small) + [pivot] + self.sortArray(big)
