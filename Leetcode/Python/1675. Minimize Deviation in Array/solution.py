# https://leetcode.com/problems/minimize-deviation-in-array/description/
# Ref: https://leetcode.com/problems/minimize-deviation-in-array/solutions/3223541/day-55-priority-queue-easiest-beginner-friendly-sol/?orderBy=most_votes


import heapq


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        max_heap = []
        min_num = float("inf")
        deviation = float("inf")
        for num in nums:
            if num % 2 != 0:    # Odd * 2 = even
                num *= 2
            min_num = min(min_num, num)
            # For make max_heap convert to negative
            heapq.heappush(max_heap, -num)

        while True:
            max_num = -heapq.heappop(max_heap)
            deviation = min(deviation, max_num - min_num)
            """
            If the element is odd, multiply it by 2
            Odd * 2 = even
            If the element is even, divide it by 2
            They make loop so when max number is odd break 
            """
            if max_num % 2 != 0:
                break
            max_num //= 2
            # Check because this number can be the minimum after divide by 2
            min_num = min(min_num, max_num)
            heapq.heappush(max_heap, -max_num)
        return deviation
