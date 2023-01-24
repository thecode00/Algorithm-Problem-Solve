# https://leetcode.com/problems/intersection-of-two-arrays/description/


from bisect import bisect_left
from typing import List


class Solution:  # Without library
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersect = set()
        nums1.sort()
        for num in nums2:
            if num in intersect:    # Pass already search number 
                continue
            start, end = 0, len(nums1) - 1
            while start <= end:
                mid = start + (end - start) // 2
                if nums1[mid] == num:
                    intersect.add(num)
                    break
                elif nums1[mid] > num:
                    end = mid - 1
                else:
                    start = mid + 1
        return list(intersect)


class Solution:  # Use library
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersect = set()
        nums1.sort()
        for num in nums2:
            if num in intersect:    # Pass already search number 
                continue
            index = bisect_left(nums1, num)
            if index < len(nums1) and nums1[index] == num:
                intersect.add(num)
        return list(intersect)


class Solution:  # Two pointer
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersect = set()
        nums1.sort()
        nums2.sort()
        p1, p2 = 0, 0
        while p1 < len(nums1) and p2<len(nums2):
            if nums1[p1] == nums2[p2]:
                intersect.add(nums1[p1])
                p1 += 1
                p2 += 1
            elif nums1[p1] > nums2[p2]:
                p2 += 1
            else:
                p1 += 1
        
        return list(intersect)