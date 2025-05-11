# https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/description

class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        # Count zero count and sum
        zero1, zero2 = nums1.count(0), nums2.count(0)
        sum1, sum2 = sum(nums1) + zero1, sum(nums2) + zero2


        if sum2 > sum1:
            zero1, zero2 = zero2, zero1
            sum1, sum2 = sum2, sum1
        
        if sum1 != sum2 and zero2 == 0:
            return -1
        
        return sum1