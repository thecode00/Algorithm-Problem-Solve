# https://leetcode.com/problems/median-of-two-sorted-arrays/


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 += nums2
        nums1.sort()
        length = len(nums1)

        return (
            nums1[length // 2]
            if length % 2 != 0
            else (nums1[length // 2] + nums1[length // 2 - 1]) / 2
        )
