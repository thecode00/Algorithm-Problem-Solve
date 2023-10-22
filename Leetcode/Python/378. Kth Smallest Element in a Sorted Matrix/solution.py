# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        temp = []
        for l in matrix:
            temp += l
        return sorted(temp)[k - 1]