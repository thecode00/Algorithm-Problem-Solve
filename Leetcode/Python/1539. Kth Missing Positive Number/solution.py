# https://leetcode.com/problems/kth-missing-positive-number/


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        index = 0
        num = 1
        while k > 0:
            if index < len(arr) and num == arr[index]:
                index += 1
            else:
                k -= 1
            num += 1    
        return num - 1  # num - 1 is answer because num is added to num at the end of the while loop.
