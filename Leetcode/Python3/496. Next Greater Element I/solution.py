# https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = []
        for num in nums1:
            value = -1
            check = False
            for n in nums2:
                if n == num:
                    check = True
                if check and num < n:
                    value = n
                    break
            answer.append(value)
        return answer
