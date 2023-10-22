# https://leetcode.com/problems/check-if-n-and-its-double-exist/

from selectors import EpollSelector


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        length = len(arr)
        for idx in range(length - 1):
            target = arr[idx] * 2
            # When sort in ascending order if element is negative element * 2 exists before the current element
            # So we need set the binary search range to the before current element
            if arr[idx] >= 0:
                start, end = idx + 1, length - 1
            else:
                start, end = 0, idx - 1
            while start <= end:
                mid = (start + end) >> 1
                if arr[mid] == target:
                    print(arr[mid], arr[idx], target)
                    return True
                elif arr[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
        return False