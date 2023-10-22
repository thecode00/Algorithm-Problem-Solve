# https://leetcode.com/problems/delete-and-earn/

from collections import Counter


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)
        dp1, dp2 = 0, 0
        for key in sorted(list(count.keys())):
            # When earn score need delete key - 1 so if key - 1 not in nums dp + socres 
            if key - 1 not in count:
                dp1, dp2 = dp2, dp2 + key * count[key]
            else:   # else compare with dp[key - 1], dp[key - 2] + score
                dp1, dp2 = dp2, max(dp1 + key * count[key], dp2)
        return dp2
