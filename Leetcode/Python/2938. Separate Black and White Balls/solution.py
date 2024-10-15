# https://leetcode.com/problems/separate-black-and-white-balls/description

class Solution:
    def minimumSteps(self, s: str) -> int:
        swap_count = 0
        put_zero_index = 0

        for idx, val in enumerate(s):
            if val == "0":
                # We can swap only adjacent element, so swap step is (current index - (last zero index + 1))
                swap_count += idx - put_zero_index
                put_zero_index += 1

        return swap_count
