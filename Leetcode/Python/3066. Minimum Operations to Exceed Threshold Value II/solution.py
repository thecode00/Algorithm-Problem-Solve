# https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/description

import heapq


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # nums size = (2 <= nums.length <= 2 * 10 ^ 5) and many insert, so use heap
        heapq.heapify(nums)
        count = 0

        while nums[0] < k:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)

            heapq.heappush(nums, x * 2 + y)

            count += 1

        return count
