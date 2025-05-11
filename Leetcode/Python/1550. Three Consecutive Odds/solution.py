# https://leetcode.com/problems/three-consecutive-odds/description

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for idx in range(len(arr) - 2):
            for i in range(idx, idx + 3):
                if arr[i] % 2 == 0:
                    break
            else:
                return True
        
        return False