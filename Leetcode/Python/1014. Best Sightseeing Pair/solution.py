# https://leetcode.com/problems/best-sightseeing-pair/description

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_left = values[0]
        max_value = 0

        # Maximize values[i] + i
        for idx in range(1, len(values)):
            max_value = max(max_value, max_left + values[idx] - idx)
            max_left = max(max_left, values[idx] + idx)

        return max_value
