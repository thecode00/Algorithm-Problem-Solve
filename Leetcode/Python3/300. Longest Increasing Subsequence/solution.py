# https://leetcode.com/problems/longest-increasing-subsequence/description/
# Time complexity: O(n log n)

from bisect import bisect_left


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = []
        for num in nums:
            if not lis or lis[-1] < num:
                lis.append(num)
                continue
            lis[bisect_left(lis, num)] = num
        return len(lis)
