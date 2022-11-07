"""
https://leetcode.com/problems/maximum-69-number/
Time Complexity: O(N)
"""


class Solution:
    def maximum69Number(self, num: int) -> int:
        num_list = list(str(num))
        for idx, val in enumerate(num_list):
            if val == "6":
                num_list[idx] = "9"
                return int("".join(num_list))
        return num
