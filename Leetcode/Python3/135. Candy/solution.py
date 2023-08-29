from typing import List


class Solution:  # Space complexity: O(N)
    def candy(self, ratings: List[int]) -> int:
        candys = [1] * len(ratings)
        # Check left child
        for i in range(len(ratings) - 1):
            if ratings[i] < ratings[i + 1]:
                candys[i + 1] = candys[i] + 1
        # Check right child
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candys[i] = max(candys[i + 1] + 1, candys[i])
        return sum(candys)
