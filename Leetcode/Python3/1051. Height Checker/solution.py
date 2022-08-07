# https://leetcode.com/problems/height-checker/

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        temp = sorted(heights[:])   # Copy heights list
        answer = 0
        for n1, n2 in zip(heights, temp):
            if n1 != n2:
                answer += 1
        return answer