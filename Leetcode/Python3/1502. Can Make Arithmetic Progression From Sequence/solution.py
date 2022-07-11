# https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        d = arr[1] - arr[0]  # Common difference
        for idx in range(len(arr) - 1):
            if arr[idx + 1] - arr[idx] != d:
                return False
        return True
