# https://leetcode.com/problems/merge-sorted-array/

class Solution:  # Time complexity: O(m + n)
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Sort top to bottom

        idx1 = m - 1    # Index of nums1
        idx2 = n - 1    # Index of nums2
        idx3 = m + n - 1  # Index of not sorted index

        while idx2 >= 0:
            if idx1 >= 0 and nums1[idx1] >= nums2[idx2]:
                nums1[idx3] = nums1[idx1]
                idx1 -= 1
            else:
                nums1[idx3] = nums2[idx2]
                idx2 -= 1
            idx3 -= 1


class Solution:  # Time complexity: O(log m)
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[m + i] = nums2[i]
        print(nums1)
        nums1.sort()


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for idx, num in enumerate(nums2, m):
            nums1[idx] = num
        nums1.sort()
