# https://leetcode.com/problems/koko-eating-bananas/


from math import ceil


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start, end = 1, max(piles)
        while start < end:
            mid = start + (end - start) // 2    # Prevent overflow python not necessary.
            spend_time = 0
            for banana in piles:
                spend_time += ceil(banana / mid)
            if spend_time > h:  # If spend_time bigger than h mid cant be answer so move start to mid + 1
                start = mid + 1
            else:   # If spend_time <= h, mid can be answer so move end to mid
                end = mid
        return start
