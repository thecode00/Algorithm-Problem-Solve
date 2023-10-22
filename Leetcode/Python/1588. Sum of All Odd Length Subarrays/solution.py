# https://leetcode.com/problems/sum-of-all-odd-length-subarrays/

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        length = len(arr)
        answer = 0
        for l in range(0, length, 2):
            for idx in range(0, length - l):
                answer += sum(arr[idx: idx + l + 1])
        return answer
