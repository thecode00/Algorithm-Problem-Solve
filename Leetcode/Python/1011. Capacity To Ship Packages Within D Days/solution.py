# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        start, end = max(weights), sum(weights)
        while start < end:
            """
            mid = (start + end) // 2 = (start // 2) + (end // 2)
            start // 2 = start - (start // 2)
            mid = start - (start // 2) + (end // 2) = start + (end - start) // 2
            """
            mid = start + (end - start) // 2
            cur_capacity, require_days = mid, 1
            for weight in weights:
                if cur_capacity - weight < 0:
                    require_days += 1
                    cur_capacity = mid - weight
                else:
                    cur_capacity -= weight

            if require_days > days:
                start = mid + 1
            else:
                end = mid
        return start


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        start, end = 0, sum(weights)
        while start < end:
            mid = start + (end - start) // 2

            cur_capacity = mid
            require_days = 1
            idx = 0
            while idx < len(weights):
                if mid - weights[idx] < 0:  # Ship cant hold package
                    require_days = float("inf")
                    break
                if cur_capacity - weights[idx] >= 0:
                    cur_capacity -= weights[idx]
                else:   # When current capacity less than current package
                    cur_capacity = mid - weights[idx]
                    require_days += 1
                idx += 1

            if require_days <= days:
                end = mid
            else:
                start = mid + 1
        return start
