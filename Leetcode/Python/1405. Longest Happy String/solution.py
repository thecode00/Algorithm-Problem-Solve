# https://leetcode.com/problems/longest-happy-string/description

import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        result = []

        if a:
            heapq.heappush(heap, (-a, "a"))
        if b:
            heapq.heappush(heap, (-b, "b"))
        if c:
            heapq.heappush(heap, (-c, "c"))

        while heap:
            count, cur_char = heapq.heappop(heap)
            count *= -1

            # Current char repeat three times, find another char
            if len(result) >= 2 and result[-1] == result[-2] == cur_char:
                if not heap:  # No remain char
                    break

                next_count, next_char = heapq.heappop(heap)
                next_count *= -1
                result.append(next_char)
                next_count -= 1

                if next_count > 0:
                    heapq.heappush(heap, (-next_count, next_char))
                heapq.heappush(heap, (-count, cur_char))
            else:
                result.append(cur_char)
                count -= 1

                if count > 0:
                    heapq.heappush(heap, (-count, cur_char))

        return "".join(result)
