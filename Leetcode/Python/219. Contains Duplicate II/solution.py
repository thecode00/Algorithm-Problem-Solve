# https://leetcode.com/problems/contains-duplicate-ii/

from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        duplicate_index = {}
        for idx, num in enumerate(nums):
            if num in duplicate_index and abs(duplicate_index[num] - idx) <= k:
                return True
            # Update last num index
            duplicate_index[num] = idx

        return False
