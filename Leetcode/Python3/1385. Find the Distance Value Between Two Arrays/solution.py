# https://leetcode.com/problems/find-the-distance-value-between-two-arrays/

class Solution:
    # Brute force
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        answer = len(arr1)
        for idx in range(len(arr1)):
            for num in arr2:
                if abs(arr1[idx] - num) <= d:
                    answer -= 1
                    break
        return answer

    # Birary search
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        length = len(arr1)
        answer = length
        for idx in range(length):
            start, end = 0, len(arr2) - 1
            while start <= end:
                mid = start + (end - start) // 2
                if abs(arr1[idx] - arr2[mid]) <= d:
                    answer -= 1
                    break
                elif arr2[mid] >= arr1[idx]:
                    end = mid - 1
                else:
                    start = mid + 1
        return answer
