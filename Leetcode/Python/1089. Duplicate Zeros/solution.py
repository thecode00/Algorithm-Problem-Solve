# https://leetcode.com/problems/duplicate-zeros/

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        temp = arr[:]
        pt1, pt2 = 0, 0 # Used two pointer algorithm
        length = len(arr)
        while pt1 <= length:
            arr[pt1] = temp[pt2]
            if temp[pt2] == 0:
                pt1 += 1
                if pt1 <= length:
                    arr[pt1] = temp[pt2]
            pt1 += 1
            pt2 += 1
        # print(arr)