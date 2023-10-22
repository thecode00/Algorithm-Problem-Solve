# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/?envType=study-plan-v2&id=leetcode-75
# Time complexity: O(N)


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)
        return [candy + extraCandies >= max_candy for candy in candies]
