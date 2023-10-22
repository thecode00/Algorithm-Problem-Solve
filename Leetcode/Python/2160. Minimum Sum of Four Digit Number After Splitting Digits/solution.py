# https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/


class Solution:
    def minimumSum(self, num: int) -> int:
        num_list = sorted(str(num))
        # num range is 1000 <= num <= 9999 always get 4 digit
        new1, new2 = num_list[0] + num_list[-1], num_list[1] + num_list[-2]
        return int(new1) + int(new2)
