# https://leetcode.com/problems/house-robber-ii/

class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if length <= 1:
            return nums[-1]
        nums = nums * 2
        print(nums)

        def memorization(houses):
            dp = [0] * length
            dp[0], dp[1] = houses[0], max(houses[0], houses[1])
            for idx in range(2, length):
                dp[idx] = max(houses[idx] + dp[idx - 2], dp[idx - 1])
            return dp[-1]
        answer = 0
        for idx in range(length):
            answer = max(answer, memorization(nums[idx: idx + length]))
        return answer
