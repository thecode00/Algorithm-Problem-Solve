# https://leetcode.com/problems/subarray-sum-equals-k/description/

from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        for idx in range(1, len(nums)):
            nums[idx] += nums[idx - 1]
        
        k_count = 0
        sum_hash = defaultdict(int)
        for p_sum in nums:
            if p_sum == k:
                k_count += 1
            
            if p_sum - k in sum_hash:
                k_count += sum_hash[p_sum - k]
            
            sum_hash[p_sum] += 1
        return k_count