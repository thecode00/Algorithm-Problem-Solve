# https://leetcode.com/problems/duplicate-zeros/

class Solution:     # Two pointer
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        temp = arr[:]
        pt1, pt2 = 0, 0
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


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        prev_zero = [0] * len(arr)
        # Count zero
        for idx, val in enumerate(arr):
            if idx > 0:
                prev_zero[idx] += prev_zero[idx - 1]
            if val == 0 and idx + 1 < len(arr):
                prev_zero[idx + 1] += 1

        # Move element to index + amount previous zero
        for idx in range(len(arr) - 1, -1, -1):
            new_position = prev_zero[idx] + idx
            if new_position >= len(arr):
                continue

            arr[new_position] = arr[idx]
            if arr[idx] == 0 and new_position + 1 < len(arr):
                arr[new_position + 1] = 0
