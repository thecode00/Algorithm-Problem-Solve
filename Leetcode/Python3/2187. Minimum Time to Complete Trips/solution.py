# https://leetcode.com/problems/minimum-time-to-complete-trips/


class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        time.sort()
        # Max time == smallest time * totalTrips
        start, end = 0, time[0] * totalTrips
        while start < end:
            mid = start + (end - start) // 2    # mid == time
            cur_trips = 0
            for bus in time:
                cur_trips += mid // bus
            if cur_trips < totalTrips:  # If current trips small than totalTrips it cant be answer so move start to mid + 1
                start = mid + 1
            else:   # Current trips is greater than or equal totalTrips mid is can be answer so move end to mid
                end = mid
        return end  # start is also the answer
